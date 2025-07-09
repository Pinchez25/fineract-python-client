# fineract_client.ClientApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate1**](ClientApi.md#activate1) | **POST** /v1/clients/{clientId} | Activate a Client | Close a Client | Reject a Client | Withdraw a Client | Reactivate a Client | UndoReject a Client | UndoWithdraw a Client | Assign a Staff | Unassign a Staff | Update Default Savings Account | Propose a Client Transfer | Withdraw a Client Transfer | Reject a Client Transfer | Accept a Client Transfer | Propose and Accept a Client Transfer
[**apply_command**](ClientApi.md#apply_command) | **POST** /v1/clients/external-id/{externalId} | Activate a Client | Close a Client | Reject a Client | Withdraw a Client | Reactivate a Client | UndoReject a Client | UndoWithdraw a Client | Assign a Staff | Unassign a Staff | Update Default Savings Account | Propose a Client Transfer | Withdraw a Client Transfer | Reject a Client Transfer | Accept a Client Transfer | Propose and Accept a Client Transfer
[**create6**](ClientApi.md#create6) | **POST** /v1/clients | Create a Client
[**delete10**](ClientApi.md#delete10) | **DELETE** /v1/clients/external-id/{externalId} | Delete a Client
[**delete9**](ClientApi.md#delete9) | **DELETE** /v1/clients/{clientId} | Delete a Client
[**get_client_template**](ClientApi.md#get_client_template) | **GET** /v1/clients/downloadtemplate | 
[**post_client_template**](ClientApi.md#post_client_template) | **POST** /v1/clients/uploadtemplate | 
[**retrieve_all21**](ClientApi.md#retrieve_all21) | **GET** /v1/clients | List Clients
[**retrieve_associated_accounts**](ClientApi.md#retrieve_associated_accounts) | **GET** /v1/clients/{clientId}/accounts | Retrieve client accounts overview
[**retrieve_associated_accounts1**](ClientApi.md#retrieve_associated_accounts1) | **GET** /v1/clients/external-id/{externalId}/accounts | Retrieve client accounts overview
[**retrieve_obligee_details**](ClientApi.md#retrieve_obligee_details) | **GET** /v1/clients/{clientId}/obligeedetails | Retrieve client obligee details
[**retrieve_obligee_details1**](ClientApi.md#retrieve_obligee_details1) | **GET** /v1/clients/external-id/{externalId}/obligeedetails | Retrieve client obligee details
[**retrieve_one11**](ClientApi.md#retrieve_one11) | **GET** /v1/clients/{clientId} | Retrieve a Client
[**retrieve_one12**](ClientApi.md#retrieve_one12) | **GET** /v1/clients/external-id/{externalId} | Retrieve a Client by External Id
[**retrieve_template5**](ClientApi.md#retrieve_template5) | **GET** /v1/clients/template | Retrieve Client Details Template
[**retrieve_transfer_template**](ClientApi.md#retrieve_transfer_template) | **GET** /v1/clients/{clientId}/transferproposaldate | Retrieve client transfer template
[**retrieve_transfer_template1**](ClientApi.md#retrieve_transfer_template1) | **GET** /v1/clients/external-id/{externalId}/transferproposaldate | Retrieve client transfer template
[**update10**](ClientApi.md#update10) | **PUT** /v1/clients/{clientId} | Update a Client
[**update11**](ClientApi.md#update11) | **PUT** /v1/clients/external-id/{externalId} | Update a Client using the External Id


# **activate1**
> PostClientsClientIdResponse activate1(client_id, post_clients_client_id_request, command=command)

Activate a Client | Close a Client | Reject a Client | Withdraw a Client | Reactivate a Client | UndoReject a Client | UndoWithdraw a Client | Assign a Staff | Unassign a Staff | Update Default Savings Account | Propose a Client Transfer | Withdraw a Client Transfer | Reject a Client Transfer | Accept a Client Transfer | Propose and Accept a Client Transfer

Activate a Client:

Clients can be created in a Pending state. This API exists to enable client activation (for when a client becomes an approved member of the financial Institution).

If the client happens to be already active this API will result in an error.

Close a Client:

Clients can be closed if they do not have any non-closed loans/savingsAccount. This API exists to close a client .

If the client have any active loans/savingsAccount this API will result in an error.

Reject a Client:

Clients can be rejected when client is in pending for activation status.

If the client is any other status, this API throws an error.

Mandatory Fields: rejectionDate, rejectionReasonId

Withdraw a Client:

Client applications can be withdrawn when client is in a pending for activation status.

If the client is any other status, this API throws an error.

Mandatory Fields: withdrawalDate, withdrawalReasonId

Reactivate a Client: Clients can be reactivated after they have been closed.

Trying to reactivate a client in any other state throws an error.

Mandatory Fields: reactivationDate

UndoReject a Client:

Clients can be reactivated after they have been rejected.

Trying to reactivate a client in any other state throws an error.

Mandatory Fields: reopenedDateUndoWithdraw a Client:

Clients can be reactivated after they have been withdrawn.

Trying to reactivate a client in any other state throws an error.

Mandatory Fields: reopenedDate

Assign a Staff:

Allows you to assign a Staff for existed Client.

The selected Staff should belong to the same office (or an officer higher up in the hierarchy) as the Client he manages.

Unassign a Staff:

Allows you to unassign the Staff assigned to a Client.

Update Default Savings Account:

Allows you to modify or assign a default savings account for an existing Client.

The selected savings account should be one among the existing savings account for a particular customer.

Propose a Client Transfer:

Allows you to propose the transfer of a Client to a different Office.

Withdraw a Client Transfer:

Allows you to withdraw the proposed transfer of a Client to a different Office.

Withdrawal can happen only if the destination Branch (to which the transfer was proposed) has not already accepted the transfer proposal

Reject a Client Transfer:

Allows the Destination Branch to reject the proposed Client Transfer.

Accept a Client Transfer:

Allows the Destination Branch to accept the proposed Client Transfer.

The destination branch may also choose to link this client to a group (in which case, any existing active JLG loan of the client is rescheduled to match the meeting frequency of the group) and loan Officer at the time of accepting the transfer

Propose and Accept a Client Transfer:

Abstraction over the Propose and Accept Client Transfer API's which enable a user with Data Scope over both the Target and Destination Branches to directly transfer a Client to the destination Office.

Showing request/response for 'Reject a Client Transfer'

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_clients_client_id_request import PostClientsClientIdRequest
from fineract_client.models.post_clients_client_id_response import PostClientsClientIdResponse
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
    api_instance = fineract_client.ClientApi(api_client)
    client_id = 56 # int | clientId
    post_clients_client_id_request = fineract_client.PostClientsClientIdRequest() # PostClientsClientIdRequest | 
    command = 'command_example' # str | command (optional)

    try:
        # Activate a Client | Close a Client | Reject a Client | Withdraw a Client | Reactivate a Client | UndoReject a Client | UndoWithdraw a Client | Assign a Staff | Unassign a Staff | Update Default Savings Account | Propose a Client Transfer | Withdraw a Client Transfer | Reject a Client Transfer | Accept a Client Transfer | Propose and Accept a Client Transfer
        api_response = api_instance.activate1(client_id, post_clients_client_id_request, command=command)
        print("The response of ClientApi->activate1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientApi->activate1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**| clientId | 
 **post_clients_client_id_request** | [**PostClientsClientIdRequest**](PostClientsClientIdRequest.md)|  | 
 **command** | **str**| command | [optional] 

### Return type

[**PostClientsClientIdResponse**](PostClientsClientIdResponse.md)

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

# **apply_command**
> PostClientsClientIdResponse apply_command(external_id, post_clients_client_id_request, command=command)

Activate a Client | Close a Client | Reject a Client | Withdraw a Client | Reactivate a Client | UndoReject a Client | UndoWithdraw a Client | Assign a Staff | Unassign a Staff | Update Default Savings Account | Propose a Client Transfer | Withdraw a Client Transfer | Reject a Client Transfer | Accept a Client Transfer | Propose and Accept a Client Transfer

Activate a Client:

Clients can be created in a Pending state. This API exists to enable client activation (for when a client becomes an approved member of the financial Institution).

If the client happens to be already active this API will result in an error.

Close a Client:

Clients can be closed if they do not have any non-closed loans/savingsAccount. This API exists to close a client .

If the client have any active loans/savingsAccount this API will result in an error.

Reject a Client:

Clients can be rejected when client is in pending for activation status.

If the client is any other status, this API throws an error.

Mandatory Fields: rejectionDate, rejectionReasonId

Withdraw a Client:

Client applications can be withdrawn when client is in a pending for activation status.

If the client is any other status, this API throws an error.

Mandatory Fields: withdrawalDate, withdrawalReasonId

Reactivate a Client: Clients can be reactivated after they have been closed.

Trying to reactivate a client in any other state throws an error.

Mandatory Fields: reactivationDate

UndoReject a Client:

Clients can be reactivated after they have been rejected.

Trying to reactivate a client in any other state throws an error.

Mandatory Fields: reopenedDateUndoWithdraw a Client:

Clients can be reactivated after they have been withdrawn.

Trying to reactivate a client in any other state throws an error.

Mandatory Fields: reopenedDate

Assign a Staff:

Allows you to assign a Staff for existed Client.

The selected Staff should belong to the same office (or an officer higher up in the hierarchy) as the Client he manages.

Unassign a Staff:

Allows you to unassign the Staff assigned to a Client.

Update Default Savings Account:

Allows you to modify or assign a default savings account for an existing Client.

The selected savings account should be one among the existing savings account for a particular customer.

Propose a Client Transfer:

Allows you to propose the transfer of a Client to a different Office.

Withdraw a Client Transfer:

Allows you to withdraw the proposed transfer of a Client to a different Office.

Withdrawal can happen only if the destination Branch (to which the transfer was proposed) has not already accepted the transfer proposal

Reject a Client Transfer:

Allows the Destination Branch to reject the proposed Client Transfer.

Accept a Client Transfer:

Allows the Destination Branch to accept the proposed Client Transfer.

The destination branch may also choose to link this client to a group (in which case, any existing active JLG loan of the client is rescheduled to match the meeting frequency of the group) and loan Officer at the time of accepting the transfer

Propose and Accept a Client Transfer:

Abstraction over the Propose and Accept Client Transfer API's which enable a user with Data Scope over both the Target and Destination Branches to directly transfer a Client to the destination Office.

Showing request/response for 'Reject a Client Transfer'

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_clients_client_id_request import PostClientsClientIdRequest
from fineract_client.models.post_clients_client_id_response import PostClientsClientIdResponse
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
    api_instance = fineract_client.ClientApi(api_client)
    external_id = 'external_id_example' # str | externalId
    post_clients_client_id_request = fineract_client.PostClientsClientIdRequest() # PostClientsClientIdRequest | 
    command = 'command_example' # str | command (optional)

    try:
        # Activate a Client | Close a Client | Reject a Client | Withdraw a Client | Reactivate a Client | UndoReject a Client | UndoWithdraw a Client | Assign a Staff | Unassign a Staff | Update Default Savings Account | Propose a Client Transfer | Withdraw a Client Transfer | Reject a Client Transfer | Accept a Client Transfer | Propose and Accept a Client Transfer
        api_response = api_instance.apply_command(external_id, post_clients_client_id_request, command=command)
        print("The response of ClientApi->apply_command:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientApi->apply_command: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_id** | **str**| externalId | 
 **post_clients_client_id_request** | [**PostClientsClientIdRequest**](PostClientsClientIdRequest.md)|  | 
 **command** | **str**| command | [optional] 

### Return type

[**PostClientsClientIdResponse**](PostClientsClientIdResponse.md)

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

# **create6**
> PostClientsResponse create6(post_clients_request)

Create a Client

Note:

1. You can enter either:firstname/middlename/lastname - for a person (middlename is optional) OR fullname - for a business or organisation (or person known by one name).

2.If address is enable(enable-address=true), then additional field called address has to be passed.

Mandatory Fields: firstname and lastname OR fullname, officeId, active=true and activationDate OR active=false, if(address enabled) address

Optional Fields: groupId, externalId, accountNo, staffId, mobileNo, savingsProductId, genderId, clientTypeId, clientClassificationId

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_clients_request import PostClientsRequest
from fineract_client.models.post_clients_response import PostClientsResponse
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
    api_instance = fineract_client.ClientApi(api_client)
    post_clients_request = fineract_client.PostClientsRequest() # PostClientsRequest | 

    try:
        # Create a Client
        api_response = api_instance.create6(post_clients_request)
        print("The response of ClientApi->create6:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientApi->create6: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_clients_request** | [**PostClientsRequest**](PostClientsRequest.md)|  | 

### Return type

[**PostClientsResponse**](PostClientsResponse.md)

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

# **delete10**
> DeleteClientsClientIdResponse delete10(external_id, body)

Delete a Client

If a client is in Pending state, you are allowed to Delete it. The delete is a 'hard delete' and cannot be recovered from. Once clients become active or have loans or savings associated with them, you cannot delete the client but you may Close the client if they have left the program.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.delete_clients_client_id_response import DeleteClientsClientIdResponse
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
    api_instance = fineract_client.ClientApi(api_client)
    external_id = 'external_id_example' # str | externalId
    body = None # object | 

    try:
        # Delete a Client
        api_response = api_instance.delete10(external_id, body)
        print("The response of ClientApi->delete10:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientApi->delete10: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_id** | **str**| externalId | 
 **body** | **object**|  | 

### Return type

[**DeleteClientsClientIdResponse**](DeleteClientsClientIdResponse.md)

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

# **delete9**
> DeleteClientsClientIdResponse delete9(client_id, body)

Delete a Client

If a client is in Pending state, you are allowed to Delete it. The delete is a 'hard delete' and cannot be recovered from. Once clients become active or have loans or savings associated with them, you cannot delete the client but you may Close the client if they have left the program.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.delete_clients_client_id_response import DeleteClientsClientIdResponse
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
    api_instance = fineract_client.ClientApi(api_client)
    client_id = 56 # int | clientId
    body = None # object | 

    try:
        # Delete a Client
        api_response = api_instance.delete9(client_id, body)
        print("The response of ClientApi->delete9:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientApi->delete9: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**| clientId | 
 **body** | **object**|  | 

### Return type

[**DeleteClientsClientIdResponse**](DeleteClientsClientIdResponse.md)

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

# **get_client_template**
> get_client_template(legal_form_type=legal_form_type, office_id=office_id, staff_id=staff_id, date_format=date_format)

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
    api_instance = fineract_client.ClientApi(api_client)
    legal_form_type = 'legal_form_type_example' # str |  (optional)
    office_id = 56 # int |  (optional)
    staff_id = 56 # int |  (optional)
    date_format = 'date_format_example' # str |  (optional)

    try:
        api_instance.get_client_template(legal_form_type=legal_form_type, office_id=office_id, staff_id=staff_id, date_format=date_format)
    except Exception as e:
        print("Exception when calling ClientApi->get_client_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **legal_form_type** | **str**|  | [optional] 
 **office_id** | **int**|  | [optional] 
 **staff_id** | **int**|  | [optional] 
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

# **post_client_template**
> str post_client_template(legal_form_type=legal_form_type, date_format=date_format, locale=locale, uploaded_input_stream=uploaded_input_stream)

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
    api_instance = fineract_client.ClientApi(api_client)
    legal_form_type = 'legal_form_type_example' # str |  (optional)
    date_format = 'date_format_example' # str |  (optional)
    locale = 'locale_example' # str |  (optional)
    uploaded_input_stream = None # bytearray |  (optional)

    try:
        api_response = api_instance.post_client_template(legal_form_type=legal_form_type, date_format=date_format, locale=locale, uploaded_input_stream=uploaded_input_stream)
        print("The response of ClientApi->post_client_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientApi->post_client_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **legal_form_type** | **str**|  | [optional] 
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

# **retrieve_all21**
> GetClientsResponse retrieve_all21(office_id=office_id, external_id=external_id, display_name=display_name, first_name=first_name, last_name=last_name, status=status, under_hierarchy=under_hierarchy, offset=offset, limit=limit, order_by=order_by, sort_order=sort_order, orphans_only=orphans_only)

List Clients

The list capability of clients can support pagination and sorting.

Example Requests:

clients

clients?fields=displayName,officeName,timeline

clients?offset=10&limit=50

clients?orderBy=displayName&sortOrder=DESC

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_clients_response import GetClientsResponse
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
    api_instance = fineract_client.ClientApi(api_client)
    office_id = 56 # int | officeId (optional)
    external_id = 'external_id_example' # str | externalId (optional)
    display_name = 'display_name_example' # str | displayName (optional)
    first_name = 'first_name_example' # str | firstName (optional)
    last_name = 'last_name_example' # str | lastName (optional)
    status = 'status_example' # str | status (optional)
    under_hierarchy = 'under_hierarchy_example' # str | underHierarchy (optional)
    offset = 56 # int | offset (optional)
    limit = 56 # int | limit (optional)
    order_by = 'order_by_example' # str | orderBy (optional)
    sort_order = 'sort_order_example' # str | sortOrder (optional)
    orphans_only = True # bool | orphansOnly (optional)

    try:
        # List Clients
        api_response = api_instance.retrieve_all21(office_id=office_id, external_id=external_id, display_name=display_name, first_name=first_name, last_name=last_name, status=status, under_hierarchy=under_hierarchy, offset=offset, limit=limit, order_by=order_by, sort_order=sort_order, orphans_only=orphans_only)
        print("The response of ClientApi->retrieve_all21:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientApi->retrieve_all21: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | **int**| officeId | [optional] 
 **external_id** | **str**| externalId | [optional] 
 **display_name** | **str**| displayName | [optional] 
 **first_name** | **str**| firstName | [optional] 
 **last_name** | **str**| lastName | [optional] 
 **status** | **str**| status | [optional] 
 **under_hierarchy** | **str**| underHierarchy | [optional] 
 **offset** | **int**| offset | [optional] 
 **limit** | **int**| limit | [optional] 
 **order_by** | **str**| orderBy | [optional] 
 **sort_order** | **str**| sortOrder | [optional] 
 **orphans_only** | **bool**| orphansOnly | [optional] 

### Return type

[**GetClientsResponse**](GetClientsResponse.md)

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

# **retrieve_associated_accounts**
> GetClientsClientIdAccountsResponse retrieve_associated_accounts(client_id)

Retrieve client accounts overview

An example of how a loan portfolio summary can be provided. This is requested in a specific use case of the community application.
It is quite reasonable to add resources like this to simplify User Interface development.

Example Requests:
 
clients/1/accounts

clients/1/accounts?fields=loanAccounts,savingsAccounts

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_clients_client_id_accounts_response import GetClientsClientIdAccountsResponse
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
    api_instance = fineract_client.ClientApi(api_client)
    client_id = 56 # int | clientId

    try:
        # Retrieve client accounts overview
        api_response = api_instance.retrieve_associated_accounts(client_id)
        print("The response of ClientApi->retrieve_associated_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientApi->retrieve_associated_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**| clientId | 

### Return type

[**GetClientsClientIdAccountsResponse**](GetClientsClientIdAccountsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_associated_accounts1**
> GetClientsClientIdAccountsResponse retrieve_associated_accounts1(external_id)

Retrieve client accounts overview

An example of how a loan portfolio summary can be provided. This is requested in a specific use case of the community application.
It is quite reasonable to add resources like this to simplify User Interface development.

Example Requests:
 
clients/123-456/accounts

clients/123-456/accounts?fields=loanAccounts,savingsAccounts

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_clients_client_id_accounts_response import GetClientsClientIdAccountsResponse
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
    api_instance = fineract_client.ClientApi(api_client)
    external_id = 'external_id_example' # str | externalId

    try:
        # Retrieve client accounts overview
        api_response = api_instance.retrieve_associated_accounts1(external_id)
        print("The response of ClientApi->retrieve_associated_accounts1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientApi->retrieve_associated_accounts1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_id** | **str**| externalId | 

### Return type

[**GetClientsClientIdAccountsResponse**](GetClientsClientIdAccountsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_obligee_details**
> GetClientObligeeDetailsResponse retrieve_obligee_details(client_id)

Retrieve client obligee details

Retrieve client obligee details

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_client_obligee_details_response import GetClientObligeeDetailsResponse
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
    api_instance = fineract_client.ClientApi(api_client)
    client_id = 56 # int | 

    try:
        # Retrieve client obligee details
        api_response = api_instance.retrieve_obligee_details(client_id)
        print("The response of ClientApi->retrieve_obligee_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientApi->retrieve_obligee_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**|  | 

### Return type

[**GetClientObligeeDetailsResponse**](GetClientObligeeDetailsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_obligee_details1**
> GetClientObligeeDetailsResponse retrieve_obligee_details1(external_id)

Retrieve client obligee details

Retrieve client obligee details using the client external Id

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_client_obligee_details_response import GetClientObligeeDetailsResponse
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
    api_instance = fineract_client.ClientApi(api_client)
    external_id = 'external_id_example' # str | 

    try:
        # Retrieve client obligee details
        api_response = api_instance.retrieve_obligee_details1(external_id)
        print("The response of ClientApi->retrieve_obligee_details1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientApi->retrieve_obligee_details1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_id** | **str**|  | 

### Return type

[**GetClientObligeeDetailsResponse**](GetClientObligeeDetailsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_one11**
> GetClientsClientIdResponse retrieve_one11(client_id, staff_in_selected_office_only=staff_in_selected_office_only)

Retrieve a Client

Example Requests:

clients/1


clients/1?template=true


clients/1?fields=id,displayName,officeName

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_clients_client_id_response import GetClientsClientIdResponse
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
    api_instance = fineract_client.ClientApi(api_client)
    client_id = 56 # int | clientId
    staff_in_selected_office_only = False # bool | staffInSelectedOfficeOnly (optional) (default to False)

    try:
        # Retrieve a Client
        api_response = api_instance.retrieve_one11(client_id, staff_in_selected_office_only=staff_in_selected_office_only)
        print("The response of ClientApi->retrieve_one11:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientApi->retrieve_one11: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**| clientId | 
 **staff_in_selected_office_only** | **bool**| staffInSelectedOfficeOnly | [optional] [default to False]

### Return type

[**GetClientsClientIdResponse**](GetClientsClientIdResponse.md)

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

# **retrieve_one12**
> GetClientsClientIdResponse retrieve_one12(external_id, staff_in_selected_office_only=staff_in_selected_office_only)

Retrieve a Client by External Id

Example Requests:

clients/123-456


clients/123-456?template=true


clients/123-456?fields=id,displayName,officeName

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_clients_client_id_response import GetClientsClientIdResponse
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
    api_instance = fineract_client.ClientApi(api_client)
    external_id = 'external_id_example' # str | externalId
    staff_in_selected_office_only = False # bool | staffInSelectedOfficeOnly (optional) (default to False)

    try:
        # Retrieve a Client by External Id
        api_response = api_instance.retrieve_one12(external_id, staff_in_selected_office_only=staff_in_selected_office_only)
        print("The response of ClientApi->retrieve_one12:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientApi->retrieve_one12: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_id** | **str**| externalId | 
 **staff_in_selected_office_only** | **bool**| staffInSelectedOfficeOnly | [optional] [default to False]

### Return type

[**GetClientsClientIdResponse**](GetClientsClientIdResponse.md)

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

# **retrieve_template5**
> GetClientsTemplateResponse retrieve_template5(office_id=office_id, command_param=command_param, staff_in_selected_office_only=staff_in_selected_office_only)

Retrieve Client Details Template

This is a convenience resource. It can be useful when building maintenance user interface screens for client applications. The template data returned consists of any or all of:

Field Defaults
Allowed Value Lists

Example Request:

clients/template

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_clients_template_response import GetClientsTemplateResponse
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
    api_instance = fineract_client.ClientApi(api_client)
    office_id = 56 # int | officeId (optional)
    command_param = 'command_param_example' # str | commandParam (optional)
    staff_in_selected_office_only = False # bool | staffInSelectedOfficeOnly (optional) (default to False)

    try:
        # Retrieve Client Details Template
        api_response = api_instance.retrieve_template5(office_id=office_id, command_param=command_param, staff_in_selected_office_only=staff_in_selected_office_only)
        print("The response of ClientApi->retrieve_template5:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientApi->retrieve_template5: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | **int**| officeId | [optional] 
 **command_param** | **str**| commandParam | [optional] 
 **staff_in_selected_office_only** | **bool**| staffInSelectedOfficeOnly | [optional] [default to False]

### Return type

[**GetClientsTemplateResponse**](GetClientsTemplateResponse.md)

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

# **retrieve_transfer_template**
> GetClientTransferProposalDateResponse retrieve_transfer_template(client_id)

Retrieve client transfer template

Retrieve client transfer template

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_client_transfer_proposal_date_response import GetClientTransferProposalDateResponse
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
    api_instance = fineract_client.ClientApi(api_client)
    client_id = 56 # int | 

    try:
        # Retrieve client transfer template
        api_response = api_instance.retrieve_transfer_template(client_id)
        print("The response of ClientApi->retrieve_transfer_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientApi->retrieve_transfer_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**|  | 

### Return type

[**GetClientTransferProposalDateResponse**](GetClientTransferProposalDateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_transfer_template1**
> GetClientTransferProposalDateResponse retrieve_transfer_template1(external_id)

Retrieve client transfer template

Retrieve client transfer template using the client external Id

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_client_transfer_proposal_date_response import GetClientTransferProposalDateResponse
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
    api_instance = fineract_client.ClientApi(api_client)
    external_id = 'external_id_example' # str | 

    try:
        # Retrieve client transfer template
        api_response = api_instance.retrieve_transfer_template1(external_id)
        print("The response of ClientApi->retrieve_transfer_template1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientApi->retrieve_transfer_template1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_id** | **str**|  | 

### Return type

[**GetClientTransferProposalDateResponse**](GetClientTransferProposalDateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update10**
> PutClientsClientIdResponse update10(client_id, put_clients_client_id_request)

Update a Client

Note: You can update any of the basic attributes of a client (but not its associations) using this API.

Changing the relationship between a client and its office is not supported through this API. An API specific to handling transfers of clients between offices is available for the same.

The relationship between a client and a group must be removed through the Groups API.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.put_clients_client_id_request import PutClientsClientIdRequest
from fineract_client.models.put_clients_client_id_response import PutClientsClientIdResponse
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
    api_instance = fineract_client.ClientApi(api_client)
    client_id = 56 # int | clientId
    put_clients_client_id_request = fineract_client.PutClientsClientIdRequest() # PutClientsClientIdRequest | 

    try:
        # Update a Client
        api_response = api_instance.update10(client_id, put_clients_client_id_request)
        print("The response of ClientApi->update10:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientApi->update10: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**| clientId | 
 **put_clients_client_id_request** | [**PutClientsClientIdRequest**](PutClientsClientIdRequest.md)|  | 

### Return type

[**PutClientsClientIdResponse**](PutClientsClientIdResponse.md)

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

# **update11**
> PutClientsClientIdResponse update11(external_id, put_clients_client_id_request)

Update a Client using the External Id

Note: You can update any of the basic attributes of a client (but not its associations) using this API.

Changing the relationship between a client and its office is not supported through this API. An API specific to handling transfers of clients between offices is available for the same.

The relationship between a client and a group must be removed through the Groups API.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.put_clients_client_id_request import PutClientsClientIdRequest
from fineract_client.models.put_clients_client_id_response import PutClientsClientIdResponse
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
    api_instance = fineract_client.ClientApi(api_client)
    external_id = 'external_id_example' # str | externalId
    put_clients_client_id_request = fineract_client.PutClientsClientIdRequest() # PutClientsClientIdRequest | 

    try:
        # Update a Client using the External Id
        api_response = api_instance.update11(external_id, put_clients_client_id_request)
        print("The response of ClientApi->update11:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientApi->update11: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_id** | **str**| externalId | 
 **put_clients_client_id_request** | [**PutClientsClientIdRequest**](PutClientsClientIdRequest.md)|  | 

### Return type

[**PutClientsClientIdResponse**](PutClientsClientIdResponse.md)

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

