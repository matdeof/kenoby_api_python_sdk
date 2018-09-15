# swagger_client.ScreeningGroupsApi

All URIs are relative to *https://api.kenoby.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_screening_groups**](ScreeningGroupsApi.md#create_screening_groups) | **POST** /screeningGroups | Create a new screeningGroups
[**disable_screening_group**](ScreeningGroupsApi.md#disable_screening_group) | **POST** /screeningGroups/:id/disable | Disable a specific screeningGroup
[**getscreening_group**](ScreeningGroupsApi.md#getscreening_group) | **GET** /screeningGroups/{screeningGroupId} | Return a specific screeningGroup instance.
[**getscreening_groups**](ScreeningGroupsApi.md#getscreening_groups) | **GET** /screeningGroups | List multiple screeningGroups resources.
[**order_screening_groups**](ScreeningGroupsApi.md#order_screening_groups) | **POST** /screeningGroups/order | Order screeningGroups
[**updatescreening_groups**](ScreeningGroupsApi.md#updatescreening_groups) | **PUT** /screeningGroups/{screeningGroupId} | Update a specific screeningGroup instance.


# **create_screening_groups**
> create_screening_groups(authorization, x_tenant, x_version, body)

Create a new screeningGroups

Create a new screeningGroups

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScreeningGroupsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
body = swagger_client.ScreeningGroups() # ScreeningGroups | Data used to create a new screeningGroups

try:
    # Create a new screeningGroups
    api_instance.create_screening_groups(authorization, x_tenant, x_version, body)
except ApiException as e:
    print("Exception when calling ScreeningGroupsApi->create_screening_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **body** | [**ScreeningGroups**](ScreeningGroups.md)| Data used to create a new screeningGroups | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_screening_group**
> disable_screening_group(authorization, x_tenant, x_version)

Disable a specific screeningGroup

Disable a specific screeningGroup

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScreeningGroupsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)

try:
    # Disable a specific screeningGroup
    api_instance.disable_screening_group(authorization, x_tenant, x_version)
except ApiException as e:
    print("Exception when calling ScreeningGroupsApi->disable_screening_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
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

# **getscreening_group**
> ScreeningGroups getscreening_group(authorization, x_tenant, x_version, screening_group_id)

Return a specific screeningGroup instance.

Return a specific screeningGroup instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScreeningGroupsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
screening_group_id = 'screening_group_id_example' # str | The ID of the screeningGroups that will be retrieved.

try:
    # Return a specific screeningGroup instance.
    api_response = api_instance.getscreening_group(authorization, x_tenant, x_version, screening_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScreeningGroupsApi->getscreening_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **screening_group_id** | **str**| The ID of the screeningGroups that will be retrieved. | 

### Return type

[**ScreeningGroups**](ScreeningGroups.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getscreening_groups**
> InterviewScriptsList getscreening_groups(authorization, x_tenant, x_version, page=page, page_size=page_size, order_by=order_by, select_0=select_0, select_1=select_1, filter_by_name_like=filter_by_name_like, filter_by_created_at_from=filter_by_created_at_from, filter_by_created_at_to=filter_by_created_at_to, count_0_filter_by_name_like=count_0_filter_by_name_like, count_1_filter_by_created_at_from=count_1_filter_by_created_at_from, search_by=search_by)

List multiple screeningGroups resources.

This operation allows you to list and search for screeningGroups resources provided query arguments.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScreeningGroupsApi()
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
    # List multiple screeningGroups resources.
    api_response = api_instance.getscreening_groups(authorization, x_tenant, x_version, page=page, page_size=page_size, order_by=order_by, select_0=select_0, select_1=select_1, filter_by_name_like=filter_by_name_like, filter_by_created_at_from=filter_by_created_at_from, filter_by_created_at_to=filter_by_created_at_to, count_0_filter_by_name_like=count_0_filter_by_name_like, count_1_filter_by_created_at_from=count_1_filter_by_created_at_from, search_by=search_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScreeningGroupsApi->getscreening_groups: %s\n" % e)
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

# **order_screening_groups**
> order_screening_groups(authorization, x_tenant, x_version)

Order screeningGroups

Order screeningGroups

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScreeningGroupsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)

try:
    # Order screeningGroups
    api_instance.order_screening_groups(authorization, x_tenant, x_version)
except ApiException as e:
    print("Exception when calling ScreeningGroupsApi->order_screening_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
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

# **updatescreening_groups**
> ScreeningGroups updatescreening_groups(authorization, x_tenant, x_version, screening_group_id, body)

Update a specific screeningGroup instance.

Update a specific screeningGroup instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScreeningGroupsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
screening_group_id = 'screening_group_id_example' # str | The ID of the screeningGroups that will be updated.
body = swagger_client.ScreeningGroups() # ScreeningGroups | Data used to update screeningGroups

try:
    # Update a specific screeningGroup instance.
    api_response = api_instance.updatescreening_groups(authorization, x_tenant, x_version, screening_group_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScreeningGroupsApi->updatescreening_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **screening_group_id** | **str**| The ID of the screeningGroups that will be updated. | 
 **body** | [**ScreeningGroups**](ScreeningGroups.md)| Data used to update screeningGroups | 

### Return type

[**ScreeningGroups**](ScreeningGroups.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

