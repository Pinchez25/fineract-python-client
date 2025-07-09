# PagedRequestExternalAssetOwnerSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] 
**request** | [**ExternalAssetOwnerSearchRequest**](ExternalAssetOwnerSearchRequest.md) |  | [optional] 
**size** | **int** |  | [optional] 
**sorts** | [**List[SortOrder]**](SortOrder.md) |  | [optional] 

## Example

```python
from fineract_client.models.paged_request_external_asset_owner_search_request import PagedRequestExternalAssetOwnerSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PagedRequestExternalAssetOwnerSearchRequest from a JSON string
paged_request_external_asset_owner_search_request_instance = PagedRequestExternalAssetOwnerSearchRequest.from_json(json)
# print the JSON string representation of the object
print PagedRequestExternalAssetOwnerSearchRequest.to_json()

# convert the object into a dict
paged_request_external_asset_owner_search_request_dict = paged_request_external_asset_owner_search_request_instance.to_dict()
# create an instance of PagedRequestExternalAssetOwnerSearchRequest from a dict
paged_request_external_asset_owner_search_request_form_dict = paged_request_external_asset_owner_search_request.from_dict(paged_request_external_asset_owner_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


