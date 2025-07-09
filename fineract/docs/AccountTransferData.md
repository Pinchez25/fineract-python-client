# AccountTransferData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | [**CurrencyData**](CurrencyData.md) |  | [optional] 
**from_account** | [**PortfolioAccountData**](PortfolioAccountData.md) |  | [optional] 
**from_account_options** | [**List[PortfolioAccountData]**](PortfolioAccountData.md) |  | [optional] 
**from_account_type** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 
**from_account_type_options** | [**List[EnumOptionData]**](EnumOptionData.md) |  | [optional] 
**from_client** | [**ClientData**](ClientData.md) |  | [optional] 
**from_client_options** | [**List[ClientData]**](ClientData.md) |  | [optional] 
**from_office** | [**OfficeData**](OfficeData.md) |  | [optional] 
**from_office_options** | [**List[OfficeData]**](OfficeData.md) |  | [optional] 
**id** | **int** |  | [optional] 
**reversed** | **bool** |  | [optional] 
**to_account** | [**PortfolioAccountData**](PortfolioAccountData.md) |  | [optional] 
**to_account_options** | [**List[PortfolioAccountData]**](PortfolioAccountData.md) |  | [optional] 
**to_account_type** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 
**to_account_type_options** | [**List[EnumOptionData]**](EnumOptionData.md) |  | [optional] 
**to_client** | [**ClientData**](ClientData.md) |  | [optional] 
**to_client_options** | [**List[ClientData]**](ClientData.md) |  | [optional] 
**to_office** | [**OfficeData**](OfficeData.md) |  | [optional] 
**to_office_options** | [**List[OfficeData]**](OfficeData.md) |  | [optional] 
**transfer_amount** | **float** |  | [optional] 
**transfer_date** | **date** |  | [optional] 
**transfer_description** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.account_transfer_data import AccountTransferData

# TODO update the JSON string below
json = "{}"
# create an instance of AccountTransferData from a JSON string
account_transfer_data_instance = AccountTransferData.from_json(json)
# print the JSON string representation of the object
print AccountTransferData.to_json()

# convert the object into a dict
account_transfer_data_dict = account_transfer_data_instance.to_dict()
# create an instance of AccountTransferData from a dict
account_transfer_data_form_dict = account_transfer_data.from_dict(account_transfer_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


