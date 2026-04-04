from typing import Mapping

type _JSONValue = (
    str | int | float | bool | None | list["_JSONValue"] | dict[str, "_JSONValue"]
)

_dataNames: dict[str, str] = {
    "score": "得分",
    "recognized_text": "识别文本",
    "strengths": "优势",
    "content_deficiencies": "不足",
    "logic_flaws": "逻辑缺陷",
    "coherence_evaluation": "连贯性评价",
    "structure_optimization": "结构优化",
    "knowledge_point_summary": "知识点",
    "timestamp": "时间戳",
    "word_usage_errors": "错词",
    "phrase_usage_errors": "错短语",
    "sentence_usage_errors": "错句子",
    "tense_usage_errors": "错时态",
    "highlight_sentences": "好句子",
    "advanced_expression_suggestions": "高级表达建议",
    "advanced_vocabulary": "高级词汇",
    "advanced_expression_pattern": "高级表达模式",
    "personalized_sample": "个性化样例",
}


def _to_markdown_key(key: str, level: int = 2) -> str:
    return f"{'#' * level} {_dataNames.get(key, key)}"


def _dict_to_markdown(data: Mapping[str, _JSONValue], level: int = 2) -> list[str]:
    # sourcery skip: low-code-quality
    lines: list[str] = []
    for key, value in data.items():
        title = _to_markdown_key(key, level)
        if isinstance(value, (str, int)):
            lines.append(f"{title}: {value}")
            continue

        if isinstance(value, list):
            if len(value) == 0:
                lines.append(f"{title}: (空)")
                continue

            # 对纯文本列表做简单 bullet
            if all(isinstance(item, (str, int)) for item in value):
                lines.append(f"{title}:")
                lines.extend(f"- {item}" for item in value)
                continue

            # 对 dict 列表，逐条展开为有序子条目（条目数字 + 内部缩进子 bullet）
            if all(isinstance(item, dict) for item in value):
                lines.append(f"#### {_dataNames.get(key, key)}:")
                for idx, item in enumerate(value, start=1):
                    # 尝试从常见字段中提取更有意义的条目标题
                    if isinstance(item, dict):
                        # 优先使用 title，其次 text，找不到就回退到 “Item {idx}”
                        item_label = (
                            str(item.get("title"))
                            if "title" in item and item.get("title")
                            else str(item.get("text"))
                            if "text" in item and item.get("text")
                            else f"Item {idx}"
                        )
                    else:
                        item_label = f"Item {idx}"
                    lines.append(f"{idx}. {item_label}")
                    if isinstance(item, dict):
                        for sub_key, sub_val in item.items():
                            if (
                                isinstance(sub_val, (str, int))
                                or not isinstance(sub_val, list)
                                and not isinstance(sub_val, dict)
                            ):
                                lines.append(
                                    f"    - {_dataNames.get(sub_key, sub_key)}: {sub_val}"
                                )
                            elif isinstance(sub_val, list):
                                lines.append(
                                    f"    - {_dataNames.get(sub_key, sub_key)}:"
                                )
                                lines.extend(f"        - {sub_item}" for sub_item in sub_val)
                            else:
                                # 递归一层字典内容，格式化为缩进子 bullet
                                nested = _dict_to_markdown(sub_val, level + 2)
                                lines.extend(f"    - {nline}" for nline in nested)
                    else:
                        lines.append(f"    - {result2Markdown(item, level + 1)}")
                continue

            # 回退：混合列表/不规则类型
            lines.append(f"{title}:")
            lines.extend(f"- {result2Markdown(item, level + 1)}" for item in value)
            continue

        if isinstance(value, dict):
            lines.append(title)
            lines.extend(_dict_to_markdown(value, level + 1))
            continue

        lines.append(f"{title}: {value}")
    return lines


def result2Markdown(data: _JSONValue, level: int = 2) -> str:
    if isinstance(data, (str | int | float | bool | None)):
        return f"- {data}"

    if isinstance(data, list):
        if len(data) == 0:
            return "(空)"
        lines: list[str] = []
        lines.extend(result2Markdown(item, level + 1) for item in data)
        return "\n".join(lines)

    # dict
    lines = _dict_to_markdown(data, level)
    return "\n\n".join(lines)
