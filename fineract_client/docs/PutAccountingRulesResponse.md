# PutAccountingRulesResponse

PutAccountingRulesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**PutAccountingRulesResponsechangesSwagger**](PutAccountingRulesResponsechangesSwagger.md) |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_accounting_rules_response import PutAccountingRulesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PutAccountingRulesResponse from a JSON string
put_accounting_rules_response_instance = PutAccountingRulesResponse.from_json(json)
# print the JSON string representation of the object
print(PutAccountingRulesResponse.to_json())

# convert the object into a dict
put_accounting_rules_response_dict = put_accounting_rules_response_instance.to_dict()
# create an instance of PutAccountingRulesResponse from a dict
put_accounting_rules_response_from_dict = PutAccountingRulesResponse.from_dict(put_accounting_rules_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


