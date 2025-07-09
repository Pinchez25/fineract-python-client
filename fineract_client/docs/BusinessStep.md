# BusinessStep

BusinessStep

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order** | **int** |  | [optional] 
**step_name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.business_step import BusinessStep

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessStep from a JSON string
business_step_instance = BusinessStep.from_json(json)
# print the JSON string representation of the object
print(BusinessStep.to_json())

# convert the object into a dict
business_step_dict = business_step_instance.to_dict()
# create an instance of BusinessStep from a dict
business_step_from_dict = BusinessStep.from_dict(business_step_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


