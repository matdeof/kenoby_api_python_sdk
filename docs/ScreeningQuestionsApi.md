# swagger_client.ScreeningQuestionsApi

All URIs are relative to *https://api.kenoby.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_screening_questions**](ScreeningQuestionsApi.md#create_screening_questions) | **POST** /screeningQuestions | Create a new screeningQuestions
[**disable_screening_questions**](ScreeningQuestionsApi.md#disable_screening_questions) | **POST** /screeningQuestions/:id/disable | Disable a specific screeningQuestions
[**getscreening_question**](ScreeningQuestionsApi.md#getscreening_question) | **GET** /screeningQuestions/{screeningQuestionId} | Return a specific screeningQuestion instance.
[**getscreening_questions**](ScreeningQuestionsApi.md#getscreening_questions) | **GET** /screeningQuestions | List multiple screeningQuestions resources.
[**updatescreening_questions**](ScreeningQuestionsApi.md#updatescreening_questions) | **PUT** /screeningQuestions/{screeningQuestionId} | Update a specific screeningQuestion instance.


# **create_screening_questions**
> create_screening_questions(authorization, x_tenant, x_version, body)

Create a new screeningQuestions

Create a new screeningQuestions

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScreeningQuestionsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
body = swagger_client.ScreeningQuestions() # ScreeningQuestions | Data used to create a new screeningQuestions

try:
    # Create a new screeningQuestions
    api_instance.create_screening_questions(authorization, x_tenant, x_version, body)
except ApiException as e:
    print("Exception when calling ScreeningQuestionsApi->create_screening_questions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **body** | [**ScreeningQuestions**](ScreeningQuestions.md)| Data used to create a new screeningQuestions | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_screening_questions**
> disable_screening_questions(authorization, x_tenant, x_version)

Disable a specific screeningQuestions

Disable a specific screeningQuestions

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScreeningQuestionsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)

try:
    # Disable a specific screeningQuestions
    api_instance.disable_screening_questions(authorization, x_tenant, x_version)
except ApiException as e:
    print("Exception when calling ScreeningQuestionsApi->disable_screening_questions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getscreening_question**
> ScreeningQuestions getscreening_question(authorization, x_tenant, x_version, screening_question_id)

Return a specific screeningQuestion instance.

Return a specific screeningQuestion instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScreeningQuestionsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
screening_question_id = 'screening_question_id_example' # str | The ID of the screeningQuestions that will be retrieved.

try:
    # Return a specific screeningQuestion instance.
    api_response = api_instance.getscreening_question(authorization, x_tenant, x_version, screening_question_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScreeningQuestionsApi->getscreening_question: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **screening_question_id** | **str**| The ID of the screeningQuestions that will be retrieved. | 

### Return type

[**ScreeningQuestions**](ScreeningQuestions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getscreening_questions**
> InterviewScriptsList getscreening_questions(authorization, x_tenant, x_version, page=page, page_size=page_size, order_by=order_by, select_0=select_0, select_1=select_1, filter_by_name_like=filter_by_name_like, filter_by_created_at_from=filter_by_created_at_from, filter_by_created_at_to=filter_by_created_at_to, count_0_filter_by_name_like=count_0_filter_by_name_like, count_1_filter_by_created_at_from=count_1_filter_by_created_at_from, search_by=search_by)

List multiple screeningQuestions resources.

This operation allows you to list and search for screeningQuestions resources provided query arguments.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScreeningQuestionsApi()
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
    # List multiple screeningQuestions resources.
    api_response = api_instance.getscreening_questions(authorization, x_tenant, x_version, page=page, page_size=page_size, order_by=order_by, select_0=select_0, select_1=select_1, filter_by_name_like=filter_by_name_like, filter_by_created_at_from=filter_by_created_at_from, filter_by_created_at_to=filter_by_created_at_to, count_0_filter_by_name_like=count_0_filter_by_name_like, count_1_filter_by_created_at_from=count_1_filter_by_created_at_from, search_by=search_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScreeningQuestionsApi->getscreening_questions: %s\n" % e)
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

[**InterviewScriptsList**](InterviewScriptsList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updatescreening_questions**
> ScreeningQuestions updatescreening_questions(authorization, x_tenant, x_version, screening_question_id, body)

Update a specific screeningQuestion instance.

Update a specific screeningQuestion instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScreeningQuestionsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
screening_question_id = 'screening_question_id_example' # str | The ID of the screeningQuestions that will be updated.
body = swagger_client.ScreeningQuestions() # ScreeningQuestions | Data used to update screeningQuestions

try:
    # Update a specific screeningQuestion instance.
    api_response = api_instance.updatescreening_questions(authorization, x_tenant, x_version, screening_question_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScreeningQuestionsApi->updatescreening_questions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **screening_question_id** | **str**| The ID of the screeningQuestions that will be updated. | 
 **body** | [**ScreeningQuestions**](ScreeningQuestions.md)| Data used to update screeningQuestions | 

### Return type

[**ScreeningQuestions**](ScreeningQuestions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

