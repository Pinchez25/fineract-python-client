# AdvancedQueryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_query** | [**AdvancedQueryData**](AdvancedQueryData.md) |  | [optional] 
**datatable_queries** | [**List[TableQueryData]**](TableQueryData.md) |  | [optional] 

## Example

```python
from fineract_client.models.advanced_query_request import AdvancedQueryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AdvancedQueryRequest from a JSON string
advanced_query_request_instance = AdvancedQueryRequest.from_json(json)
# print the JSON string representation of the object
print(AdvancedQueryRequest.to_json())

# convert the object into a dict
advanced_query_request_dict = advanced_query_request_instance.to_dict()
# create an instance of AdvancedQueryRequest from a dict
advanced_query_request_from_dict = AdvancedQueryRequest.from_dict(advanced_query_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


