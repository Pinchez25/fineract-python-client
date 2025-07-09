# GetTaxesComponentsResponse

GetTaxesComponentsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credit_account** | [**GetTaxesComponentsCreditAccount**](GetTaxesComponentsCreditAccount.md) |  | [optional] 
**credit_account_type** | [**GetTaxesComponentsCreditAccountType**](GetTaxesComponentsCreditAccountType.md) |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**percentage** | **float** |  | [optional] 
**start_date** | **date** |  | [optional] 
**tax_components_histories** | **List[object]** |  | [optional] 

## Example

```python
from fineract_client.models.get_taxes_components_response import GetTaxesComponentsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTaxesComponentsResponse from a JSON string
get_taxes_components_response_instance = GetTaxesComponentsResponse.from_json(json)
# print the JSON string representation of the object
print GetTaxesComponentsResponse.to_json()

# convert the object into a dict
get_taxes_components_response_dict = get_taxes_components_response_instance.to_dict()
# create an instance of GetTaxesComponentsResponse from a dict
get_taxes_components_response_form_dict = get_taxes_components_response.from_dict(get_taxes_components_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


