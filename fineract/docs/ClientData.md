# ClientData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_no** | **str** |  | [optional] 
**activation_date** | **date** |  | [optional] 
**active** | **bool** |  | [optional] 
**address** | **List[object]** |  | [optional] 
**client_classification** | [**CodeValueData**](CodeValueData.md) |  | [optional] 
**client_classification_id** | **int** |  | [optional] 
**client_classification_options** | [**List[CodeValueData]**](CodeValueData.md) |  | [optional] 
**client_collateral_managements** | [**List[ClientCollateralManagementData]**](ClientCollateralManagementData.md) |  | [optional] 
**client_legal_form_options** | [**List[EnumOptionData]**](EnumOptionData.md) |  | [optional] 
**client_non_person_constitution_options** | [**List[CodeValueData]**](CodeValueData.md) |  | [optional] 
**client_non_person_details** | **object** |  | [optional] 
**client_non_person_main_business_line_options** | [**List[CodeValueData]**](CodeValueData.md) |  | [optional] 
**client_type** | [**CodeValueData**](CodeValueData.md) |  | [optional] 
**client_type_id** | **int** |  | [optional] 
**client_type_options** | [**List[CodeValueData]**](CodeValueData.md) |  | [optional] 
**datatables** | [**List[DatatableData]**](DatatableData.md) |  | [optional] 
**date_format** | **str** |  | [optional] 
**date_of_birth** | **date** |  | [optional] 
**display_name** | **str** |  | [optional] 
**email_address** | **str** |  | [optional] 
**external_id** | [**ExternalId**](ExternalId.md) |  | [optional] 
**family_member_options** | [**ClientFamilyMembersData**](ClientFamilyMembersData.md) |  | [optional] 
**firstname** | **str** |  | [optional] 
**fullname** | **str** |  | [optional] 
**gender** | [**CodeValueData**](CodeValueData.md) |  | [optional] 
**gender_id** | **int** |  | [optional] 
**gender_options** | [**List[CodeValueData]**](CodeValueData.md) |  | [optional] 
**groups** | [**List[GroupGeneralData]**](GroupGeneralData.md) |  | [optional] 
**id** | **int** |  | [optional] 
**image_id** | **int** |  | [optional] 
**image_present** | **bool** |  | [optional] 
**is_address_enabled** | **bool** |  | [optional] 
**is_staff** | **bool** |  | [optional] 
**lastname** | **str** |  | [optional] 
**legal_form** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 
**legal_form_id** | **int** |  | [optional] 
**locale** | **str** |  | [optional] 
**middlename** | **str** |  | [optional] 
**mobile_no** | **str** |  | [optional] 
**narrations** | [**List[CodeValueData]**](CodeValueData.md) |  | [optional] 
**office_id** | **int** |  | [optional] 
**office_name** | **str** |  | [optional] 
**office_options** | [**List[OfficeData]**](OfficeData.md) |  | [optional] 
**row_index** | **int** |  | [optional] 
**saving_account_options** | [**List[SavingsAccountData]**](SavingsAccountData.md) |  | [optional] 
**saving_product_options** | [**List[SavingsProductData]**](SavingsProductData.md) |  | [optional] 
**savings_account_id** | **int** |  | [optional] 
**savings_product_id** | **int** |  | [optional] 
**savings_product_name** | **str** |  | [optional] 
**staff_id** | **int** |  | [optional] 
**staff_name** | **str** |  | [optional] 
**staff_options** | [**List[StaffData]**](StaffData.md) |  | [optional] 
**status** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 
**sub_status** | [**CodeValueData**](CodeValueData.md) |  | [optional] 
**submitted_on_date** | **date** |  | [optional] 
**timeline** | [**ClientTimelineData**](ClientTimelineData.md) |  | [optional] 
**transfer_to_office_id** | **int** |  | [optional] 
**transfer_to_office_name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.client_data import ClientData

# TODO update the JSON string below
json = "{}"
# create an instance of ClientData from a JSON string
client_data_instance = ClientData.from_json(json)
# print the JSON string representation of the object
print(ClientData.to_json())

# convert the object into a dict
client_data_dict = client_data_instance.to_dict()
# create an instance of ClientData from a dict
client_data_from_dict = ClientData.from_dict(client_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


