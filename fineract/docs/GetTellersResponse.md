# GetTellersResponse

GetTellersResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credit_account_id** | **int** |  | [optional] 
**debit_account_id** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**office_id** | **int** |  | [optional] 
**office_name** | **str** |  | [optional] 
**start_date** | **date** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_tellers_response import GetTellersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTellersResponse from a JSON string
get_tellers_response_instance = GetTellersResponse.from_json(json)
# print the JSON string representation of the object
print GetTellersResponse.to_json()

# convert the object into a dict
get_tellers_response_dict = get_tellers_response_instance.to_dict()
# create an instance of GetTellersResponse from a dict
get_tellers_response_form_dict = get_tellers_response.from_dict(get_tellers_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


