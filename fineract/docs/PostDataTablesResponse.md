# PostDataTablesResponse

PostDataTablesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_identifier** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.post_data_tables_response import PostDataTablesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostDataTablesResponse from a JSON string
post_data_tables_response_instance = PostDataTablesResponse.from_json(json)
# print the JSON string representation of the object
print(PostDataTablesResponse.to_json())

# convert the object into a dict
post_data_tables_response_dict = post_data_tables_response_instance.to_dict()
# create an instance of PostDataTablesResponse from a dict
post_data_tables_response_from_dict = PostDataTablesResponse.from_dict(post_data_tables_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


