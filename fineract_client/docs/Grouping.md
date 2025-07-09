# Grouping


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entities** | [**List[Entity]**](Entity.md) |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.grouping import Grouping

# TODO update the JSON string below
json = "{}"
# create an instance of Grouping from a JSON string
grouping_instance = Grouping.from_json(json)
# print the JSON string representation of the object
print(Grouping.to_json())

# convert the object into a dict
grouping_dict = grouping_instance.to_dict()
# create an instance of Grouping from a dict
grouping_from_dict = Grouping.from_dict(grouping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


