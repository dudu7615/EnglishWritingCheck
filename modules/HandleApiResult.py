from typing import get_type_hints, Any
import types
from .utils import DataTypes

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

type _Data = str | int | list[Any] | dict[str, Any]

def result2Markdown(data: _Data, output: str = ""):
    if isinstance(data, str|int):
        output += f"{data}\n\n"
    elif isinstance(data, list):
        for item in data:
            output += result2Markdown(item, output)
    else:
        for key, value in data.items():
            output += f"## {_dataNames.get(key, key)}\n\n"
            output += result2Markdown(value, output)
    return output