# TaxDetailsData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | [optional] 
**tax_component** | [**TaxComponentData**](TaxComponentData.md) |  | [optional] 

## Example

```python
from fineract_client.models.tax_details_data import TaxDetailsData

# TODO update the JSON string below
json = "{}"
# create an instance of TaxDetailsData from a JSON string
tax_details_data_instance = TaxDetailsData.from_json(json)
# print the JSON string representation of the object
print(TaxDetailsData.to_json())

# convert the object into a dict
tax_details_data_dict = tax_details_data_instance.to_dict()
# create an instance of TaxDetailsData from a dict
tax_details_data_from_dict = TaxDetailsData.from_dict(tax_details_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


