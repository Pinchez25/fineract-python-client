# ContentDisposition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creation_date** | **datetime** |  | [optional] 
**file_name** | **str** |  | [optional] 
**modification_date** | **datetime** |  | [optional] 
**parameters** | **Dict[str, str]** |  | [optional] 
**read_date** | **datetime** |  | [optional] 
**size** | **int** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.content_disposition import ContentDisposition

# TODO update the JSON string below
json = "{}"
# create an instance of ContentDisposition from a JSON string
content_disposition_instance = ContentDisposition.from_json(json)
# print the JSON string representation of the object
print(ContentDisposition.to_json())

# convert the object into a dict
content_disposition_dict = content_disposition_instance.to_dict()
# create an instance of ContentDisposition from a dict
content_disposition_from_dict = ContentDisposition.from_dict(content_disposition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


