# fineract_client.DataTablesApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**advanced_query**](DataTablesApi.md#advanced_query) | **POST** /v1/datatables/{datatable}/query | Query Data Table values
[**create_datatable**](DataTablesApi.md#create_datatable) | **POST** /v1/datatables | Create Data Table
[**create_datatable_entry**](DataTablesApi.md#create_datatable_entry) | **POST** /v1/datatables/{datatable}/{apptableId} | Create Entry in Data Table
[**delete_datatable**](DataTablesApi.md#delete_datatable) | **DELETE** /v1/datatables/{datatableName} | Delete Data Table
[**delete_datatable_entries**](DataTablesApi.md#delete_datatable_entries) | **DELETE** /v1/datatables/{datatable}/{apptableId} | Delete Entry(s) in Data Table
[**delete_datatable_entry**](DataTablesApi.md#delete_datatable_entry) | **DELETE** /v1/datatables/{datatable}/{apptableId}/{datatableId} | Delete Entry in Datatable (One to Many)
[**deregister_datatable**](DataTablesApi.md#deregister_datatable) | **POST** /v1/datatables/deregister/{datatable} | Deregister Data Table
[**get_datatable**](DataTablesApi.md#get_datatable) | **GET** /v1/datatables/{datatable} | Retrieve Data Table Details
[**get_datatable1**](DataTablesApi.md#get_datatable1) | **GET** /v1/datatables/{datatable}/{apptableId} | Retrieve Entry(s) from Data Table
[**get_datatable_many_entry**](DataTablesApi.md#get_datatable_many_entry) | **GET** /v1/datatables/{datatable}/{apptableId}/{datatableId} | 
[**get_datatables**](DataTablesApi.md#get_datatables) | **GET** /v1/datatables | List Data Tables
[**query_values**](DataTablesApi.md#query_values) | **GET** /v1/datatables/{datatable}/query | Query Data Table values
[**register_datatable**](DataTablesApi.md#register_datatable) | **POST** /v1/datatables/register/{datatable}/{apptable} | Register Data Table
[**update_datatable**](DataTablesApi.md#update_datatable) | **PUT** /v1/datatables/{datatableName} | Update Data Table
[**update_datatable_entry_one_to_many**](DataTablesApi.md#update_datatable_entry_one_to_many) | **PUT** /v1/datatables/{datatable}/{apptableId}/{datatableId} | Update Entry in Data Table (One to Many)
[**update_datatable_entry_oneto_one**](DataTablesApi.md#update_datatable_entry_oneto_one) | **PUT** /v1/datatables/{datatable}/{apptableId} | Update Entry in Data Table (One to One)


# **advanced_query**
> str advanced_query(datatable, paged_local_request_advanced_query_data=paged_local_request_advanced_query_data)

Query Data Table values

Query values from a registered data table.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.paged_local_request_advanced_query_data import PagedLocalRequestAdvancedQueryData
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
    api_instance = fineract_client.DataTablesApi(api_client)
    datatable = 'datatable_example' # str | datatable
    paged_local_request_advanced_query_data = fineract_client.PagedLocalRequestAdvancedQueryData() # PagedLocalRequestAdvancedQueryData |  (optional)

    try:
        # Query Data Table values
        api_response = api_instance.advanced_query(datatable, paged_local_request_advanced_query_data=paged_local_request_advanced_query_data)
        print("The response of DataTablesApi->advanced_query:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTablesApi->advanced_query: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datatable** | **str**| datatable | 
 **paged_local_request_advanced_query_data** | [**PagedLocalRequestAdvancedQueryData**](PagedLocalRequestAdvancedQueryData.md)|  | [optional] 

### Return type

**str**

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

# **create_datatable**
> PostDataTablesResponse create_datatable(post_data_tables_request)

Create Data Table

Create a new data table and registers it with the Apache Fineract Core application table.  Field Descriptions  Mandatory - datatableName :   The name of the Data Table.  Mandatory - apptableName  Application table name. Must be one of the following:  m_client  m_group  m_loan  m_office  m_saving_account  m_product_loan  m_savings_product  Mandatory - columns   An array of columns in the new Data Table.  Optional - multiRow  Allows to create multiple entries in the Data Table. Optional, defaults to false. If this property is not provided Data Table will allow only one entry.  Field Descriptions - columns  Mandatory - name  Name of the created column. Can contain only alphanumeric characters, underscores and spaces, but cannot start with a number. Cannot start or end with an underscore or space.  Mandatory - type  Column type. Must be one of the following:  Boolean  Date  DateTime  Decimal  Dropdown   Number  String  Text  Mandatory [type = Dropdown] - code  Used in Code description fields. Column name becomes: code_cd_name. Mandatory if using type Dropdown, otherwise an error is returned.  Optional - mandatory  Determines whether this column must have a value in every entry. Optional, defaults to false.  Mandatory [type = String] - length  Length of the text field. Mandatory if type String is used, otherwise an error is returned.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_data_tables_request import PostDataTablesRequest
from fineract_client.models.post_data_tables_response import PostDataTablesResponse
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
    api_instance = fineract_client.DataTablesApi(api_client)
    post_data_tables_request = fineract_client.PostDataTablesRequest() # PostDataTablesRequest | 

    try:
        # Create Data Table
        api_response = api_instance.create_datatable(post_data_tables_request)
        print("The response of DataTablesApi->create_datatable:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTablesApi->create_datatable: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_data_tables_request** | [**PostDataTablesRequest**](PostDataTablesRequest.md)|  | 

### Return type

[**PostDataTablesResponse**](PostDataTablesResponse.md)

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

# **create_datatable_entry**
> PostDataTablesAppTableIdResponse create_datatable_entry(datatable, apptable_id, body)

Create Entry in Data Table

Adds a row to the data table.  Note that the default datatable UI functionality converts any field name containing spaces to underscores when using the API. This means the field name \"Business Description\" is considered the same as \"Business_Description\". So you shouldn't have both \"versions\" in any data table.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_data_tables_app_table_id_response import PostDataTablesAppTableIdResponse
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
    api_instance = fineract_client.DataTablesApi(api_client)
    datatable = 'datatable_example' # str | datatable
    apptable_id = 56 # int | apptableId
    body = 'body_example' # str | {   \"BusinessDescription\": \"Livestock sales\",   \"Comment\": \"First comment made\",   \"Education_cv\": \"Primary\",   \"Gender_cd\": 6,   \"HighestRatePaid\": 8.5,   \"NextVisit\": \"01 October 2012\",   \"YearsinBusiness\": 5,   \"dateFormat\": \"dd MMMM yyyy\",   \"locale\": \"en\" }

    try:
        # Create Entry in Data Table
        api_response = api_instance.create_datatable_entry(datatable, apptable_id, body)
        print("The response of DataTablesApi->create_datatable_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTablesApi->create_datatable_entry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datatable** | **str**| datatable | 
 **apptable_id** | **int**| apptableId | 
 **body** | **str**| {   \&quot;BusinessDescription\&quot;: \&quot;Livestock sales\&quot;,   \&quot;Comment\&quot;: \&quot;First comment made\&quot;,   \&quot;Education_cv\&quot;: \&quot;Primary\&quot;,   \&quot;Gender_cd\&quot;: 6,   \&quot;HighestRatePaid\&quot;: 8.5,   \&quot;NextVisit\&quot;: \&quot;01 October 2012\&quot;,   \&quot;YearsinBusiness\&quot;: 5,   \&quot;dateFormat\&quot;: \&quot;dd MMMM yyyy\&quot;,   \&quot;locale\&quot;: \&quot;en\&quot; } | 

### Return type

[**PostDataTablesAppTableIdResponse**](PostDataTablesAppTableIdResponse.md)

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

# **delete_datatable**
> DeleteDataTablesResponse delete_datatable(datatable_name)

Delete Data Table

Deletes a data table and deregisters it from the Apache Fineract Core application table.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.delete_data_tables_response import DeleteDataTablesResponse
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
    api_instance = fineract_client.DataTablesApi(api_client)
    datatable_name = 'datatable_name_example' # str | datatableName

    try:
        # Delete Data Table
        api_response = api_instance.delete_datatable(datatable_name)
        print("The response of DataTablesApi->delete_datatable:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTablesApi->delete_datatable: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datatable_name** | **str**| datatableName | 

### Return type

[**DeleteDataTablesResponse**](DeleteDataTablesResponse.md)

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

# **delete_datatable_entries**
> DeleteDataTablesDatatableAppTableIdResponse delete_datatable_entries(datatable, apptable_id)

Delete Entry(s) in Data Table

Deletes the entry (if it exists) for data tables that are one-to-one with the application table.  Deletes the entries (if they exist) for data tables that are one-to-many with the application table.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.delete_data_tables_datatable_app_table_id_response import DeleteDataTablesDatatableAppTableIdResponse
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
    api_instance = fineract_client.DataTablesApi(api_client)
    datatable = 'datatable_example' # str | datatable
    apptable_id = 56 # int | apptableId

    try:
        # Delete Entry(s) in Data Table
        api_response = api_instance.delete_datatable_entries(datatable, apptable_id)
        print("The response of DataTablesApi->delete_datatable_entries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTablesApi->delete_datatable_entries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datatable** | **str**| datatable | 
 **apptable_id** | **int**| apptableId | 

### Return type

[**DeleteDataTablesDatatableAppTableIdResponse**](DeleteDataTablesDatatableAppTableIdResponse.md)

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

# **delete_datatable_entry**
> DeleteDataTablesDatatableAppTableIdDatatableIdResponse delete_datatable_entry(datatable, apptable_id, datatable_id)

Delete Entry in Datatable (One to Many)

Deletes the entry (if it exists) for data tables that are one to many with the application table.  

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.delete_data_tables_datatable_app_table_id_datatable_id_response import DeleteDataTablesDatatableAppTableIdDatatableIdResponse
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
    api_instance = fineract_client.DataTablesApi(api_client)
    datatable = '{}' # str | datatable
    apptable_id = 56 # int | apptableId
    datatable_id = 56 # int | datatableId

    try:
        # Delete Entry in Datatable (One to Many)
        api_response = api_instance.delete_datatable_entry(datatable, apptable_id, datatable_id)
        print("The response of DataTablesApi->delete_datatable_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTablesApi->delete_datatable_entry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datatable** | **str**| datatable | 
 **apptable_id** | **int**| apptableId | 
 **datatable_id** | **int**| datatableId | 

### Return type

[**DeleteDataTablesDatatableAppTableIdDatatableIdResponse**](DeleteDataTablesDatatableAppTableIdDatatableIdResponse.md)

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

# **deregister_datatable**
> PutDataTablesResponse deregister_datatable(datatable)

Deregister Data Table

Deregisters a data table. It will no longer be available through the API.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.put_data_tables_response import PutDataTablesResponse
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
    api_instance = fineract_client.DataTablesApi(api_client)
    datatable = 'datatable_example' # str | datatable

    try:
        # Deregister Data Table
        api_response = api_instance.deregister_datatable(datatable)
        print("The response of DataTablesApi->deregister_datatable:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTablesApi->deregister_datatable: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datatable** | **str**| datatable | 

### Return type

[**PutDataTablesResponse**](PutDataTablesResponse.md)

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

# **get_datatable**
> GetDataTablesResponse get_datatable(datatable)

Retrieve Data Table Details

Lists a registered data table details and the Apache Fineract Core application table they are registered to.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_data_tables_response import GetDataTablesResponse
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
    api_instance = fineract_client.DataTablesApi(api_client)
    datatable = 'datatable_example' # str | datatable

    try:
        # Retrieve Data Table Details
        api_response = api_instance.get_datatable(datatable)
        print("The response of DataTablesApi->get_datatable:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTablesApi->get_datatable: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datatable** | **str**| datatable | 

### Return type

[**GetDataTablesResponse**](GetDataTablesResponse.md)

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

# **get_datatable1**
> str get_datatable1(datatable, apptable_id, order=order)

Retrieve Entry(s) from Data Table

Gets the entry (if it exists) for data tables that are one to one with the application table.  Gets the entries (if they exist) for data tables that are one to many with the application table.  Note: The 'fields' parameter is not available for datatables.  ARGUMENTS orderoptional Specifies the order in which data is returned.genericResultSetoptional, defaults to false If 'true' an optimised JSON format is returned suitable for tabular display of data. This format is used by the default data tables UI functionality. Example Requests:  datatables/extra_client_details/1   datatables/extra_family_details/1?order=`Date of Birth` desc   datatables/extra_client_details/1?genericResultSet=true

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
    api_instance = fineract_client.DataTablesApi(api_client)
    datatable = 'datatable_example' # str | datatable
    apptable_id = 56 # int | apptableId
    order = 'order_example' # str | order (optional)

    try:
        # Retrieve Entry(s) from Data Table
        api_response = api_instance.get_datatable1(datatable, apptable_id, order=order)
        print("The response of DataTablesApi->get_datatable1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTablesApi->get_datatable1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datatable** | **str**| datatable | 
 **apptable_id** | **int**| apptableId | 
 **order** | **str**| order | [optional] 

### Return type

**str**

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

# **get_datatable_many_entry**
> str get_datatable_many_entry(datatable, apptable_id, datatable_id, order=order, generic_result_set=generic_result_set)



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
    api_instance = fineract_client.DataTablesApi(api_client)
    datatable = 'datatable_example' # str | 
    apptable_id = 56 # int | 
    datatable_id = 56 # int | 
    order = 'order_example' # str |  (optional)
    generic_result_set = False # bool | Optional flag to format the response (optional) (default to False)

    try:
        api_response = api_instance.get_datatable_many_entry(datatable, apptable_id, datatable_id, order=order, generic_result_set=generic_result_set)
        print("The response of DataTablesApi->get_datatable_many_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTablesApi->get_datatable_many_entry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datatable** | **str**|  | 
 **apptable_id** | **int**|  | 
 **datatable_id** | **int**|  | 
 **order** | **str**|  | [optional] 
 **generic_result_set** | **bool**| Optional flag to format the response | [optional] [default to False]

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_datatables**
> List[GetDataTablesResponse] get_datatables(apptable=apptable)

List Data Tables

Lists registered data tables and the Apache Fineract Core application table they are registered to.  ARGUMENTS  apptable  - optional The Apache Fineract core application table.  Example Requests:  datatables?apptable=m_client   datatables

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_data_tables_response import GetDataTablesResponse
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
    api_instance = fineract_client.DataTablesApi(api_client)
    apptable = 'apptable_example' # str | apptable (optional)

    try:
        # List Data Tables
        api_response = api_instance.get_datatables(apptable=apptable)
        print("The response of DataTablesApi->get_datatables:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTablesApi->get_datatables: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apptable** | **str**| apptable | [optional] 

### Return type

[**List[GetDataTablesResponse]**](GetDataTablesResponse.md)

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

# **query_values**
> str query_values(datatable, column_filter=column_filter, value_filter=value_filter, result_columns=result_columns)

Query Data Table values

Query values from a registered data table.

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
    api_instance = fineract_client.DataTablesApi(api_client)
    datatable = 'datatable_example' # str | datatable
    column_filter = 'column_filter_example' # str | columnFilter (optional)
    value_filter = 'value_filter_example' # str | valueFilter (optional)
    result_columns = 'result_columns_example' # str | resultColumns (optional)

    try:
        # Query Data Table values
        api_response = api_instance.query_values(datatable, column_filter=column_filter, value_filter=value_filter, result_columns=result_columns)
        print("The response of DataTablesApi->query_values:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTablesApi->query_values: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datatable** | **str**| datatable | 
 **column_filter** | **str**| columnFilter | [optional] 
 **value_filter** | **str**| valueFilter | [optional] 
 **result_columns** | **str**| resultColumns | [optional] 

### Return type

**str**

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

# **register_datatable**
> PutDataTablesResponse register_datatable(datatable, apptable, body=body)

Register Data Table

Registers a data table with the Apache Fineract Core application table. This allows the data table to be maintained through the API. In case the datatable is a PPI (survey table), a parameter category should be pass along with the request. The API currently support one category (200)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.put_data_tables_response import PutDataTablesResponse
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
    api_instance = fineract_client.DataTablesApi(api_client)
    datatable = 'datatable_example' # str | datatable
    apptable = 'apptable_example' # str | apptable
    body = None # object |  (optional)

    try:
        # Register Data Table
        api_response = api_instance.register_datatable(datatable, apptable, body=body)
        print("The response of DataTablesApi->register_datatable:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTablesApi->register_datatable: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datatable** | **str**| datatable | 
 **apptable** | **str**| apptable | 
 **body** | **object**|  | [optional] 

### Return type

[**PutDataTablesResponse**](PutDataTablesResponse.md)

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

# **update_datatable**
> PutDataTablesResponse update_datatable(datatable_name, put_data_tables_request)

Update Data Table

Modifies fields of a data table. If the apptableName parameter is passed, data table is deregistered and registered with the new application table.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.put_data_tables_request import PutDataTablesRequest
from fineract_client.models.put_data_tables_response import PutDataTablesResponse
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
    api_instance = fineract_client.DataTablesApi(api_client)
    datatable_name = 'datatable_name_example' # str | datatableName
    put_data_tables_request = fineract_client.PutDataTablesRequest() # PutDataTablesRequest | 

    try:
        # Update Data Table
        api_response = api_instance.update_datatable(datatable_name, put_data_tables_request)
        print("The response of DataTablesApi->update_datatable:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTablesApi->update_datatable: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datatable_name** | **str**| datatableName | 
 **put_data_tables_request** | [**PutDataTablesRequest**](PutDataTablesRequest.md)|  | 

### Return type

[**PutDataTablesResponse**](PutDataTablesResponse.md)

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

# **update_datatable_entry_one_to_many**
> PutDataTablesAppTableIdDatatableIdResponse update_datatable_entry_one_to_many(datatable, apptable_id, datatable_id, body)

Update Entry in Data Table (One to Many)

Updates the row (if it exists) of the data table.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.put_data_tables_app_table_id_datatable_id_response import PutDataTablesAppTableIdDatatableIdResponse
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
    api_instance = fineract_client.DataTablesApi(api_client)
    datatable = 'datatable_example' # str | datatable
    apptable_id = 56 # int | apptableId
    datatable_id = 56 # int | datatableId
    body = 'body_example' # str | 

    try:
        # Update Entry in Data Table (One to Many)
        api_response = api_instance.update_datatable_entry_one_to_many(datatable, apptable_id, datatable_id, body)
        print("The response of DataTablesApi->update_datatable_entry_one_to_many:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTablesApi->update_datatable_entry_one_to_many: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datatable** | **str**| datatable | 
 **apptable_id** | **int**| apptableId | 
 **datatable_id** | **int**| datatableId | 
 **body** | **str**|  | 

### Return type

[**PutDataTablesAppTableIdDatatableIdResponse**](PutDataTablesAppTableIdDatatableIdResponse.md)

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

# **update_datatable_entry_oneto_one**
> PutDataTablesAppTableIdResponse update_datatable_entry_oneto_one(datatable, apptable_id, body)

Update Entry in Data Table (One to One)

Updates the row (if it exists) of the data table.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.put_data_tables_app_table_id_response import PutDataTablesAppTableIdResponse
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
    api_instance = fineract_client.DataTablesApi(api_client)
    datatable = 'datatable_example' # str | datatable
    apptable_id = 56 # int | apptableId
    body = 'body_example' # str | 

    try:
        # Update Entry in Data Table (One to One)
        api_response = api_instance.update_datatable_entry_oneto_one(datatable, apptable_id, body)
        print("The response of DataTablesApi->update_datatable_entry_oneto_one:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTablesApi->update_datatable_entry_oneto_one: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datatable** | **str**| datatable | 
 **apptable_id** | **int**| apptableId | 
 **body** | **str**|  | 

### Return type

[**PutDataTablesAppTableIdResponse**](PutDataTablesAppTableIdResponse.md)

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

