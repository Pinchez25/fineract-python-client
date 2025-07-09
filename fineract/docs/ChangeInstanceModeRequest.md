# ChangeInstanceModeRequest

ChangeInstanceModeRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_manager_enabled** | **bool** |  | 
**batch_worker_enabled** | **bool** |  | 
**read_enabled** | **bool** |  | 
**write_enabled** | **bool** |  | 

## Example

```python
from fineract_client.models.change_instance_mode_request import ChangeInstanceModeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeInstanceModeRequest from a JSON string
change_instance_mode_request_instance = ChangeInstanceModeRequest.from_json(json)
# print the JSON string representation of the object
print ChangeInstanceModeRequest.to_json()

# convert the object into a dict
change_instance_mode_request_dict = change_instance_mode_request_instance.to_dict()
# create an instance of ChangeInstanceModeRequest from a dict
change_instance_mode_request_form_dict = change_instance_mode_request.from_dict(change_instance_mode_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


