# SavingsAccountChargesPaidByData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | [optional] 
**charge_id** | **int** |  | [optional] 
**fee_charge** | **bool** |  | [optional] 
**penalty_charge** | **bool** |  | [optional] 
**savings_account_charge_data** | [**SavingsAccountChargeData**](SavingsAccountChargeData.md) |  | [optional] 

## Example

```python
from fineract_client.models.savings_account_charges_paid_by_data import SavingsAccountChargesPaidByData

# TODO update the JSON string below
json = "{}"
# create an instance of SavingsAccountChargesPaidByData from a JSON string
savings_account_charges_paid_by_data_instance = SavingsAccountChargesPaidByData.from_json(json)
# print the JSON string representation of the object
print SavingsAccountChargesPaidByData.to_json()

# convert the object into a dict
savings_account_charges_paid_by_data_dict = savings_account_charges_paid_by_data_instance.to_dict()
# create an instance of SavingsAccountChargesPaidByData from a dict
savings_account_charges_paid_by_data_form_dict = savings_account_charges_paid_by_data.from_dict(savings_account_charges_paid_by_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


