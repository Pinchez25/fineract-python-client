# PutOfficesOfficeIdResponse

PutOfficesOfficeIdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**PutOfficesOfficeIdResponseChanges**](PutOfficesOfficeIdResponseChanges.md) |  | [optional] 
**office_id** | **int** |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_offices_office_id_response import PutOfficesOfficeIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PutOfficesOfficeIdResponse from a JSON string
put_offices_office_id_response_instance = PutOfficesOfficeIdResponse.from_json(json)
# print the JSON string representation of the object
print PutOfficesOfficeIdResponse.to_json()

# convert the object into a dict
put_offices_office_id_response_dict = put_offices_office_id_response_instance.to_dict()
# create an instance of PutOfficesOfficeIdResponse from a dict
put_offices_office_id_response_form_dict = put_offices_office_id_response.from_dict(put_offices_office_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


