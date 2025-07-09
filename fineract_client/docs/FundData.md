# FundData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.fund_data import FundData

# TODO update the JSON string below
json = "{}"
# create an instance of FundData from a JSON string
fund_data_instance = FundData.from_json(json)
# print the JSON string representation of the object
print(FundData.to_json())

# convert the object into a dict
fund_data_dict = fund_data_instance.to_dict()
# create an instance of FundData from a dict
fund_data_from_dict = FundData.from_dict(fund_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


