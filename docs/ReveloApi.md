# swagger_client.ReveloApi

All URIs are relative to *https://api.kenoby.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createrevelo**](ReveloApi.md#createrevelo) | **POST** /revelo/apply/{positionId} | Create a new revelo applicant
[**getrevelos**](ReveloApi.md#getrevelos) | **GET** /revelo/{token} | List multiple revelo resources.


# **createrevelo**
> createrevelo(position_id, token, body)

Create a new revelo applicant

Create a new revelo applicant

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReveloApi()
position_id = 'position_id_example' # str | Position id.
token = '' # str | revelo postback token (default to )
body = swagger_client.Publications() # Publications | Data used to create a new revelo applicant

try:
    # Create a new revelo applicant
    api_instance.createrevelo(position_id, token, body)
except ApiException as e:
    print("Exception when calling ReveloApi->createrevelo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **position_id** | **str**| Position id. | 
 **token** | **str**| revelo postback token | [default to ]
 **body** | [**Publications**](Publications.md)| Data used to create a new revelo applicant | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getrevelos**
> Publications getrevelos(token)

List multiple revelo resources.

This operation allows you to list and search for revelo resources provided query arguments.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReveloApi()
token = 'token_example' # str | The access token from Revelo.

try:
    # List multiple revelo resources.
    api_response = api_instance.getrevelos(token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReveloApi->getrevelos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| The access token from Revelo. | 

### Return type

[**Publications**](Publications.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

