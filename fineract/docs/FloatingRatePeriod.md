# FloatingRatePeriod


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**created_by** | **int** |  | 
**created_date** | **datetime** |  | 
**created_date_time** | **datetime** |  | 
**differential_to_base_lending_rate** | **bool** |  | [optional] 
**floating_rate** | [**FloatingRate**](FloatingRate.md) |  | [optional] 
**from_date** | **date** |  | [optional] 
**id** | **int** |  | [optional] 
**interest_rate** | **float** |  | [optional] 
**last_modified_by** | **int** |  | 
**last_modified_date** | **datetime** |  | 
**last_modified_date_time** | **datetime** |  | 
**new** | **bool** |  | [optional] 

## Example

```python
from fineract_client.models.floating_rate_period import FloatingRatePeriod

# TODO update the JSON string below
json = "{}"
# create an instance of FloatingRatePeriod from a JSON string
floating_rate_period_instance = FloatingRatePeriod.from_json(json)
# print the JSON string representation of the object
print(FloatingRatePeriod.to_json())

# convert the object into a dict
floating_rate_period_dict = floating_rate_period_instance.to_dict()
# create an instance of FloatingRatePeriod from a dict
floating_rate_period_from_dict = FloatingRatePeriod.from_dict(floating_rate_period_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


