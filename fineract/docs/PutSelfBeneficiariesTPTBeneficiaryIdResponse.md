# PutSelfBeneficiariesTPTBeneficiaryIdResponse

PutSelfBeneficiariesTPTBeneficiaryIdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**PutSelfBeneficiariesChanges**](PutSelfBeneficiariesChanges.md) |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_self_beneficiaries_tpt_beneficiary_id_response import PutSelfBeneficiariesTPTBeneficiaryIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PutSelfBeneficiariesTPTBeneficiaryIdResponse from a JSON string
put_self_beneficiaries_tpt_beneficiary_id_response_instance = PutSelfBeneficiariesTPTBeneficiaryIdResponse.from_json(json)
# print the JSON string representation of the object
print(PutSelfBeneficiariesTPTBeneficiaryIdResponse.to_json())

# convert the object into a dict
put_self_beneficiaries_tpt_beneficiary_id_response_dict = put_self_beneficiaries_tpt_beneficiary_id_response_instance.to_dict()
# create an instance of PutSelfBeneficiariesTPTBeneficiaryIdResponse from a dict
put_self_beneficiaries_tpt_beneficiary_id_response_from_dict = PutSelfBeneficiariesTPTBeneficiaryIdResponse.from_dict(put_self_beneficiaries_tpt_beneficiary_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


