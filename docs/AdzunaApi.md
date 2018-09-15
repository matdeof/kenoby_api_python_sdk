# swagger_client.AdzunaApi

All URIs are relative to *https://api.kenoby.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getadzunas**](AdzunaApi.md#getadzunas) | **GET** /adzuna | List multiple adzuna resources.


# **getadzunas**
> Publications getadzunas(token)

List multiple adzuna resources.

This operation allows you to list and search for adzuna resources provided query arguments.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdzunaApi()
token = 'token_example' # str | The access token from Adzuna.

try:
    # List multiple adzuna resources.
    api_response = api_instance.getadzunas(token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdzunaApi->getadzunas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| The access token from Adzuna. | 

### Return type

[**Publications**](Publications.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

