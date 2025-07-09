# ExternalAssetOwnerSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_from_date** | **date** |  | [optional] 
**effective_to_date** | **date** |  | [optional] 
**submitted_from_date** | **date** |  | [optional] 
**submitted_to_date** | **date** |  | [optional] 
**text** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.external_asset_owner_search_request import ExternalAssetOwnerSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalAssetOwnerSearchRequest from a JSON string
external_asset_owner_search_request_instance = ExternalAssetOwnerSearchRequest.from_json(json)
# print the JSON string representation of the object
print ExternalAssetOwnerSearchRequest.to_json()

# convert the object into a dict
external_asset_owner_search_request_dict = external_asset_owner_search_request_instance.to_dict()
# create an instance of ExternalAssetOwnerSearchRequest from a dict
external_asset_owner_search_request_form_dict = external_asset_owner_search_request.from_dict(external_asset_owner_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


