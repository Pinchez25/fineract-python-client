# PostSelfLoansData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activation_date** | **str** |  | [optional] 
**date_format** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.post_self_loans_data import PostSelfLoansData

# TODO update the JSON string below
json = "{}"
# create an instance of PostSelfLoansData from a JSON string
post_self_loans_data_instance = PostSelfLoansData.from_json(json)
# print the JSON string representation of the object
print PostSelfLoansData.to_json()

# convert the object into a dict
post_self_loans_data_dict = post_self_loans_data_instance.to_dict()
# create an instance of PostSelfLoansData from a dict
post_self_loans_data_form_dict = post_self_loans_data.from_dict(post_self_loans_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


