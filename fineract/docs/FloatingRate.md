# FloatingRate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**base_lending_rate** | **bool** |  | [optional] 
**created_by** | **int** |  | 
**created_date** | **datetime** |  | 
**created_date_time** | **datetime** |  | 
**floating_rate_periods** | [**List[FloatingRatePeriod]**](FloatingRatePeriod.md) |  | [optional] 
**id** | **int** |  | [optional] 
**last_modified_by** | **int** |  | 
**last_modified_date** | **datetime** |  | 
**last_modified_date_time** | **datetime** |  | 
**name** | **str** |  | [optional] 
**new** | **bool** |  | [optional] 

## Example

```python
from fineract_client.models.floating_rate import FloatingRate

# TODO update the JSON string below
json = "{}"
# create an instance of FloatingRate from a JSON string
floating_rate_instance = FloatingRate.from_json(json)
# print the JSON string representation of the object
print FloatingRate.to_json()

# convert the object into a dict
floating_rate_dict = floating_rate_instance.to_dict()
# create an instance of FloatingRate from a dict
floating_rate_form_dict = floating_rate.from_dict(floating_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


