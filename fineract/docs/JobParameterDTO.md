# JobParameterDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parameter_name** | **str** |  | [optional] 
**parameter_value** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.job_parameter_dto import JobParameterDTO

# TODO update the JSON string below
json = "{}"
# create an instance of JobParameterDTO from a JSON string
job_parameter_dto_instance = JobParameterDTO.from_json(json)
# print the JSON string representation of the object
print JobParameterDTO.to_json()

# convert the object into a dict
job_parameter_dto_dict = job_parameter_dto_instance.to_dict()
# create an instance of JobParameterDTO from a dict
job_parameter_dto_form_dict = job_parameter_dto.from_dict(job_parameter_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


