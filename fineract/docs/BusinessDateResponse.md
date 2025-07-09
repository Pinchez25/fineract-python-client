# BusinessDateResponse

BusinessDateResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** |  | [optional] 
**description** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.business_date_response import BusinessDateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessDateResponse from a JSON string
business_date_response_instance = BusinessDateResponse.from_json(json)
# print the JSON string representation of the object
print(BusinessDateResponse.to_json())

# convert the object into a dict
business_date_response_dict = business_date_response_instance.to_dict()
# create an instance of BusinessDateResponse from a dict
business_date_response_from_dict = BusinessDateResponse.from_dict(business_date_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


