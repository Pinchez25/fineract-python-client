# DeleteAccountingRulesResponse

DeleteAccountingRulesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.delete_accounting_rules_response import DeleteAccountingRulesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteAccountingRulesResponse from a JSON string
delete_accounting_rules_response_instance = DeleteAccountingRulesResponse.from_json(json)
# print the JSON string representation of the object
print DeleteAccountingRulesResponse.to_json()

# convert the object into a dict
delete_accounting_rules_response_dict = delete_accounting_rules_response_instance.to_dict()
# create an instance of DeleteAccountingRulesResponse from a dict
delete_accounting_rules_response_form_dict = delete_accounting_rules_response.from_dict(delete_accounting_rules_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


