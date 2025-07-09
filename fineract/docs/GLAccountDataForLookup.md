# GLAccountDataForLookup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gl_code** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.gl_account_data_for_lookup import GLAccountDataForLookup

# TODO update the JSON string below
json = "{}"
# create an instance of GLAccountDataForLookup from a JSON string
gl_account_data_for_lookup_instance = GLAccountDataForLookup.from_json(json)
# print the JSON string representation of the object
print(GLAccountDataForLookup.to_json())

# convert the object into a dict
gl_account_data_for_lookup_dict = gl_account_data_for_lookup_instance.to_dict()
# create an instance of GLAccountDataForLookup from a dict
gl_account_data_for_lookup_from_dict = GLAccountDataForLookup.from_dict(gl_account_data_for_lookup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


