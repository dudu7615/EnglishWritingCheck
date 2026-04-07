import threading
from PySide6.QtCore import QThread, Signal
from modules import Cloudflare, FileServer, CallApi, DataTypes, Sql


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
    progress = Signal(int)  # %

    def __init__(self, tasks: list[DataTypes.Task]) -> None:
        super().__init__()
        self.tasks = tasks
        self.callApi = CallApi.CallApi()
        self.callApi.finish.connect(self._handleFinishSignal)

        self.count = 0

    def run(self):
        threading.current_thread().name = "CallApiThread"
        self.callApi.run(self.tasks)

    def _handleFinishSignal(self, task: DataTypes.Task):
        self.count += 1

        Sql.Papers.mark(int(task.id), task.apiReply)

        self.progress.emit(int(self.count / len(self.tasks) * 100))

        if self.count == len(self.tasks):
            self.finished.emit(self.tasks)
            self.terminate()
