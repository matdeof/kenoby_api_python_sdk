# swagger_client.ScreeningGroupApi

All URIs are relative to *https://api.kenoby.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**checktestisbeingused**](ScreeningGroupApi.md#checktestisbeingused) | **POST** /screening-groups/is-being-used | Check if a screening group is being used in a position.


# **checktestisbeingused**
> ScreeningTestSchema checktestisbeingused(x_tenant, x_version, screening_group_id)

Check if a screening group is being used in a position.

Check if a screening group is being used in a position.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScreeningGroupApi()
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
screening_group_id = 'screening_group_id_example' # str | The ID of the screening group that will be checked.

try:
    # Check if a screening group is being used in a position.
    api_response = api_instance.checktestisbeingused(x_tenant, x_version, screening_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScreeningGroupApi->checktestisbeingused: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **screening_group_id** | **str**| The ID of the screening group that will be checked. | 

### Return type

[**ScreeningTestSchema**](ScreeningTestSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

