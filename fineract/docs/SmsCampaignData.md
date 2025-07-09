# SmsCampaignData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**campaign_name** | **str** |  | [optional] 
**campaign_status** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 
**campaign_type** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 
**id** | **int** |  | [optional] 
**last_trigger_date** | **date** |  | [optional] 
**message** | **str** |  | [optional] 
**next_trigger_date** | **datetime** |  | [optional] 
**notification** | **bool** |  | [optional] 
**param_value** | **str** |  | [optional] 
**recurrence** | **str** |  | [optional] 
**recurrence_start_date** | **datetime** |  | [optional] 
**report_name** | **str** |  | [optional] 
**run_report_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.sms_campaign_data import SmsCampaignData

# TODO update the JSON string below
json = "{}"
# create an instance of SmsCampaignData from a JSON string
sms_campaign_data_instance = SmsCampaignData.from_json(json)
# print the JSON string representation of the object
print(SmsCampaignData.to_json())

# convert the object into a dict
sms_campaign_data_dict = sms_campaign_data_instance.to_dict()
# create an instance of SmsCampaignData from a dict
sms_campaign_data_from_dict = SmsCampaignData.from_dict(sms_campaign_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


