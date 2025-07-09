# GetSelfLoansTimeline


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expected_disbursement_date** | **date** |  | [optional] 

## Example

```python
from fineract_client.models.get_self_loans_timeline import GetSelfLoansTimeline

# TODO update the JSON string below
json = "{}"
# create an instance of GetSelfLoansTimeline from a JSON string
get_self_loans_timeline_instance = GetSelfLoansTimeline.from_json(json)
# print the JSON string representation of the object
print(GetSelfLoansTimeline.to_json())

# convert the object into a dict
get_self_loans_timeline_dict = get_self_loans_timeline_instance.to_dict()
# create an instance of GetSelfLoansTimeline from a dict
get_self_loans_timeline_from_dict = GetSelfLoansTimeline.from_dict(get_self_loans_timeline_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


