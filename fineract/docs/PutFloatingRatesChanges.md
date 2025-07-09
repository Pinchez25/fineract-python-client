# PutFloatingRatesChanges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rate_periods** | [**List[PostFloatingRatesRatePeriods]**](PostFloatingRatesRatePeriods.md) |  | [optional] 

## Example

```python
from fineract_client.models.put_floating_rates_changes import PutFloatingRatesChanges

# TODO update the JSON string below
json = "{}"
# create an instance of PutFloatingRatesChanges from a JSON string
put_floating_rates_changes_instance = PutFloatingRatesChanges.from_json(json)
# print the JSON string representation of the object
print PutFloatingRatesChanges.to_json()

# convert the object into a dict
put_floating_rates_changes_dict = put_floating_rates_changes_instance.to_dict()
# create an instance of PutFloatingRatesChanges from a dict
put_floating_rates_changes_form_dict = put_floating_rates_changes.from_dict(put_floating_rates_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


