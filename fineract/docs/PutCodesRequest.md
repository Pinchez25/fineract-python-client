# PutCodesRequest

PutCodesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.put_codes_request import PutCodesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutCodesRequest from a JSON string
put_codes_request_instance = PutCodesRequest.from_json(json)
# print the JSON string representation of the object
print(PutCodesRequest.to_json())

# convert the object into a dict
put_codes_request_dict = put_codes_request_instance.to_dict()
# create an instance of PutCodesRequest from a dict
put_codes_request_from_dict = PutCodesRequest.from_dict(put_codes_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


