# CalculateFixedDepositInterestResponse

CalculateFixedDepositInterestResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maturity_amount** | **float** |  | [optional] 
**warning** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.calculate_fixed_deposit_interest_response import CalculateFixedDepositInterestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CalculateFixedDepositInterestResponse from a JSON string
calculate_fixed_deposit_interest_response_instance = CalculateFixedDepositInterestResponse.from_json(json)
# print the JSON string representation of the object
print CalculateFixedDepositInterestResponse.to_json()

# convert the object into a dict
calculate_fixed_deposit_interest_response_dict = calculate_fixed_deposit_interest_response_instance.to_dict()
# create an instance of CalculateFixedDepositInterestResponse from a dict
calculate_fixed_deposit_interest_response_form_dict = calculate_fixed_deposit_interest_response.from_dict(calculate_fixed_deposit_interest_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


