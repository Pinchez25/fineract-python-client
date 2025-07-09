# ChargeFeeOnMonthDay


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day_of_month** | **int** |  | [optional] 
**month** | **str** |  | [optional] 
**month_value** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.charge_fee_on_month_day import ChargeFeeOnMonthDay

# TODO update the JSON string below
json = "{}"
# create an instance of ChargeFeeOnMonthDay from a JSON string
charge_fee_on_month_day_instance = ChargeFeeOnMonthDay.from_json(json)
# print the JSON string representation of the object
print(ChargeFeeOnMonthDay.to_json())

# convert the object into a dict
charge_fee_on_month_day_dict = charge_fee_on_month_day_instance.to_dict()
# create an instance of ChargeFeeOnMonthDay from a dict
charge_fee_on_month_day_from_dict = ChargeFeeOnMonthDay.from_dict(charge_fee_on_month_day_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


