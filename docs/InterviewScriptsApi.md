# swagger_client.InterviewScriptsApi

All URIs are relative to *https://api.kenoby.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_interview_scripts**](InterviewScriptsApi.md#create_interview_scripts) | **POST** /interviewScripts | Create a new interviewScripts
[**deleteinterview_scripts**](InterviewScriptsApi.md#deleteinterview_scripts) | **DELETE** /interviewScripts/{interviewScriptsId} | Delete a specific interviewScript instance.
[**getinterview_scripts**](InterviewScriptsApi.md#getinterview_scripts) | **GET** /interviewScripts/{interviewScriptsId} | Return a specific interviewScript instance.
[**getinterview_scriptss**](InterviewScriptsApi.md#getinterview_scriptss) | **GET** /interviewScripts | List multiple interviewScripts resources.
[**updateinterview_scripts**](InterviewScriptsApi.md#updateinterview_scripts) | **PUT** /interviewScripts/{interviewScriptsId} | Update a specific interviewScript instance.


# **create_interview_scripts**
> create_interview_scripts(authorization, x_tenant, x_version, body)

Create a new interviewScripts

Create a new interviewScripts

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InterviewScriptsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
body = swagger_client.InterviewScripts() # InterviewScripts | Data used to create a new interviewScripts

try:
    # Create a new interviewScripts
    api_instance.create_interview_scripts(authorization, x_tenant, x_version, body)
except ApiException as e:
    print("Exception when calling InterviewScriptsApi->create_interview_scripts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **body** | [**InterviewScripts**](InterviewScripts.md)| Data used to create a new interviewScripts | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deleteinterview_scripts**
> InterviewScripts deleteinterview_scripts(authorization, x_tenant, x_version, interview_scripts_id, body)

Delete a specific interviewScript instance.

Delete a specific interviewScript instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InterviewScriptsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
interview_scripts_id = 'interview_scripts_id_example' # str | The ID of the interviewScripts that will be deleted.
body = swagger_client.InterviewScripts() # InterviewScripts | Data used to delete interviewScripts

try:
    # Delete a specific interviewScript instance.
    api_response = api_instance.deleteinterview_scripts(authorization, x_tenant, x_version, interview_scripts_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterviewScriptsApi->deleteinterview_scripts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **interview_scripts_id** | **str**| The ID of the interviewScripts that will be deleted. | 
 **body** | [**InterviewScripts**](InterviewScripts.md)| Data used to delete interviewScripts | 

### Return type

[**InterviewScripts**](InterviewScripts.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getinterview_scripts**
> InterviewScripts getinterview_scripts(authorization, x_tenant, x_version, interview_scripts_id)

Return a specific interviewScript instance.

Return a specific interviewScript instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InterviewScriptsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
interview_scripts_id = 'interview_scripts_id_example' # str | The ID of the interviewScripts that will be retrieved.

try:
    # Return a specific interviewScript instance.
    api_response = api_instance.getinterview_scripts(authorization, x_tenant, x_version, interview_scripts_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterviewScriptsApi->getinterview_scripts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **interview_scripts_id** | **str**| The ID of the interviewScripts that will be retrieved. | 

### Return type

[**InterviewScripts**](InterviewScripts.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getinterview_scriptss**
> InterviewScriptsList getinterview_scriptss(authorization, x_tenant, x_version, page=page, page_size=page_size, order_by=order_by, select_0=select_0, select_1=select_1, filter_by_name_like=filter_by_name_like, filter_by_created_at_from=filter_by_created_at_from, filter_by_created_at_to=filter_by_created_at_to, count_0_filter_by_name_like=count_0_filter_by_name_like, count_1_filter_by_created_at_from=count_1_filter_by_created_at_from, search_by=search_by)

List multiple interviewScripts resources.

This operation allows you to list and search for interviewScripts resources provided query arguments.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InterviewScriptsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
page = 1 # int | The page of records. Used for pagination. (optional) (default to 1)
page_size = 20 # int | How many records to limit the output. (optional) (default to 20)
order_by = 'name' # str | Which fields to sort the records on. You can use minus sign to have a reverse order. Ex.: orderBy=-name (optional) (default to name)
select_0 = '' # str | Select which fields will be returned by the query. (optional) (default to )
select_1 = '' # str | Select which fields will be returned by the query. One select for each field (optional) (default to )
filter_by_name_like = '' # str | Filter the results. This is just a sample. You can use a better tool like postman to try other filters. Ex: filterBy[fieldA]=some value&filterBy[fieldB][fieldDfromC]=other value (optional) (default to )
filter_by_created_at_from = '2015-01-01T02:00:00.000Z' # str | Filter the results greatter than a given date (optional) (default to 2015-01-01T02:00:00.000Z)
filter_by_created_at_to = '2017-01-01T02:00:00.000Z' # str | Filter the results lower than a given date (optional) (default to 2017-01-01T02:00:00.000Z)
count_0_filter_by_name_like = '' # str | Return the total records from a filterBy query. Ex.: count[0][filterBy][name][like]=Ricardo (optional) (default to )
count_1_filter_by_created_at_from = '' # str | Return the total records from createdFrom a specific date. Ex.: count[1][filterBy][createdAt][from]=2015-01-01T02:00:00.000Z (optional) (default to )
search_by = '' # str | Make a text search on main fields. Name and e-mail have higher scores. (optional) (default to )

try:
    # List multiple interviewScripts resources.
    api_response = api_instance.getinterview_scriptss(authorization, x_tenant, x_version, page=page, page_size=page_size, order_by=order_by, select_0=select_0, select_1=select_1, filter_by_name_like=filter_by_name_like, filter_by_created_at_from=filter_by_created_at_from, filter_by_created_at_to=filter_by_created_at_to, count_0_filter_by_name_like=count_0_filter_by_name_like, count_1_filter_by_created_at_from=count_1_filter_by_created_at_from, search_by=search_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterviewScriptsApi->getinterview_scriptss: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **page** | **int**| The page of records. Used for pagination. | [optional] [default to 1]
 **page_size** | **int**| How many records to limit the output. | [optional] [default to 20]
 **order_by** | **str**| Which fields to sort the records on. You can use minus sign to have a reverse order. Ex.: orderBy&#x3D;-name | [optional] [default to name]
 **select_0** | **str**| Select which fields will be returned by the query. | [optional] [default to ]
 **select_1** | **str**| Select which fields will be returned by the query. One select for each field | [optional] [default to ]
 **filter_by_name_like** | **str**| Filter the results. This is just a sample. You can use a better tool like postman to try other filters. Ex: filterBy[fieldA]&#x3D;some value&amp;filterBy[fieldB][fieldDfromC]&#x3D;other value | [optional] [default to ]
 **filter_by_created_at_from** | **str**| Filter the results greatter than a given date | [optional] [default to 2015-01-01T02:00:00.000Z]
 **filter_by_created_at_to** | **str**| Filter the results lower than a given date | [optional] [default to 2017-01-01T02:00:00.000Z]
 **count_0_filter_by_name_like** | **str**| Return the total records from a filterBy query. Ex.: count[0][filterBy][name][like]&#x3D;Ricardo | [optional] [default to ]
 **count_1_filter_by_created_at_from** | **str**| Return the total records from createdFrom a specific date. Ex.: count[1][filterBy][createdAt][from]&#x3D;2015-01-01T02:00:00.000Z | [optional] [default to ]
 **search_by** | **str**| Make a text search on main fields. Name and e-mail have higher scores. | [optional] [default to ]

### Return type

[**InterviewScriptsList**](InterviewScriptsList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updateinterview_scripts**
> InterviewScripts updateinterview_scripts(authorization, x_tenant, x_version, interview_scripts_id, body)

Update a specific interviewScript instance.

Update a specific interviewScript instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InterviewScriptsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
interview_scripts_id = 'interview_scripts_id_example' # str | The ID of the interviewScripts that will be updated.
body = swagger_client.InterviewScripts() # InterviewScripts | Data used to update interviewScripts

try:
    # Update a specific interviewScript instance.
    api_response = api_instance.updateinterview_scripts(authorization, x_tenant, x_version, interview_scripts_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterviewScriptsApi->updateinterview_scripts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **interview_scripts_id** | **str**| The ID of the interviewScripts that will be updated. | 
 **body** | [**InterviewScripts**](InterviewScripts.md)| Data used to update interviewScripts | 

### Return type

[**InterviewScripts**](InterviewScripts.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

