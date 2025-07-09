# FloatingRatePeriodData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**created_by** | **str** |  | [optional] 
**created_on** | **datetime** |  | [optional] 
**differential_to_base_lending_rate** | **bool** |  | [optional] 
**from_date** | **date** |  | [optional] 
**from_date_as_local_date** | **date** |  | [optional] 
**id** | **int** |  | [optional] 
**interest_rate** | **float** |  | [optional] 
**modified_by** | **str** |  | [optional] 
**modified_on** | **datetime** |  | [optional] 

## Example

```python
from fineract_client.models.floating_rate_period_data import FloatingRatePeriodData

# TODO update the JSON string below
json = "{}"
# create an instance of FloatingRatePeriodData from a JSON string
floating_rate_period_data_instance = FloatingRatePeriodData.from_json(json)
# print the JSON string representation of the object
print(FloatingRatePeriodData.to_json())

# convert the object into a dict
floating_rate_period_data_dict = floating_rate_period_data_instance.to_dict()
# create an instance of FloatingRatePeriodData from a dict
floating_rate_period_data_from_dict = FloatingRatePeriodData.from_dict(floating_rate_period_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


