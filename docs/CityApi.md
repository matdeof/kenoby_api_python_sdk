# swagger_client.CityApi

All URIs are relative to *https://api.kenoby.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getcities**](CityApi.md#getcities) | **GET** /city | Returns a list of cities available


# **getcities**
> getcities(x_version, city)

Returns a list of cities available

Returns a list of cities available

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CityApi()
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
city = '3.0.0' # str | The string to search cities. (default to 3.0.0)

try:
    # Returns a list of cities available
    api_instance.getcities(x_version, city)
except ApiException as e:
    print("Exception when calling CityApi->getcities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **city** | **str**| The string to search cities. | [default to 3.0.0]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

