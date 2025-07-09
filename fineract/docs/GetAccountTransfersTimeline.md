# GetAccountTransfersTimeline


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activated_by_firstname** | **str** |  | [optional] 
**activated_by_lastname** | **str** |  | [optional] 
**activated_by_username** | **str** |  | [optional] 
**activated_on_date** | **date** |  | [optional] 
**submitted_by_firstname** | **str** |  | [optional] 
**submitted_by_lastname** | **str** |  | [optional] 
**submitted_by_username** | **str** |  | [optional] 
**submitted_on_date** | **date** |  | [optional] 

## Example

```python
from fineract_client.models.get_account_transfers_timeline import GetAccountTransfersTimeline

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountTransfersTimeline from a JSON string
get_account_transfers_timeline_instance = GetAccountTransfersTimeline.from_json(json)
# print the JSON string representation of the object
print GetAccountTransfersTimeline.to_json()

# convert the object into a dict
get_account_transfers_timeline_dict = get_account_transfers_timeline_instance.to_dict()
# create an instance of GetAccountTransfersTimeline from a dict
get_account_transfers_timeline_form_dict = get_account_transfers_timeline.from_dict(get_account_transfers_timeline_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


