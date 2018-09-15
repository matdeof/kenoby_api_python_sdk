# swagger_client.DashboardApi

All URIs are relative to *https://api.kenoby.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dashboards**](DashboardApi.md#create_dashboards) | **POST** /dashboards | Create a new dashboards


# **create_dashboards**
> create_dashboards(authorization, x_tenant, x_version, body)

Create a new dashboards

Create a new dashboards

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DashboardApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
body = swagger_client.Dashboards() # Dashboards | Data used to create a new dashboards

try:
    # Create a new dashboards
    api_instance.create_dashboards(authorization, x_tenant, x_version, body)
except ApiException as e:
    print("Exception when calling DashboardApi->create_dashboards: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **body** | [**Dashboards**](Dashboards.md)| Data used to create a new dashboards | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

