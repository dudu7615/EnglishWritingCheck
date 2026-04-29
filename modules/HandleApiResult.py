from typing import cast
from pydantic import BaseModel
import markdown as md
from . import Enums, DataTypes, Paths


def _handleDict(data: BaseModel, level: int = 0, count: int = 0) -> str:
    output: list[str] = []
    output.extend(
        (
            f"{'  ' * (level + 2)}- **{key}**: {value}"  # md 非有序列表中的无序列表首项，没有前导数字
            if i != 0
            or count
            == 0  # 只有当当前项不是列表中的第一项或者当前项不是列表项时，才添加前导数字
            else f"{'  ' * level} {count}. - **{key}**: {value}"
        )
        for i, (key, value) in enumerate(data)
    )
    return "\n".join(output)


def _handleList(data: list[BaseModel], level: int = 0) -> str:
    output: list[str] = []
    output.extend(_handleDict(data[i], level, i + 1) for i in range(len(data)))
    return "\n".join(output)


def result2Markdown(data: DataTypes.Result, options: Enums.ShowDetaleOption) -> str:
    markdown = ""
    for option in Enums.ShowDetaleOption:
        if options & option:
            if value := getattr(data, (option.name or ""), None):
                if isinstance(value, list):
                    markdown += f"### {Enums.optionNames.get(option, option.name)}\n"
                    markdown += _handleList(cast(list[BaseModel], value)) + "\n"
                else:
                    markdown += f"### {Enums.optionNames.get(option, option.name)}\n"
                    markdown += _handleDict(value) + "\n"

    return markdown


def result2Html(
    data: DataTypes.Result | None = None,
    options: Enums.ShowDetaleOption = Enums.ShowDetaleOption.NONE,
) -> str:
    markdown = "<h1>未批改</h1>" if data is None else result2Markdown(data, options)
    template = (Paths.html / "template.html").read_text(encoding="utf-8")
    html = md.markdown(markdown, extensions=["extra"])
    return template.replace("{{html}}", html)
