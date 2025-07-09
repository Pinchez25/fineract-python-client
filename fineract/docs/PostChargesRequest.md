# PostChargesRequest

PostChargesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**amount** | **float** |  | [optional] 
**charge_applies_to** | **int** |  | [optional] 
**charge_calculation_type** | **int** |  | [optional] 
**charge_payment_mode** | **int** |  | [optional] 
**charge_time_type** | **int** |  | [optional] 
**currency_code** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 
**month_day_format** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**penalty** | **bool** |  | [optional] 

## Example

```python
from fineract_client.models.post_charges_request import PostChargesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostChargesRequest from a JSON string
post_charges_request_instance = PostChargesRequest.from_json(json)
# print the JSON string representation of the object
print(PostChargesRequest.to_json())

# convert the object into a dict
post_charges_request_dict = post_charges_request_instance.to_dict()
# create an instance of PostChargesRequest from a dict
post_charges_request_from_dict = PostChargesRequest.from_dict(post_charges_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


