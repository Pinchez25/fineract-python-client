# GetClientsTemplateResponse

GetClientsTemplateResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activation_date** | **date** |  | [optional] 
**datatables** | [**List[GetClientsDataTables]**](GetClientsDataTables.md) |  | [optional] 
**office_id** | **int** |  | [optional] 
**office_options** | [**List[GetClientsOfficeOptions]**](GetClientsOfficeOptions.md) |  | [optional] 
**saving_product_options** | [**List[GetClientsSavingProductOptions]**](GetClientsSavingProductOptions.md) |  | [optional] 
**staff_options** | [**List[GetClientsStaffOptions]**](GetClientsStaffOptions.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_clients_template_response import GetClientsTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetClientsTemplateResponse from a JSON string
get_clients_template_response_instance = GetClientsTemplateResponse.from_json(json)
# print the JSON string representation of the object
print(GetClientsTemplateResponse.to_json())

# convert the object into a dict
get_clients_template_response_dict = get_clients_template_response_instance.to_dict()
# create an instance of GetClientsTemplateResponse from a dict
get_clients_template_response_from_dict = GetClientsTemplateResponse.from_dict(get_clients_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


