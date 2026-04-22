from modules import DataTypes
from pathlib import Path

resultJson = Path("test/1/reply.json").read_text(encoding="utf-8")

test: DataTypes.ApiReply = DataTypes.ApiReply.model_validate_json(resultJson)

print(test)
