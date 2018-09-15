# swagger_client.AuditApi

All URIs are relative to *https://api.kenoby.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getaudit**](AuditApi.md#getaudit) | **GET** /audits/{auditId} | Return a specific audit instance.


# **getaudit**
> Audits getaudit(authorization, x_tenant, x_version, audit_id)

Return a specific audit instance.

Return a specific audit instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuditApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
audit_id = 'audit_id_example' # str | The ID of the audit that will be retrieved.

try:
    # Return a specific audit instance.
    api_response = api_instance.getaudit(authorization, x_tenant, x_version, audit_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditApi->getaudit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **audit_id** | **str**| The ID of the audit that will be retrieved. | 

### Return type

[**Audits**](Audits.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

