# MoneyData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | 
**currency** | **str** |  | 

## Example

```python
from fineract_client.models.money_data import MoneyData

# TODO update the JSON string below
json = "{}"
# create an instance of MoneyData from a JSON string
money_data_instance = MoneyData.from_json(json)
# print the JSON string representation of the object
print MoneyData.to_json()

# convert the object into a dict
money_data_dict = money_data_instance.to_dict()
# create an instance of MoneyData from a dict
money_data_form_dict = money_data.from_dict(money_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


