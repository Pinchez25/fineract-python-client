# PostalAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_line1** | **str** |  | [optional] 
**address_line2** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 
**state_province** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.postal_address import PostalAddress

# TODO update the JSON string below
json = "{}"
# create an instance of PostalAddress from a JSON string
postal_address_instance = PostalAddress.from_json(json)
# print the JSON string representation of the object
print PostalAddress.to_json()

# convert the object into a dict
postal_address_dict = postal_address_instance.to_dict()
# create an instance of PostalAddress from a dict
postal_address_form_dict = postal_address.from_dict(postal_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


