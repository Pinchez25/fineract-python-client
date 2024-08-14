# fineract_client.MixReportApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_xbrl_report**](MixReportApi.md#retrieve_xbrl_report) | **GET** /v1/mixreport | 

# **retrieve_xbrl_report**
> str retrieve_xbrl_report(start_date=start_date, end_date=end_date, currency=currency)



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
api_instance = fineract_client.MixReportApi(fineract_client.ApiClient(configuration))
start_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
currency = 'currency_example' # str |  (optional)

try:
    api_response = api_instance.retrieve_xbrl_report(start_date=start_date, end_date=end_date, currency=currency)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MixReportApi->retrieve_xbrl_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | [optional] 
 **end_date** | **datetime**|  | [optional] 
 **currency** | **str**|  | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

