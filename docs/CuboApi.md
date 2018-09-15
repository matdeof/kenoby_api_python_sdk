# swagger_client.CuboApi

All URIs are relative to *https://api.kenoby.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getcubos**](CuboApi.md#getcubos) | **GET** /cubo | List multiple cubo resources.
[**getcubotokenvalidators**](CuboApi.md#getcubotokenvalidators) | **POST** /cubo/token-validator | Cubo access-token validate.


# **getcubos**
> Publications getcubos()

List multiple cubo resources.

This operation allows you to list and search for cubo resources provided query arguments.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CuboApi()

try:
    # List multiple cubo resources.
    api_response = api_instance.getcubos()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CuboApi->getcubos: %s\n" % e)
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

# **getcubotokenvalidators**
> Publications getcubotokenvalidators(authorization, x_tenant, x_version, token)

Cubo access-token validate.

This operation allows you verify authorization token of CUBO integration.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CuboApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
token = 'token_example' # str | The access token from Cubo.

try:
    # Cubo access-token validate.
    api_response = api_instance.getcubotokenvalidators(authorization, x_tenant, x_version, token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CuboApi->getcubotokenvalidators: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **token** | **str**| The access token from Cubo. | 

### Return type

[**Publications**](Publications.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

