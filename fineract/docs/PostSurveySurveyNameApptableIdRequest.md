# PostSurveySurveyNameApptableIdRequest

PostSurveySurveyNameApptableIdRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** |  | [optional] 
**date_format** | **datetime** |  | [optional] 
**locale** | **str** |  | [optional] 
**ppi_businessoccupation_cd_q3_businessoccupation** | **int** |  | [optional] 
**ppi_floortype_cd_q5_floortype** | **int** |  | [optional] 
**ppi_fryingpans_cd_q10_fryingpans** | **int** |  | [optional] 
**ppi_habitablerooms_cd_q4_habitablerooms** | **int** |  | [optional] 
**ppi_highestschool_cd_q2_highestschool** | **int** |  | [optional] 
**ppi_household_members_cd_q1_householdmembers** | **int** |  | [optional] 
**ppi_irons_cd_q7_irons** | **int** |  | [optional] 
**ppi_lightingsource_cd_q6_lightingsource** | **int** |  | [optional] 
**ppi_mosquitonets_cd_q8_mosquitonets** | **int** |  | [optional] 
**ppi_towels_cd_q9_towels** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_survey_survey_name_apptable_id_request import PostSurveySurveyNameApptableIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostSurveySurveyNameApptableIdRequest from a JSON string
post_survey_survey_name_apptable_id_request_instance = PostSurveySurveyNameApptableIdRequest.from_json(json)
# print the JSON string representation of the object
print PostSurveySurveyNameApptableIdRequest.to_json()

# convert the object into a dict
post_survey_survey_name_apptable_id_request_dict = post_survey_survey_name_apptable_id_request_instance.to_dict()
# create an instance of PostSurveySurveyNameApptableIdRequest from a dict
post_survey_survey_name_apptable_id_request_form_dict = post_survey_survey_name_apptable_id_request.from_dict(post_survey_survey_name_apptable_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


