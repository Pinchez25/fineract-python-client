# LoanProductProvisioningEntryData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amountreserved** | **float** |  | [optional] 
**balance** | **float** |  | [optional] 
**category_id** | **int** |  | [optional] 
**category_name** | **str** |  | [optional] 
**criteria_id** | **int** |  | [optional] 
**currency_code** | **str** |  | [optional] 
**expense_account** | **int** |  | [optional] 
**expense_account_code** | **str** |  | [optional] 
**expense_account_name** | **str** |  | [optional] 
**history_id** | **int** |  | [optional] 
**liability_account_code** | **str** |  | [optional] 
**liability_account_name** | **str** |  | [optional] 
**liablity_account** | **int** |  | [optional] 
**office_id** | **int** |  | [optional] 
**office_name** | **str** |  | [optional] 
**overdue_in_days** | **int** |  | [optional] 
**percentage** | **float** |  | [optional] 
**product_id** | **int** |  | [optional] 
**product_name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.loan_product_provisioning_entry_data import LoanProductProvisioningEntryData

# TODO update the JSON string below
json = "{}"
# create an instance of LoanProductProvisioningEntryData from a JSON string
loan_product_provisioning_entry_data_instance = LoanProductProvisioningEntryData.from_json(json)
# print the JSON string representation of the object
print LoanProductProvisioningEntryData.to_json()

# convert the object into a dict
loan_product_provisioning_entry_data_dict = loan_product_provisioning_entry_data_instance.to_dict()
# create an instance of LoanProductProvisioningEntryData from a dict
loan_product_provisioning_entry_data_form_dict = loan_product_provisioning_entry_data.from_dict(loan_product_provisioning_entry_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


