# PutTellersResponseChanges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_format** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**end_date** | **date** |  | [optional] 
**locale** | **str** |  | [optional] 
**start_date** | **date** |  | [optional] 

## Example

```python
from fineract_client.models.put_tellers_response_changes import PutTellersResponseChanges

# TODO update the JSON string below
json = "{}"
# create an instance of PutTellersResponseChanges from a JSON string
put_tellers_response_changes_instance = PutTellersResponseChanges.from_json(json)
# print the JSON string representation of the object
print PutTellersResponseChanges.to_json()

# convert the object into a dict
put_tellers_response_changes_dict = put_tellers_response_changes_instance.to_dict()
# create an instance of PutTellersResponseChanges from a dict
put_tellers_response_changes_form_dict = put_tellers_response_changes.from_dict(put_tellers_response_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


