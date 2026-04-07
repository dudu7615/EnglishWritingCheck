import fastapi
import uvicorn
from fastapi.responses import FileResponse, JSONResponse
from modules.utils.Logger import logger
from modules import Paths

_app = fastapi.FastAPI()


@_app.get("/{filePath:path}")
async def _handle(filePath: str):  # type: ignore
    """提供文件服务"""
    try:
        base = Paths.data / "imgs"
        path = (base / filePath).resolve()
        
        # Prevent path traversal attacks
        if not path.is_relative_to(base.resolve()):
            return JSONResponse({"error": "访问被拒绝"}, status_code=403)

        if path.is_file():
            return FileResponse(path)

        if path.is_dir():
            items = [item.name for item in sorted(path.iterdir())]
            return {"items": items}

        return JSONResponse({"error": "路径不存在"}, status_code=404)
    except Exception as e:
        logger.error(f"错误: {e}")
        return JSONResponse({"error": str(e)}, status_code=500)


def run(port: int):
    uvicorn.run(_app, host="0.0.0.0", port=port)
