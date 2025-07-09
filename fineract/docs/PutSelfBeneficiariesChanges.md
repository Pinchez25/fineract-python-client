# PutSelfBeneficiariesChanges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**transfer_limit** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_self_beneficiaries_changes import PutSelfBeneficiariesChanges

# TODO update the JSON string below
json = "{}"
# create an instance of PutSelfBeneficiariesChanges from a JSON string
put_self_beneficiaries_changes_instance = PutSelfBeneficiariesChanges.from_json(json)
# print the JSON string representation of the object
print(PutSelfBeneficiariesChanges.to_json())

# convert the object into a dict
put_self_beneficiaries_changes_dict = put_self_beneficiaries_changes_instance.to_dict()
# create an instance of PutSelfBeneficiariesChanges from a dict
put_self_beneficiaries_changes_from_dict = PutSelfBeneficiariesChanges.from_dict(put_self_beneficiaries_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


