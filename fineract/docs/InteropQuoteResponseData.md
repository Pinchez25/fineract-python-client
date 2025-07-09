# InteropQuoteResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | **Dict[str, object]** |  | [optional] 
**client_id** | **int** |  | [optional] 
**command_id** | **int** |  | [optional] 
**credit_bureau_report_data** | **Dict[str, object]** |  | [optional] 
**expiration** | **str** |  | [optional] 
**extension_list** | [**List[ExtensionData]**](ExtensionData.md) |  | [optional] 
**fsp_commission** | [**MoneyData**](MoneyData.md) |  | [optional] 
**fsp_fee** | [**MoneyData**](MoneyData.md) |  | [optional] 
**glim_id** | **int** |  | [optional] 
**group_id** | **int** |  | [optional] 
**gsim_id** | **int** |  | [optional] 
**loan_id** | **int** |  | [optional] 
**office_id** | **int** |  | [optional] 
**product_id** | **int** |  | [optional] 
**quote_code** | **str** |  | 
**resource_external_id** | [**ExternalId**](ExternalId.md) |  | [optional] 
**resource_id** | **int** |  | [optional] 
**resource_identifier** | **str** |  | [optional] 
**rollback_transaction** | **bool** |  | [optional] 
**savings_id** | **int** |  | [optional] 
**state** | **str** |  | 
**sub_resource_external_id** | [**ExternalId**](ExternalId.md) |  | [optional] 
**sub_resource_id** | **int** |  | [optional] 
**transaction_code** | **str** |  | 
**transaction_id** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.interop_quote_response_data import InteropQuoteResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of InteropQuoteResponseData from a JSON string
interop_quote_response_data_instance = InteropQuoteResponseData.from_json(json)
# print the JSON string representation of the object
print InteropQuoteResponseData.to_json()

# convert the object into a dict
interop_quote_response_data_dict = interop_quote_response_data_instance.to_dict()
# create an instance of InteropQuoteResponseData from a dict
interop_quote_response_data_form_dict = interop_quote_response_data.from_dict(interop_quote_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


