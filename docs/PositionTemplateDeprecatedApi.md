# swagger_client.PositionTemplateDeprecatedApi

All URIs are relative to *https://api.kenoby.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createpositiontemplate**](PositionTemplateDeprecatedApi.md#createpositiontemplate) | **POST** /position-template | Create a new position template
[**delete_position_template**](PositionTemplateDeprecatedApi.md#delete_position_template) | **DELETE** /position-template/{positionTemplateId} | Delete a specific position template instance
[**get_applicant_fields**](PositionTemplateDeprecatedApi.md#get_applicant_fields) | **GET** /position-template/{positionTemplateId}/applicant-fields | List multiple applicant custom fields of a specific position template
[**getpositiontemplate**](PositionTemplateDeprecatedApi.md#getpositiontemplate) | **GET** /position-template/{positionTemplateId} | Return a specific position template instance.
[**getpositiontemplates**](PositionTemplateDeprecatedApi.md#getpositiontemplates) | **GET** /position-template | List multiple positions template resources.
[**importpositiontemplate**](PositionTemplateDeprecatedApi.md#importpositiontemplate) | **POST** /position-template/import | Import a new position template
[**updatepositiontemplate**](PositionTemplateDeprecatedApi.md#updatepositiontemplate) | **PUT** /position-template/{positionTemplateId} | Update a specific position template instance.


# **createpositiontemplate**
> createpositiontemplate(authorization, x_tenant, x_version, body)

Create a new position template

Deprecated, use '/position-templates' prefix instead.   Create a new position template

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PositionTemplateDeprecatedApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
body = swagger_client.PositionTemplate() # PositionTemplate | Data used to create a new position template

try:
    # Create a new position template
    api_instance.createpositiontemplate(authorization, x_tenant, x_version, body)
except ApiException as e:
    print("Exception when calling PositionTemplateDeprecatedApi->createpositiontemplate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **body** | [**PositionTemplate**](PositionTemplate.md)| Data used to create a new position template | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_position_template**
> delete_position_template(authorization, x_tenant, x_version, position_template_id)

Delete a specific position template instance

Deprecated, use '/position-templates' prefix instead.   Delete a specific position template instance

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PositionTemplateDeprecatedApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
position_template_id = 'position_template_id_example' # str | The ID of the position template that will be deleted.

try:
    # Delete a specific position template instance
    api_instance.delete_position_template(authorization, x_tenant, x_version, position_template_id)
except ApiException as e:
    print("Exception when calling PositionTemplateDeprecatedApi->delete_position_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **position_template_id** | **str**| The ID of the position template that will be deleted. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_applicant_fields**
> PositionCustomFieldList get_applicant_fields(authorization, x_tenant, x_version, position_template_id)

List multiple applicant custom fields of a specific position template

Deprecated, use '/position-templates' prefix instead.   This operation allows you to list applicant custom fields of a specific template resource provided query arguments

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PositionTemplateDeprecatedApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
position_template_id = 'position_template_id_example' # str | The ID of the position template to retrieve applicant custom fields.

try:
    # List multiple applicant custom fields of a specific position template
    api_response = api_instance.get_applicant_fields(authorization, x_tenant, x_version, position_template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PositionTemplateDeprecatedApi->get_applicant_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **position_template_id** | **str**| The ID of the position template to retrieve applicant custom fields. | 

### Return type

[**PositionCustomFieldList**](PositionCustomFieldList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getpositiontemplate**
> PositionTemplate getpositiontemplate(authorization, x_tenant, x_version, position_template_id)

Return a specific position template instance.

Deprecated, use '/position-templates' prefix instead.   Return a specific position template instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PositionTemplateDeprecatedApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
position_template_id = 'position_template_id_example' # str | The ID of the position template that will be retrieved.

try:
    # Return a specific position template instance.
    api_response = api_instance.getpositiontemplate(authorization, x_tenant, x_version, position_template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PositionTemplateDeprecatedApi->getpositiontemplate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **position_template_id** | **str**| The ID of the position template that will be retrieved. | 

### Return type

[**PositionTemplate**](PositionTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getpositiontemplates**
> PositionTemplatesList getpositiontemplates(authorization, x_tenant, x_version, page=page, page_size=page_size, order_by=order_by, select_0=select_0, select_1=select_1, filter_by_name_like=filter_by_name_like, count_0_filter_by_name_like=count_0_filter_by_name_like, count_1_filter_by_created_at_from=count_1_filter_by_created_at_from, search_by=search_by)

List multiple positions template resources.

Deprecated, use '/position-templates' prefix instead.   This operation allows you to list and search for positions template resources provided query arguments.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PositionTemplateDeprecatedApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
page = 1 # int | The page of records. Used for pagination. (optional) (default to 1)
page_size = 20 # int | How many records to limit the output. (optional) (default to 20)
order_by = 'name' # str | Which fields to sort the records on. You can use minus sign to have a reverse order. Ex.: orderBy=-name (optional) (default to name)
select_0 = '' # str | Select which fields will be returned by the query. (optional) (default to )
select_1 = '' # str | Select which fields will be returned by the query. One select for each field (optional) (default to )
filter_by_name_like = '' # str | Filter the results. This is just a sample. You can use a better tool like postman to try other filters. Ex: filterBy[fieldA]=some value&filterBy[fieldB][fieldDfromC]=other value (optional) (default to )
count_0_filter_by_name_like = '' # str | Return the total records from a filterBy query. Ex.: count[0][filterBy][name][like]=My Position Template (optional) (default to )
count_1_filter_by_created_at_from = '' # str | Return the total records from createdFrom a specific date. Ex.: count[1][filterBy][createdAt][from]=2015-01-01T02:00:00.000Z (optional) (default to )
search_by = '' # str | Make a text search on main fields. (optional) (default to )

try:
    # List multiple positions template resources.
    api_response = api_instance.getpositiontemplates(authorization, x_tenant, x_version, page=page, page_size=page_size, order_by=order_by, select_0=select_0, select_1=select_1, filter_by_name_like=filter_by_name_like, count_0_filter_by_name_like=count_0_filter_by_name_like, count_1_filter_by_created_at_from=count_1_filter_by_created_at_from, search_by=search_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PositionTemplateDeprecatedApi->getpositiontemplates: %s\n" % e)
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
 **count_0_filter_by_name_like** | **str**| Return the total records from a filterBy query. Ex.: count[0][filterBy][name][like]&#x3D;My Position Template | [optional] [default to ]
 **count_1_filter_by_created_at_from** | **str**| Return the total records from createdFrom a specific date. Ex.: count[1][filterBy][createdAt][from]&#x3D;2015-01-01T02:00:00.000Z | [optional] [default to ]
 **search_by** | **str**| Make a text search on main fields. | [optional] [default to ]

### Return type

[**PositionTemplatesList**](PositionTemplatesList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **importpositiontemplate**
> importpositiontemplate(authorization, x_tenant, x_version, body)

Import a new position template

Deprecated, use '/position-templates' prefix instead.   Import a new position template

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PositionTemplateDeprecatedApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
body = swagger_client.Users() # Users | Data used to import a new users

try:
    # Import a new position template
    api_instance.importpositiontemplate(authorization, x_tenant, x_version, body)
except ApiException as e:
    print("Exception when calling PositionTemplateDeprecatedApi->importpositiontemplate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **body** | [**Users**](Users.md)| Data used to import a new users | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updatepositiontemplate**
> PositionTemplate updatepositiontemplate(authorization, x_tenant, x_version, position_template_id, body)

Update a specific position template instance.

Deprecated, use '/position-templates' prefix instead.   Update a specific position template instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PositionTemplateDeprecatedApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
position_template_id = 'position_template_id_example' # str | The ID of the position template that will be updated.
body = swagger_client.PositionTemplate() # PositionTemplate | Data used to update positions

try:
    # Update a specific position template instance.
    api_response = api_instance.updatepositiontemplate(authorization, x_tenant, x_version, position_template_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PositionTemplateDeprecatedApi->updatepositiontemplate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **position_template_id** | **str**| The ID of the position template that will be updated. | 
 **body** | [**PositionTemplate**](PositionTemplate.md)| Data used to update positions | 

### Return type

[**PositionTemplate**](PositionTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

