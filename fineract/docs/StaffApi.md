# fineract_client.StaffApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create3**](StaffApi.md#create3) | **POST** /v1/staff | Create a staff member
[**get_template1**](StaffApi.md#get_template1) | **GET** /v1/staff/downloadtemplate | 
[**post_template**](StaffApi.md#post_template) | **POST** /v1/staff/uploadtemplate | 
[**retrieve_all16**](StaffApi.md#retrieve_all16) | **GET** /v1/staff | Retrieve Staff
[**retrieve_one8**](StaffApi.md#retrieve_one8) | **GET** /v1/staff/{staffId} | Retrieve a Staff Member
[**update7**](StaffApi.md#update7) | **PUT** /v1/staff/{staffId} | Update a Staff Member


# **create3**
> CreateStaffResponse create3(post_staff_request)

Create a staff member

Creates a staff member.  Mandatory Fields:  officeId, firstname, lastname  Optional Fields:  isLoanOfficer, isActive

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.create_staff_response import CreateStaffResponse
from fineract_client.models.post_staff_request import PostStaffRequest
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
    api_instance = fineract_client.StaffApi(api_client)
    post_staff_request = fineract_client.PostStaffRequest() # PostStaffRequest | 

    try:
        # Create a staff member
        api_response = api_instance.create3(post_staff_request)
        print("The response of StaffApi->create3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StaffApi->create3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_staff_request** | [**PostStaffRequest**](PostStaffRequest.md)|  | 

### Return type

[**CreateStaffResponse**](CreateStaffResponse.md)

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

# **get_template1**
> get_template1(office_id=office_id, date_format=date_format)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
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
    api_instance = fineract_client.StaffApi(api_client)
    office_id = 56 # int |  (optional)
    date_format = 'date_format_example' # str |  (optional)

    try:
        api_instance.get_template1(office_id=office_id, date_format=date_format)
    except Exception as e:
        print("Exception when calling StaffApi->get_template1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | **int**|  | [optional] 
 **date_format** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.ms-excel

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_template**
> str post_template(date_format=date_format, locale=locale, uploaded_input_stream=uploaded_input_stream)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
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
    api_instance = fineract_client.StaffApi(api_client)
    date_format = 'date_format_example' # str |  (optional)
    locale = 'locale_example' # str |  (optional)
    uploaded_input_stream = None # bytearray |  (optional)

    try:
        api_response = api_instance.post_template(date_format=date_format, locale=locale, uploaded_input_stream=uploaded_input_stream)
        print("The response of StaffApi->post_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StaffApi->post_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **date_format** | **str**|  | [optional] 
 **locale** | **str**|  | [optional] 
 **uploaded_input_stream** | **bytearray**|  | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_all16**
> List[RetrieveOneResponse] retrieve_all16(office_id=office_id, staff_in_office_hierarchy=staff_in_office_hierarchy, loan_officers_only=loan_officers_only, status=status)

Retrieve Staff

Returns the list of staff members.  Example Requests:  staff     Retrieve a Staff by status  Returns the details of a Staff based on status.  By default it Returns all the ACTIVE Staff.  If status=INACTIVE, then it returns all INACTIVE Staff.  and for status=ALL, it Returns both ACTIVE and INACTIVE Staff.  Example Requests:  staff?status=active

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.retrieve_one_response import RetrieveOneResponse
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
    api_instance = fineract_client.StaffApi(api_client)
    office_id = 56 # int | officeId (optional)
    staff_in_office_hierarchy = False # bool | staffInOfficeHierarchy (optional) (default to False)
    loan_officers_only = False # bool | loanOfficersOnly (optional) (default to False)
    status = 'active' # str | status (optional) (default to 'active')

    try:
        # Retrieve Staff
        api_response = api_instance.retrieve_all16(office_id=office_id, staff_in_office_hierarchy=staff_in_office_hierarchy, loan_officers_only=loan_officers_only, status=status)
        print("The response of StaffApi->retrieve_all16:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StaffApi->retrieve_all16: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | **int**| officeId | [optional] 
 **staff_in_office_hierarchy** | **bool**| staffInOfficeHierarchy | [optional] [default to False]
 **loan_officers_only** | **bool**| loanOfficersOnly | [optional] [default to False]
 **status** | **str**| status | [optional] [default to &#39;active&#39;]

### Return type

[**List[RetrieveOneResponse]**](RetrieveOneResponse.md)

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

# **retrieve_one8**
> RetrieveOneResponse retrieve_one8(staff_id)

Retrieve a Staff Member

Returns the details of a Staff Member.  Example Requests:  staff/1

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.retrieve_one_response import RetrieveOneResponse
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
    api_instance = fineract_client.StaffApi(api_client)
    staff_id = 56 # int | staffId

    try:
        # Retrieve a Staff Member
        api_response = api_instance.retrieve_one8(staff_id)
        print("The response of StaffApi->retrieve_one8:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StaffApi->retrieve_one8: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **staff_id** | **int**| staffId | 

### Return type

[**RetrieveOneResponse**](RetrieveOneResponse.md)

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

# **update7**
> UpdateStaffResponse update7(staff_id, put_staff_request)

Update a Staff Member

Updates the details of a staff member.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.put_staff_request import PutStaffRequest
from fineract_client.models.update_staff_response import UpdateStaffResponse
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
    api_instance = fineract_client.StaffApi(api_client)
    staff_id = 56 # int | staffId
    put_staff_request = fineract_client.PutStaffRequest() # PutStaffRequest | 

    try:
        # Update a Staff Member
        api_response = api_instance.update7(staff_id, put_staff_request)
        print("The response of StaffApi->update7:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StaffApi->update7: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **staff_id** | **int**| staffId | 
 **put_staff_request** | [**PutStaffRequest**](PutStaffRequest.md)|  | 

### Return type

[**UpdateStaffResponse**](UpdateStaffResponse.md)

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

