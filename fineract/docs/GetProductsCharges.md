# GetProductsCharges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**amount** | **int** |  | [optional] 
**charge_applies_to** | [**GetChargeAppliesTo**](GetChargeAppliesTo.md) |  | [optional] 
**charge_calculation_type** | [**GetChargeCalculationType**](GetChargeCalculationType.md) |  | [optional] 
**charge_payment_mode** | [**GetChargePaymentMode**](GetChargePaymentMode.md) |  | [optional] 
**charge_time_type** | [**GetChargeTimeType**](GetChargeTimeType.md) |  | [optional] 
**currency** | [**GetChargesCurrency**](GetChargesCurrency.md) |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**penalty** | **bool** |  | [optional] 

## Example

```python
from fineract_client.models.get_products_charges import GetProductsCharges

# TODO update the JSON string below
json = "{}"
# create an instance of GetProductsCharges from a JSON string
get_products_charges_instance = GetProductsCharges.from_json(json)
# print the JSON string representation of the object
print(GetProductsCharges.to_json())

# convert the object into a dict
get_products_charges_dict = get_products_charges_instance.to_dict()
# create an instance of GetProductsCharges from a dict
get_products_charges_from_dict = GetProductsCharges.from_dict(get_products_charges_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


