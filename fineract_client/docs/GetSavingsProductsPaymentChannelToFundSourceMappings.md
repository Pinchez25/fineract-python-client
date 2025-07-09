# GetSavingsProductsPaymentChannelToFundSourceMappings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fund_source_account** | [**GetSavingsProductsFundSourceAccount**](GetSavingsProductsFundSourceAccount.md) |  | [optional] 
**payment_type** | [**GetSavingsProductsPaymentType**](GetSavingsProductsPaymentType.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_savings_products_payment_channel_to_fund_source_mappings import GetSavingsProductsPaymentChannelToFundSourceMappings

# TODO update the JSON string below
json = "{}"
# create an instance of GetSavingsProductsPaymentChannelToFundSourceMappings from a JSON string
get_savings_products_payment_channel_to_fund_source_mappings_instance = GetSavingsProductsPaymentChannelToFundSourceMappings.from_json(json)
# print the JSON string representation of the object
print(GetSavingsProductsPaymentChannelToFundSourceMappings.to_json())

# convert the object into a dict
get_savings_products_payment_channel_to_fund_source_mappings_dict = get_savings_products_payment_channel_to_fund_source_mappings_instance.to_dict()
# create an instance of GetSavingsProductsPaymentChannelToFundSourceMappings from a dict
get_savings_products_payment_channel_to_fund_source_mappings_from_dict = GetSavingsProductsPaymentChannelToFundSourceMappings.from_dict(get_savings_products_payment_channel_to_fund_source_mappings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


