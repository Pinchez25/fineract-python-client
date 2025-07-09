# PutDelinquencyRangeResponse

PutDelinquencyRangeResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**PostDelinquencyRangeRequest**](PostDelinquencyRangeRequest.md) |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_delinquency_range_response import PutDelinquencyRangeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PutDelinquencyRangeResponse from a JSON string
put_delinquency_range_response_instance = PutDelinquencyRangeResponse.from_json(json)
# print the JSON string representation of the object
print PutDelinquencyRangeResponse.to_json()

# convert the object into a dict
put_delinquency_range_response_dict = put_delinquency_range_response_instance.to_dict()
# create an instance of PutDelinquencyRangeResponse from a dict
put_delinquency_range_response_form_dict = put_delinquency_range_response.from_dict(put_delinquency_range_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


