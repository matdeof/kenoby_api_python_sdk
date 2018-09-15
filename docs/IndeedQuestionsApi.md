# swagger_client.IndeedQuestionsApi

All URIs are relative to *https://api.kenoby.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**indeed_questions_get**](IndeedQuestionsApi.md#indeed_questions_get) | **GET** /indeed/questions | List indeed questions resources.


# **indeed_questions_get**
> Publications indeed_questions_get()

List indeed questions resources.

This operation allows you to list indeed questions resources.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IndeedQuestionsApi()

try:
    # List indeed questions resources.
    api_response = api_instance.indeed_questions_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndeedQuestionsApi->indeed_questions_get: %s\n" % e)
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

