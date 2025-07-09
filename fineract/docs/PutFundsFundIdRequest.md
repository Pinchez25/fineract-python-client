# PutFundsFundIdRequest

PutFundsFundIdRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.put_funds_fund_id_request import PutFundsFundIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutFundsFundIdRequest from a JSON string
put_funds_fund_id_request_instance = PutFundsFundIdRequest.from_json(json)
# print the JSON string representation of the object
print(PutFundsFundIdRequest.to_json())

# convert the object into a dict
put_funds_fund_id_request_dict = put_funds_fund_id_request_instance.to_dict()
# create an instance of PutFundsFundIdRequest from a dict
put_funds_fund_id_request_from_dict = PutFundsFundIdRequest.from_dict(put_funds_fund_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


