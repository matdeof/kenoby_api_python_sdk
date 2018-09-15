# swagger_client.JobDescriptionTemplatesApi

All URIs are relative to *https://api.kenoby.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createjob_description_templates**](JobDescriptionTemplatesApi.md#createjob_description_templates) | **POST** /job-description-templates | Create a new job-description-templates
[**deletejob_description_templates**](JobDescriptionTemplatesApi.md#deletejob_description_templates) | **DELETE** /job-description-templates/{job-description-templatesId} | Delete a specific job-description-template instance.
[**getjob_description_templates**](JobDescriptionTemplatesApi.md#getjob_description_templates) | **GET** /job-description-templates/{job-description-templatesId} | Return a specific job-description-template instance.
[**getjob_description_templatess**](JobDescriptionTemplatesApi.md#getjob_description_templatess) | **GET** /job-description-templates | List multiple job-description-templates resources.
[**updatejob_description_templates**](JobDescriptionTemplatesApi.md#updatejob_description_templates) | **PUT** /job-description-templates/{job-description-templatesId} | Update a specific job-description-template instance.


# **createjob_description_templates**
> createjob_description_templates(authorization, x_tenant, x_version, body)

Create a new job-description-templates

Create a new job-description-templates

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.JobDescriptionTemplatesApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
body = swagger_client.JobDescriptionTemplates() # JobDescriptionTemplates | Data used to create a new job-description-templates

try:
    # Create a new job-description-templates
    api_instance.createjob_description_templates(authorization, x_tenant, x_version, body)
except ApiException as e:
    print("Exception when calling JobDescriptionTemplatesApi->createjob_description_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **body** | [**JobDescriptionTemplates**](JobDescriptionTemplates.md)| Data used to create a new job-description-templates | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deletejob_description_templates**
> JobDescriptionTemplates deletejob_description_templates(authorization, x_tenant, x_version, job_description_templates_id, body)

Delete a specific job-description-template instance.

Delete a specific job-description-template instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.JobDescriptionTemplatesApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
job_description_templates_id = 'job_description_templates_id_example' # str | The ID of the job-description-templates that will be deleted.
body = swagger_client.JobDescriptionTemplates() # JobDescriptionTemplates | Data used to delete job-description-templates

try:
    # Delete a specific job-description-template instance.
    api_response = api_instance.deletejob_description_templates(authorization, x_tenant, x_version, job_description_templates_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobDescriptionTemplatesApi->deletejob_description_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **job_description_templates_id** | **str**| The ID of the job-description-templates that will be deleted. | 
 **body** | [**JobDescriptionTemplates**](JobDescriptionTemplates.md)| Data used to delete job-description-templates | 

### Return type

[**JobDescriptionTemplates**](JobDescriptionTemplates.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getjob_description_templates**
> JobDescriptionTemplates getjob_description_templates(authorization, x_tenant, x_version, job_description_templates_id)

Return a specific job-description-template instance.

Return a specific job-description-template instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.JobDescriptionTemplatesApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
job_description_templates_id = 'job_description_templates_id_example' # str | The ID of the job-description-templates that will be retrieved.

try:
    # Return a specific job-description-template instance.
    api_response = api_instance.getjob_description_templates(authorization, x_tenant, x_version, job_description_templates_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobDescriptionTemplatesApi->getjob_description_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **job_description_templates_id** | **str**| The ID of the job-description-templates that will be retrieved. | 

### Return type

[**JobDescriptionTemplates**](JobDescriptionTemplates.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getjob_description_templatess**
> JobDescriptionTemplatesList getjob_description_templatess(authorization, x_tenant, x_version, page=page, page_size=page_size, order_by=order_by, select_0=select_0, select_1=select_1, filter_by_name_like=filter_by_name_like, filter_by_subject_like=filter_by_subject_like, filter_by_description_like=filter_by_description_like, filter_by_created_at_from=filter_by_created_at_from, filter_by_created_at_to=filter_by_created_at_to, filter_by_or_0_name_like=filter_by_or_0_name_like, filter_by_or_1_subject_like=filter_by_or_1_subject_like, count_0_filter_by_name_like=count_0_filter_by_name_like, count_1_filter_by_created_at_from=count_1_filter_by_created_at_from)

List multiple job-description-templates resources.

This operation allows you to list and search for job-description-templates resources provided query arguments.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.JobDescriptionTemplatesApi()
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
filter_by_description_like = '' # str | Filter the results. This is just a sample. You can use a better tool like postman to try other filters. Ex: filterBy[fieldA]=some value&filterBy[fieldB][fieldDfromC]=other value (optional) (default to )
filter_by_created_at_from = '2015-01-01T02:00:00.000Z' # str | Filter the results greatter than a given date (optional) (default to 2015-01-01T02:00:00.000Z)
filter_by_created_at_to = '2017-01-01T02:00:00.000Z' # str | Filter the results lower than a given date (optional) (default to 2017-01-01T02:00:00.000Z)
filter_by_or_0_name_like = '' # str | Filter the results associating more than one parameter. This is just a sample using 'or' sintax. (optional) (default to )
filter_by_or_1_subject_like = '' # str | Filter the results associating more than one parameter. This is just a sample using 'or' sintax. (optional) (default to )
count_0_filter_by_name_like = '' # str | Return the total records from a filterBy query. Ex.: count[0][filterBy][name][like]=Ricardo (optional) (default to )
count_1_filter_by_created_at_from = '' # str | Return the total records from createdFrom a specific date. Ex.: count[1][filterBy][createdAt][from]=2015-01-01T02:00:00.000Z (optional) (default to )

try:
    # List multiple job-description-templates resources.
    api_response = api_instance.getjob_description_templatess(authorization, x_tenant, x_version, page=page, page_size=page_size, order_by=order_by, select_0=select_0, select_1=select_1, filter_by_name_like=filter_by_name_like, filter_by_subject_like=filter_by_subject_like, filter_by_description_like=filter_by_description_like, filter_by_created_at_from=filter_by_created_at_from, filter_by_created_at_to=filter_by_created_at_to, filter_by_or_0_name_like=filter_by_or_0_name_like, filter_by_or_1_subject_like=filter_by_or_1_subject_like, count_0_filter_by_name_like=count_0_filter_by_name_like, count_1_filter_by_created_at_from=count_1_filter_by_created_at_from)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobDescriptionTemplatesApi->getjob_description_templatess: %s\n" % e)
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
 **filter_by_description_like** | **str**| Filter the results. This is just a sample. You can use a better tool like postman to try other filters. Ex: filterBy[fieldA]&#x3D;some value&amp;filterBy[fieldB][fieldDfromC]&#x3D;other value | [optional] [default to ]
 **filter_by_created_at_from** | **str**| Filter the results greatter than a given date | [optional] [default to 2015-01-01T02:00:00.000Z]
 **filter_by_created_at_to** | **str**| Filter the results lower than a given date | [optional] [default to 2017-01-01T02:00:00.000Z]
 **filter_by_or_0_name_like** | **str**| Filter the results associating more than one parameter. This is just a sample using &#39;or&#39; sintax. | [optional] [default to ]
 **filter_by_or_1_subject_like** | **str**| Filter the results associating more than one parameter. This is just a sample using &#39;or&#39; sintax. | [optional] [default to ]
 **count_0_filter_by_name_like** | **str**| Return the total records from a filterBy query. Ex.: count[0][filterBy][name][like]&#x3D;Ricardo | [optional] [default to ]
 **count_1_filter_by_created_at_from** | **str**| Return the total records from createdFrom a specific date. Ex.: count[1][filterBy][createdAt][from]&#x3D;2015-01-01T02:00:00.000Z | [optional] [default to ]

### Return type

[**JobDescriptionTemplatesList**](JobDescriptionTemplatesList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updatejob_description_templates**
> JobDescriptionTemplates updatejob_description_templates(authorization, x_tenant, x_version, job_description_templates_id, body)

Update a specific job-description-template instance.

Update a specific job-description-template instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.JobDescriptionTemplatesApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
job_description_templates_id = 'job_description_templates_id_example' # str | The ID of the job-description-templates that will be updated.
body = swagger_client.JobDescriptionTemplates() # JobDescriptionTemplates | Data used to update job-description-templates

try:
    # Update a specific job-description-template instance.
    api_response = api_instance.updatejob_description_templates(authorization, x_tenant, x_version, job_description_templates_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobDescriptionTemplatesApi->updatejob_description_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **job_description_templates_id** | **str**| The ID of the job-description-templates that will be updated. | 
 **body** | [**JobDescriptionTemplates**](JobDescriptionTemplates.md)| Data used to update job-description-templates | 

### Return type

[**JobDescriptionTemplates**](JobDescriptionTemplates.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

