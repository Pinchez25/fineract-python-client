# GetIncomeFromFeeAccountId


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gl_code** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_income_from_fee_account_id import GetIncomeFromFeeAccountId

# TODO update the JSON string below
json = "{}"
# create an instance of GetIncomeFromFeeAccountId from a JSON string
get_income_from_fee_account_id_instance = GetIncomeFromFeeAccountId.from_json(json)
# print the JSON string representation of the object
print GetIncomeFromFeeAccountId.to_json()

# convert the object into a dict
get_income_from_fee_account_id_dict = get_income_from_fee_account_id_instance.to_dict()
# create an instance of GetIncomeFromFeeAccountId from a dict
get_income_from_fee_account_id_form_dict = get_income_from_fee_account_id.from_dict(get_income_from_fee_account_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


