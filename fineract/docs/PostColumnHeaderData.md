# PostColumnHeaderData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Used in Code Value fields. Column name becomes: code_cd_name. Mandatory if using type Dropdown, otherwise an error is returned. | [optional] 
**indexed** | **bool** | Defaults to false | [optional] 
**length** | **int** | Length of the text field. Mandatory if type String is used, otherwise an error is returned. | [optional] 
**mandatory** | **bool** | Defaults to false | [optional] 
**name** | **str** |  | 
**type** | **str** | Any of them: Boolean | Date | DateTime | Decimal | Dropdown | Number | String | Text | 
**unique** | **bool** | Defaults to false | [optional] 

## Example

```python
from fineract_client.models.post_column_header_data import PostColumnHeaderData

# TODO update the JSON string below
json = "{}"
# create an instance of PostColumnHeaderData from a JSON string
post_column_header_data_instance = PostColumnHeaderData.from_json(json)
# print the JSON string representation of the object
print(PostColumnHeaderData.to_json())

# convert the object into a dict
post_column_header_data_dict = post_column_header_data_instance.to_dict()
# create an instance of PostColumnHeaderData from a dict
post_column_header_data_from_dict = PostColumnHeaderData.from_dict(post_column_header_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


