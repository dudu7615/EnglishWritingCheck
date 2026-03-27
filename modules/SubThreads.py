import threading
from PySide6.QtCore import QThread, Signal
from modules import Cloudflare, FileServer, CallApi, DataTypes


class CloudflareThread(QThread):
    result = Signal(str)

    def __init__(self, port: int, timeout: int = 10):
        super().__init__()
        self.port = port
        self.timeout = timeout

    def run(self):
        threading.current_thread().name = "CloudflareThread"
        url = Cloudflare.run(self.port, self.timeout)
        self.result.emit(url)


class FileServerThread(QThread):
    def __init__(self, port: int) -> None:
        super().__init__()
        self.port = port

    def run(self):
        threading.current_thread().name = "FileServerThread"
        FileServer.run(self.port)


class CallApiThread(QThread):
    finished = Signal(object)  # list[DataTypes.Task]
    def __init__(self, tasks: list[DataTypes.Task]) -> None:
        super().__init__()
        self.tasks = tasks

    def run(self):
        threading.current_thread().name = "CallApiThread"
        CallApi.run(self.tasks)
        self.finished.emit(self.tasks)