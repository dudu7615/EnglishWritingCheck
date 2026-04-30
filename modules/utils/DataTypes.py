from pathlib import Path
from pydantic import BaseModel, Field, field_validator, model_validator
from . import Enums


class Config(BaseModel):    
    url: str = Field(default="https://api.extreme-code.cn/API/dhxx.php")
    key: str
    detaleOptions: int = Field(default=Enums.ShowDetaleOption.ALL)



class ApiReply(BaseModel):
    code: int  # 200
    message: str  # success
    data: ApiReply_data


class ApiReply_data(BaseModel):
    task_id: str
    result: Result = Field()
    request_id: str  # UUID

    @field_validator("result", mode="before")
    @classmethod
    def _str2result(cls, v: str | dict[str, str | int]) -> Result:
        if isinstance(v, str):
            return Result.model_validate_json(v)
        return Result.model_validate(v)


class Result(BaseModel):
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
    class word_usage_error(BaseModel):
        错误单词: str
        原句引用: str
        修正形式: str
        错误原因解释: str

    class phrase_usage_error(BaseModel):
        错误短语: str
        原句引用: str
        修正形式: str
        错误原因解释: str

    class sentence_usage_error(BaseModel):
        错误句子: str
        修正后的句子: str
        错误原因解释: str

    class tense_usage_error(BaseModel):
        原句: str
        错误点说明: str
        修正原则解释: str

    class highlight_sentence(BaseModel):
        原句: str
        亮点分析: str

    class advanced_expression_suggestion(BaseModel):
        对应的学生原句: str
        修改后的完整英文句子: str
        对应的中文翻译: str
        修改点说明: str
        修改理由: str

    class advanced_vocabulary(BaseModel):
        词汇: str
        所在句子: str
        选择该词作为高级词汇的原因说明: str = Field(
            alias="选择该词作为“高级词汇”的原因说明"
        )

        @model_validator(mode="before")
        @classmethod
        def _alias(cls, values: dict[str, str | int]) -> dict[str, str | int]:
            """ sql中的字段是不带引号的，但alias设置导致结果必须带引号 """
            targetKey = "选择该词作为高级词汇的原因说明"
            apiKey = "选择该词作为“高级词汇”的原因说明"
            if targetKey in values and apiKey not in values:
                values[apiKey] = values.pop(targetKey)
            return values

    class advanced_expression_pattern(BaseModel):
        原句: str
        表达方式说明: str
        其在高考阅卷中的价值解释: str

    class personalized_sample(BaseModel):
        sample_text: str
        revision_explanation: str


class Task(BaseModel):
    id: str
    examRemoteId: str
    imgUrl: str
    imgPath: Path
    apiReply: ApiReply | None = None
