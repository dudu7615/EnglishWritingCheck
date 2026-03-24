from PySide6.QtCore import QThread, Signal
from modules import Cloudflare, FileServer, CallApi, DataTypes


class CloudflareThread(QThread):
    result = Signal(str)

    def __init__(self, port: int, timeout: int = 10):
        super().__init__()
        self.port = port
        self.timeout = timeout

    def run(self):
        url = Cloudflare.run(self.port, self.timeout)
        self.result.emit(url)
        self.terminate()


class FileServerThread(QThread):
    def __init__(self, port: int) -> None:
        super().__init__()
        self.port = port

    def run(self):
        FileServer.run(self.port)


class CallApiThread(QThread):
    def __init__(self, tasks: list[DataTypes.Task]) -> None:
        super().__init__()
        self.tasks = tasks

    def run(self):
        CallApi.run(self.tasks)