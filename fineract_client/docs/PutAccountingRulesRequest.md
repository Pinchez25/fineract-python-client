# PutAccountingRulesRequest

PutAccountingRulesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.put_accounting_rules_request import PutAccountingRulesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutAccountingRulesRequest from a JSON string
put_accounting_rules_request_instance = PutAccountingRulesRequest.from_json(json)
# print the JSON string representation of the object
print(PutAccountingRulesRequest.to_json())

# convert the object into a dict
put_accounting_rules_request_dict = put_accounting_rules_request_instance.to_dict()
# create an instance of PutAccountingRulesRequest from a dict
put_accounting_rules_request_from_dict = PutAccountingRulesRequest.from_dict(put_accounting_rules_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


