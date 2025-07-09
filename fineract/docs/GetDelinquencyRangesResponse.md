# GetDelinquencyRangesResponse

GetDelinquencyRangesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**classification** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**maximum_age_days** | **int** |  | [optional] 
**minimum_age_days** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_delinquency_ranges_response import GetDelinquencyRangesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetDelinquencyRangesResponse from a JSON string
get_delinquency_ranges_response_instance = GetDelinquencyRangesResponse.from_json(json)
# print the JSON string representation of the object
print GetDelinquencyRangesResponse.to_json()

# convert the object into a dict
get_delinquency_ranges_response_dict = get_delinquency_ranges_response_instance.to_dict()
# create an instance of GetDelinquencyRangesResponse from a dict
get_delinquency_ranges_response_form_dict = get_delinquency_ranges_response.from_dict(get_delinquency_ranges_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


