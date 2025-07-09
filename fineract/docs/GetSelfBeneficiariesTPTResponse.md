# GetSelfBeneficiariesTPTResponse

GetSelfBeneficiariesTPTResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_number** | **int** |  | [optional] 
**account_type** | [**GetSelfBeneficiariesAccountOptions**](GetSelfBeneficiariesAccountOptions.md) |  | [optional] 
**client_name** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**office_name** | **str** |  | [optional] 
**transfer_limit** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_self_beneficiaries_tpt_response import GetSelfBeneficiariesTPTResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSelfBeneficiariesTPTResponse from a JSON string
get_self_beneficiaries_tpt_response_instance = GetSelfBeneficiariesTPTResponse.from_json(json)
# print the JSON string representation of the object
print(GetSelfBeneficiariesTPTResponse.to_json())

# convert the object into a dict
get_self_beneficiaries_tpt_response_dict = get_self_beneficiaries_tpt_response_instance.to_dict()
# create an instance of GetSelfBeneficiariesTPTResponse from a dict
get_self_beneficiaries_tpt_response_from_dict = GetSelfBeneficiariesTPTResponse.from_dict(get_self_beneficiaries_tpt_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


