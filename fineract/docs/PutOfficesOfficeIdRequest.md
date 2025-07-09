# PutOfficesOfficeIdRequest

PutOfficesOfficeIdRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_format** | **str** |  | [optional] 
**external_id** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**opening_date** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.put_offices_office_id_request import PutOfficesOfficeIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutOfficesOfficeIdRequest from a JSON string
put_offices_office_id_request_instance = PutOfficesOfficeIdRequest.from_json(json)
# print the JSON string representation of the object
print(PutOfficesOfficeIdRequest.to_json())

# convert the object into a dict
put_offices_office_id_request_dict = put_offices_office_id_request_instance.to_dict()
# create an instance of PutOfficesOfficeIdRequest from a dict
put_offices_office_id_request_from_dict = PutOfficesOfficeIdRequest.from_dict(put_offices_office_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


