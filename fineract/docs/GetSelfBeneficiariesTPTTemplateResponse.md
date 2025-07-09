# GetSelfBeneficiariesTPTTemplateResponse

GetSelfBeneficiariesTPTTemplateResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_type_options** | [**List[GetSelfBeneficiariesAccountOptions]**](GetSelfBeneficiariesAccountOptions.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_self_beneficiaries_tpt_template_response import GetSelfBeneficiariesTPTTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSelfBeneficiariesTPTTemplateResponse from a JSON string
get_self_beneficiaries_tpt_template_response_instance = GetSelfBeneficiariesTPTTemplateResponse.from_json(json)
# print the JSON string representation of the object
print GetSelfBeneficiariesTPTTemplateResponse.to_json()

# convert the object into a dict
get_self_beneficiaries_tpt_template_response_dict = get_self_beneficiaries_tpt_template_response_instance.to_dict()
# create an instance of GetSelfBeneficiariesTPTTemplateResponse from a dict
get_self_beneficiaries_tpt_template_response_form_dict = get_self_beneficiaries_tpt_template_response.from_dict(get_self_beneficiaries_tpt_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


