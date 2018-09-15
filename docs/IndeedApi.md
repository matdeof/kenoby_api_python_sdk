# swagger_client.IndeedApi

All URIs are relative to *https://api.kenoby.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createindeed**](IndeedApi.md#createindeed) | **POST** /indeed | Create a new indeed applicant
[**getindeeds**](IndeedApi.md#getindeeds) | **GET** /indeed | List multiple indeed resources.


# **createindeed**
> createindeed(x_indeed_signature, body)

Create a new indeed applicant

Create a new indeed applicant

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IndeedApi()
x_indeed_signature = '' # str | X-Indeed-Signature (default to )
body = swagger_client.Publications() # Publications | Data used to create a new indeed applicant

try:
    # Create a new indeed applicant
    api_instance.createindeed(x_indeed_signature, body)
except ApiException as e:
    print("Exception when calling IndeedApi->createindeed: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_indeed_signature** | **str**| X-Indeed-Signature | [default to ]
 **body** | [**Publications**](Publications.md)| Data used to create a new indeed applicant | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getindeeds**
> Publications getindeeds()

List multiple indeed resources.

This operation allows you to list and search for indeed resources provided query arguments.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IndeedApi()

try:
    # List multiple indeed resources.
    api_response = api_instance.getindeeds()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndeedApi->getindeeds: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Publications**](Publications.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

