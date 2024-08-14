# fineract_client.SelfRunReportApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**run_report1**](SelfRunReportApi.md#run_report1) | **GET** /v1/self/runreports/{reportName} | Running A Report

# **run_report1**
> GetRunReportResponse run_report1(report_name)

Running A Report

Example Requests:   self/runreports/Client%20Details?R_officeId=1   self/runreports/Client%20Details?R_officeId=1&exportCSV=true

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
api_instance = fineract_client.SelfRunReportApi(fineract_client.ApiClient(configuration))
report_name = 'report_name_example' # str | reportName

try:
    # Running A Report
    api_response = api_instance.run_report1(report_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SelfRunReportApi->run_report1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_name** | **str**| reportName | 

### Return type

[**GetRunReportResponse**](GetRunReportResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/pdf, application/vnd.ms-excel, text/csv, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

