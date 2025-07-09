# GetSelfLoansTemplateResponse

GetSelfLoansTemplateResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **int** |  | [optional] 
**client_name** | **str** |  | [optional] 
**client_office_id** | **int** |  | [optional] 
**product_options** | [**List[GetSelfLoansProductOptions]**](GetSelfLoansProductOptions.md) |  | [optional] 
**timeline** | [**GetSelfLoansTimeline**](GetSelfLoansTimeline.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_self_loans_template_response import GetSelfLoansTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSelfLoansTemplateResponse from a JSON string
get_self_loans_template_response_instance = GetSelfLoansTemplateResponse.from_json(json)
# print the JSON string representation of the object
print(GetSelfLoansTemplateResponse.to_json())

# convert the object into a dict
get_self_loans_template_response_dict = get_self_loans_template_response_instance.to_dict()
# create an instance of GetSelfLoansTemplateResponse from a dict
get_self_loans_template_response_from_dict = GetSelfLoansTemplateResponse.from_dict(get_self_loans_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


