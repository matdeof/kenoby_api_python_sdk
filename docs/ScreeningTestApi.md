# swagger_client.ScreeningTestApi

All URIs are relative to *https://api.kenoby.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getoriginaltestsforstage**](ScreeningTestApi.md#getoriginaltestsforstage) | **POST** /screening-tests/original-tests | Returns the original tests for a specific stage
[**getscreeningtestposition**](ScreeningTestApi.md#getscreeningtestposition) | **GET** /screening-tests | Returns possible screening test for a specific position and application
[**listmindsightfunctions**](ScreeningTestApi.md#listmindsightfunctions) | **GET** /screening-tests/list-mindsight-tests | Get Mindsight functions from Mindsight API
[**rankdonetest**](ScreeningTestApi.md#rankdonetest) | **GET** /screening-tests/rankdone-test | Get Rankdone test from Rankdone API
[**rankdonetest_0**](ScreeningTestApi.md#rankdonetest_0) | **GET** /screening-tests/check-rankdone-test | Check Rankdone test from Rankdone API
[**rankdonetests**](ScreeningTestApi.md#rankdonetests) | **GET** /screening-tests/list-rankdone-tests | Get Rankdone tests from Rankdone API
[**testprocessaudio**](ScreeningTestApi.md#testprocessaudio) | **GET** /screening-tests/upload-audio | Upload audio using Google API
[**validatetesttokenscreeningtest**](ScreeningTestApi.md#validatetesttokenscreeningtest) | **POST** /screening-tests/screening-test-valid | Validate token and return if applicant already filled screeningTest.


# **getoriginaltestsforstage**
> Mappings getoriginaltestsforstage(x_tenant, x_version, mappings_id, body)

Returns the original tests for a specific stage

Returns the original tests for a specific stage

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScreeningTestApi()
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
mappings_id = 'mappings_id_example' # str | The ID of the mappings that will be checked.
body = swagger_client.Mappings() # Mappings | Data used to check mapping

try:
    # Returns the original tests for a specific stage
    api_response = api_instance.getoriginaltestsforstage(x_tenant, x_version, mappings_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScreeningTestApi->getoriginaltestsforstage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **mappings_id** | **str**| The ID of the mappings that will be checked. | 
 **body** | [**Mappings**](Mappings.md)| Data used to check mapping | 

### Return type

[**Mappings**](Mappings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getscreeningtestposition**
> getscreeningtestposition(positions_id, application_id)

Returns possible screening test for a specific position and application

Returns possible screening questions for a specific position and application

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScreeningTestApi()
positions_id = 'positions_id_example' # str | The ID of the positions that the token will be generated.
application_id = 'application_id_example' # str | The ID of the positions that the token will be generated.

try:
    # Returns possible screening test for a specific position and application
    api_instance.getscreeningtestposition(positions_id, application_id)
except ApiException as e:
    print("Exception when calling ScreeningTestApi->getscreeningtestposition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **positions_id** | **str**| The ID of the positions that the token will be generated. | 
 **application_id** | **str**| The ID of the positions that the token will be generated. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **listmindsightfunctions**
> listmindsightfunctions(x_tenant, x_version)

Get Mindsight functions from Mindsight API

Get Mindsight functions from Mindsight API

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScreeningTestApi()
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)

try:
    # Get Mindsight functions from Mindsight API
    api_instance.listmindsightfunctions(x_tenant, x_version)
except ApiException as e:
    print("Exception when calling ScreeningTestApi->listmindsightfunctions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rankdonetest**
> rankdonetest(x_tenant, x_version, test_id)

Get Rankdone test from Rankdone API

Get Rankdone test from Rankdone API

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScreeningTestApi()
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
test_id = 'test_id_example' # str | testId of Rankdone test API

try:
    # Get Rankdone test from Rankdone API
    api_instance.rankdonetest(x_tenant, x_version, test_id)
except ApiException as e:
    print("Exception when calling ScreeningTestApi->rankdonetest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **test_id** | **str**| testId of Rankdone test API | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rankdonetest_0**
> rankdonetest_0(x_tenant, x_version, mapping_id, stage_id, original_test)

Check Rankdone test from Rankdone API

Check Rankdone test from Rankdone API

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScreeningTestApi()
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
mapping_id = 'mapping_id_example' # str | mappingId
stage_id = 'stage_id_example' # str | stage of the test
original_test = 'original_test_example' # str | originalTest id of the test (in position)

try:
    # Check Rankdone test from Rankdone API
    api_instance.rankdonetest_0(x_tenant, x_version, mapping_id, stage_id, original_test)
except ApiException as e:
    print("Exception when calling ScreeningTestApi->rankdonetest_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **mapping_id** | **str**| mappingId | 
 **stage_id** | **str**| stage of the test | 
 **original_test** | **str**| originalTest id of the test (in position) | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rankdonetests**
> rankdonetests(x_tenant, x_version, page, search=search)

Get Rankdone tests from Rankdone API

Get Rankdone tests from Rankdone API

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScreeningTestApi()
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
page = 56 # int | page of results (10 per page)
search = 'search_example' # str | text for searching (optional)

try:
    # Get Rankdone tests from Rankdone API
    api_instance.rankdonetests(x_tenant, x_version, page, search=search)
except ApiException as e:
    print("Exception when calling ScreeningTestApi->rankdonetests: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **page** | **int**| page of results (10 per page) | 
 **search** | **str**| text for searching | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **testprocessaudio**
> testprocessaudio(x_tenant, x_version, uri)

Upload audio using Google API

Upload audio using Google API

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScreeningTestApi()
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
uri = 'uri_example' # str | Google Cloud audio file

try:
    # Upload audio using Google API
    api_instance.testprocessaudio(x_tenant, x_version, uri)
except ApiException as e:
    print("Exception when calling ScreeningTestApi->testprocessaudio: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **uri** | **str**| Google Cloud audio file | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validatetesttokenscreeningtest**
> Mappings validatetesttokenscreeningtest(x_tenant, x_version, mappings_id, body)

Validate token and return if applicant already filled screeningTest.

Validate token and return if applicant already filled screeningTest.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScreeningTestApi()
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
mappings_id = 'mappings_id_example' # str | The ID of the mappings that will be checked.
body = swagger_client.Mappings() # Mappings | Data used to check mapping

try:
    # Validate token and return if applicant already filled screeningTest.
    api_response = api_instance.validatetesttokenscreeningtest(x_tenant, x_version, mappings_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScreeningTestApi->validatetesttokenscreeningtest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **mappings_id** | **str**| The ID of the mappings that will be checked. | 
 **body** | [**Mappings**](Mappings.md)| Data used to check mapping | 

### Return type

[**Mappings**](Mappings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

