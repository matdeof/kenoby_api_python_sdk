# swagger_client.TenantsApi

All URIs are relative to *https://api.kenoby.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**allowedremovestage**](TenantsApi.md#allowedremovestage) | **POST** /tenants/{tenantsId}/allowed-remove-stage | Verify remove tenant&#39;s defaultStage.
[**beta_features**](TenantsApi.md#beta_features) | **GET** /tenants/beta-features | Returns beta features active in tenant.
[**createtenants**](TenantsApi.md#createtenants) | **POST** /tenants | Create a new tenants
[**getjobsitestenant**](TenantsApi.md#getjobsitestenant) | **GET** /tenants/{tenantId}/jobsites | Returns the jobsites for a specific tenant
[**gettenants**](TenantsApi.md#gettenants) | **GET** /tenants/{tenantsId} | Return a specific tenant instance.
[**gettenantss**](TenantsApi.md#gettenantss) | **GET** /tenants | List multiple tenants resources.
[**ping_request**](TenantsApi.md#ping_request) | **GET** /tenants/{tenantsId}/ping | Ping request to update user session.
[**updatetenants**](TenantsApi.md#updatetenants) | **PUT** /tenants/{tenantsId} | Update a specific tenant instance.
[**updatetenantsjobsite**](TenantsApi.md#updatetenantsjobsite) | **PUT** /tenants/{tenantsId}/jobsite | Update a specific tenant&#39;s jobsite.


# **allowedremovestage**
> Tenants allowedremovestage(authorization, x_tenant, x_version, tenants_id, body)

Verify remove tenant's defaultStage.

Verify remove tenant's defaultStage.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TenantsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
tenants_id = 'tenants_id_example' # str | The ID of the tenants that will be updated.
body = swagger_client.Tenants() # Tenants | Data used to update tenants

try:
    # Verify remove tenant's defaultStage.
    api_response = api_instance.allowedremovestage(authorization, x_tenant, x_version, tenants_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantsApi->allowedremovestage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **tenants_id** | **str**| The ID of the tenants that will be updated. | 
 **body** | [**Tenants**](Tenants.md)| Data used to update tenants | 

### Return type

[**Tenants**](Tenants.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **beta_features**
> beta_features(x_tenant, tenants_id)

Returns beta features active in tenant.

Returns beta features active in tenant.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TenantsApi()
x_tenant = '' # str | The tenant id. (default to )
tenants_id = 'tenants_id_example' # str | The ID of the user tenant.

try:
    # Returns beta features active in tenant.
    api_instance.beta_features(x_tenant, tenants_id)
except ApiException as e:
    print("Exception when calling TenantsApi->beta_features: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**| The tenant id. | [default to ]
 **tenants_id** | **str**| The ID of the user tenant. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **createtenants**
> createtenants(authorization, x_tenant, x_version, body)

Create a new tenants

Create a new tenants

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TenantsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
body = swagger_client.Tenants() # Tenants | Data used to create a new tenants

try:
    # Create a new tenants
    api_instance.createtenants(authorization, x_tenant, x_version, body)
except ApiException as e:
    print("Exception when calling TenantsApi->createtenants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **body** | [**Tenants**](Tenants.md)| Data used to create a new tenants | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getjobsitestenant**
> getjobsitestenant(tenant_id)

Returns the jobsites for a specific tenant

Returns the jobsites for a specific tenant

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TenantsApi()
tenant_id = 'tenant_id_example' # str | The ID of the tenant that will search.

try:
    # Returns the jobsites for a specific tenant
    api_instance.getjobsitestenant(tenant_id)
except ApiException as e:
    print("Exception when calling TenantsApi->getjobsitestenant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The ID of the tenant that will search. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gettenants**
> Tenants gettenants(authorization, x_tenant, x_version, tenants_id)

Return a specific tenant instance.

Return a specific tenant instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TenantsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
tenants_id = 'tenants_id_example' # str | The ID of the tenants that will be retrieved.

try:
    # Return a specific tenant instance.
    api_response = api_instance.gettenants(authorization, x_tenant, x_version, tenants_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantsApi->gettenants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **tenants_id** | **str**| The ID of the tenants that will be retrieved. | 

### Return type

[**Tenants**](Tenants.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gettenantss**
> TenantsList gettenantss(authorization, x_tenant, x_version, page=page, page_size=page_size, order_by=order_by, select_0=select_0, select_1=select_1, filter_by_name_like=filter_by_name_like, filter_by_slug=filter_by_slug, filter_by_created_at_from=filter_by_created_at_from, filter_by_created_at_to=filter_by_created_at_to, filter_by_or_0_name_like=filter_by_or_0_name_like, filter_by_or_1_slug_like=filter_by_or_1_slug_like, count_0_filter_by_name_like=count_0_filter_by_name_like, count_1_filter_by_created_at_from=count_1_filter_by_created_at_from)

List multiple tenants resources.

This operation allows you to list and search for tenants resources provided query arguments.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TenantsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
page = 1 # int | The page of records. Used for pagination. (optional) (default to 1)
page_size = 20 # int | How many records to limit the output. (optional) (default to 20)
order_by = 'name' # str | Which fields to sort the records on. You can use minus sign to have a reverse order. Ex.: orderBy=-name (optional) (default to name)
select_0 = '' # str | Select which fields will be returned by the query. (optional) (default to )
select_1 = '' # str | Select which fields will be returned by the query. One select for each field (optional) (default to )
filter_by_name_like = '' # str | Filter the results. This is just a sample. You can use a better tool like postman to try other filters. Ex: filterBy[fieldA]=some value&filterBy[fieldB][fieldDfromC]=other value (optional) (default to )
filter_by_slug = '' # str | Filter the results. This is just a sample. You can use a better tool like postman to try other filters. Ex: filterBy[fieldA]=some value&filterBy[fieldB][fieldDfromC]=other value (optional) (default to )
filter_by_created_at_from = '2015-01-01T02:00:00.000Z' # str | Filter the results greatter than a given date (optional) (default to 2015-01-01T02:00:00.000Z)
filter_by_created_at_to = '2017-01-01T02:00:00.000Z' # str | Filter the results lower than a given date (optional) (default to 2017-01-01T02:00:00.000Z)
filter_by_or_0_name_like = '' # str | Filter the results associating more than one parameter. This is just a sample using 'or' sintax. (optional) (default to )
filter_by_or_1_slug_like = '' # str | Filter the results associating more than one parameter. This is just a sample using 'or' sintax. (optional) (default to )
count_0_filter_by_name_like = '' # str | Return the total records from a filterBy query. Ex.: count[0][filterBy][name][like]=Ricardo (optional) (default to )
count_1_filter_by_created_at_from = '' # str | Return the total records from createdFrom a specific date. Ex.: count[1][filterBy][createdAt][from]=2015-01-01T02:00:00.000Z (optional) (default to )

try:
    # List multiple tenants resources.
    api_response = api_instance.gettenantss(authorization, x_tenant, x_version, page=page, page_size=page_size, order_by=order_by, select_0=select_0, select_1=select_1, filter_by_name_like=filter_by_name_like, filter_by_slug=filter_by_slug, filter_by_created_at_from=filter_by_created_at_from, filter_by_created_at_to=filter_by_created_at_to, filter_by_or_0_name_like=filter_by_or_0_name_like, filter_by_or_1_slug_like=filter_by_or_1_slug_like, count_0_filter_by_name_like=count_0_filter_by_name_like, count_1_filter_by_created_at_from=count_1_filter_by_created_at_from)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantsApi->gettenantss: %s\n" % e)
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
 **filter_by_slug** | **str**| Filter the results. This is just a sample. You can use a better tool like postman to try other filters. Ex: filterBy[fieldA]&#x3D;some value&amp;filterBy[fieldB][fieldDfromC]&#x3D;other value | [optional] [default to ]
 **filter_by_created_at_from** | **str**| Filter the results greatter than a given date | [optional] [default to 2015-01-01T02:00:00.000Z]
 **filter_by_created_at_to** | **str**| Filter the results lower than a given date | [optional] [default to 2017-01-01T02:00:00.000Z]
 **filter_by_or_0_name_like** | **str**| Filter the results associating more than one parameter. This is just a sample using &#39;or&#39; sintax. | [optional] [default to ]
 **filter_by_or_1_slug_like** | **str**| Filter the results associating more than one parameter. This is just a sample using &#39;or&#39; sintax. | [optional] [default to ]
 **count_0_filter_by_name_like** | **str**| Return the total records from a filterBy query. Ex.: count[0][filterBy][name][like]&#x3D;Ricardo | [optional] [default to ]
 **count_1_filter_by_created_at_from** | **str**| Return the total records from createdFrom a specific date. Ex.: count[1][filterBy][createdAt][from]&#x3D;2015-01-01T02:00:00.000Z | [optional] [default to ]

### Return type

[**TenantsList**](TenantsList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ping_request**
> ping_request(authorization, x_tenant, x_version, tenants_id)

Ping request to update user session.

Ping request to update user session.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TenantsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
tenants_id = 'tenants_id_example' # str | The ID of the user tenant.

try:
    # Ping request to update user session.
    api_instance.ping_request(authorization, x_tenant, x_version, tenants_id)
except ApiException as e:
    print("Exception when calling TenantsApi->ping_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **tenants_id** | **str**| The ID of the user tenant. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updatetenants**
> Tenants updatetenants(authorization, x_tenant, x_version, tenants_id, body)

Update a specific tenant instance.

Update a specific tenant instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TenantsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
tenants_id = 'tenants_id_example' # str | The ID of the tenants that will be updated.
body = swagger_client.Tenants() # Tenants | Data used to update tenants

try:
    # Update a specific tenant instance.
    api_response = api_instance.updatetenants(authorization, x_tenant, x_version, tenants_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantsApi->updatetenants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **tenants_id** | **str**| The ID of the tenants that will be updated. | 
 **body** | [**Tenants**](Tenants.md)| Data used to update tenants | 

### Return type

[**Tenants**](Tenants.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updatetenantsjobsite**
> Tenants updatetenantsjobsite(authorization, x_tenant, x_version, tenants_id, body)

Update a specific tenant's jobsite.

Update a specific tenant's jobsite.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TenantsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
tenants_id = 'tenants_id_example' # str | The ID of the tenants that will be updated.
body = swagger_client.Tenants() # Tenants | Data used to update tenants

try:
    # Update a specific tenant's jobsite.
    api_response = api_instance.updatetenantsjobsite(authorization, x_tenant, x_version, tenants_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantsApi->updatetenantsjobsite: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **tenants_id** | **str**| The ID of the tenants that will be updated. | 
 **body** | [**Tenants**](Tenants.md)| Data used to update tenants | 

### Return type

[**Tenants**](Tenants.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

