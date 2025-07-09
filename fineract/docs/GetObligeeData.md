# GetObligeeData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_number** | **str** |  | [optional] 
**amount_released** | **float** |  | [optional] 
**amount_transferred** | **float** |  | [optional] 
**display_name** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**guarantee_amount** | **float** |  | [optional] 
**last_name** | **str** |  | [optional] 
**loan_amount** | **float** |  | [optional] 

## Example

```python
from fineract_client.models.get_obligee_data import GetObligeeData

# TODO update the JSON string below
json = "{}"
# create an instance of GetObligeeData from a JSON string
get_obligee_data_instance = GetObligeeData.from_json(json)
# print the JSON string representation of the object
print GetObligeeData.to_json()

# convert the object into a dict
get_obligee_data_dict = get_obligee_data_instance.to_dict()
# create an instance of GetObligeeData from a dict
get_obligee_data_form_dict = get_obligee_data.from_dict(get_obligee_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


