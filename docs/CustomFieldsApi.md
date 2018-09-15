# swagger_client.CustomFieldsApi

All URIs are relative to *https://api.kenoby.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createcustom_fields**](CustomFieldsApi.md#createcustom_fields) | **POST** /custom-fields | Create a new custom-fields
[**getcustom_fields**](CustomFieldsApi.md#getcustom_fields) | **GET** /custom-fields/{custom-fieldsId} | Return a specific custom-field instance.
[**getcustom_fields_auto_fill**](CustomFieldsApi.md#getcustom_fields_auto_fill) | **GET** /custom-fields/{custom-fieldsId}/auto-fill | Return a specific custom-field auto-fill instance.
[**getcustom_fieldss**](CustomFieldsApi.md#getcustom_fieldss) | **GET** /custom-fields | List multiple custom-fields resources.
[**postcustom_fields_auto_fill**](CustomFieldsApi.md#postcustom_fields_auto_fill) | **POST** /custom-fields/{custom-fieldsId}/auto-fill | Returns a search of custom-fields auto-fill instances.
[**updatecustom_fields**](CustomFieldsApi.md#updatecustom_fields) | **PUT** /custom-fields/{custom-fieldsId} | Update a specific custom-field instance.


# **createcustom_fields**
> createcustom_fields(authorization, x_tenant, x_version, body)

Create a new custom-fields

Create a new custom-fields

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CustomFieldsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
body = swagger_client.CustomFields() # CustomFields | Data used to create a new custom-fields

try:
    # Create a new custom-fields
    api_instance.createcustom_fields(authorization, x_tenant, x_version, body)
except ApiException as e:
    print("Exception when calling CustomFieldsApi->createcustom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **body** | [**CustomFields**](CustomFields.md)| Data used to create a new custom-fields | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getcustom_fields**
> CustomFields getcustom_fields(authorization, x_tenant, x_version, custom_fields_id)

Return a specific custom-field instance.

Return a specific custom-field instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CustomFieldsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
custom_fields_id = 'custom_fields_id_example' # str | The ID of the custom-fields that will be retrieved.

try:
    # Return a specific custom-field instance.
    api_response = api_instance.getcustom_fields(authorization, x_tenant, x_version, custom_fields_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomFieldsApi->getcustom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **custom_fields_id** | **str**| The ID of the custom-fields that will be retrieved. | 

### Return type

[**CustomFields**](CustomFields.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getcustom_fields_auto_fill**
> CustomFields getcustom_fields_auto_fill(authorization, x_tenant, x_version, custom_fields_id)

Return a specific custom-field auto-fill instance.

Return a specific custom-field auto-fill instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CustomFieldsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
custom_fields_id = 'custom_fields_id_example' # str | The ID of the custom-fields that will be retrieved.

try:
    # Return a specific custom-field auto-fill instance.
    api_response = api_instance.getcustom_fields_auto_fill(authorization, x_tenant, x_version, custom_fields_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomFieldsApi->getcustom_fields_auto_fill: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **custom_fields_id** | **str**| The ID of the custom-fields that will be retrieved. | 

### Return type

[**CustomFields**](CustomFields.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getcustom_fieldss**
> CustomFieldsList getcustom_fieldss(authorization, x_tenant, x_version, page=page, page_size=page_size, order_by=order_by, select_0=select_0, select_1=select_1, filter_by_code=filter_by_code, filter_by_name=filter_by_name, filter_by_created_at_from=filter_by_created_at_from, filter_by_created_at_to=filter_by_created_at_to, filter_by_or_0_name_like=filter_by_or_0_name_like, filter_by_or_1_code_like=filter_by_or_1_code_like, count_0_filter_by_name=count_0_filter_by_name, count_1_filter_by_created_at_from=count_1_filter_by_created_at_from)

List multiple custom-fields resources.

This operation allows you to list and search for custom-fields resources provided query arguments.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CustomFieldsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
page = 1 # int | The page of records. Used for pagination. (optional) (default to 1)
page_size = 20 # int | How many records to limit the output. (optional) (default to 20)
order_by = 'order' # str | Which fields to sort the records on. You can use minus sign to have a reverse order. Ex.: orderBy=order (optional) (default to order)
select_0 = '' # str | Select which fields will be returned by the query. (optional) (default to )
select_1 = '' # str | Select which fields will be returned by the query. One select for each field (optional) (default to )
filter_by_code = '' # str | Filter the results. This is just a sample. You can use a better tool like postman to try other filters. Ex: filterBy[fieldA]=some value&filterBy[fieldB][fieldDfromC]=other value (optional) (default to )
filter_by_name = '' # str | Filter the results. This is just a sample. You can use a better tool like postman to try other filters. Ex: filterBy[fieldA]=some value&filterBy[fieldB][fieldDfromC]=other value (optional) (default to )
filter_by_created_at_from = '2015-01-01T02:00:00.000Z' # str | Filter the results greatter than a given date (optional) (default to 2015-01-01T02:00:00.000Z)
filter_by_created_at_to = '2017-01-01T02:00:00.000Z' # str | Filter the results lower than a given date (optional) (default to 2017-01-01T02:00:00.000Z)
filter_by_or_0_name_like = '' # str | Filter the results associating more than one parameter. This is just a sample using 'or' sintax. (optional) (default to )
filter_by_or_1_code_like = '' # str | Filter the results associating more than one parameter. This is just a sample using 'or' sintax. (optional) (default to )
count_0_filter_by_name = '' # str | Return the total records from a filterBy query. Ex.: count[0][filterBy][name][like]=Ricardo (optional) (default to )
count_1_filter_by_created_at_from = '' # str | Return the total records from createdFrom a specific date. Ex.: count[1][filterBy][createdAt][from]=2015-01-01T02:00:00.000Z (optional) (default to )

try:
    # List multiple custom-fields resources.
    api_response = api_instance.getcustom_fieldss(authorization, x_tenant, x_version, page=page, page_size=page_size, order_by=order_by, select_0=select_0, select_1=select_1, filter_by_code=filter_by_code, filter_by_name=filter_by_name, filter_by_created_at_from=filter_by_created_at_from, filter_by_created_at_to=filter_by_created_at_to, filter_by_or_0_name_like=filter_by_or_0_name_like, filter_by_or_1_code_like=filter_by_or_1_code_like, count_0_filter_by_name=count_0_filter_by_name, count_1_filter_by_created_at_from=count_1_filter_by_created_at_from)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomFieldsApi->getcustom_fieldss: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **page** | **int**| The page of records. Used for pagination. | [optional] [default to 1]
 **page_size** | **int**| How many records to limit the output. | [optional] [default to 20]
 **order_by** | **str**| Which fields to sort the records on. You can use minus sign to have a reverse order. Ex.: orderBy&#x3D;order | [optional] [default to order]
 **select_0** | **str**| Select which fields will be returned by the query. | [optional] [default to ]
 **select_1** | **str**| Select which fields will be returned by the query. One select for each field | [optional] [default to ]
 **filter_by_code** | **str**| Filter the results. This is just a sample. You can use a better tool like postman to try other filters. Ex: filterBy[fieldA]&#x3D;some value&amp;filterBy[fieldB][fieldDfromC]&#x3D;other value | [optional] [default to ]
 **filter_by_name** | **str**| Filter the results. This is just a sample. You can use a better tool like postman to try other filters. Ex: filterBy[fieldA]&#x3D;some value&amp;filterBy[fieldB][fieldDfromC]&#x3D;other value | [optional] [default to ]
 **filter_by_created_at_from** | **str**| Filter the results greatter than a given date | [optional] [default to 2015-01-01T02:00:00.000Z]
 **filter_by_created_at_to** | **str**| Filter the results lower than a given date | [optional] [default to 2017-01-01T02:00:00.000Z]
 **filter_by_or_0_name_like** | **str**| Filter the results associating more than one parameter. This is just a sample using &#39;or&#39; sintax. | [optional] [default to ]
 **filter_by_or_1_code_like** | **str**| Filter the results associating more than one parameter. This is just a sample using &#39;or&#39; sintax. | [optional] [default to ]
 **count_0_filter_by_name** | **str**| Return the total records from a filterBy query. Ex.: count[0][filterBy][name][like]&#x3D;Ricardo | [optional] [default to ]
 **count_1_filter_by_created_at_from** | **str**| Return the total records from createdFrom a specific date. Ex.: count[1][filterBy][createdAt][from]&#x3D;2015-01-01T02:00:00.000Z | [optional] [default to ]

### Return type

[**CustomFieldsList**](CustomFieldsList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **postcustom_fields_auto_fill**
> CustomFields postcustom_fields_auto_fill(authorization, x_tenant, x_version, custom_fields_id)

Returns a search of custom-fields auto-fill instances.

Returns a search of custom-fields auto-fill instances.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CustomFieldsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
custom_fields_id = 'custom_fields_id_example' # str | The ID of the custom-fields that will be retrieved.

try:
    # Returns a search of custom-fields auto-fill instances.
    api_response = api_instance.postcustom_fields_auto_fill(authorization, x_tenant, x_version, custom_fields_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomFieldsApi->postcustom_fields_auto_fill: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **custom_fields_id** | **str**| The ID of the custom-fields that will be retrieved. | 

### Return type

[**CustomFields**](CustomFields.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updatecustom_fields**
> CustomFields updatecustom_fields(authorization, x_tenant, x_version, custom_fields_id, body)

Update a specific custom-field instance.

Update a specific custom-field instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CustomFieldsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
custom_fields_id = 'custom_fields_id_example' # str | The ID of the custom-fields that will be updated.
body = swagger_client.CustomFields() # CustomFields | Data used to update custom-fields

try:
    # Update a specific custom-field instance.
    api_response = api_instance.updatecustom_fields(authorization, x_tenant, x_version, custom_fields_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomFieldsApi->updatecustom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **custom_fields_id** | **str**| The ID of the custom-fields that will be updated. | 
 **body** | [**CustomFields**](CustomFields.md)| Data used to update custom-fields | 

### Return type

[**CustomFields**](CustomFields.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

