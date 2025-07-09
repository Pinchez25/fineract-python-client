# GetSelfSavingsSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_balance** | **int** |  | [optional] 
**currency** | [**GetSelfSavingsCurrency**](GetSelfSavingsCurrency.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_self_savings_summary import GetSelfSavingsSummary

# TODO update the JSON string below
json = "{}"
# create an instance of GetSelfSavingsSummary from a JSON string
get_self_savings_summary_instance = GetSelfSavingsSummary.from_json(json)
# print the JSON string representation of the object
print(GetSelfSavingsSummary.to_json())

# convert the object into a dict
get_self_savings_summary_dict = get_self_savings_summary_instance.to_dict()
# create an instance of GetSelfSavingsSummary from a dict
get_self_savings_summary_from_dict = GetSelfSavingsSummary.from_dict(get_self_savings_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


