# fineract_client.ListReportMailingJobHistoryApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_all_by_report_mailing_job_id**](ListReportMailingJobHistoryApi.md#retrieve_all_by_report_mailing_job_id) | **GET** /v1/reportmailingjobrunhistory | List Report Mailing Job History


# **retrieve_all_by_report_mailing_job_id**
> ReportMailingJobRunHistoryData retrieve_all_by_report_mailing_job_id(report_mailing_job_id=report_mailing_job_id, offset=offset, limit=limit, order_by=order_by, sort_order=sort_order)

List Report Mailing Job History

The list capability of report mailing job history can support pagination and sorting.  Example Requests:  reportmailingjobrunhistory/1

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.report_mailing_job_run_history_data import ReportMailingJobRunHistoryData
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
    api_instance = fineract_client.ListReportMailingJobHistoryApi(api_client)
    report_mailing_job_id = 56 # int | reportMailingJobId (optional)
    offset = 56 # int | offset (optional)
    limit = 56 # int | limit (optional)
    order_by = 'order_by_example' # str | orderBy (optional)
    sort_order = 'sort_order_example' # str | sortOrder (optional)

    try:
        # List Report Mailing Job History
        api_response = api_instance.retrieve_all_by_report_mailing_job_id(report_mailing_job_id=report_mailing_job_id, offset=offset, limit=limit, order_by=order_by, sort_order=sort_order)
        print("The response of ListReportMailingJobHistoryApi->retrieve_all_by_report_mailing_job_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListReportMailingJobHistoryApi->retrieve_all_by_report_mailing_job_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_mailing_job_id** | **int**| reportMailingJobId | [optional] 
 **offset** | **int**| offset | [optional] 
 **limit** | **int**| limit | [optional] 
 **order_by** | **str**| orderBy | [optional] 
 **sort_order** | **str**| sortOrder | [optional] 

### Return type

[**ReportMailingJobRunHistoryData**](ReportMailingJobRunHistoryData.md)

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

