# PutFundsFundIdResponse

PutFundsFundIdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**PutFundsFundIdRequest**](PutFundsFundIdRequest.md) |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_funds_fund_id_response import PutFundsFundIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PutFundsFundIdResponse from a JSON string
put_funds_fund_id_response_instance = PutFundsFundIdResponse.from_json(json)
# print the JSON string representation of the object
print(PutFundsFundIdResponse.to_json())

# convert the object into a dict
put_funds_fund_id_response_dict = put_funds_fund_id_response_instance.to_dict()
# create an instance of PutFundsFundIdResponse from a dict
put_funds_fund_id_response_from_dict = PutFundsFundIdResponse.from_dict(put_funds_fund_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


