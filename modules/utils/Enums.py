from enum import IntFlag, auto


class ShowDetaleOption(IntFlag):
    NONE = 0
    recognized_text = auto()  # 识别文本
    strengths = auto()  # 优势
    content_deficiencies = auto()  # 不足
    logic_flaws = auto()  # 逻辑缺陷
    coherence_evaluation = auto()  # 连贯性评价
    structure_optimization = auto()  # 结构优化
    knowledge_point_summary = auto()  # 知识点
    timestamp = auto()

    word_usage_errors = auto()  # 错词
    phrase_usage_errors = auto()  # 错短语
    sentence_usage_errors = auto()  # 错句子
    tense_usage_errors = auto()  # 错时态
    highlight_sentences = auto()  # 好句子
    advanced_expression_suggestions = auto()  # 高级表达建议

    advanced_vocabulary = auto()  # 高级词汇
    advanced_expression_pattern = auto()  # 高级表达模式
    personalized_sample = auto()  # 个性化样例


optionNames: dict[ShowDetaleOption, str] = {
    ShowDetaleOption.NONE: "无",
    ShowDetaleOption.recognized_text: "识别文本",
    ShowDetaleOption.strengths: "优势",
    ShowDetaleOption.content_deficiencies: "不足",
    ShowDetaleOption.logic_flaws: "逻辑缺陷",
    ShowDetaleOption.coherence_evaluation: "连贯性评价",
    ShowDetaleOption.structure_optimization: "结构优化",
    ShowDetaleOption.knowledge_point_summary: "知识点",
    ShowDetaleOption.timestamp: "时间戳",
    ShowDetaleOption.word_usage_errors: "错词",
    ShowDetaleOption.phrase_usage_errors: "错短语",
    ShowDetaleOption.sentence_usage_errors: "错句子",
    ShowDetaleOption.tense_usage_errors: "错时态",
    ShowDetaleOption.highlight_sentences: "好句子",
    ShowDetaleOption.advanced_expression_suggestions: "高级表达建议",
    ShowDetaleOption.advanced_vocabulary: "高级词汇",
    ShowDetaleOption.advanced_expression_pattern: "高级表达模式",
    ShowDetaleOption.personalized_sample: "个性化样例",
}

oppositeOptionNames: dict[str, ShowDetaleOption] = {
    value: key for key, value in optionNames.items()
}
