# swagger_client.JobsitesApi

All URIs are relative to *https://api.kenoby.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_by_type**](JobsitesApi.md#count_by_type) | **GET** /jobsites/count/byType | Return the amount of jobsite internal / external of the tenant
[**create_jobsites**](JobsitesApi.md#create_jobsites) | **POST** /jobsites | Create a new jobsites
[**deletejobsites**](JobsitesApi.md#deletejobsites) | **DELETE** /jobsites/{jobsitesId} | Delete a specific jobsite instance.
[**duplicatejobsite**](JobsitesApi.md#duplicatejobsite) | **POST** /jobsites/{jobsitesId}/duplicate | Duplicate a specific jobsite instance.
[**getjobsite**](JobsitesApi.md#getjobsite) | **GET** /jobsites/slug/{jobsiteSlug} | Return a specific jobsite instance.
[**getjobsites**](JobsitesApi.md#getjobsites) | **GET** /jobsites/{jobsitesId} | Return a specific jobsite instance.
[**getjobsitess**](JobsitesApi.md#getjobsitess) | **GET** /jobsites | List multiple jobsites resources.
[**updatejobsites**](JobsitesApi.md#updatejobsites) | **PUT** /jobsites/{jobsitesId} | Update a specific jobsite instance.


# **count_by_type**
> Jobsites count_by_type(authorization, x_tenant)

Return the amount of jobsite internal / external of the tenant

Return the amount of jobsite internal / external of the tenant

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.JobsitesApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = 'x_tenant_example' # str | The tenant id.

try:
    # Return the amount of jobsite internal / external of the tenant
    api_response = api_instance.count_by_type(authorization, x_tenant)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsitesApi->count_by_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | 

### Return type

[**Jobsites**](Jobsites.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_jobsites**
> create_jobsites(authorization, x_tenant, x_version, body)

Create a new jobsites

Create a new jobsites

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.JobsitesApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
body = swagger_client.Jobsites() # Jobsites | Data used to create a new jobsites

try:
    # Create a new jobsites
    api_instance.create_jobsites(authorization, x_tenant, x_version, body)
except ApiException as e:
    print("Exception when calling JobsitesApi->create_jobsites: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **body** | [**Jobsites**](Jobsites.md)| Data used to create a new jobsites | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deletejobsites**
> Jobsites deletejobsites(authorization, x_tenant, x_version, jobsites_id, body)

Delete a specific jobsite instance.

Delete a specific jobsite instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.JobsitesApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
jobsites_id = 'jobsites_id_example' # str | The ID of the jobsites that will be deleted.
body = swagger_client.Jobsites() # Jobsites | Data used to delete jobsites

try:
    # Delete a specific jobsite instance.
    api_response = api_instance.deletejobsites(authorization, x_tenant, x_version, jobsites_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsitesApi->deletejobsites: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **jobsites_id** | **str**| The ID of the jobsites that will be deleted. | 
 **body** | [**Jobsites**](Jobsites.md)| Data used to delete jobsites | 

### Return type

[**Jobsites**](Jobsites.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **duplicatejobsite**
> Jobsites duplicatejobsite(authorization, x_tenant, jobsites_id)

Duplicate a specific jobsite instance.

Duplicate a specific jobsite instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.JobsitesApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = 'x_tenant_example' # str | The tenant id.
jobsites_id = 'jobsites_id_example' # str | The ID of the jobsites that will be deleted.

try:
    # Duplicate a specific jobsite instance.
    api_response = api_instance.duplicatejobsite(authorization, x_tenant, jobsites_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsitesApi->duplicatejobsite: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | 
 **jobsites_id** | **str**| The ID of the jobsites that will be deleted. | 

### Return type

[**Jobsites**](Jobsites.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getjobsite**
> Jobsites getjobsite(authorization, jobsite_slug)

Return a specific jobsite instance.

Return a specific jobsite instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.JobsitesApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
jobsite_slug = 'jobsite_slug_example' # str | The slug of the jobsites that will be retrieved.

try:
    # Return a specific jobsite instance.
    api_response = api_instance.getjobsite(authorization, jobsite_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsitesApi->getjobsite: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **jobsite_slug** | **str**| The slug of the jobsites that will be retrieved. | 

### Return type

[**Jobsites**](Jobsites.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getjobsites**
> Jobsites getjobsites(authorization, x_tenant, x_version, jobsites_id)

Return a specific jobsite instance.

Return a specific jobsite instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.JobsitesApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
jobsites_id = 'jobsites_id_example' # str | The ID of the jobsites that will be retrieved.

try:
    # Return a specific jobsite instance.
    api_response = api_instance.getjobsites(authorization, x_tenant, x_version, jobsites_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsitesApi->getjobsites: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **jobsites_id** | **str**| The ID of the jobsites that will be retrieved. | 

### Return type

[**Jobsites**](Jobsites.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getjobsitess**
> JobsitesList getjobsitess(authorization, x_tenant, x_version, page=page, page_size=page_size, order_by=order_by, select_0=select_0, select_1=select_1, filter_by_name_like=filter_by_name_like, filter_by_created_at_from=filter_by_created_at_from, filter_by_created_at_to=filter_by_created_at_to, count_0_filter_by_name_like=count_0_filter_by_name_like, count_1_filter_by_created_at_from=count_1_filter_by_created_at_from, search_by=search_by)

List multiple jobsites resources.

This operation allows you to list and search for jobsites resources provided query arguments.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.JobsitesApi()
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
    # List multiple jobsites resources.
    api_response = api_instance.getjobsitess(authorization, x_tenant, x_version, page=page, page_size=page_size, order_by=order_by, select_0=select_0, select_1=select_1, filter_by_name_like=filter_by_name_like, filter_by_created_at_from=filter_by_created_at_from, filter_by_created_at_to=filter_by_created_at_to, count_0_filter_by_name_like=count_0_filter_by_name_like, count_1_filter_by_created_at_from=count_1_filter_by_created_at_from, search_by=search_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsitesApi->getjobsitess: %s\n" % e)
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

[**JobsitesList**](JobsitesList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updatejobsites**
> Jobsites updatejobsites(authorization, x_tenant, x_version, jobsites_id, body)

Update a specific jobsite instance.

Update a specific jobsite instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.JobsitesApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
jobsites_id = 'jobsites_id_example' # str | The ID of the jobsites that will be updated.
body = swagger_client.Jobsites() # Jobsites | Data used to update jobsites

try:
    # Update a specific jobsite instance.
    api_response = api_instance.updatejobsites(authorization, x_tenant, x_version, jobsites_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsitesApi->updatejobsites: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **jobsites_id** | **str**| The ID of the jobsites that will be updated. | 
 **body** | [**Jobsites**](Jobsites.md)| Data used to update jobsites | 

### Return type

[**Jobsites**](Jobsites.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

