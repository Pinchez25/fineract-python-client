# PutSavingsChanges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**interest_rate** | **float** |  | [optional] 
**locale** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.put_savings_changes import PutSavingsChanges

# TODO update the JSON string below
json = "{}"
# create an instance of PutSavingsChanges from a JSON string
put_savings_changes_instance = PutSavingsChanges.from_json(json)
# print the JSON string representation of the object
print(PutSavingsChanges.to_json())

# convert the object into a dict
put_savings_changes_dict = put_savings_changes_instance.to_dict()
# create an instance of PutSavingsChanges from a dict
put_savings_changes_from_dict = PutSavingsChanges.from_dict(put_savings_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


