# swagger_client.ElasticsearchApi

All URIs are relative to *https://api.kenoby.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**searchapplicants**](ElasticsearchApi.md#searchapplicants) | **POST** /elastic/search | Search applicants by elastic search


# **searchapplicants**
> searchapplicants(authorization, x_tenant, x_version, body)

Search applicants by elastic search

Create a new applicants

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ElasticsearchApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
body = swagger_client.Applicants() # Applicants | Query used to search applicants

try:
    # Search applicants by elastic search
    api_instance.searchapplicants(authorization, x_tenant, x_version, body)
except ApiException as e:
    print("Exception when calling ElasticsearchApi->searchapplicants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **body** | [**Applicants**](Applicants.md)| Query used to search applicants | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

