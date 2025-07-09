# ExternalTransferDataDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**details_id** | **int** |  | [optional] 
**total_fee_charges_outstanding** | **float** |  | [optional] 
**total_interest_outstanding** | **float** |  | [optional] 
**total_outstanding** | **float** |  | [optional] 
**total_overpaid** | **float** |  | [optional] 
**total_penalty_charges_outstanding** | **float** |  | [optional] 
**total_principal_outstanding** | **float** |  | [optional] 

## Example

```python
from fineract_client.models.external_transfer_data_details import ExternalTransferDataDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalTransferDataDetails from a JSON string
external_transfer_data_details_instance = ExternalTransferDataDetails.from_json(json)
# print the JSON string representation of the object
print ExternalTransferDataDetails.to_json()

# convert the object into a dict
external_transfer_data_details_dict = external_transfer_data_details_instance.to_dict()
# create an instance of ExternalTransferDataDetails from a dict
external_transfer_data_details_form_dict = external_transfer_data_details.from_dict(external_transfer_data_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


