# PostAccountingRulesRequest

PostAccountingRulesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_to_credit** | **int** |  | [optional] 
**account_to_debit** | **int** |  | [optional] 
**description** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**office_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_accounting_rules_request import PostAccountingRulesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostAccountingRulesRequest from a JSON string
post_accounting_rules_request_instance = PostAccountingRulesRequest.from_json(json)
# print the JSON string representation of the object
print(PostAccountingRulesRequest.to_json())

# convert the object into a dict
post_accounting_rules_request_dict = post_accounting_rules_request_instance.to_dict()
# create an instance of PostAccountingRulesRequest from a dict
post_accounting_rules_request_from_dict = PostAccountingRulesRequest.from_dict(post_accounting_rules_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


