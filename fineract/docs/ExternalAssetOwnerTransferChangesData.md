# ExternalAssetOwnerTransferChangesData

ExternalAssetOwnerTransferChangesData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner_external_id** | **str** |  | [optional] 
**purchase_price_ratio** | **str** |  | [optional] 
**settlement_date** | **date** |  | [optional] 
**transfer_external_id** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.external_asset_owner_transfer_changes_data import ExternalAssetOwnerTransferChangesData

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalAssetOwnerTransferChangesData from a JSON string
external_asset_owner_transfer_changes_data_instance = ExternalAssetOwnerTransferChangesData.from_json(json)
# print the JSON string representation of the object
print ExternalAssetOwnerTransferChangesData.to_json()

# convert the object into a dict
external_asset_owner_transfer_changes_data_dict = external_asset_owner_transfer_changes_data_instance.to_dict()
# create an instance of ExternalAssetOwnerTransferChangesData from a dict
external_asset_owner_transfer_changes_data_form_dict = external_asset_owner_transfer_changes_data.from_dict(external_asset_owner_transfer_changes_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


