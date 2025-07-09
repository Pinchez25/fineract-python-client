# ChargeToGLAccountMapper


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**charge** | [**ChargeData**](ChargeData.md) |  | [optional] 
**income_account** | [**GLAccountData**](GLAccountData.md) |  | [optional] 

## Example

```python
from fineract_client.models.charge_to_gl_account_mapper import ChargeToGLAccountMapper

# TODO update the JSON string below
json = "{}"
# create an instance of ChargeToGLAccountMapper from a JSON string
charge_to_gl_account_mapper_instance = ChargeToGLAccountMapper.from_json(json)
# print the JSON string representation of the object
print ChargeToGLAccountMapper.to_json()

# convert the object into a dict
charge_to_gl_account_mapper_dict = charge_to_gl_account_mapper_instance.to_dict()
# create an instance of ChargeToGLAccountMapper from a dict
charge_to_gl_account_mapper_form_dict = charge_to_gl_account_mapper.from_dict(charge_to_gl_account_mapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


