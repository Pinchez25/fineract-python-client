# GetEntityDatatableChecksTemplateResponse

GetEntityDatatableChecksTemplateResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datatables** | **List[object]** |  | [optional] 
**entities** | **List[str]** |  | [optional] 
**loan_product_datas** | [**List[LoanProductData]**](LoanProductData.md) |  | [optional] 
**savings_product_datas** | [**List[SavingsProductData]**](SavingsProductData.md) |  | [optional] 
**status_client** | **List[object]** |  | [optional] 
**status_group** | **List[object]** |  | [optional] 
**status_loans** | **List[object]** |  | [optional] 
**status_savings** | **List[object]** |  | [optional] 

## Example

```python
from fineract_client.models.get_entity_datatable_checks_template_response import GetEntityDatatableChecksTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetEntityDatatableChecksTemplateResponse from a JSON string
get_entity_datatable_checks_template_response_instance = GetEntityDatatableChecksTemplateResponse.from_json(json)
# print the JSON string representation of the object
print GetEntityDatatableChecksTemplateResponse.to_json()

# convert the object into a dict
get_entity_datatable_checks_template_response_dict = get_entity_datatable_checks_template_response_instance.to_dict()
# create an instance of GetEntityDatatableChecksTemplateResponse from a dict
get_entity_datatable_checks_template_response_form_dict = get_entity_datatable_checks_template_response.from_dict(get_entity_datatable_checks_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


