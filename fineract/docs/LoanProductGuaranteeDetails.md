# LoanProductGuaranteeDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**mandatory_guarantee** | **float** |  | [optional] 
**minimum_guarantee_from_guarantor** | **float** |  | [optional] 
**minimum_guarantee_from_own_funds** | **float** |  | [optional] 
**new** | **bool** |  | [optional] 

## Example

```python
from fineract_client.models.loan_product_guarantee_details import LoanProductGuaranteeDetails

# TODO update the JSON string below
json = "{}"
# create an instance of LoanProductGuaranteeDetails from a JSON string
loan_product_guarantee_details_instance = LoanProductGuaranteeDetails.from_json(json)
# print the JSON string representation of the object
print LoanProductGuaranteeDetails.to_json()

# convert the object into a dict
loan_product_guarantee_details_dict = loan_product_guarantee_details_instance.to_dict()
# create an instance of LoanProductGuaranteeDetails from a dict
loan_product_guarantee_details_form_dict = loan_product_guarantee_details.from_dict(loan_product_guarantee_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


