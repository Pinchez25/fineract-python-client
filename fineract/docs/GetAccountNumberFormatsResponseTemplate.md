# GetAccountNumberFormatsResponseTemplate

GetAccountNumberFormatsResponseTemplate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_type_options** | [**List[EnumOptionData]**](EnumOptionData.md) |  | [optional] 
**prefix_type_options** | **Dict[str, List[EnumOptionData]]** |  | [optional] 

## Example

```python
from fineract_client.models.get_account_number_formats_response_template import GetAccountNumberFormatsResponseTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountNumberFormatsResponseTemplate from a JSON string
get_account_number_formats_response_template_instance = GetAccountNumberFormatsResponseTemplate.from_json(json)
# print the JSON string representation of the object
print GetAccountNumberFormatsResponseTemplate.to_json()

# convert the object into a dict
get_account_number_formats_response_template_dict = get_account_number_formats_response_template_instance.to_dict()
# create an instance of GetAccountNumberFormatsResponseTemplate from a dict
get_account_number_formats_response_template_form_dict = get_account_number_formats_response_template.from_dict(get_account_number_formats_response_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


