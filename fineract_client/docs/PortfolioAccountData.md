# PortfolioAccountData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_no** | **str** |  | [optional] 
**amt_for_transfer** | **float** |  | [optional] 
**client_id** | **int** |  | [optional] 
**client_name** | **str** |  | [optional] 
**currency** | [**CurrencyData**](CurrencyData.md) |  | [optional] 
**currency_code** | **str** |  | [optional] 
**external_id** | **str** |  | [optional] 
**field_officer_id** | **int** |  | [optional] 
**field_officer_name** | **str** |  | [optional] 
**group_id** | **int** |  | [optional] 
**group_name** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**product_id** | **int** |  | [optional] 
**product_name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.portfolio_account_data import PortfolioAccountData

# TODO update the JSON string below
json = "{}"
# create an instance of PortfolioAccountData from a JSON string
portfolio_account_data_instance = PortfolioAccountData.from_json(json)
# print the JSON string representation of the object
print(PortfolioAccountData.to_json())

# convert the object into a dict
portfolio_account_data_dict = portfolio_account_data_instance.to_dict()
# create an instance of PortfolioAccountData from a dict
portfolio_account_data_from_dict = PortfolioAccountData.from_dict(portfolio_account_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


