# PaymentTypeToGLAccountMapper


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fund_source_account** | [**GLAccountData**](GLAccountData.md) |  | [optional] 
**payment_type** | [**PaymentTypeData**](PaymentTypeData.md) |  | [optional] 

## Example

```python
from fineract_client.models.payment_type_to_gl_account_mapper import PaymentTypeToGLAccountMapper

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentTypeToGLAccountMapper from a JSON string
payment_type_to_gl_account_mapper_instance = PaymentTypeToGLAccountMapper.from_json(json)
# print the JSON string representation of the object
print(PaymentTypeToGLAccountMapper.to_json())

# convert the object into a dict
payment_type_to_gl_account_mapper_dict = payment_type_to_gl_account_mapper_instance.to_dict()
# create an instance of PaymentTypeToGLAccountMapper from a dict
payment_type_to_gl_account_mapper_from_dict = PaymentTypeToGLAccountMapper.from_dict(payment_type_to_gl_account_mapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


