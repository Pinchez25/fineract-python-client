# CashierData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**end_date** | **date** |  | [optional] 
**end_time** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**is_full_day** | **bool** |  | [optional] 
**office_id** | **int** |  | [optional] 
**office_name** | **str** |  | [optional] 
**staff_id** | **int** |  | [optional] 
**staff_name** | **str** |  | [optional] 
**staff_options** | [**List[StaffData]**](StaffData.md) |  | [optional] 
**start_date** | **date** |  | [optional] 
**start_time** | **str** |  | [optional] 
**teller_id** | **int** |  | [optional] 
**teller_name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.cashier_data import CashierData

# TODO update the JSON string below
json = "{}"
# create an instance of CashierData from a JSON string
cashier_data_instance = CashierData.from_json(json)
# print the JSON string representation of the object
print CashierData.to_json()

# convert the object into a dict
cashier_data_dict = cashier_data_instance.to_dict()
# create an instance of CashierData from a dict
cashier_data_form_dict = cashier_data.from_dict(cashier_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


