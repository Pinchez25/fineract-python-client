# GetTellersTellerIdCashiersTemplateResponse

GetTellersTellerIdCashiersTemplateResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**office_id** | **int** |  | [optional] 
**office_name** | **str** |  | [optional] 
**staff_options** | [**List[StaffData]**](StaffData.md) |  | [optional] 
**teller_id** | **int** |  | [optional] 
**teller_name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_tellers_teller_id_cashiers_template_response import GetTellersTellerIdCashiersTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTellersTellerIdCashiersTemplateResponse from a JSON string
get_tellers_teller_id_cashiers_template_response_instance = GetTellersTellerIdCashiersTemplateResponse.from_json(json)
# print the JSON string representation of the object
print GetTellersTellerIdCashiersTemplateResponse.to_json()

# convert the object into a dict
get_tellers_teller_id_cashiers_template_response_dict = get_tellers_teller_id_cashiers_template_response_instance.to_dict()
# create an instance of GetTellersTellerIdCashiersTemplateResponse from a dict
get_tellers_teller_id_cashiers_template_response_form_dict = get_tellers_teller_id_cashiers_template_response.from_dict(get_tellers_teller_id_cashiers_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


