# GetSavingsInterestPostingPeriodType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_savings_interest_posting_period_type import GetSavingsInterestPostingPeriodType

# TODO update the JSON string below
json = "{}"
# create an instance of GetSavingsInterestPostingPeriodType from a JSON string
get_savings_interest_posting_period_type_instance = GetSavingsInterestPostingPeriodType.from_json(json)
# print the JSON string representation of the object
print GetSavingsInterestPostingPeriodType.to_json()

# convert the object into a dict
get_savings_interest_posting_period_type_dict = get_savings_interest_posting_period_type_instance.to_dict()
# create an instance of GetSavingsInterestPostingPeriodType from a dict
get_savings_interest_posting_period_type_form_dict = get_savings_interest_posting_period_type.from_dict(get_savings_interest_posting_period_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


