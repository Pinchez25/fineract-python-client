# GetLoanPaymentChannelToFundSourceMappings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fund_source_account_id** | **int** |  | [optional] 
**payment_type_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_loan_payment_channel_to_fund_source_mappings import GetLoanPaymentChannelToFundSourceMappings

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoanPaymentChannelToFundSourceMappings from a JSON string
get_loan_payment_channel_to_fund_source_mappings_instance = GetLoanPaymentChannelToFundSourceMappings.from_json(json)
# print the JSON string representation of the object
print GetLoanPaymentChannelToFundSourceMappings.to_json()

# convert the object into a dict
get_loan_payment_channel_to_fund_source_mappings_dict = get_loan_payment_channel_to_fund_source_mappings_instance.to_dict()
# create an instance of GetLoanPaymentChannelToFundSourceMappings from a dict
get_loan_payment_channel_to_fund_source_mappings_form_dict = get_loan_payment_channel_to_fund_source_mappings.from_dict(get_loan_payment_channel_to_fund_source_mappings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


