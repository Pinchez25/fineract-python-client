# GetCentersResponse

GetCentersResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_items** | [**List[GetCentersPageItems]**](GetCentersPageItems.md) |  | [optional] 
**total_filtered_records** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_centers_response import GetCentersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetCentersResponse from a JSON string
get_centers_response_instance = GetCentersResponse.from_json(json)
# print the JSON string representation of the object
print GetCentersResponse.to_json()

# convert the object into a dict
get_centers_response_dict = get_centers_response_instance.to_dict()
# create an instance of GetCentersResponse from a dict
get_centers_response_form_dict = get_centers_response.from_dict(get_centers_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


