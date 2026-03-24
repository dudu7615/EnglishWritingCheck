from modules import logger, config, DataTypes
from typing import Any
import httpx
import anyio
import json


def _decodeReply(reply: str) -> DataTypes.ApiReply:
    reply = reply.replace(
        "选择该词作为“高级词汇”的原因说明", "选择该词作为高级词汇的原因说明"
    )
    data: dict[str, Any] = json.loads(reply)
    data["data"]["result"] = json.loads(str(data["data"]["result"]))
    return DataTypes.ApiReply(**data)


async def _callApi(task: DataTypes.Task, client: httpx.AsyncClient) -> None:
    params: dict[str, str] = {
        "apikey": config["key"],
        "id": task.id,
        "ocr": task.imgUrl,
    }

    for _ in range(3):
        try:
            response = await client.post(config["url"], params=params)
            if response.status_code != 200:
                logger.warning(
                    f"尝试调用 API 失败，任务 {task.id} 状态码: {response.status_code}"
                )
                continue
            task.apiReply = _decodeReply(response.text)
            logger.info(f"API 调用成功，任务 {task.id}")
            return
        except Exception as e:
            logger.warning(f"调用 API 报错，任务 {task.id}: {e}")
            continue
    logger.error(f"调用 API 失败，任务 {task.id}，经过 3 次尝试")


async def _main(tasks: list[DataTypes.Task]) -> None:
    """批量异步调用 API"""
    semaphore: anyio.Semaphore = anyio.Semaphore(64)

    async def wrapper(task: DataTypes.Task, client: httpx.AsyncClient) -> None:
        async with semaphore:
            await _callApi(task, client)

    async with httpx.AsyncClient(timeout=120) as client:
        async with anyio.create_task_group() as tg:
            for task in tasks:
                tg.start_soon(wrapper, task, client)


def run(tasks: list[DataTypes.Task]):
    anyio.run(_main, tasks)