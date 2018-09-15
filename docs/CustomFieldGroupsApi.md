# swagger_client.CustomFieldGroupsApi

All URIs are relative to *https://api.kenoby.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createcustom_field_groups**](CustomFieldGroupsApi.md#createcustom_field_groups) | **POST** /custom-field-groups | Create a new custom-field-groups
[**getcustom_field_groups**](CustomFieldGroupsApi.md#getcustom_field_groups) | **GET** /custom-field-groups/{custom-field-groupsId} | Return a specific custom-field-group instance.
[**getcustom_field_groupss**](CustomFieldGroupsApi.md#getcustom_field_groupss) | **GET** /custom-field-groups | List multiple custom-field-groups resources.
[**updatecustom_field_groups**](CustomFieldGroupsApi.md#updatecustom_field_groups) | **PUT** /custom-field-groups/{custom-field-groupsId} | Update a specific custom-field-group instance.


# **createcustom_field_groups**
> createcustom_field_groups(authorization, x_tenant, x_version, body)

Create a new custom-field-groups

Create a new custom-field-groups

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CustomFieldGroupsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
body = swagger_client.CustomFieldGroups() # CustomFieldGroups | Data used to create a new custom-field-groups

try:
    # Create a new custom-field-groups
    api_instance.createcustom_field_groups(authorization, x_tenant, x_version, body)
except ApiException as e:
    print("Exception when calling CustomFieldGroupsApi->createcustom_field_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **body** | [**CustomFieldGroups**](CustomFieldGroups.md)| Data used to create a new custom-field-groups | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getcustom_field_groups**
> CustomFieldGroups getcustom_field_groups(authorization, x_tenant, x_version, custom_field_groups_id)

Return a specific custom-field-group instance.

Return a specific custom-field-group instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CustomFieldGroupsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
custom_field_groups_id = 'custom_field_groups_id_example' # str | The ID of the custom-field-groups that will be retrieved.

try:
    # Return a specific custom-field-group instance.
    api_response = api_instance.getcustom_field_groups(authorization, x_tenant, x_version, custom_field_groups_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomFieldGroupsApi->getcustom_field_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **custom_field_groups_id** | **str**| The ID of the custom-field-groups that will be retrieved. | 

### Return type

[**CustomFieldGroups**](CustomFieldGroups.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getcustom_field_groupss**
> CustomFieldGroupsList getcustom_field_groupss(authorization, x_tenant, x_version, page=page, page_size=page_size, order_by=order_by, select_0=select_0, select_1=select_1, filter_by_code=filter_by_code, filter_by_name=filter_by_name, filter_by_created_at_from=filter_by_created_at_from, filter_by_created_at_to=filter_by_created_at_to, filter_by_or_0_name_like=filter_by_or_0_name_like, filter_by_or_1_code_like=filter_by_or_1_code_like, count_0_filter_by_name=count_0_filter_by_name, count_1_filter_by_created_at_from=count_1_filter_by_created_at_from)

List multiple custom-field-groups resources.

This operation allows you to list and search for custom-field-groups resources provided query arguments.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CustomFieldGroupsApi()
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
    # List multiple custom-field-groups resources.
    api_response = api_instance.getcustom_field_groupss(authorization, x_tenant, x_version, page=page, page_size=page_size, order_by=order_by, select_0=select_0, select_1=select_1, filter_by_code=filter_by_code, filter_by_name=filter_by_name, filter_by_created_at_from=filter_by_created_at_from, filter_by_created_at_to=filter_by_created_at_to, filter_by_or_0_name_like=filter_by_or_0_name_like, filter_by_or_1_code_like=filter_by_or_1_code_like, count_0_filter_by_name=count_0_filter_by_name, count_1_filter_by_created_at_from=count_1_filter_by_created_at_from)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomFieldGroupsApi->getcustom_field_groupss: %s\n" % e)
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

[**CustomFieldGroupsList**](CustomFieldGroupsList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updatecustom_field_groups**
> CustomFieldGroups updatecustom_field_groups(authorization, x_tenant, x_version, custom_field_groups_id, body)

Update a specific custom-field-group instance.

Update a specific custom-field-group instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CustomFieldGroupsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
custom_field_groups_id = 'custom_field_groups_id_example' # str | The ID of the custom-field-groups that will be updated.
body = swagger_client.CustomFieldGroups() # CustomFieldGroups | Data used to update custom-field-groups

try:
    # Update a specific custom-field-group instance.
    api_response = api_instance.updatecustom_field_groups(authorization, x_tenant, x_version, custom_field_groups_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomFieldGroupsApi->updatecustom_field_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **custom_field_groups_id** | **str**| The ID of the custom-field-groups that will be updated. | 
 **body** | [**CustomFieldGroups**](CustomFieldGroups.md)| Data used to update custom-field-groups | 

### Return type

[**CustomFieldGroups**](CustomFieldGroups.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

