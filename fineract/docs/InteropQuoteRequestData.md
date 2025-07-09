# InteropQuoteRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | 
**amount** | [**MoneyData**](MoneyData.md) |  | 
**amount_type** | **str** |  | 
**expiration** | **datetime** |  | [optional] 
**expiration_local_date** | **date** |  | [optional] 
**extension_list** | [**List[ExtensionData]**](ExtensionData.md) |  | [optional] 
**fees** | [**MoneyData**](MoneyData.md) |  | [optional] 
**geo_code** | [**GeoCodeData**](GeoCodeData.md) |  | [optional] 
**note** | **str** |  | [optional] 
**quote_code** | **str** |  | 
**request_code** | **str** |  | [optional] 
**transaction_code** | **str** |  | 
**transaction_role** | **str** |  | 
**transaction_type** | [**InteropTransactionTypeData**](InteropTransactionTypeData.md) |  | [optional] 

## Example

```python
from fineract_client.models.interop_quote_request_data import InteropQuoteRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of InteropQuoteRequestData from a JSON string
interop_quote_request_data_instance = InteropQuoteRequestData.from_json(json)
# print the JSON string representation of the object
print(InteropQuoteRequestData.to_json())

# convert the object into a dict
interop_quote_request_data_dict = interop_quote_request_data_instance.to_dict()
# create an instance of InteropQuoteRequestData from a dict
interop_quote_request_data_from_dict = InteropQuoteRequestData.from_dict(interop_quote_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


