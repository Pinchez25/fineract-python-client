# LoanProductTrancheDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**multi_disburse_loan** | **bool** |  | [optional] 

## Example

```python
from fineract_client.models.loan_product_tranche_details import LoanProductTrancheDetails

# TODO update the JSON string below
json = "{}"
# create an instance of LoanProductTrancheDetails from a JSON string
loan_product_tranche_details_instance = LoanProductTrancheDetails.from_json(json)
# print the JSON string representation of the object
print(LoanProductTrancheDetails.to_json())

# convert the object into a dict
loan_product_tranche_details_dict = loan_product_tranche_details_instance.to_dict()
# create an instance of LoanProductTrancheDetails from a dict
loan_product_tranche_details_from_dict = LoanProductTrancheDetails.from_dict(loan_product_tranche_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


