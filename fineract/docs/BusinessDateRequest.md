# BusinessDateRequest

BusinessDateRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** |  | [optional] 
**date_format** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.business_date_request import BusinessDateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessDateRequest from a JSON string
business_date_request_instance = BusinessDateRequest.from_json(json)
# print the JSON string representation of the object
print BusinessDateRequest.to_json()

# convert the object into a dict
business_date_request_dict = business_date_request_instance.to_dict()
# create an instance of BusinessDateRequest from a dict
business_date_request_form_dict = business_date_request.from_dict(business_date_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


