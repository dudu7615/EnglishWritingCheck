import fastapi
import uvicorn
from fastapi.responses import FileResponse
from modules.utils.Logger import logger
from modules import Paths

_app = fastapi.FastAPI()

@_app.get("/{filePath:path}")
async def _handle(filePath: str):   # type: ignore
    """提供文件服务"""
    try:
        path = Paths.data / "imgs" / filePath
        
        if path.is_file():
            logger.info(f"下载文件: {path}")
            return FileResponse(path)
        
        if path.is_dir():
            logger.info(f"访问目录: {path}")
            items = [item.name for item in sorted(path.iterdir())]
            return {"items": items}
        
        return {"error": "路径不存在"}, 404
    except Exception as e:
        logger.error(f"错误: {e}")
        return {"error": str(e)}, 500
    

def run(port: int):
    uvicorn.run(_app, host="0.0.0.0", port=port)