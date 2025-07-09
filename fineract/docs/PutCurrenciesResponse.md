# PutCurrenciesResponse

PutCurrenciesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currencies** | **List[str]** |  | [optional] 

## Example

```python
from fineract_client.models.put_currencies_response import PutCurrenciesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PutCurrenciesResponse from a JSON string
put_currencies_response_instance = PutCurrenciesResponse.from_json(json)
# print the JSON string representation of the object
print(PutCurrenciesResponse.to_json())

# convert the object into a dict
put_currencies_response_dict = put_currencies_response_instance.to_dict()
# create an instance of PutCurrenciesResponse from a dict
put_currencies_response_from_dict = PutCurrenciesResponse.from_dict(put_currencies_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


