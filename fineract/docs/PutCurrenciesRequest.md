# PutCurrenciesRequest

PutCurrenciesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currencies** | **List[str]** |  | [optional] 

## Example

```python
from fineract_client.models.put_currencies_request import PutCurrenciesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutCurrenciesRequest from a JSON string
put_currencies_request_instance = PutCurrenciesRequest.from_json(json)
# print the JSON string representation of the object
print(PutCurrenciesRequest.to_json())

# convert the object into a dict
put_currencies_request_dict = put_currencies_request_instance.to_dict()
# create an instance of PutCurrenciesRequest from a dict
put_currencies_request_from_dict = PutCurrenciesRequest.from_dict(put_currencies_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


