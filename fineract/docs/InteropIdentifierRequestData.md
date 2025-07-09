# InteropIdentifierRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | 
**id_type** | **str** |  | 
**id_value** | **str** |  | 
**sub_id_or_type** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.interop_identifier_request_data import InteropIdentifierRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of InteropIdentifierRequestData from a JSON string
interop_identifier_request_data_instance = InteropIdentifierRequestData.from_json(json)
# print the JSON string representation of the object
print InteropIdentifierRequestData.to_json()

# convert the object into a dict
interop_identifier_request_data_dict = interop_identifier_request_data_instance.to_dict()
# create an instance of InteropIdentifierRequestData from a dict
interop_identifier_request_data_form_dict = interop_identifier_request_data.from_dict(interop_identifier_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


