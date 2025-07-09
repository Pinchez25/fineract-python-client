# PostSelfLoansDatatables


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PostSelfLoansData**](PostSelfLoansData.md) |  | [optional] 
**registered_table_name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.post_self_loans_datatables import PostSelfLoansDatatables

# TODO update the JSON string below
json = "{}"
# create an instance of PostSelfLoansDatatables from a JSON string
post_self_loans_datatables_instance = PostSelfLoansDatatables.from_json(json)
# print the JSON string representation of the object
print(PostSelfLoansDatatables.to_json())

# convert the object into a dict
post_self_loans_datatables_dict = post_self_loans_datatables_instance.to_dict()
# create an instance of PostSelfLoansDatatables from a dict
post_self_loans_datatables_from_dict = PostSelfLoansDatatables.from_dict(post_self_loans_datatables_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


