# swagger_client.MessageTemplatesApi

All URIs are relative to *https://api.kenoby.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createmessage_templates**](MessageTemplatesApi.md#createmessage_templates) | **POST** /message-templates | Create a new message-templates
[**deletemessage_templates**](MessageTemplatesApi.md#deletemessage_templates) | **DELETE** /message-templates/{message-templatesId} | Delete a specific message-template instance.
[**getmessage_templates**](MessageTemplatesApi.md#getmessage_templates) | **GET** /message-templates/{message-templatesId} | Return a specific message-template instance.
[**getmessage_templatess**](MessageTemplatesApi.md#getmessage_templatess) | **GET** /message-templates | List multiple message-templates resources.
[**updatemessage_templates**](MessageTemplatesApi.md#updatemessage_templates) | **PUT** /message-templates/{message-templatesId} | Update a specific message-template instance.


# **createmessage_templates**
> createmessage_templates(authorization, x_tenant, x_version, body)

Create a new message-templates

Create a new message-templates

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MessageTemplatesApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
body = swagger_client.MessageTemplates() # MessageTemplates | Data used to create a new message-templates

try:
    # Create a new message-templates
    api_instance.createmessage_templates(authorization, x_tenant, x_version, body)
except ApiException as e:
    print("Exception when calling MessageTemplatesApi->createmessage_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **body** | [**MessageTemplates**](MessageTemplates.md)| Data used to create a new message-templates | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deletemessage_templates**
> MessageTemplates deletemessage_templates(authorization, x_tenant, x_version, message_templates_id, body)

Delete a specific message-template instance.

Delete a specific message-template instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MessageTemplatesApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
message_templates_id = 'message_templates_id_example' # str | The ID of the message-templates that will be deleted.
body = swagger_client.MessageTemplates() # MessageTemplates | Data used to delete message-templates

try:
    # Delete a specific message-template instance.
    api_response = api_instance.deletemessage_templates(authorization, x_tenant, x_version, message_templates_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessageTemplatesApi->deletemessage_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **message_templates_id** | **str**| The ID of the message-templates that will be deleted. | 
 **body** | [**MessageTemplates**](MessageTemplates.md)| Data used to delete message-templates | 

### Return type

[**MessageTemplates**](MessageTemplates.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getmessage_templates**
> MessageTemplates getmessage_templates(authorization, x_tenant, x_version, message_templates_id)

Return a specific message-template instance.

Return a specific message-template instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MessageTemplatesApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
message_templates_id = 'message_templates_id_example' # str | The ID of the message-templates that will be retrieved.

try:
    # Return a specific message-template instance.
    api_response = api_instance.getmessage_templates(authorization, x_tenant, x_version, message_templates_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessageTemplatesApi->getmessage_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **message_templates_id** | **str**| The ID of the message-templates that will be retrieved. | 

### Return type

[**MessageTemplates**](MessageTemplates.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getmessage_templatess**
> MessageTemplatesList getmessage_templatess(authorization, x_tenant, x_version, page=page, page_size=page_size, order_by=order_by, select_0=select_0, select_1=select_1, filter_by_name_like=filter_by_name_like, filter_by_subject_like=filter_by_subject_like, filter_by_message_like=filter_by_message_like, filter_by_created_at_from=filter_by_created_at_from, filter_by_created_at_to=filter_by_created_at_to, filter_by_or_0_name_like=filter_by_or_0_name_like, filter_by_or_1_subject_like=filter_by_or_1_subject_like, count_0_filter_by_name_like=count_0_filter_by_name_like, count_1_filter_by_created_at_from=count_1_filter_by_created_at_from)

List multiple message-templates resources.

This operation allows you to list and search for message-templates resources provided query arguments.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MessageTemplatesApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
page = 1 # int | The page of records. Used for pagination. (optional) (default to 1)
page_size = 20 # int | How many records to limit the output. (optional) (default to 20)
order_by = 'name' # str | Which fields to sort the records on. You can use minus sign to have a reverse order. Ex.: orderBy=-name (optional) (default to name)
select_0 = '' # str | Select which fields will be returned by the query. (optional) (default to )
select_1 = '' # str | Select which fields will be returned by the query. One select for each field (optional) (default to )
filter_by_name_like = '' # str | Filter the results. This is just a sample. You can use a better tool like postman to try other filters. Ex: filterBy[fieldA]=some value&filterBy[fieldB][fieldDfromC]=other value (optional) (default to )
filter_by_subject_like = '' # str | Filter the results. This is just a sample. You can use a better tool like postman to try other filters. Ex: filterBy[fieldA]=some value&filterBy[fieldB][fieldDfromC]=other value (optional) (default to )
filter_by_message_like = '' # str | Filter the results. This is just a sample. You can use a better tool like postman to try other filters. Ex: filterBy[fieldA]=some value&filterBy[fieldB][fieldDfromC]=other value (optional) (default to )
filter_by_created_at_from = '2015-01-01T02:00:00.000Z' # str | Filter the results greatter than a given date (optional) (default to 2015-01-01T02:00:00.000Z)
filter_by_created_at_to = '2017-01-01T02:00:00.000Z' # str | Filter the results lower than a given date (optional) (default to 2017-01-01T02:00:00.000Z)
filter_by_or_0_name_like = '' # str | Filter the results associating more than one parameter. This is just a sample using 'or' sintax. (optional) (default to )
filter_by_or_1_subject_like = '' # str | Filter the results associating more than one parameter. This is just a sample using 'or' sintax. (optional) (default to )
count_0_filter_by_name_like = '' # str | Return the total records from a filterBy query. Ex.: count[0][filterBy][name][like]=Ricardo (optional) (default to )
count_1_filter_by_created_at_from = '' # str | Return the total records from createdFrom a specific date. Ex.: count[1][filterBy][createdAt][from]=2015-01-01T02:00:00.000Z (optional) (default to )

try:
    # List multiple message-templates resources.
    api_response = api_instance.getmessage_templatess(authorization, x_tenant, x_version, page=page, page_size=page_size, order_by=order_by, select_0=select_0, select_1=select_1, filter_by_name_like=filter_by_name_like, filter_by_subject_like=filter_by_subject_like, filter_by_message_like=filter_by_message_like, filter_by_created_at_from=filter_by_created_at_from, filter_by_created_at_to=filter_by_created_at_to, filter_by_or_0_name_like=filter_by_or_0_name_like, filter_by_or_1_subject_like=filter_by_or_1_subject_like, count_0_filter_by_name_like=count_0_filter_by_name_like, count_1_filter_by_created_at_from=count_1_filter_by_created_at_from)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessageTemplatesApi->getmessage_templatess: %s\n" % e)
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
 **filter_by_subject_like** | **str**| Filter the results. This is just a sample. You can use a better tool like postman to try other filters. Ex: filterBy[fieldA]&#x3D;some value&amp;filterBy[fieldB][fieldDfromC]&#x3D;other value | [optional] [default to ]
 **filter_by_message_like** | **str**| Filter the results. This is just a sample. You can use a better tool like postman to try other filters. Ex: filterBy[fieldA]&#x3D;some value&amp;filterBy[fieldB][fieldDfromC]&#x3D;other value | [optional] [default to ]
 **filter_by_created_at_from** | **str**| Filter the results greatter than a given date | [optional] [default to 2015-01-01T02:00:00.000Z]
 **filter_by_created_at_to** | **str**| Filter the results lower than a given date | [optional] [default to 2017-01-01T02:00:00.000Z]
 **filter_by_or_0_name_like** | **str**| Filter the results associating more than one parameter. This is just a sample using &#39;or&#39; sintax. | [optional] [default to ]
 **filter_by_or_1_subject_like** | **str**| Filter the results associating more than one parameter. This is just a sample using &#39;or&#39; sintax. | [optional] [default to ]
 **count_0_filter_by_name_like** | **str**| Return the total records from a filterBy query. Ex.: count[0][filterBy][name][like]&#x3D;Ricardo | [optional] [default to ]
 **count_1_filter_by_created_at_from** | **str**| Return the total records from createdFrom a specific date. Ex.: count[1][filterBy][createdAt][from]&#x3D;2015-01-01T02:00:00.000Z | [optional] [default to ]

### Return type

[**MessageTemplatesList**](MessageTemplatesList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updatemessage_templates**
> MessageTemplates updatemessage_templates(authorization, x_tenant, x_version, message_templates_id, body)

Update a specific message-template instance.

Update a specific message-template instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MessageTemplatesApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
message_templates_id = 'message_templates_id_example' # str | The ID of the message-templates that will be updated.
body = swagger_client.MessageTemplates() # MessageTemplates | Data used to update message-templates

try:
    # Update a specific message-template instance.
    api_response = api_instance.updatemessage_templates(authorization, x_tenant, x_version, message_templates_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessageTemplatesApi->updatemessage_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **message_templates_id** | **str**| The ID of the message-templates that will be updated. | 
 **body** | [**MessageTemplates**](MessageTemplates.md)| Data used to update message-templates | 

### Return type

[**MessageTemplates**](MessageTemplates.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

