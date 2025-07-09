# FinancialActivityData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**mapped_gl_account_type** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.financial_activity_data import FinancialActivityData

# TODO update the JSON string below
json = "{}"
# create an instance of FinancialActivityData from a JSON string
financial_activity_data_instance = FinancialActivityData.from_json(json)
# print the JSON string representation of the object
print FinancialActivityData.to_json()

# convert the object into a dict
financial_activity_data_dict = financial_activity_data_instance.to_dict()
# create an instance of FinancialActivityData from a dict
financial_activity_data_form_dict = financial_activity_data.from_dict(financial_activity_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


