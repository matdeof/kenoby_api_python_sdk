# swagger_client.AdvancedFiltersApi

All URIs are relative to *https://api.kenoby.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createadvancedfilters**](AdvancedFiltersApi.md#createadvancedfilters) | **PUT** /advanced-filters | Create a specific advanced-filter instance.
[**deleteadvancedfilters**](AdvancedFiltersApi.md#deleteadvancedfilters) | **DELETE** /advanced-filters/{advancedFilterId} | Delete a specific advanced-filter instance.
[**getadvancedfilter**](AdvancedFiltersApi.md#getadvancedfilter) | **GET** /advanced-filters | List multiple advanced-filters resources.
[**getadvancedfilters**](AdvancedFiltersApi.md#getadvancedfilters) | **GET** /advanced-filters/{advancedFilterId} | Return a specific advanced-filter instance.
[**updateadvancedfilters**](AdvancedFiltersApi.md#updateadvancedfilters) | **PUT** /advanced-filters/{advancedFilterId} | Update a specific advanced-filter instance.


# **createadvancedfilters**
> AdvancedFilters createadvancedfilters(authorization, x_tenant, x_version, body)

Create a specific advanced-filter instance.

Create a specific advanced-filter instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdvancedFiltersApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
body = swagger_client.AdvancedFilters() # AdvancedFilters | Data used to create a new advanced-filter

try:
    # Create a specific advanced-filter instance.
    api_response = api_instance.createadvancedfilters(authorization, x_tenant, x_version, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdvancedFiltersApi->createadvancedfilters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **body** | [**AdvancedFilters**](AdvancedFilters.md)| Data used to create a new advanced-filter | 

### Return type

[**AdvancedFilters**](AdvancedFilters.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deleteadvancedfilters**
> AdvancedFilters deleteadvancedfilters(authorization, x_tenant, x_version, advanced_filter_id)

Delete a specific advanced-filter instance.

Delete a specific advanced-filter instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdvancedFiltersApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
advanced_filter_id = 'advanced_filter_id_example' # str | The ID of the advanced-filter that will be deleted.

try:
    # Delete a specific advanced-filter instance.
    api_response = api_instance.deleteadvancedfilters(authorization, x_tenant, x_version, advanced_filter_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdvancedFiltersApi->deleteadvancedfilters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **advanced_filter_id** | **str**| The ID of the advanced-filter that will be deleted. | 

### Return type

[**AdvancedFilters**](AdvancedFilters.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getadvancedfilter**
> AdvancedFiltersList getadvancedfilter(authorization, x_tenant, x_version, page=page, page_size=page_size, order_by=order_by, select_0=select_0, select_1=select_1, filter_by_name_like=filter_by_name_like, filter_by_user=filter_by_user, filter_by_created_at_from=filter_by_created_at_from, filter_by_created_at_to=filter_by_created_at_to, count_0_filter_by_message_like=count_0_filter_by_message_like, count_1_filter_by_created_at_from=count_1_filter_by_created_at_from, search_by=search_by)

List multiple advanced-filters resources.

This operation allows you to list and search for advanced-filters resources provided query arguments.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdvancedFiltersApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
page = 1 # int | The page of records. Used for pagination. (optional) (default to 1)
page_size = 20 # int | How many records to limit the output. (optional) (default to 20)
order_by = 'name' # str | Which fields to sort the records on. You can use minus sign to have a reverse order. Ex.: orderBy=-name (optional) (default to name)
select_0 = '' # str | Select which fields will be returned by the query. (optional) (default to )
select_1 = '' # str | Select which fields will be returned by the query. One select for each field (optional) (default to )
filter_by_name_like = '' # str | Filter the results. This is just a sample. You can use a better tool like postman to try other filters. Ex: filterBy[fieldA]=some value&filterBy[fieldB][fieldDfromC]=other value (optional) (default to )
filter_by_user = '' # str | Filter the results. This is just a sample. You can use a better tool like postman to try other filters. Ex: filterBy[fieldA]=some value&filterBy[fieldB][fieldDfromC]=other value (optional) (default to )
filter_by_created_at_from = '2015-01-01T02:00:00.000Z' # str | Filter the results greatter than a given date (optional) (default to 2015-01-01T02:00:00.000Z)
filter_by_created_at_to = '2017-01-01T02:00:00.000Z' # str | Filter the results lower than a given date (optional) (default to 2017-01-01T02:00:00.000Z)
count_0_filter_by_message_like = '' # str | Return the total records from a filterBy query. Ex.: count[0][filterBy][name][like]=Ricardo (optional) (default to )
count_1_filter_by_created_at_from = '' # str | Return the total records from createdFrom a specific date. Ex.: count[1][filterBy][createdAt][from]=2015-01-01T02:00:00.000Z (optional) (default to )
search_by = '' # str | Make a text search on main fields. Name and e-mail have higher scores. (optional) (default to )

try:
    # List multiple advanced-filters resources.
    api_response = api_instance.getadvancedfilter(authorization, x_tenant, x_version, page=page, page_size=page_size, order_by=order_by, select_0=select_0, select_1=select_1, filter_by_name_like=filter_by_name_like, filter_by_user=filter_by_user, filter_by_created_at_from=filter_by_created_at_from, filter_by_created_at_to=filter_by_created_at_to, count_0_filter_by_message_like=count_0_filter_by_message_like, count_1_filter_by_created_at_from=count_1_filter_by_created_at_from, search_by=search_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdvancedFiltersApi->getadvancedfilter: %s\n" % e)
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
 **filter_by_user** | **str**| Filter the results. This is just a sample. You can use a better tool like postman to try other filters. Ex: filterBy[fieldA]&#x3D;some value&amp;filterBy[fieldB][fieldDfromC]&#x3D;other value | [optional] [default to ]
 **filter_by_created_at_from** | **str**| Filter the results greatter than a given date | [optional] [default to 2015-01-01T02:00:00.000Z]
 **filter_by_created_at_to** | **str**| Filter the results lower than a given date | [optional] [default to 2017-01-01T02:00:00.000Z]
 **count_0_filter_by_message_like** | **str**| Return the total records from a filterBy query. Ex.: count[0][filterBy][name][like]&#x3D;Ricardo | [optional] [default to ]
 **count_1_filter_by_created_at_from** | **str**| Return the total records from createdFrom a specific date. Ex.: count[1][filterBy][createdAt][from]&#x3D;2015-01-01T02:00:00.000Z | [optional] [default to ]
 **search_by** | **str**| Make a text search on main fields. Name and e-mail have higher scores. | [optional] [default to ]

### Return type

[**AdvancedFiltersList**](AdvancedFiltersList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getadvancedfilters**
> AdvancedFilters getadvancedfilters(authorization, x_tenant, x_version, advanced_filter_id)

Return a specific advanced-filter instance.

Return a specific advanced-filter instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdvancedFiltersApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
advanced_filter_id = 'advanced_filter_id_example' # str | The ID of the advanced-filter that will be retrieved.

try:
    # Return a specific advanced-filter instance.
    api_response = api_instance.getadvancedfilters(authorization, x_tenant, x_version, advanced_filter_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdvancedFiltersApi->getadvancedfilters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **advanced_filter_id** | **str**| The ID of the advanced-filter that will be retrieved. | 

### Return type

[**AdvancedFilters**](AdvancedFilters.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updateadvancedfilters**
> AdvancedFilters updateadvancedfilters(authorization, x_tenant, x_version, body, advanced_filter_id)

Update a specific advanced-filter instance.

Update a specific advanced-filter instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdvancedFiltersApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
body = swagger_client.AdvancedFilters() # AdvancedFilters | Data used to update the advanced-filter
advanced_filter_id = 'advanced_filter_id_example' # str | The ID of the advanced-filter that will be retrieved.

try:
    # Update a specific advanced-filter instance.
    api_response = api_instance.updateadvancedfilters(authorization, x_tenant, x_version, body, advanced_filter_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdvancedFiltersApi->updateadvancedfilters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **body** | [**AdvancedFilters**](AdvancedFilters.md)| Data used to update the advanced-filter | 
 **advanced_filter_id** | **str**| The ID of the advanced-filter that will be retrieved. | 

### Return type

[**AdvancedFilters**](AdvancedFilters.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

