# swagger_client.CaptchaApi

All URIs are relative to *https://api.kenoby.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getcaptchaimage**](CaptchaApi.md#getcaptchaimage) | **GET** /captcha | Generate a captcha image


# **getcaptchaimage**
> getcaptchaimage(x_version)

Generate a captcha image

This operation allows to generate a captcha image

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CaptchaApi()
x_version = '3.0.0' # str | The API version. (default to 3.0.0)

try:
    # Generate a captcha image
    api_instance.getcaptchaimage(x_version)
except ApiException as e:
    print("Exception when calling CaptchaApi->getcaptchaimage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_version** | **str**| The API version. | [default to 3.0.0]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

