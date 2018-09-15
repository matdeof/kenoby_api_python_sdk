# swagger_client.JoobleApi

All URIs are relative to *https://api.kenoby.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getjooble**](JoobleApi.md#getjooble) | **GET** /jooble | List multiple jooble resources.


# **getjooble**
> Publications getjooble()

List multiple jooble resources.

This operation allows you to list and search for jooble resources provided query arguments.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.JoobleApi()

try:
    # List multiple jooble resources.
    api_response = api_instance.getjooble()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JoobleApi->getjooble: %s\n" % e)
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

