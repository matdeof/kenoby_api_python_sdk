# swagger_client.PublicationsApi

All URIs are relative to *https://api.kenoby.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createpublications**](PublicationsApi.md#createpublications) | **POST** /publications | Create a new publications
[**finishpublications**](PublicationsApi.md#finishpublications) | **PUT** /publications/{publicationsId}/finish | Finish a specific publication instance.
[**getpublications**](PublicationsApi.md#getpublications) | **GET** /publications/{publicationsId} | Return a specific publication instance.
[**getpublicationsapplicants**](PublicationsApi.md#getpublicationsapplicants) | **GET** /publications/{publicationsId}/applicants | Load all applicants in an integration.
[**getpublicationsapplications**](PublicationsApi.md#getpublicationsapplications) | **GET** /publications/{publicationsId}/applications | Return applications from a specific publication instance.
[**getpublicationscanpublish**](PublicationsApi.md#getpublicationscanpublish) | **GET** /publications/{publicationsId}/status | Return if a tenant can publish a specific integration.
[**getpublicationss**](PublicationsApi.md#getpublicationss) | **GET** /publications | List multiple publications resources.
[**updatepublications**](PublicationsApi.md#updatepublications) | **PUT** /publications/{publicationsId} | Update a specific publication instance.


# **createpublications**
> createpublications(authorization, x_tenant, x_version, body)

Create a new publications

Create a new publications

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PublicationsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
body = swagger_client.Publications() # Publications | Data used to create a new publications

try:
    # Create a new publications
    api_instance.createpublications(authorization, x_tenant, x_version, body)
except ApiException as e:
    print("Exception when calling PublicationsApi->createpublications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **body** | [**Publications**](Publications.md)| Data used to create a new publications | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **finishpublications**
> Publications finishpublications(authorization, x_tenant, x_version, publications_id)

Finish a specific publication instance.

Finish a specific publication instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PublicationsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
publications_id = 'publications_id_example' # str | The ID of the publications that will be updated.

try:
    # Finish a specific publication instance.
    api_response = api_instance.finishpublications(authorization, x_tenant, x_version, publications_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicationsApi->finishpublications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **publications_id** | **str**| The ID of the publications that will be updated. | 

### Return type

[**Publications**](Publications.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getpublications**
> Publications getpublications(authorization, x_tenant, x_version, publications_id)

Return a specific publication instance.

Return a specific publication instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PublicationsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
publications_id = 'publications_id_example' # str | The ID of the publications that will be retrieved.

try:
    # Return a specific publication instance.
    api_response = api_instance.getpublications(authorization, x_tenant, x_version, publications_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicationsApi->getpublications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **publications_id** | **str**| The ID of the publications that will be retrieved. | 

### Return type

[**Publications**](Publications.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getpublicationsapplicants**
> getpublicationsapplicants(authorization, x_tenant, x_version, publication)

Load all applicants in an integration.

Load all applicants in an integration..

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PublicationsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
publication = 'publication_example' # str | The ID of the publication that will be processed.

try:
    # Load all applicants in an integration.
    api_instance.getpublicationsapplicants(authorization, x_tenant, x_version, publication)
except ApiException as e:
    print("Exception when calling PublicationsApi->getpublicationsapplicants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **publication** | **str**| The ID of the publication that will be processed. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getpublicationsapplications**
> Publications getpublicationsapplications(authorization, x_tenant, x_version, publications_id)

Return applications from a specific publication instance.

Return applications from a specific publication instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PublicationsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
publications_id = 'publications_id_example' # str | The ID of the publications that will be retrieved.

try:
    # Return applications from a specific publication instance.
    api_response = api_instance.getpublicationsapplications(authorization, x_tenant, x_version, publications_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicationsApi->getpublicationsapplications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **publications_id** | **str**| The ID of the publications that will be retrieved. | 

### Return type

[**Publications**](Publications.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getpublicationscanpublish**
> Publications getpublicationscanpublish(authorization, x_tenant, x_version, integration_id, integration, fields)

Return if a tenant can publish a specific integration.

Return if a tenant can publish a specific integration.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PublicationsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
integration_id = 'integration_id_example' # str | The ID of the integration inside tenant.integrations.
integration = 'integration_example' # str | The name of the integration inside tenant.integrations.integrations object.
fields = ['fields_example'] # list[str] | Fields to be checked if exists.

try:
    # Return if a tenant can publish a specific integration.
    api_response = api_instance.getpublicationscanpublish(authorization, x_tenant, x_version, integration_id, integration, fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicationsApi->getpublicationscanpublish: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **integration_id** | **str**| The ID of the integration inside tenant.integrations. | 
 **integration** | **str**| The name of the integration inside tenant.integrations.integrations object. | 
 **fields** | [**list[str]**](str.md)| Fields to be checked if exists. | 

### Return type

[**Publications**](Publications.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getpublicationss**
> PublicationsList getpublicationss(authorization, x_tenant, x_version, page=page, page_size=page_size, order_by=order_by, select_0=select_0, select_1=select_1, filter_by_position=filter_by_position, filter_by_status=filter_by_status, filter_by_integration=filter_by_integration, filter_by_response=filter_by_response, filter_by_created_at_from=filter_by_created_at_from, filter_by_created_at_to=filter_by_created_at_to, count_0_filter_by_status=count_0_filter_by_status, count_1_filter_by_created_at_from=count_1_filter_by_created_at_from, search_by=search_by)

List multiple publications resources.

This operation allows you to list and search for publications resources provided query arguments.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PublicationsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
page = 1 # int | The page of records. Used for pagination. (optional) (default to 1)
page_size = 20 # int | How many records to limit the output. (optional) (default to 20)
order_by = 'name' # str | Which fields to sort the records on. You can use minus sign to have a reverse order. Ex.: orderBy=-name (optional) (default to name)
select_0 = '' # str | Select which fields will be returned by the query. (optional) (default to )
select_1 = '' # str | Select which fields will be returned by the query. One select for each field (optional) (default to )
filter_by_position = '' # str | Filter the results. This is just a sample. You can use a better tool like postman to try other filters. Ex: filterBy[fieldA]=some value&filterBy[fieldB][fieldDfromC]=other value (optional) (default to )
filter_by_status = '' # str | Filter the results. This is just a sample. You can use a better tool like postman to try other filters. Ex: filterBy[fieldA]=some value&filterBy[fieldB][fieldDfromC]=other value (optional) (default to )
filter_by_integration = '' # str | Filter the results. This is just a sample. You can use a better tool like postman to try other filters. Ex: filterBy[fieldA]=some value&filterBy[fieldB][fieldDfromC]=other value (optional) (default to )
filter_by_response = '' # str | Filter the results. This is just a sample. You can use a better tool like postman to try other filters. Ex: filterBy[fieldA]=some value&filterBy[fieldB][fieldDfromC]=other value (optional) (default to )
filter_by_created_at_from = '2015-01-01T02:00:00.000Z' # str | Filter the results greatter than a given date (optional) (default to 2015-01-01T02:00:00.000Z)
filter_by_created_at_to = '2017-01-01T02:00:00.000Z' # str | Filter the results lower than a given date (optional) (default to 2017-01-01T02:00:00.000Z)
count_0_filter_by_status = '' # str | Return the total records from a filterBy query. Ex.: count[0][filterBy][name][like]=Ricardo (optional) (default to )
count_1_filter_by_created_at_from = '' # str | Return the total records from createdFrom a specific date. Ex.: count[1][filterBy][createdAt][from]=2015-01-01T02:00:00.000Z (optional) (default to )
search_by = '' # str | Make a text search on main fields. Name and e-mail have higher scores. (optional) (default to )

try:
    # List multiple publications resources.
    api_response = api_instance.getpublicationss(authorization, x_tenant, x_version, page=page, page_size=page_size, order_by=order_by, select_0=select_0, select_1=select_1, filter_by_position=filter_by_position, filter_by_status=filter_by_status, filter_by_integration=filter_by_integration, filter_by_response=filter_by_response, filter_by_created_at_from=filter_by_created_at_from, filter_by_created_at_to=filter_by_created_at_to, count_0_filter_by_status=count_0_filter_by_status, count_1_filter_by_created_at_from=count_1_filter_by_created_at_from, search_by=search_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicationsApi->getpublicationss: %s\n" % e)
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
 **filter_by_position** | **str**| Filter the results. This is just a sample. You can use a better tool like postman to try other filters. Ex: filterBy[fieldA]&#x3D;some value&amp;filterBy[fieldB][fieldDfromC]&#x3D;other value | [optional] [default to ]
 **filter_by_status** | **str**| Filter the results. This is just a sample. You can use a better tool like postman to try other filters. Ex: filterBy[fieldA]&#x3D;some value&amp;filterBy[fieldB][fieldDfromC]&#x3D;other value | [optional] [default to ]
 **filter_by_integration** | **str**| Filter the results. This is just a sample. You can use a better tool like postman to try other filters. Ex: filterBy[fieldA]&#x3D;some value&amp;filterBy[fieldB][fieldDfromC]&#x3D;other value | [optional] [default to ]
 **filter_by_response** | **str**| Filter the results. This is just a sample. You can use a better tool like postman to try other filters. Ex: filterBy[fieldA]&#x3D;some value&amp;filterBy[fieldB][fieldDfromC]&#x3D;other value | [optional] [default to ]
 **filter_by_created_at_from** | **str**| Filter the results greatter than a given date | [optional] [default to 2015-01-01T02:00:00.000Z]
 **filter_by_created_at_to** | **str**| Filter the results lower than a given date | [optional] [default to 2017-01-01T02:00:00.000Z]
 **count_0_filter_by_status** | **str**| Return the total records from a filterBy query. Ex.: count[0][filterBy][name][like]&#x3D;Ricardo | [optional] [default to ]
 **count_1_filter_by_created_at_from** | **str**| Return the total records from createdFrom a specific date. Ex.: count[1][filterBy][createdAt][from]&#x3D;2015-01-01T02:00:00.000Z | [optional] [default to ]
 **search_by** | **str**| Make a text search on main fields. Name and e-mail have higher scores. | [optional] [default to ]

### Return type

[**PublicationsList**](PublicationsList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updatepublications**
> Publications updatepublications(authorization, x_tenant, x_version, publications_id, body)

Update a specific publication instance.

Update a specific publication instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PublicationsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
publications_id = 'publications_id_example' # str | The ID of the publications that will be updated.
body = swagger_client.Publications() # Publications | Data used to update publications

try:
    # Update a specific publication instance.
    api_response = api_instance.updatepublications(authorization, x_tenant, x_version, publications_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicationsApi->updatepublications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **publications_id** | **str**| The ID of the publications that will be updated. | 
 **body** | [**Publications**](Publications.md)| Data used to update publications | 

### Return type

[**Publications**](Publications.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

