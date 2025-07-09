# PostChargesResponse

PostChargesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_charges_response import PostChargesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostChargesResponse from a JSON string
post_charges_response_instance = PostChargesResponse.from_json(json)
# print the JSON string representation of the object
print PostChargesResponse.to_json()

# convert the object into a dict
post_charges_response_dict = post_charges_response_instance.to_dict()
# create an instance of PostChargesResponse from a dict
post_charges_response_form_dict = post_charges_response.from_dict(post_charges_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


