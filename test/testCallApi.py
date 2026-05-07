from modules import (
    CallApi,
    DataTypes,
    HandleApiResult,
    Enums,
    logger,
    SubThreads,
    Paths,
)

url = ""


def getCfUrl(result: str):
    global url
    url = result


cf = SubThreads.CloudflareThread(port=8000)
cf.result.connect(getCfUrl)
cf.start()
SubThreads.FileServerThread(port=8000).start()

while not url:
    pass

tasks: list[DataTypes.Task] = [
    DataTypes.Task(
        id="1",
        examRemoteId="60636437",
        imgUrl=f"{url}/test/image.jpg",
        imgPath=Paths.data / "imgs" / "test/image.jpg",
    ),
]
