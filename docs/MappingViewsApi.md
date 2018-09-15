# swagger_client.MappingViewsApi

All URIs are relative to *https://api.kenoby.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createmappingviews**](MappingViewsApi.md#createmappingviews) | **POST** /mapping-views | Create a new view from user in applicant to position


# **createmappingviews**
> createmappingviews(authorization, x_tenant, x_version, body)

Create a new view from user in applicant to position

Create a new view from user in applicant to position

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MappingViewsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
body = swagger_client.MappingViews() # MappingViews | Data used to create a new mapping view

try:
    # Create a new view from user in applicant to position
    api_instance.createmappingviews(authorization, x_tenant, x_version, body)
except ApiException as e:
    print("Exception when calling MappingViewsApi->createmappingviews: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **body** | [**MappingViews**](MappingViews.md)| Data used to create a new mapping view | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

