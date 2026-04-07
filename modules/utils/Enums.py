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
