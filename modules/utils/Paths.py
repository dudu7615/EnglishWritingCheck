from pathlib import Path

root = Path(__file__).parent.parent.parent
data = root / "data"
config = root / "config"
bin = root / "bin"

data.mkdir(exist_ok=True)
(data / "imgs").mkdir(exist_ok=True)
bin.mkdir(exist_ok=True)