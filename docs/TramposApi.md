# swagger_client.TramposApi

All URIs are relative to *https://api.kenoby.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gettramposs**](TramposApi.md#gettramposs) | **GET** /trampos | List multiple trampos resources.


# **gettramposs**
> Publications gettramposs()

List multiple trampos resources.

This operation allows you to list and search for trampos resources provided query arguments.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TramposApi()

try:
    # List multiple trampos resources.
    api_response = api_instance.gettramposs()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TramposApi->gettramposs: %s\n" % e)
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

