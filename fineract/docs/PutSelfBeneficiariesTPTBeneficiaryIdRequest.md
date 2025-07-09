# PutSelfBeneficiariesTPTBeneficiaryIdRequest

PutSelfBeneficiariesTPTBeneficiaryIdRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**transfer_limit** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_self_beneficiaries_tpt_beneficiary_id_request import PutSelfBeneficiariesTPTBeneficiaryIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutSelfBeneficiariesTPTBeneficiaryIdRequest from a JSON string
put_self_beneficiaries_tpt_beneficiary_id_request_instance = PutSelfBeneficiariesTPTBeneficiaryIdRequest.from_json(json)
# print the JSON string representation of the object
print(PutSelfBeneficiariesTPTBeneficiaryIdRequest.to_json())

# convert the object into a dict
put_self_beneficiaries_tpt_beneficiary_id_request_dict = put_self_beneficiaries_tpt_beneficiary_id_request_instance.to_dict()
# create an instance of PutSelfBeneficiariesTPTBeneficiaryIdRequest from a dict
put_self_beneficiaries_tpt_beneficiary_id_request_from_dict = PutSelfBeneficiariesTPTBeneficiaryIdRequest.from_dict(put_self_beneficiaries_tpt_beneficiary_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


