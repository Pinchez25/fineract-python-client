# GetTranscationEnumData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_hold** | **bool** |  | [optional] 
**amount_release** | **bool** |  | [optional] 
**approve_transfer** | **bool** |  | [optional] 
**code** | **str** |  | [optional] 
**deposit** | **bool** |  | [optional] 
**dividend_payout** | **bool** |  | [optional] 
**escheat** | **bool** |  | [optional] 
**fee_deduction** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**initiate_transfer** | **bool** |  | [optional] 
**interest_posting** | **bool** |  | [optional] 
**overdraft_fee** | **bool** |  | [optional] 
**overdraft_interest** | **bool** |  | [optional] 
**reject_transfer** | **bool** |  | [optional] 
**value** | **str** |  | [optional] 
**withdraw_transfer** | **bool** |  | [optional] 
**withdrawal** | **bool** |  | [optional] 
**withhold_tax** | **bool** |  | [optional] 
**writtenoff** | **bool** |  | [optional] 

## Example

```python
from fineract_client.models.get_transcation_enum_data import GetTranscationEnumData

# TODO update the JSON string below
json = "{}"
# create an instance of GetTranscationEnumData from a JSON string
get_transcation_enum_data_instance = GetTranscationEnumData.from_json(json)
# print the JSON string representation of the object
print(GetTranscationEnumData.to_json())

# convert the object into a dict
get_transcation_enum_data_dict = get_transcation_enum_data_instance.to_dict()
# create an instance of GetTranscationEnumData from a dict
get_transcation_enum_data_from_dict = GetTranscationEnumData.from_dict(get_transcation_enum_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


