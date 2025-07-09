# Rate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**approve_user** | [**AppUser**](AppUser.md) |  | [optional] 
**created_by** | **int** |  | [optional] 
**created_date** | **datetime** |  | [optional] 
**id** | **int** |  | [optional] 
**last_modified_by** | **int** |  | [optional] 
**last_modified_date** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**new** | **bool** |  | [optional] 
**percentage** | **float** |  | [optional] 
**product_apply** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.rate import Rate

# TODO update the JSON string below
json = "{}"
# create an instance of Rate from a JSON string
rate_instance = Rate.from_json(json)
# print the JSON string representation of the object
print Rate.to_json()

# convert the object into a dict
rate_dict = rate_instance.to_dict()
# create an instance of Rate from a dict
rate_form_dict = rate.from_dict(rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


