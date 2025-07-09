# GetSavingsAccountChargesPaidByData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | [optional] 
**charge_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_savings_account_charges_paid_by_data import GetSavingsAccountChargesPaidByData

# TODO update the JSON string below
json = "{}"
# create an instance of GetSavingsAccountChargesPaidByData from a JSON string
get_savings_account_charges_paid_by_data_instance = GetSavingsAccountChargesPaidByData.from_json(json)
# print the JSON string representation of the object
print GetSavingsAccountChargesPaidByData.to_json()

# convert the object into a dict
get_savings_account_charges_paid_by_data_dict = get_savings_account_charges_paid_by_data_instance.to_dict()
# create an instance of GetSavingsAccountChargesPaidByData from a dict
get_savings_account_charges_paid_by_data_form_dict = get_savings_account_charges_paid_by_data.from_dict(get_savings_account_charges_paid_by_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


