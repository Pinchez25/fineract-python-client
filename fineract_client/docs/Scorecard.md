# Scorecard


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_user** | [**AppUser**](AppUser.md) |  | [optional] 
**client** | [**Client**](Client.md) |  | [optional] 
**created_on** | **datetime** |  | [optional] 
**id** | **int** |  | [optional] 
**new** | **bool** |  | [optional] 
**question** | [**Question**](Question.md) |  | [optional] 
**response** | [**Response**](Response.md) |  | [optional] 
**survey** | [**Survey**](Survey.md) |  | [optional] 
**value** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.scorecard import Scorecard

# TODO update the JSON string below
json = "{}"
# create an instance of Scorecard from a JSON string
scorecard_instance = Scorecard.from_json(json)
# print the JSON string representation of the object
print(Scorecard.to_json())

# convert the object into a dict
scorecard_dict = scorecard_instance.to_dict()
# create an instance of Scorecard from a dict
scorecard_from_dict = Scorecard.from_dict(scorecard_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


