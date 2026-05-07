from modules import logger, config, DataTypes
import httpx
import anyio
from PySide6.QtCore import Signal, QObject


class CallApi(QObject):
    finish = Signal(object)  # Task

    def _decodeReply(self, reply: str) -> DataTypes.ApiReply:
        # reply = reply.replace(
        #     "选择该词作为“高级词汇”的原因说明", "选择该词作为高级词汇的原因说明"
        # )
        # data: dict[str, Any] = json.loads(reply)
        # data["data"]["result"] = json.loads(str(data["data"]["result"]))

        return DataTypes.ApiReply.model_validate_json(reply)

    async def _callApi(self, task: DataTypes.Task, client: httpx.AsyncClient) -> None:
        params: dict[str, str] = {
            "apikey": config.key,
            "id": task.examRemoteId,
            "ocr": task.imgUrl,
        }

        for _ in range(3):
            try:
                response = await client.post(config.url, params=params)
                if response.status_code != 200:
                    logger.warning(
                        f"尝试调用 API 失败，任务 {task.id} 状态码: {response.status_code}"
                    )
                    continue

            except Exception as e:
                logger.warning(f"调用 API 报错，任务 {task.id}: {e}")
                continue
            try:
                task.apiReply = self._decodeReply(response.text)
                self.finish.emit(task)
                return
            except Exception as e:
                logger.warning(f"解析 API 回复失败，任务 {task.id}: {e}")
                continue
        logger.error(f"调用 API 失败，任务 {task.id}，经过 3 次尝试")

    async def _main(self, tasks: list[DataTypes.Task]) -> None:
        """批量异步调用 API"""
        semaphore: anyio.Semaphore = anyio.Semaphore(64)

        async def wrapper(task: DataTypes.Task, client: httpx.AsyncClient) -> None:
            async with semaphore:
                try:
                    await self._callApi(task, client)
                except Exception as e:
                    logger.error(
                        f"任务 {getattr(task, 'id', None)} wrapper 层异常: {e}"
                    )

        async with httpx.AsyncClient(timeout=300) as client:
            async with anyio.create_task_group() as tg:
                for task in tasks:
                    tg.start_soon(wrapper, task, client)

    def run(self, tasks: list[DataTypes.Task]):
        anyio.run(self._main, tasks)
