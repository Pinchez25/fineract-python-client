# GetCentersTemplateResponse

GetCentersTemplateResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activation_date** | **date** |  | [optional] 
**active** | **bool** |  | [optional] 
**office_id** | **int** |  | [optional] 
**office_options** | [**List[GetCentersOfficeOptions]**](GetCentersOfficeOptions.md) |  | [optional] 
**staff_options** | [**List[GetCentersStaffOptions]**](GetCentersStaffOptions.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_centers_template_response import GetCentersTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetCentersTemplateResponse from a JSON string
get_centers_template_response_instance = GetCentersTemplateResponse.from_json(json)
# print the JSON string representation of the object
print(GetCentersTemplateResponse.to_json())

# convert the object into a dict
get_centers_template_response_dict = get_centers_template_response_instance.to_dict()
# create an instance of GetCentersTemplateResponse from a dict
get_centers_template_response_from_dict = GetCentersTemplateResponse.from_dict(get_centers_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


