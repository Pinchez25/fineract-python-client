# PostAccountsCharges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** |  | [optional] 
**charge_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_accounts_charges import PostAccountsCharges

# TODO update the JSON string below
json = "{}"
# create an instance of PostAccountsCharges from a JSON string
post_accounts_charges_instance = PostAccountsCharges.from_json(json)
# print the JSON string representation of the object
print(PostAccountsCharges.to_json())

# convert the object into a dict
post_accounts_charges_dict = post_accounts_charges_instance.to_dict()
# create an instance of PostAccountsCharges from a dict
post_accounts_charges_from_dict = PostAccountsCharges.from_dict(post_accounts_charges_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


