from typing import cast
from pydantic import BaseModel
from . import Enums, DataTypes


def _handleDict(data: BaseModel, level: int = 0, count: int = 0) -> str:
    output: list[str] = []
    output.extend(
        (
            f"{'  ' * (level + 2)}- **{key}**: {value}"  # md 非有序列表中的无序列表首项，没有前导数字
            if i != 0 or count == 0  # 只有当当前项不是列表中的第一项或者当前项不是列表项时，才添加前导数字
            else f"{'  ' * level} {count}. - **{key}**: {value}"
        )
        for i, (key, value) in enumerate(data)
    )
    return "\n".join(output)


def _handleList(data: list[BaseModel], level: int = 0) -> str:
    output: list[str] = []
    output.extend(_handleDict(data[i], level, i + 1) for i in range(len(data)))
    # output.extend(_handleDict(item, level+1) for item in data)
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
