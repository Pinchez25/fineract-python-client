# PagedLocalRequestAdvancedQueryDataLocaleObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **str** |  | [optional] 
**display_country** | **str** |  | [optional] 
**display_language** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**display_script** | **str** |  | [optional] 
**display_variant** | **str** |  | [optional] 
**extension_keys** | **List[str]** |  | [optional] 
**iso3_country** | **str** |  | [optional] 
**iso3_language** | **str** |  | [optional] 
**language** | **str** |  | [optional] 
**script** | **str** |  | [optional] 
**unicode_locale_attributes** | **List[str]** |  | [optional] 
**unicode_locale_keys** | **List[str]** |  | [optional] 
**variant** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.paged_local_request_advanced_query_data_locale_object import PagedLocalRequestAdvancedQueryDataLocaleObject

# TODO update the JSON string below
json = "{}"
# create an instance of PagedLocalRequestAdvancedQueryDataLocaleObject from a JSON string
paged_local_request_advanced_query_data_locale_object_instance = PagedLocalRequestAdvancedQueryDataLocaleObject.from_json(json)
# print the JSON string representation of the object
print(PagedLocalRequestAdvancedQueryDataLocaleObject.to_json())

# convert the object into a dict
paged_local_request_advanced_query_data_locale_object_dict = paged_local_request_advanced_query_data_locale_object_instance.to_dict()
# create an instance of PagedLocalRequestAdvancedQueryDataLocaleObject from a dict
paged_local_request_advanced_query_data_locale_object_from_dict = PagedLocalRequestAdvancedQueryDataLocaleObject.from_dict(paged_local_request_advanced_query_data_locale_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


