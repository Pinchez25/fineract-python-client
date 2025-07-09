# RateData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**percentage** | **float** |  | [optional] 
**product_apply** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 

## Example

```python
from fineract_client.models.rate_data import RateData

# TODO update the JSON string below
json = "{}"
# create an instance of RateData from a JSON string
rate_data_instance = RateData.from_json(json)
# print the JSON string representation of the object
print(RateData.to_json())

# convert the object into a dict
rate_data_dict = rate_data_instance.to_dict()
# create an instance of RateData from a dict
rate_data_from_dict = RateData.from_dict(rate_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


