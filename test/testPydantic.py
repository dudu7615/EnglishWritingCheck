from pydantic import BaseModel, Field

class TestModel(BaseModel):
    id: int
    name: str
    age: int = Field(default=0, alias="age0")

test = TestModel(id=1, name="Alice", age0=30)
print(test)
test_dict = TestModel.model_validate({"id": 2, "name": "Bob", "age0": 25})
print(test_dict)
test_json = TestModel.model_validate_json('{"id": 3, "name": "Charlie", "age0": 20, "extra_field": "ignored"}')
print(test_json)

class TestModelList(BaseModel):
    items: list[int]
    models: list[TestModel]

test_list = TestModelList(items=[1, 2, 3], models=[test, test_dict, test_json])
print(test_list)
test_list_json = TestModelList.model_validate_json('{"items": [1, 2, 3], "models": [{"id": 1, "name": "Alice", "age0": 30}, {"id": 2, "name": "Bob", "age0": 25}, {"id": 3, "name": "Charlie", "age0": 20}]}')
print(test_list_json)
