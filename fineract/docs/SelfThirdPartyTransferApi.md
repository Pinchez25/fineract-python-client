# fineract_client.SelfThirdPartyTransferApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add**](SelfThirdPartyTransferApi.md#add) | **POST** /v1/self/beneficiaries/tpt | Add TPT Beneficiary
[**delete22**](SelfThirdPartyTransferApi.md#delete22) | **DELETE** /v1/self/beneficiaries/tpt/{beneficiaryId} | Delete TPT Beneficiary
[**retrieve_all35**](SelfThirdPartyTransferApi.md#retrieve_all35) | **GET** /v1/self/beneficiaries/tpt | Get All TPT Beneficiary
[**template16**](SelfThirdPartyTransferApi.md#template16) | **GET** /v1/self/beneficiaries/tpt/template | Beneficiary Third Party Transfer Template
[**update23**](SelfThirdPartyTransferApi.md#update23) | **PUT** /v1/self/beneficiaries/tpt/{beneficiaryId} | Update TPT Beneficiary


# **add**
> PostSelfBeneficiariesTPTResponse add(post_self_beneficiaries_tpt_request)

Add TPT Beneficiary

Api to add third party beneficiary linked to current user.

Parameter Definitions

name : Nick name for beneficiary, should be unique for an self service user

officeName : Office Name of beneficiary(not id)

accountNumber : Account Number of beneficiary(not id)

transferLimit : Each transfer initiated to this account will not exceed this amount

Example Requests:

/self/beneficiaries/tpt

Mandatory Fields: name, officeName, accountNumber, accountType

Optional Fields: transferLimit

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_self_beneficiaries_tpt_request import PostSelfBeneficiariesTPTRequest
from fineract_client.models.post_self_beneficiaries_tpt_response import PostSelfBeneficiariesTPTResponse
from fineract_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/fineract-provider/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = fineract_client.Configuration(
    host = "http://localhost/fineract-provider/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = fineract_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: tenantid
configuration.api_key['tenantid'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tenantid'] = 'Bearer'

# Enter a context with an instance of the API client
with fineract_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fineract_client.SelfThirdPartyTransferApi(api_client)
    post_self_beneficiaries_tpt_request = fineract_client.PostSelfBeneficiariesTPTRequest() # PostSelfBeneficiariesTPTRequest | 

    try:
        # Add TPT Beneficiary
        api_response = api_instance.add(post_self_beneficiaries_tpt_request)
        print("The response of SelfThirdPartyTransferApi->add:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SelfThirdPartyTransferApi->add: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_self_beneficiaries_tpt_request** | [**PostSelfBeneficiariesTPTRequest**](PostSelfBeneficiariesTPTRequest.md)|  | 

### Return type

[**PostSelfBeneficiariesTPTResponse**](PostSelfBeneficiariesTPTResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete22**
> DeleteSelfBeneficiariesTPTBeneficiaryIdResponse delete22(beneficiary_id)

Delete TPT Beneficiary

Api to delete third party beneficiary linked to current user.

Example Requests:

/self/beneficiaries/tpt/{beneficiaryId}

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.delete_self_beneficiaries_tpt_beneficiary_id_response import DeleteSelfBeneficiariesTPTBeneficiaryIdResponse
from fineract_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/fineract-provider/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = fineract_client.Configuration(
    host = "http://localhost/fineract-provider/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = fineract_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: tenantid
configuration.api_key['tenantid'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tenantid'] = 'Bearer'

# Enter a context with an instance of the API client
with fineract_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fineract_client.SelfThirdPartyTransferApi(api_client)
    beneficiary_id = 56 # int | 

    try:
        # Delete TPT Beneficiary
        api_response = api_instance.delete22(beneficiary_id)
        print("The response of SelfThirdPartyTransferApi->delete22:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SelfThirdPartyTransferApi->delete22: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **beneficiary_id** | **int**|  | 

### Return type

[**DeleteSelfBeneficiariesTPTBeneficiaryIdResponse**](DeleteSelfBeneficiariesTPTBeneficiaryIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_all35**
> List[GetSelfBeneficiariesTPTResponse] retrieve_all35()

Get All TPT Beneficiary

Api to get all third party beneficiary linked to current user.

Example Requests:

/self/beneficiaries/tpt

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_self_beneficiaries_tpt_response import GetSelfBeneficiariesTPTResponse
from fineract_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/fineract-provider/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = fineract_client.Configuration(
    host = "http://localhost/fineract-provider/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = fineract_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: tenantid
configuration.api_key['tenantid'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tenantid'] = 'Bearer'

# Enter a context with an instance of the API client
with fineract_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fineract_client.SelfThirdPartyTransferApi(api_client)

    try:
        # Get All TPT Beneficiary
        api_response = api_instance.retrieve_all35()
        print("The response of SelfThirdPartyTransferApi->retrieve_all35:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SelfThirdPartyTransferApi->retrieve_all35: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[GetSelfBeneficiariesTPTResponse]**](GetSelfBeneficiariesTPTResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **template16**
> GetSelfBeneficiariesTPTTemplateResponse template16()

Beneficiary Third Party Transfer Template

Returns Account Type enumerations. Self User is expected to know office name and account number to be able to add beneficiary.

Example Requests:

/self/beneficiaries/tpt/template

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_self_beneficiaries_tpt_template_response import GetSelfBeneficiariesTPTTemplateResponse
from fineract_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/fineract-provider/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = fineract_client.Configuration(
    host = "http://localhost/fineract-provider/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = fineract_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: tenantid
configuration.api_key['tenantid'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tenantid'] = 'Bearer'

# Enter a context with an instance of the API client
with fineract_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fineract_client.SelfThirdPartyTransferApi(api_client)

    try:
        # Beneficiary Third Party Transfer Template
        api_response = api_instance.template16()
        print("The response of SelfThirdPartyTransferApi->template16:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SelfThirdPartyTransferApi->template16: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetSelfBeneficiariesTPTTemplateResponse**](GetSelfBeneficiariesTPTTemplateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update23**
> PutSelfBeneficiariesTPTBeneficiaryIdResponse update23(beneficiary_id, put_self_beneficiaries_tpt_beneficiary_id_request)

Update TPT Beneficiary

Api to update third party beneficiary linked to current user.

Example Requests:

/self/beneficiaries/tpt/{beneficiaryId}

Optional Fields: name, transferLimit

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.put_self_beneficiaries_tpt_beneficiary_id_request import PutSelfBeneficiariesTPTBeneficiaryIdRequest
from fineract_client.models.put_self_beneficiaries_tpt_beneficiary_id_response import PutSelfBeneficiariesTPTBeneficiaryIdResponse
from fineract_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/fineract-provider/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = fineract_client.Configuration(
    host = "http://localhost/fineract-provider/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = fineract_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: tenantid
configuration.api_key['tenantid'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tenantid'] = 'Bearer'

# Enter a context with an instance of the API client
with fineract_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fineract_client.SelfThirdPartyTransferApi(api_client)
    beneficiary_id = 56 # int | beneficiaryId
    put_self_beneficiaries_tpt_beneficiary_id_request = fineract_client.PutSelfBeneficiariesTPTBeneficiaryIdRequest() # PutSelfBeneficiariesTPTBeneficiaryIdRequest | 

    try:
        # Update TPT Beneficiary
        api_response = api_instance.update23(beneficiary_id, put_self_beneficiaries_tpt_beneficiary_id_request)
        print("The response of SelfThirdPartyTransferApi->update23:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SelfThirdPartyTransferApi->update23: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **beneficiary_id** | **int**| beneficiaryId | 
 **put_self_beneficiaries_tpt_beneficiary_id_request** | [**PutSelfBeneficiariesTPTBeneficiaryIdRequest**](PutSelfBeneficiariesTPTBeneficiaryIdRequest.md)|  | 

### Return type

[**PutSelfBeneficiariesTPTBeneficiaryIdResponse**](PutSelfBeneficiariesTPTBeneficiaryIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

