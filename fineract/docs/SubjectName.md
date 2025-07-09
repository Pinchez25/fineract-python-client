# SubjectName


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**middle_name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.subject_name import SubjectName

# TODO update the JSON string below
json = "{}"
# create an instance of SubjectName from a JSON string
subject_name_instance = SubjectName.from_json(json)
# print the JSON string representation of the object
print(SubjectName.to_json())

# convert the object into a dict
subject_name_dict = subject_name_instance.to_dict()
# create an instance of SubjectName from a dict
subject_name_from_dict = SubjectName.from_dict(subject_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


