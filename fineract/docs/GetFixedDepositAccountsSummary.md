# GetFixedDepositAccountsSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_balance** | **float** |  | [optional] 
**currency** | [**GetFixedDepositAccountsCurrency**](GetFixedDepositAccountsCurrency.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_fixed_deposit_accounts_summary import GetFixedDepositAccountsSummary

# TODO update the JSON string below
json = "{}"
# create an instance of GetFixedDepositAccountsSummary from a JSON string
get_fixed_deposit_accounts_summary_instance = GetFixedDepositAccountsSummary.from_json(json)
# print the JSON string representation of the object
print(GetFixedDepositAccountsSummary.to_json())

# convert the object into a dict
get_fixed_deposit_accounts_summary_dict = get_fixed_deposit_accounts_summary_instance.to_dict()
# create an instance of GetFixedDepositAccountsSummary from a dict
get_fixed_deposit_accounts_summary_from_dict = GetFixedDepositAccountsSummary.from_dict(get_fixed_deposit_accounts_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


