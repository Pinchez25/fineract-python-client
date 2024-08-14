# fineract_client.FundsApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_fund**](FundsApi.md#create_fund) | **POST** /v1/funds | Create a Fund
[**retrieve_fund**](FundsApi.md#retrieve_fund) | **GET** /v1/funds/{fundId} | Retrieve a Fund
[**retrieve_funds**](FundsApi.md#retrieve_funds) | **GET** /v1/funds | Retrieve Funds
[**update_fund**](FundsApi.md#update_fund) | **PUT** /v1/funds/{fundId} | Update a Fund

# **create_fund**
> PostFundsResponse create_fund(body)

Create a Fund

Creates a Fund

### Example
```python
from __future__ import print_function
import time
import fineract_client
from fineract_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = fineract_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: tenantid
configuration = fineract_client.Configuration()
configuration.api_key['fineract-platform-tenantid'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['fineract-platform-tenantid'] = 'Bearer'

# create an instance of the API class
api_instance = fineract_client.FundsApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostFundsRequest() # PostFundsRequest | 

try:
    # Create a Fund
    api_response = api_instance.create_fund(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundsApi->create_fund: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostFundsRequest**](PostFundsRequest.md)|  | 

### Return type

[**PostFundsResponse**](PostFundsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_fund**
> GetFundsResponse retrieve_fund(fund_id)

Retrieve a Fund

Returns the details of a Fund.  Example Requests:  funds/1

### Example
```python
from __future__ import print_function
import time
import fineract_client
from fineract_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = fineract_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: tenantid
configuration = fineract_client.Configuration()
configuration.api_key['fineract-platform-tenantid'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['fineract-platform-tenantid'] = 'Bearer'

# create an instance of the API class
api_instance = fineract_client.FundsApi(fineract_client.ApiClient(configuration))
fund_id = 789 # int | fundId

try:
    # Retrieve a Fund
    api_response = api_instance.retrieve_fund(fund_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundsApi->retrieve_fund: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fund_id** | **int**| fundId | 

### Return type

[**GetFundsResponse**](GetFundsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_funds**
> list[GetFundsResponse] retrieve_funds()

Retrieve Funds

Returns the list of funds.  Example Requests:  funds

### Example
```python
from __future__ import print_function
import time
import fineract_client
from fineract_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = fineract_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: tenantid
configuration = fineract_client.Configuration()
configuration.api_key['fineract-platform-tenantid'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['fineract-platform-tenantid'] = 'Bearer'

# create an instance of the API class
api_instance = fineract_client.FundsApi(fineract_client.ApiClient(configuration))

try:
    # Retrieve Funds
    api_response = api_instance.retrieve_funds()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundsApi->retrieve_funds: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[GetFundsResponse]**](GetFundsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_fund**
> PutFundsFundIdResponse update_fund(body, fund_id)

Update a Fund

Updates the details of a fund.

### Example
```python
from __future__ import print_function
import time
import fineract_client
from fineract_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = fineract_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: tenantid
configuration = fineract_client.Configuration()
configuration.api_key['fineract-platform-tenantid'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['fineract-platform-tenantid'] = 'Bearer'

# create an instance of the API class
api_instance = fineract_client.FundsApi(fineract_client.ApiClient(configuration))
body = fineract_client.PutFundsFundIdRequest() # PutFundsFundIdRequest | 
fund_id = 789 # int | fundId

try:
    # Update a Fund
    api_response = api_instance.update_fund(body, fund_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundsApi->update_fund: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutFundsFundIdRequest**](PutFundsFundIdRequest.md)|  | 
 **fund_id** | **int**| fundId | 

### Return type

[**PutFundsFundIdResponse**](PutFundsFundIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

