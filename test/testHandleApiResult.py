from modules import HandleApiResult

test = {
    "data": {
        "result": {
            "score": 85,
            "recognized_text": "This is a sample text.",
            "strengths": "strengths",
            "word_usage_errors": [                {
                "错误单词": "sample",
                 "原句引用": "This is a sample text.",
                 "修正形式": "This is a sample text.",
                 "错误原因解释": "错误原因解释"
                 
                 }

            ]
        }
    }
}

print(HandleApiResult.result2Markdown(test))