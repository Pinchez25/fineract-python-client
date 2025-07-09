# GetClientObligeeDetailsResponse

GetClientObligeeDetailsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obligees** | [**List[GetObligeeData]**](GetObligeeData.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_client_obligee_details_response import GetClientObligeeDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetClientObligeeDetailsResponse from a JSON string
get_client_obligee_details_response_instance = GetClientObligeeDetailsResponse.from_json(json)
# print the JSON string representation of the object
print GetClientObligeeDetailsResponse.to_json()

# convert the object into a dict
get_client_obligee_details_response_dict = get_client_obligee_details_response_instance.to_dict()
# create an instance of GetClientObligeeDetailsResponse from a dict
get_client_obligee_details_response_form_dict = get_client_obligee_details_response.from_dict(get_client_obligee_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


