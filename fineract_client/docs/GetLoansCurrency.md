# GetLoansCurrency


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**decimal_places** | **int** |  | [optional] 
**display_label** | **str** |  | [optional] 
**display_symbol** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**name_code** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_loans_currency import GetLoansCurrency

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoansCurrency from a JSON string
get_loans_currency_instance = GetLoansCurrency.from_json(json)
# print the JSON string representation of the object
print(GetLoansCurrency.to_json())

# convert the object into a dict
get_loans_currency_dict = get_loans_currency_instance.to_dict()
# create an instance of GetLoansCurrency from a dict
get_loans_currency_from_dict = GetLoansCurrency.from_dict(get_loans_currency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


