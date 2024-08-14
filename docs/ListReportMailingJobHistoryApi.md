# fineract_client.ListReportMailingJobHistoryApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_all_by_report_mailing_job_id**](ListReportMailingJobHistoryApi.md#retrieve_all_by_report_mailing_job_id) | **GET** /v1/reportmailingjobrunhistory | List Report Mailing Job History

# **retrieve_all_by_report_mailing_job_id**
> ReportMailingJobRunHistoryData retrieve_all_by_report_mailing_job_id(report_mailing_job_id=report_mailing_job_id, offset=offset, limit=limit, order_by=order_by, sort_order=sort_order)

List Report Mailing Job History

The list capability of report mailing job history can support pagination and sorting.  Example Requests:  reportmailingjobrunhistory/1

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
api_instance = fineract_client.ListReportMailingJobHistoryApi(fineract_client.ApiClient(configuration))
report_mailing_job_id = 789 # int | reportMailingJobId (optional)
offset = 56 # int | offset (optional)
limit = 56 # int | limit (optional)
order_by = 'order_by_example' # str | orderBy (optional)
sort_order = 'sort_order_example' # str | sortOrder (optional)

try:
    # List Report Mailing Job History
    api_response = api_instance.retrieve_all_by_report_mailing_job_id(report_mailing_job_id=report_mailing_job_id, offset=offset, limit=limit, order_by=order_by, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

