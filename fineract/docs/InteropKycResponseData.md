# InteropKycResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**birth_country** | **str** |  | [optional] 
**changes** | **Dict[str, object]** |  | [optional] 
**client_id** | **int** |  | [optional] 
**command_id** | **int** |  | [optional] 
**contact_phone** | **str** |  | [optional] 
**credit_bureau_report_data** | **Dict[str, object]** |  | [optional] 
**date_of_birth** | **str** |  | [optional] 
**email_address** | **str** |  | [optional] 
**gender** | **str** |  | [optional] 
**glim_id** | **int** |  | [optional] 
**group_id** | **int** |  | [optional] 
**gsim_id** | **int** |  | [optional] 
**id_document** | [**List[IdDocument]**](IdDocument.md) |  | [optional] 
**loan_id** | **int** |  | [optional] 
**nationality** | **str** |  | [optional] 
**office_id** | **int** |  | [optional] 
**postal_address** | [**PostalAddress**](PostalAddress.md) |  | [optional] 
**product_id** | **int** |  | [optional] 
**resource_external_id** | [**ExternalId**](ExternalId.md) |  | [optional] 
**resource_id** | **int** |  | [optional] 
**resource_identifier** | **str** |  | [optional] 
**rollback_transaction** | **bool** |  | [optional] 
**savings_id** | **int** |  | [optional] 
**sub_resource_external_id** | [**ExternalId**](ExternalId.md) |  | [optional] 
**sub_resource_id** | **int** |  | [optional] 
**subject_name** | [**SubjectName**](SubjectName.md) |  | [optional] 
**transaction_id** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.interop_kyc_response_data import InteropKycResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of InteropKycResponseData from a JSON string
interop_kyc_response_data_instance = InteropKycResponseData.from_json(json)
# print the JSON string representation of the object
print(InteropKycResponseData.to_json())

# convert the object into a dict
interop_kyc_response_data_dict = interop_kyc_response_data_instance.to_dict()
# create an instance of InteropKycResponseData from a dict
interop_kyc_response_data_from_dict = InteropKycResponseData.from_dict(interop_kyc_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


