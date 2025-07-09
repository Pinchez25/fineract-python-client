# GetLoansTemplateResponse

GetLoansTemplateResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **int** |  | [optional] 
**client_name** | **str** |  | [optional] 
**client_office_id** | **int** |  | [optional] 
**product_options** | [**List[GetLoansTemplateProductOptions]**](GetLoansTemplateProductOptions.md) |  | [optional] 
**timeline** | [**GetLoansTemplateTimeline**](GetLoansTemplateTimeline.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_loans_template_response import GetLoansTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoansTemplateResponse from a JSON string
get_loans_template_response_instance = GetLoansTemplateResponse.from_json(json)
# print the JSON string representation of the object
print GetLoansTemplateResponse.to_json()

# convert the object into a dict
get_loans_template_response_dict = get_loans_template_response_instance.to_dict()
# create an instance of GetLoansTemplateResponse from a dict
get_loans_template_response_form_dict = get_loans_template_response.from_dict(get_loans_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


