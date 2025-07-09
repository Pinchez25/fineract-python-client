# FloatingRateData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**base_lending_rate** | **bool** |  | [optional] 
**created_by** | **str** |  | [optional] 
**created_on** | **datetime** |  | [optional] 
**id** | **int** |  | [optional] 
**modified_by** | **str** |  | [optional] 
**modified_on** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**rate_periods** | [**List[FloatingRatePeriodData]**](FloatingRatePeriodData.md) |  | [optional] 

## Example

```python
from fineract_client.models.floating_rate_data import FloatingRateData

# TODO update the JSON string below
json = "{}"
# create an instance of FloatingRateData from a JSON string
floating_rate_data_instance = FloatingRateData.from_json(json)
# print the JSON string representation of the object
print FloatingRateData.to_json()

# convert the object into a dict
floating_rate_data_dict = floating_rate_data_instance.to_dict()
# create an instance of FloatingRateData from a dict
floating_rate_data_form_dict = floating_rate_data.from_dict(floating_rate_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


