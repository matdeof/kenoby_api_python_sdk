# swagger_client.InterviewsApi

All URIs are relative to *https://api.kenoby.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancelinterviews**](InterviewsApi.md#cancelinterviews) | **PUT** /interviews/{interviewsId}/cancel | Cancel a specific interview instance.
[**createinterviews**](InterviewsApi.md#createinterviews) | **POST** /interviews | Create a new interviews
[**finishinterviews**](InterviewsApi.md#finishinterviews) | **PUT** /interviews/{interviewsId}/finish | Finish a specific interview instance.
[**getinterviews**](InterviewsApi.md#getinterviews) | **GET** /interviews/{interviewsId} | Return a specific interview instance.
[**getinterviewsinterviewers**](InterviewsApi.md#getinterviewsinterviewers) | **GET** /interviews/{interviewsId}/interviewers | Return a specific interview with interviewers to be faster.
[**getinterviewss**](InterviewsApi.md#getinterviewss) | **GET** /interviews | List multiple interviews resources.
[**getinterviewtenant**](InterviewsApi.md#getinterviewtenant) | **POST** /interviews/tenant/{interviewsId} | Get interview tenant.
[**sendreminderinterviews**](InterviewsApi.md#sendreminderinterviews) | **POST** /interviews/{interviewsId}/send-reminder | Send an e-mail reminder.
[**updateinterviews**](InterviewsApi.md#updateinterviews) | **PUT** /interviews/{interviewsId} | Update a specific interview instance.


# **cancelinterviews**
> Interviews cancelinterviews(authorization, x_tenant, x_version, interviews_id, body)

Cancel a specific interview instance.

Cancel a specific interview instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InterviewsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
interviews_id = 'interviews_id_example' # str | The ID of the interviews that will be updated.
body = swagger_client.InterviewReport() # InterviewReport | Data used to update interviews

try:
    # Cancel a specific interview instance.
    api_response = api_instance.cancelinterviews(authorization, x_tenant, x_version, interviews_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterviewsApi->cancelinterviews: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **interviews_id** | **str**| The ID of the interviews that will be updated. | 
 **body** | [**InterviewReport**](InterviewReport.md)| Data used to update interviews | 

### Return type

[**Interviews**](Interviews.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **createinterviews**
> createinterviews(authorization, x_tenant, x_version, body)

Create a new interviews

Create a new interviews

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InterviewsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
body = swagger_client.Interviews() # Interviews | Data used to create a new interviews

try:
    # Create a new interviews
    api_instance.createinterviews(authorization, x_tenant, x_version, body)
except ApiException as e:
    print("Exception when calling InterviewsApi->createinterviews: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **body** | [**Interviews**](Interviews.md)| Data used to create a new interviews | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **finishinterviews**
> Interviews finishinterviews(authorization, x_tenant, x_version, interviews_id, body)

Finish a specific interview instance.

Finish a specific interview instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InterviewsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
interviews_id = 'interviews_id_example' # str | The ID of the interviews that will be updated.
body = swagger_client.InterviewReport() # InterviewReport | Data used to update interviews

try:
    # Finish a specific interview instance.
    api_response = api_instance.finishinterviews(authorization, x_tenant, x_version, interviews_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterviewsApi->finishinterviews: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **interviews_id** | **str**| The ID of the interviews that will be updated. | 
 **body** | [**InterviewReport**](InterviewReport.md)| Data used to update interviews | 

### Return type

[**Interviews**](Interviews.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getinterviews**
> Interviews getinterviews(authorization, x_tenant, x_version, interviews_id)

Return a specific interview instance.

Return a specific interview instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InterviewsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
interviews_id = 'interviews_id_example' # str | The ID of the interviews that will be retrieved.

try:
    # Return a specific interview instance.
    api_response = api_instance.getinterviews(authorization, x_tenant, x_version, interviews_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterviewsApi->getinterviews: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **interviews_id** | **str**| The ID of the interviews that will be retrieved. | 

### Return type

[**Interviews**](Interviews.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getinterviewsinterviewers**
> Interviews getinterviewsinterviewers(authorization, x_tenant, x_version, interviews_id)

Return a specific interview with interviewers to be faster.

Return a specific interview with interviewers to be faster.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InterviewsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
interviews_id = 'interviews_id_example' # str | The ID of the interviews that will be retrieved.

try:
    # Return a specific interview with interviewers to be faster.
    api_response = api_instance.getinterviewsinterviewers(authorization, x_tenant, x_version, interviews_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterviewsApi->getinterviewsinterviewers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **interviews_id** | **str**| The ID of the interviews that will be retrieved. | 

### Return type

[**Interviews**](Interviews.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getinterviewss**
> InterviewsList getinterviewss(authorization, x_tenant, x_version, page=page, page_size=page_size, order_by=order_by, select_0=select_0, select_1=select_1, filter_by_scheduler=filter_by_scheduler, filter_by_interviewer=filter_by_interviewer, filter_by_applicant=filter_by_applicant, filter_by_date_from=filter_by_date_from, filter_by_date_to=filter_by_date_to, filter_by_created_at_from=filter_by_created_at_from, filter_by_created_at_to=filter_by_created_at_to, filter_by_or_0_interviewer=filter_by_or_0_interviewer, filter_by_or_1_scheduler=filter_by_or_1_scheduler, filter_by_custom_fields_0_field=filter_by_custom_fields_0_field, filter_by_custom_fields_0_value_from=filter_by_custom_fields_0_value_from, count_0_filter_by_name_like=count_0_filter_by_name_like, count_1_filter_by_created_at_from=count_1_filter_by_created_at_from, search_by=search_by)

List multiple interviews resources.

This operation allows you to list and search for interviews resources provided query arguments.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InterviewsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
page = 1 # int | The page of records. Used for pagination. (optional) (default to 1)
page_size = 20 # int | How many records to limit the output. (optional) (default to 20)
order_by = 'name' # str | Which fields to sort the records on. You can use minus sign to have a reverse order. Ex.: orderBy=-name (optional) (default to name)
select_0 = '' # str | Select which fields will be returned by the query. (optional) (default to )
select_1 = '' # str | Select which fields will be returned by the query. One select for each field (optional) (default to )
filter_by_scheduler = '' # str | Filter the results. This is just a sample. You can use a better tool like postman to try other filters. Ex: filterBy[fieldA]=some value&filterBy[fieldB][fieldDfromC]=other value (optional) (default to )
filter_by_interviewer = '' # str | Filter the results. This is just a sample. You can use a better tool like postman to try other filters. Ex: filterBy[fieldA]=some value&filterBy[fieldB][fieldDfromC]=other value (optional) (default to )
filter_by_applicant = '' # str | Filter the results. This is just a sample. You can use a better tool like postman to try other filters. Ex: filterBy[fieldA]=some value&filterBy[fieldB][fieldDfromC]=other value (optional) (default to )
filter_by_date_from = '' # str | Filter the results greatter than a given date. Ex.: 2015-01-01T02:00:00.000Z (optional) (default to )
filter_by_date_to = '' # str | Filter the results greatter than a given date. Ex.: 2017-01-01T02:00:00.000Z (optional) (default to )
filter_by_created_at_from = '2015-01-01T02:00:00.000Z' # str | Filter the results greatter than a given date (optional) (default to 2015-01-01T02:00:00.000Z)
filter_by_created_at_to = '2017-01-01T02:00:00.000Z' # str | Filter the results lower than a given date (optional) (default to 2017-01-01T02:00:00.000Z)
filter_by_or_0_interviewer = '' # str | Filter the results associating more than one parameter. This is just a sample using 'or' sintax. (optional) (default to )
filter_by_or_1_scheduler = '' # str | Filter the results associating more than one parameter. This is just a sample using 'or' sintax. (optional) (default to )
filter_by_custom_fields_0_field = '' # str | Filter the results associating more than one parameter. This is just a sample using 'and' sintax. (optional) (default to )
filter_by_custom_fields_0_value_from = '' # str | Filter the results associating more than one parameter. This is just a sample using 'and' sintax. (optional) (default to )
count_0_filter_by_name_like = '' # str | Return the total records from a filterBy query. Ex.: count[0][filterBy][name][like]=Ricardo (optional) (default to )
count_1_filter_by_created_at_from = '' # str | Return the total records from createdFrom a specific date. Ex.: count[1][filterBy][createdAt][from]=2015-01-01T02:00:00.000Z (optional) (default to )
search_by = '' # str | Make a text search on main fields. Name and e-mail have higher scores. (optional) (default to )

try:
    # List multiple interviews resources.
    api_response = api_instance.getinterviewss(authorization, x_tenant, x_version, page=page, page_size=page_size, order_by=order_by, select_0=select_0, select_1=select_1, filter_by_scheduler=filter_by_scheduler, filter_by_interviewer=filter_by_interviewer, filter_by_applicant=filter_by_applicant, filter_by_date_from=filter_by_date_from, filter_by_date_to=filter_by_date_to, filter_by_created_at_from=filter_by_created_at_from, filter_by_created_at_to=filter_by_created_at_to, filter_by_or_0_interviewer=filter_by_or_0_interviewer, filter_by_or_1_scheduler=filter_by_or_1_scheduler, filter_by_custom_fields_0_field=filter_by_custom_fields_0_field, filter_by_custom_fields_0_value_from=filter_by_custom_fields_0_value_from, count_0_filter_by_name_like=count_0_filter_by_name_like, count_1_filter_by_created_at_from=count_1_filter_by_created_at_from, search_by=search_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterviewsApi->getinterviewss: %s\n" % e)
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
 **filter_by_scheduler** | **str**| Filter the results. This is just a sample. You can use a better tool like postman to try other filters. Ex: filterBy[fieldA]&#x3D;some value&amp;filterBy[fieldB][fieldDfromC]&#x3D;other value | [optional] [default to ]
 **filter_by_interviewer** | **str**| Filter the results. This is just a sample. You can use a better tool like postman to try other filters. Ex: filterBy[fieldA]&#x3D;some value&amp;filterBy[fieldB][fieldDfromC]&#x3D;other value | [optional] [default to ]
 **filter_by_applicant** | **str**| Filter the results. This is just a sample. You can use a better tool like postman to try other filters. Ex: filterBy[fieldA]&#x3D;some value&amp;filterBy[fieldB][fieldDfromC]&#x3D;other value | [optional] [default to ]
 **filter_by_date_from** | **str**| Filter the results greatter than a given date. Ex.: 2015-01-01T02:00:00.000Z | [optional] [default to ]
 **filter_by_date_to** | **str**| Filter the results greatter than a given date. Ex.: 2017-01-01T02:00:00.000Z | [optional] [default to ]
 **filter_by_created_at_from** | **str**| Filter the results greatter than a given date | [optional] [default to 2015-01-01T02:00:00.000Z]
 **filter_by_created_at_to** | **str**| Filter the results lower than a given date | [optional] [default to 2017-01-01T02:00:00.000Z]
 **filter_by_or_0_interviewer** | **str**| Filter the results associating more than one parameter. This is just a sample using &#39;or&#39; sintax. | [optional] [default to ]
 **filter_by_or_1_scheduler** | **str**| Filter the results associating more than one parameter. This is just a sample using &#39;or&#39; sintax. | [optional] [default to ]
 **filter_by_custom_fields_0_field** | **str**| Filter the results associating more than one parameter. This is just a sample using &#39;and&#39; sintax. | [optional] [default to ]
 **filter_by_custom_fields_0_value_from** | **str**| Filter the results associating more than one parameter. This is just a sample using &#39;and&#39; sintax. | [optional] [default to ]
 **count_0_filter_by_name_like** | **str**| Return the total records from a filterBy query. Ex.: count[0][filterBy][name][like]&#x3D;Ricardo | [optional] [default to ]
 **count_1_filter_by_created_at_from** | **str**| Return the total records from createdFrom a specific date. Ex.: count[1][filterBy][createdAt][from]&#x3D;2015-01-01T02:00:00.000Z | [optional] [default to ]
 **search_by** | **str**| Make a text search on main fields. Name and e-mail have higher scores. | [optional] [default to ]

### Return type

[**InterviewsList**](InterviewsList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getinterviewtenant**
> Interviews getinterviewtenant(interviews_id)

Get interview tenant.

Get interview tenant for users multi tenant.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InterviewsApi()
interviews_id = 'interviews_id_example' # str | The ID of the interviews that will get tenant.

try:
    # Get interview tenant.
    api_response = api_instance.getinterviewtenant(interviews_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterviewsApi->getinterviewtenant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interviews_id** | **str**| The ID of the interviews that will get tenant. | 

### Return type

[**Interviews**](Interviews.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sendreminderinterviews**
> Interviews sendreminderinterviews(authorization, x_tenant, x_version, interviews_id)

Send an e-mail reminder.

Send an e-mail reminder.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InterviewsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
interviews_id = 'interviews_id_example' # str | The ID of the interviews that will be send a reminder.

try:
    # Send an e-mail reminder.
    api_response = api_instance.sendreminderinterviews(authorization, x_tenant, x_version, interviews_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterviewsApi->sendreminderinterviews: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **interviews_id** | **str**| The ID of the interviews that will be send a reminder. | 

### Return type

[**Interviews**](Interviews.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updateinterviews**
> Interviews updateinterviews(authorization, x_tenant, x_version, interviews_id, body)

Update a specific interview instance.

Update a specific interview instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InterviewsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
interviews_id = 'interviews_id_example' # str | The ID of the interviews that will be updated.
body = swagger_client.Interviews() # Interviews | Data used to update interviews

try:
    # Update a specific interview instance.
    api_response = api_instance.updateinterviews(authorization, x_tenant, x_version, interviews_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterviewsApi->updateinterviews: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **interviews_id** | **str**| The ID of the interviews that will be updated. | 
 **body** | [**Interviews**](Interviews.md)| Data used to update interviews | 

### Return type

[**Interviews**](Interviews.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

