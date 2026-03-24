from dataclasses import dataclass
from typing import TypedDict
from pathlib import Path


class ApiConfig(TypedDict):
    key: str
    url: str


class ApiReply(TypedDict):
    code: int  # 200
    message: str  # success
    data: ApiReply_data


class ApiReply_data(TypedDict):
    task_id: str
    result: Result
    request_id: str  # UUID


class Result(TypedDict):
    score: int
    recognized_text: str  # 识别文本
    strengths: str  # 优势
    content_deficiencies: str  # 不足
    logic_flaws: str  # 逻辑缺陷
    coherence_evaluation: str  # 连贯性评价
    structure_optimization: str  # 结构优化
    knowledge_point_summary: str
    timestamp: str

    word_usage_errors: list[ResultDetale.word_usage_error]
    phrase_usage_errors: list[ResultDetale.phrase_usage_error]
    sentence_usage_errors: list[ResultDetale.sentence_usage_error]
    tense_usage_errors: list[ResultDetale.tense_usage_error]
    highlight_sentences: list[ResultDetale.highlight_sentence]
    advanced_expression_suggestions: list[ResultDetale.advanced_expression_suggestion]

    advanced_vocabulary: ResultDetale.advanced_vocabulary
    advanced_expression_pattern: ResultDetale.advanced_expression_pattern
    personalized_sample: ResultDetale.personalized_sample


class ResultDetale:

    class word_usage_error(TypedDict):
        错误单词: str
        原句引用: str
        修正形式: str
        错误原因解释: str

    class phrase_usage_error(TypedDict):
        错误短语: str
        原句引用: str
        修正形式: str
        错误原因解释: str

    class sentence_usage_error(TypedDict):
        错误句子: str
        修正后的句子: str
        错误原因解释: str

    class tense_usage_error(TypedDict):
        错误时态: str
        原句引用: str
        修正形式: str
        错误原因解释: str

    class highlight_sentence(TypedDict):
        原句: str
        亮点分析: str

    class advanced_expression_suggestion(TypedDict):
        对应的学生原句: str
        修改后的完整英文句子: str
        对应的中文翻译: str
        修改点说明: str
        修改理由: str

    class advanced_vocabulary(TypedDict):
        词汇: str
        所在句子: str
        选择该词作为高级词汇的原因说明: str  # 选择该词作为“高级词汇”的原因说明

    class advanced_expression_pattern(TypedDict):
        原句: str
        表达方式说明: str
        其在高考阅卷中的价值解释: str

    class personalized_sample(TypedDict):
        sample_text: str
        revision_explanation: str


@dataclass
class Task:
    id: str
    imgUrl: str
    imgPath: Path
    apiReply: ApiReply

