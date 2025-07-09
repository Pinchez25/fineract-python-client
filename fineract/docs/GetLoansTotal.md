# GetLoansTotal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | [optional] 
**currency_code** | **str** |  | [optional] 
**default_name** | **str** |  | [optional] 
**digits_after_decimal** | **int** |  | [optional] 
**display_symbol** | **str** |  | [optional] 
**display_symbol_value** | **str** |  | [optional] 
**greater_than_zero** | **bool** |  | [optional] 
**in_multiples_of** | **int** |  | [optional] 
**name_code** | **str** |  | [optional] 
**zero** | **bool** |  | [optional] 

## Example

```python
from fineract_client.models.get_loans_total import GetLoansTotal

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoansTotal from a JSON string
get_loans_total_instance = GetLoansTotal.from_json(json)
# print the JSON string representation of the object
print GetLoansTotal.to_json()

# convert the object into a dict
get_loans_total_dict = get_loans_total_instance.to_dict()
# create an instance of GetLoansTotal from a dict
get_loans_total_form_dict = get_loans_total.from_dict(get_loans_total_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


