# PutExternalServiceRequest

PutExternalServiceRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** |  | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.put_external_service_request import PutExternalServiceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutExternalServiceRequest from a JSON string
put_external_service_request_instance = PutExternalServiceRequest.from_json(json)
# print the JSON string representation of the object
print(PutExternalServiceRequest.to_json())

# convert the object into a dict
put_external_service_request_dict = put_external_service_request_instance.to_dict()
# create an instance of PutExternalServiceRequest from a dict
put_external_service_request_from_dict = PutExternalServiceRequest.from_dict(put_external_service_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


