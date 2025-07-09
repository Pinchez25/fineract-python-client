# GetAccountsTimeline


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activated_date** | **date** |  | [optional] 
**approved_by_firstname** | **str** |  | [optional] 
**approved_by_lastname** | **str** |  | [optional] 
**approved_by_username** | **str** |  | [optional] 
**approved_date** | **date** |  | [optional] 
**submitted_by_firstname** | **str** |  | [optional] 
**submitted_by_lastname** | **str** |  | [optional] 
**submitted_by_username** | **str** |  | [optional] 
**submitted_on_date** | **date** |  | [optional] 

## Example

```python
from fineract_client.models.get_accounts_timeline import GetAccountsTimeline

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountsTimeline from a JSON string
get_accounts_timeline_instance = GetAccountsTimeline.from_json(json)
# print the JSON string representation of the object
print GetAccountsTimeline.to_json()

# convert the object into a dict
get_accounts_timeline_dict = get_accounts_timeline_instance.to_dict()
# create an instance of GetAccountsTimeline from a dict
get_accounts_timeline_form_dict = get_accounts_timeline.from_dict(get_accounts_timeline_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


