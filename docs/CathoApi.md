# swagger_client.CathoApi

All URIs are relative to *https://api.kenoby.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createcatho**](CathoApi.md#createcatho) | **POST** /catho | Create a new catho applicant


# **createcatho**
> createcatho(x_indeed_signature, body)

Create a new catho applicant

Create a new catho applicant

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CathoApi()
x_indeed_signature = '' # str | X-Indeed-Signature (default to )
body = swagger_client.Publications() # Publications | Data used to create a new catho applicant

try:
    # Create a new catho applicant
    api_instance.createcatho(x_indeed_signature, body)
except ApiException as e:
    print("Exception when calling CathoApi->createcatho: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_indeed_signature** | **str**| X-Indeed-Signature | [default to ]
 **body** | [**Publications**](Publications.md)| Data used to create a new catho applicant | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

