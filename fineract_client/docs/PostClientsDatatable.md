# PostClientsDatatable

List of PostClientsDatatable

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **Dict[str, object]** |  | [optional] 
**registered_table_name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.post_clients_datatable import PostClientsDatatable

# TODO update the JSON string below
json = "{}"
# create an instance of PostClientsDatatable from a JSON string
post_clients_datatable_instance = PostClientsDatatable.from_json(json)
# print the JSON string representation of the object
print(PostClientsDatatable.to_json())

# convert the object into a dict
post_clients_datatable_dict = post_clients_datatable_instance.to_dict()
# create an instance of PostClientsDatatable from a dict
post_clients_datatable_from_dict = PostClientsDatatable.from_dict(post_clients_datatable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


