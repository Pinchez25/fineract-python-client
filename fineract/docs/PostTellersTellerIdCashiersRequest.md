# PostTellersTellerIdCashiersRequest

PostTellersTellerIdCashiersRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_format** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**end_date** | **date** |  | [optional] 
**is_full_day** | **bool** |  | [optional] 
**locale** | **str** |  | [optional] 
**staff_id** | **int** |  | [optional] 
**start_date** | **date** |  | [optional] 

## Example

```python
from fineract_client.models.post_tellers_teller_id_cashiers_request import PostTellersTellerIdCashiersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostTellersTellerIdCashiersRequest from a JSON string
post_tellers_teller_id_cashiers_request_instance = PostTellersTellerIdCashiersRequest.from_json(json)
# print the JSON string representation of the object
print(PostTellersTellerIdCashiersRequest.to_json())

# convert the object into a dict
post_tellers_teller_id_cashiers_request_dict = post_tellers_teller_id_cashiers_request_instance.to_dict()
# create an instance of PostTellersTellerIdCashiersRequest from a dict
post_tellers_teller_id_cashiers_request_from_dict = PostTellersTellerIdCashiersRequest.from_dict(post_tellers_teller_id_cashiers_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


