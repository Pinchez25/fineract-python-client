# BatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** |  | [optional] 
**headers** | [**List[Header]**](Header.md) |  | [optional] 
**method** | **str** |  | [optional] 
**reference** | **int** |  | [optional] 
**relative_url** | **str** |  | [optional] 
**request_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.batch_request import BatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BatchRequest from a JSON string
batch_request_instance = BatchRequest.from_json(json)
# print the JSON string representation of the object
print BatchRequest.to_json()

# convert the object into a dict
batch_request_dict = batch_request_instance.to_dict()
# create an instance of BatchRequest from a dict
batch_request_form_dict = batch_request.from_dict(batch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


