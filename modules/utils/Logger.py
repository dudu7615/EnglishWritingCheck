from PySide6.QtCore import QObject, Signal
from loguru import logger
from ansi2html import Ansi2HTMLConverter


class _LoggerHandle(QObject):
    log = Signal(str)

    def __init__(self):
        super().__init__()
        self.converter = Ansi2HTMLConverter(inline=True)

    def write(self, message: str):
        self.log.emit(self.converter.convert(message.rstrip("\n"), full=True))

    def flush(self):
        pass


uiLogger = _LoggerHandle()
logger.add(
    uiLogger.write,
    colorize=True,
    level="DEBUG",  # 最低输出级别
    catch=True,  # 捕获sink异常，避免UI崩溃
)
