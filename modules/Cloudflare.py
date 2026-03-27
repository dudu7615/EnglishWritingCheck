import subprocess
import re
import time
import threading
import io
from queue import Queue
from modules import Paths, logger


_exitReadOutput = False

def _read_output(stream: io.TextIOWrapper | None, queue: Queue[str]):
    """在独立线程中读取流数据"""
    global _exitReadOutput

    if stream is None:
        return
    for line in stream:
        queue.put(line)
        if _exitReadOutput:
            return

def run(port: int, timeout: int = 10) -> str | None:
    """
    启动 cloudflared 进程并在 {timeout} 秒内从其输出中提取 URL
    进程会在后台持续运行
    """
    global _exitReadOutput
    # cloudflared tunnel --url http://127.0.0.1:8000
    process = subprocess.Popen(
        [str(Paths.bin / "cloudflared.exe"), "tunnel", "--url", f"http://127.0.0.1:{port}"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    # 创建队列和线程来读取输出
    queue: Queue[str] = Queue()
    stdoutThread = threading.Thread(name = "CloudflareStdout", target=_read_output, args=(process.stdout, queue), daemon=True)
    stderrThread = threading.Thread(name = "CloudflareStderr", target=_read_output, args=(process.stderr, queue), daemon=True)
    stdoutThread.start()
    stderrThread.start()
    
    startTime = time.time()
    
    try:
        while time.time() - startTime < timeout:
            try:
                # 非阻塞方式从队列取数据
                line = queue.get(timeout=0.1)
                match = re.search(r'https://[a-zA-Z0-9\-]+\.trycloudflare\.com', line)
                if match:
                    url = match.group(0)
                    logger.info(f"Cloudflare URL: {url}")
                    _exitReadOutput = True
                    return url
            except:
                # 队列为空，继续等待
                pass
        
        logger.error(f"在 {timeout} 秒内未能提取 Cloudflare URL")
        _exitReadOutput = True
        return None
    except Exception as e:
        logger.error(f"获取 Cloudflare URL 时出错: {e}")
        _exitReadOutput = True
        return None


