from modules import DataTypes
from pathlib import Path
from modules import Sql


resultJson = Path("test/1/reply.json").read_text(encoding="utf-8")

test: DataTypes.ApiReply = DataTypes.ApiReply.model_validate_json(resultJson)

Sql.Papers.mark(1, comment=test)

if paper := Sql.Papers.get(1):
    print(paper.comment)
