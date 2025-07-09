# GetSavingsSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_balance** | **float** |  | [optional] 
**currency** | [**GetSavingsCurrency**](GetSavingsCurrency.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_savings_summary import GetSavingsSummary

# TODO update the JSON string below
json = "{}"
# create an instance of GetSavingsSummary from a JSON string
get_savings_summary_instance = GetSavingsSummary.from_json(json)
# print the JSON string representation of the object
print GetSavingsSummary.to_json()

# convert the object into a dict
get_savings_summary_dict = get_savings_summary_instance.to_dict()
# create an instance of GetSavingsSummary from a dict
get_savings_summary_form_dict = get_savings_summary.from_dict(get_savings_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


