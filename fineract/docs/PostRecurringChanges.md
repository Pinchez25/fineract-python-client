# PostRecurringChanges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_number** | **str** |  | [optional] 
**bank_number** | **str** |  | [optional] 
**check_number** | **str** |  | [optional] 
**receipt_number** | **str** |  | [optional] 
**routing_code** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.post_recurring_changes import PostRecurringChanges

# TODO update the JSON string below
json = "{}"
# create an instance of PostRecurringChanges from a JSON string
post_recurring_changes_instance = PostRecurringChanges.from_json(json)
# print the JSON string representation of the object
print(PostRecurringChanges.to_json())

# convert the object into a dict
post_recurring_changes_dict = post_recurring_changes_instance.to_dict()
# create an instance of PostRecurringChanges from a dict
post_recurring_changes_from_dict = PostRecurringChanges.from_dict(post_recurring_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


