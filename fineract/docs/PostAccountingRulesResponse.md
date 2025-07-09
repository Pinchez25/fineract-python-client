# PostAccountingRulesResponse

PostAccountingRulesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**office_id** | **int** |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_accounting_rules_response import PostAccountingRulesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostAccountingRulesResponse from a JSON string
post_accounting_rules_response_instance = PostAccountingRulesResponse.from_json(json)
# print the JSON string representation of the object
print PostAccountingRulesResponse.to_json()

# convert the object into a dict
post_accounting_rules_response_dict = post_accounting_rules_response_instance.to_dict()
# create an instance of PostAccountingRulesResponse from a dict
post_accounting_rules_response_form_dict = post_accounting_rules_response.from_dict(post_accounting_rules_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


