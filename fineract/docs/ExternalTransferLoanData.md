# ExternalTransferLoanData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_id** | **str** |  | [optional] 
**loan_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.external_transfer_loan_data import ExternalTransferLoanData

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalTransferLoanData from a JSON string
external_transfer_loan_data_instance = ExternalTransferLoanData.from_json(json)
# print the JSON string representation of the object
print ExternalTransferLoanData.to_json()

# convert the object into a dict
external_transfer_loan_data_dict = external_transfer_loan_data_instance.to_dict()
# create an instance of ExternalTransferLoanData from a dict
external_transfer_loan_data_form_dict = external_transfer_loan_data.from_dict(external_transfer_loan_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


