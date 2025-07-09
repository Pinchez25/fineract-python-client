# PutTellersRequest

PutTellersRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_format** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**end_date** | **date** |  | [optional] 
**locale** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**office_id** | **int** |  | [optional] 
**start_date** | **date** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.put_tellers_request import PutTellersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutTellersRequest from a JSON string
put_tellers_request_instance = PutTellersRequest.from_json(json)
# print the JSON string representation of the object
print PutTellersRequest.to_json()

# convert the object into a dict
put_tellers_request_dict = put_tellers_request_instance.to_dict()
# create an instance of PutTellersRequest from a dict
put_tellers_request_form_dict = put_tellers_request.from_dict(put_tellers_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


