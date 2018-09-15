# swagger_client.ApplicantRankdoneTestFinishApi

All URIs are relative to *https://api.kenoby.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rankdonescreeningtestfinish**](ApplicantRankdoneTestFinishApi.md#rankdonescreeningtestfinish) | **GET** /screening-tests/rankdone/finish | Rankdone API sends a request to Kenoby informing a candidate that finished a test on their platform.


# **rankdonescreeningtestfinish**
> ApplicantsscreeningTests rankdonescreeningtestfinish(applicant_id)

Rankdone API sends a request to Kenoby informing a candidate that finished a test on their platform.

Rankdone API sends a request to Kenoby informing a candidate that finished a test on their platform.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicantRankdoneTestFinishApi()
applicant_id = 'applicant_id_example' # str | The ID of the application that will be retrieved.

try:
    # Rankdone API sends a request to Kenoby informing a candidate that finished a test on their platform.
    api_response = api_instance.rankdonescreeningtestfinish(applicant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicantRankdoneTestFinishApi->rankdonescreeningtestfinish: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicant_id** | **str**| The ID of the application that will be retrieved. | 

### Return type

[**ApplicantsscreeningTests**](ApplicantsscreeningTests.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

