# UpdatePostDatedCheckRequest

UpdatePostDatedCheckRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_no** | **int** |  | [optional] 
**amount** | **float** |  | [optional] 
**var_date** | **date** |  | [optional] 
**date_format** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**repayment_date** | **date** |  | [optional] 

## Example

```python
from fineract_client.models.update_post_dated_check_request import UpdatePostDatedCheckRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePostDatedCheckRequest from a JSON string
update_post_dated_check_request_instance = UpdatePostDatedCheckRequest.from_json(json)
# print the JSON string representation of the object
print UpdatePostDatedCheckRequest.to_json()

# convert the object into a dict
update_post_dated_check_request_dict = update_post_dated_check_request_instance.to_dict()
# create an instance of UpdatePostDatedCheckRequest from a dict
update_post_dated_check_request_form_dict = update_post_dated_check_request.from_dict(update_post_dated_check_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


