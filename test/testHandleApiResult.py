from modules import HandleApiResult, DataTypes, Enums
from pathlib import Path

resultJson = Path("test/1/result.json").read_text(encoding="utf-8")

test: DataTypes.Result = DataTypes.Result.model_validate_json(resultJson)

print(
    HandleApiResult.result2Markdown(
        test,
        Enums.ShowDetaleOption.word_usage_errors
        | Enums.ShowDetaleOption.advanced_expression_pattern
        | Enums.ShowDetaleOption.advanced_vocabulary
        # | Enums.ShowDetaleOption.personalized_sample
        | Enums.ShowDetaleOption.sentence_usage_errors
        | Enums.ShowDetaleOption.tense_usage_errors,
    )
)

print(
    HandleApiResult.result2Html(
        test,
        Enums.ShowDetaleOption.word_usage_errors
        | Enums.ShowDetaleOption.advanced_expression_pattern
        | Enums.ShowDetaleOption.advanced_vocabulary
        # | Enums.ShowDetaleOption.personalized_sample
        | Enums.ShowDetaleOption.sentence_usage_errors
        | Enums.ShowDetaleOption.tense_usage_errors,
    )
)
