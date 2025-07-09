# ProcessingResultLookup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**processing_result** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.processing_result_lookup import ProcessingResultLookup

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessingResultLookup from a JSON string
processing_result_lookup_instance = ProcessingResultLookup.from_json(json)
# print the JSON string representation of the object
print ProcessingResultLookup.to_json()

# convert the object into a dict
processing_result_lookup_dict = processing_result_lookup_instance.to_dict()
# create an instance of ProcessingResultLookup from a dict
processing_result_lookup_form_dict = processing_result_lookup.from_dict(processing_result_lookup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


