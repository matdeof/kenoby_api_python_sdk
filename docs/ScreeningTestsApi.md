# swagger_client.ScreeningtestsApi

All URIs are relative to *https://api.kenoby.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createapiscreeningtest**](ScreeningtestsApi.md#createapiscreeningtest) | **POST** /screening-tests/create-api-test | Save and return a specific API screening test type.
[**createapiscreeningtest_0**](ScreeningtestsApi.md#createapiscreeningtest_0) | **POST** /screening-tests/add-applicant-scores | Save and return apiTests to applicant.


# **createapiscreeningtest**
> ApplicantsscreeningTests createapiscreeningtest(name)

Save and return a specific API screening test type.

Save and return a specific API screening test type.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScreeningtestsApi()
name = 'name_example' # str | The name of the test.

try:
    # Save and return a specific API screening test type.
    api_response = api_instance.createapiscreeningtest(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScreeningtestsApi->createapiscreeningtest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the test. | 

### Return type

[**ApplicantsscreeningTests**](ApplicantsscreeningTests.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **createapiscreeningtest_0**
> ApplicantsscreeningTests createapiscreeningtest_0(api_tests)

Save and return apiTests to applicant.

Save and return apiTests to applicant.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScreeningtestsApi()
api_tests = 'api_tests_example' # str | The array of API tests.

try:
    # Save and return apiTests to applicant.
    api_response = api_instance.createapiscreeningtest_0(api_tests)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScreeningtestsApi->createapiscreeningtest_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_tests** | **str**| The array of API tests. | 

### Return type

[**ApplicantsscreeningTests**](ApplicantsscreeningTests.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

