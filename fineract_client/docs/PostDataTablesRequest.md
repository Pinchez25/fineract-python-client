# PostDataTablesRequest

PostDataTablesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apptable_name** | **str** |  | 
**columns** | [**List[PostColumnHeaderData]**](PostColumnHeaderData.md) |  | 
**datatable_name** | **str** |  | 
**entity_sub_type** | **str** |  | [optional] 
**multi_row** | **bool** | Allows to create multiple entries in the Data Table. Optional, defaults to false. If this property is not provided Data Table will allow only one entry. | [optional] 

## Example

```python
from fineract_client.models.post_data_tables_request import PostDataTablesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostDataTablesRequest from a JSON string
post_data_tables_request_instance = PostDataTablesRequest.from_json(json)
# print the JSON string representation of the object
print(PostDataTablesRequest.to_json())

# convert the object into a dict
post_data_tables_request_dict = post_data_tables_request_instance.to_dict()
# create an instance of PostDataTablesRequest from a dict
post_data_tables_request_from_dict = PostDataTablesRequest.from_dict(post_data_tables_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


