# ClientCollateralManagementData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**pct_to_base** | **float** |  | [optional] 
**quantity** | **float** |  | [optional] 
**total** | **float** |  | [optional] 
**total_collateral** | **float** |  | [optional] 
**unit_price** | **float** |  | [optional] 

## Example

```python
from fineract_client.models.client_collateral_management_data import ClientCollateralManagementData

# TODO update the JSON string below
json = "{}"
# create an instance of ClientCollateralManagementData from a JSON string
client_collateral_management_data_instance = ClientCollateralManagementData.from_json(json)
# print the JSON string representation of the object
print(ClientCollateralManagementData.to_json())

# convert the object into a dict
client_collateral_management_data_dict = client_collateral_management_data_instance.to_dict()
# create an instance of ClientCollateralManagementData from a dict
client_collateral_management_data_from_dict = ClientCollateralManagementData.from_dict(client_collateral_management_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


