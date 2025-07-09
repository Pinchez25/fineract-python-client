# fineract_client.RunReportsApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_all_available_exports**](RunReportsApi.md#retrieve_all_available_exports) | **GET** /v1/runreports/availableExports/{reportName} | Return all available export types for the specific report
[**run_report**](RunReportsApi.md#run_report) | **GET** /v1/runreports/{reportName} | Running a Report


# **retrieve_all_available_exports**
> List[ReportExportType] retrieve_all_available_exports(report_name, is_self_service_user_report=is_self_service_user_report)

Return all available export types for the specific report

Returns the list of all available export types.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.report_export_type import ReportExportType
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
    api_instance = fineract_client.RunReportsApi(api_client)
    report_name = 'report_name_example' # str | reportName
    is_self_service_user_report = False # bool | isSelfServiceUserReport (optional) (default to False)

    try:
        # Return all available export types for the specific report
        api_response = api_instance.retrieve_all_available_exports(report_name, is_self_service_user_report=is_self_service_user_report)
        print("The response of RunReportsApi->retrieve_all_available_exports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunReportsApi->retrieve_all_available_exports: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_name** | **str**| reportName | 
 **is_self_service_user_report** | **bool**| isSelfServiceUserReport | [optional] [default to False]

### Return type

[**List[ReportExportType]**](ReportExportType.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of available export types |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_report**
> RunReportsResponse run_report(report_name, is_self_service_user_report=is_self_service_user_report)

Running a Report

This resource allows you to run and receive output from pre-defined Apache Fineract reports.  Reports can also be used to provide data for searching and workflow functionality.  The default output is a JSON formatted \"Generic Resultset\". The Generic Resultset contains Column Heading as well as Data information. However, you can export to CSV format by simply adding \"&exportCSV=true\" to the end of your URL.  If Pentaho reports have been pre-defined, they can also be run through this resource. Pentaho reports can return HTML, PDF or CSV formats.  The Apache Fineract reference application uses a JQuery plugin called stretchy reporting which, itself, uses this reports resource to provide a pretty flexible reporting User Interface (UI).    Example Requests:  runreports/Client%20Listing?R_officeId=1   runreports/Client%20Listing?R_officeId=1&exportCSV=true   runreports/OfficeIdSelectOne?R_officeId=1&parameterType=true   runreports/OfficeIdSelectOne?R_officeId=1&parameterType=true&exportCSV=true   runreports/Expected%20Payments%20By%20Date%20-%20Formatted?R_endDate=2013-04-30&R_loanOfficerId=-1&R_officeId=1&R_startDate=2013-04-16&output-type=HTML&R_officeId=1   runreports/Expected%20Payments%20By%20Date%20-%20Formatted?R_endDate=2013-04-30&R_loanOfficerId=-1&R_officeId=1&R_startDate=2013-04-16&output-type=XLS&R_officeId=1   runreports/Expected%20Payments%20By%20Date%20-%20Formatted?R_endDate=2013-04-30&R_loanOfficerId=-1&R_officeId=1&R_startDate=2013-04-16&output-type=CSV&R_officeId=1   runreports/Expected%20Payments%20By%20Date%20-%20Formatted?R_endDate=2013-04-30&R_loanOfficerId=-1&R_officeId=1&R_startDate=2013-04-16&output-type=PDF&R_officeId=1

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.run_reports_response import RunReportsResponse
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
    api_instance = fineract_client.RunReportsApi(api_client)
    report_name = 'report_name_example' # str | reportName
    is_self_service_user_report = False # bool | isSelfServiceUserReport (optional) (default to False)

    try:
        # Running a Report
        api_response = api_instance.run_report(report_name, is_self_service_user_report=is_self_service_user_report)
        print("The response of RunReportsApi->run_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunReportsApi->run_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_name** | **str**| reportName | 
 **is_self_service_user_report** | **bool**| isSelfServiceUserReport | [optional] [default to False]

### Return type

[**RunReportsResponse**](RunReportsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/pdf, application/vnd.ms-excel, text/csv, text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

