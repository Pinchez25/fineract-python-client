# fineract_client.StaffApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create3**](StaffApi.md#create3) | **POST** /v1/staff | Create a staff member
[**get_template1**](StaffApi.md#get_template1) | **GET** /v1/staff/downloadtemplate | 
[**post_template**](StaffApi.md#post_template) | **POST** /v1/staff/uploadtemplate | 
[**retrieve_all16**](StaffApi.md#retrieve_all16) | **GET** /v1/staff | Retrieve Staff
[**retrieve_one8**](StaffApi.md#retrieve_one8) | **GET** /v1/staff/{staffId} | Retrieve a Staff Member
[**update7**](StaffApi.md#update7) | **PUT** /v1/staff/{staffId} | Update a Staff Member

# **create3**
> CreateStaffResponse create3(body)

Create a staff member

Creates a staff member.  Mandatory Fields:  officeId, firstname, lastname  Optional Fields:  isLoanOfficer, isActive

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
api_instance = fineract_client.StaffApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostStaffRequest() # PostStaffRequest | 

try:
    # Create a staff member
    api_response = api_instance.create3(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StaffApi->create3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostStaffRequest**](PostStaffRequest.md)|  | 

### Return type

[**CreateStaffResponse**](CreateStaffResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template1**
> get_template1(office_id=office_id, date_format=date_format)



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
api_instance = fineract_client.StaffApi(fineract_client.ApiClient(configuration))
office_id = 789 # int |  (optional)
date_format = 'date_format_example' # str |  (optional)

try:
    api_instance.get_template1(office_id=office_id, date_format=date_format)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_template**
> str post_template(date_format=date_format, locale=locale, uploaded_input_stream=uploaded_input_stream)



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
api_instance = fineract_client.StaffApi(fineract_client.ApiClient(configuration))
date_format = 'date_format_example' # str |  (optional)
locale = 'locale_example' # str |  (optional)
uploaded_input_stream = 'uploaded_input_stream_example' # str |  (optional)

try:
    api_response = api_instance.post_template(date_format=date_format, locale=locale, uploaded_input_stream=uploaded_input_stream)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StaffApi->post_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **date_format** | **str**|  | [optional] 
 **locale** | **str**|  | [optional] 
 **uploaded_input_stream** | **str**|  | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_all16**
> list[RetrieveOneResponse] retrieve_all16(office_id=office_id, staff_in_office_hierarchy=staff_in_office_hierarchy, loan_officers_only=loan_officers_only, status=status)

Retrieve Staff

Returns the list of staff members.  Example Requests:  staff     Retrieve a Staff by status  Returns the details of a Staff based on status.  By default it Returns all the ACTIVE Staff.  If status=INACTIVE, then it returns all INACTIVE Staff.  and for status=ALL, it Returns both ACTIVE and INACTIVE Staff.  Example Requests:  staff?status=active

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
api_instance = fineract_client.StaffApi(fineract_client.ApiClient(configuration))
office_id = 789 # int | officeId (optional)
staff_in_office_hierarchy = false # bool | staffInOfficeHierarchy (optional) (default to false)
loan_officers_only = false # bool | loanOfficersOnly (optional) (default to false)
status = 'active' # str | status (optional) (default to active)

try:
    # Retrieve Staff
    api_response = api_instance.retrieve_all16(office_id=office_id, staff_in_office_hierarchy=staff_in_office_hierarchy, loan_officers_only=loan_officers_only, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StaffApi->retrieve_all16: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | **int**| officeId | [optional] 
 **staff_in_office_hierarchy** | **bool**| staffInOfficeHierarchy | [optional] [default to false]
 **loan_officers_only** | **bool**| loanOfficersOnly | [optional] [default to false]
 **status** | **str**| status | [optional] [default to active]

### Return type

[**list[RetrieveOneResponse]**](RetrieveOneResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_one8**
> RetrieveOneResponse retrieve_one8(staff_id)

Retrieve a Staff Member

Returns the details of a Staff Member.  Example Requests:  staff/1

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
api_instance = fineract_client.StaffApi(fineract_client.ApiClient(configuration))
staff_id = 789 # int | staffId

try:
    # Retrieve a Staff Member
    api_response = api_instance.retrieve_one8(staff_id)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update7**
> UpdateStaffResponse update7(body, staff_id)

Update a Staff Member

Updates the details of a staff member.

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
api_instance = fineract_client.StaffApi(fineract_client.ApiClient(configuration))
body = fineract_client.PutStaffRequest() # PutStaffRequest | 
staff_id = 789 # int | staffId

try:
    # Update a Staff Member
    api_response = api_instance.update7(body, staff_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StaffApi->update7: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutStaffRequest**](PutStaffRequest.md)|  | 
 **staff_id** | **int**| staffId | 

### Return type

[**UpdateStaffResponse**](UpdateStaffResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

