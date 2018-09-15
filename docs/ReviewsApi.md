# swagger_client.ReviewsApi

All URIs are relative to *https://api.kenoby.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createreviews**](ReviewsApi.md#createreviews) | **POST** /reviews | Create a new reviews
[**deletereviews**](ReviewsApi.md#deletereviews) | **PUT** /reviews/{reviewsId}/delete | Delete a specific review instance.
[**getreviews**](ReviewsApi.md#getreviews) | **GET** /reviews/{reviewsId} | Return a specific review instance.
[**getreviewss**](ReviewsApi.md#getreviewss) | **GET** /reviews | List multiple reviews resources.
[**updatereviews**](ReviewsApi.md#updatereviews) | **PUT** /reviews/{reviewsId} | Update a specific review instance.


# **createreviews**
> createreviews(authorization, x_tenant, x_version, body)

Create a new reviews

Create a new reviews

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReviewsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
body = swagger_client.Reviews() # Reviews | Data used to create a new reviews

try:
    # Create a new reviews
    api_instance.createreviews(authorization, x_tenant, x_version, body)
except ApiException as e:
    print("Exception when calling ReviewsApi->createreviews: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **body** | [**Reviews**](Reviews.md)| Data used to create a new reviews | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deletereviews**
> Reviews deletereviews(authorization, x_tenant, x_version, reviews_id, body)

Delete a specific review instance.

Delete a specific review instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReviewsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
reviews_id = 'reviews_id_example' # str | The ID of the reviews that will be updated.
body = swagger_client.Reviews() # Reviews | Data used to update reviews

try:
    # Delete a specific review instance.
    api_response = api_instance.deletereviews(authorization, x_tenant, x_version, reviews_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReviewsApi->deletereviews: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **reviews_id** | **str**| The ID of the reviews that will be updated. | 
 **body** | [**Reviews**](Reviews.md)| Data used to update reviews | 

### Return type

[**Reviews**](Reviews.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getreviews**
> Reviews getreviews(authorization, x_tenant, x_version, reviews_id)

Return a specific review instance.

Return a specific review instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReviewsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
reviews_id = 'reviews_id_example' # str | The ID of the reviews that will be retrieved.

try:
    # Return a specific review instance.
    api_response = api_instance.getreviews(authorization, x_tenant, x_version, reviews_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReviewsApi->getreviews: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **reviews_id** | **str**| The ID of the reviews that will be retrieved. | 

### Return type

[**Reviews**](Reviews.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getreviewss**
> ReviewsList getreviewss(authorization, x_tenant, x_version, page=page, page_size=page_size, order_by=order_by, select_0=select_0, select_1=select_1, filter_by_review_like=filter_by_review_like, filter_by_user=filter_by_user, filter_by_applicant=filter_by_applicant, filter_by_position=filter_by_position, filter_by_created_at_from=filter_by_created_at_from, filter_by_created_at_to=filter_by_created_at_to, filter_by_custom_fields_0_field=filter_by_custom_fields_0_field, filter_by_custom_fields_0_value_from=filter_by_custom_fields_0_value_from, count_0_filter_by_review_like=count_0_filter_by_review_like, count_1_filter_by_created_at_from=count_1_filter_by_created_at_from)

List multiple reviews resources.

This operation allows you to list and search for reviews resources provided query arguments.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReviewsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
page = 1 # int | The page of records. Used for pagination. (optional) (default to 1)
page_size = 20 # int | How many records to limit the output. (optional) (default to 20)
order_by = 'name' # str | Which fields to sort the records on. You can use minus sign to have a reverse order. Ex.: orderBy=-name (optional) (default to name)
select_0 = '' # str | Select which fields will be returned by the query. (optional) (default to )
select_1 = '' # str | Select which fields will be returned by the query. One select for each field (optional) (default to )
filter_by_review_like = '' # str | Filter the results. This is just a sample. You can use a better tool like postman to try other filters. Ex: filterBy[fieldA]=some value&filterBy[fieldB][fieldDfromC]=other value (optional) (default to )
filter_by_user = '' # str | Filter the results. This is just a sample. You can use a better tool like postman to try other filters. Ex: filterBy[fieldA]=some value&filterBy[fieldB][fieldDfromC]=other value (optional) (default to )
filter_by_applicant = '' # str | Filter the results. This is just a sample. You can use a better tool like postman to try other filters. Ex: filterBy[fieldA]=some value&filterBy[fieldB][fieldDfromC]=other value (optional) (default to )
filter_by_position = '' # str | Filter the results. This is just a sample. You can use a better tool like postman to try other filters. Ex: filterBy[fieldA]=some value&filterBy[fieldB][fieldDfromC]=other value (optional) (default to )
filter_by_created_at_from = '2015-01-01T02:00:00.000Z' # str | Filter the results greatter than a given date (optional) (default to 2015-01-01T02:00:00.000Z)
filter_by_created_at_to = '2017-01-01T02:00:00.000Z' # str | Filter the results lower than a given date (optional) (default to 2017-01-01T02:00:00.000Z)
filter_by_custom_fields_0_field = '' # str | Filter the results associating more than one parameter. This is just a sample using 'and' sintax. (optional) (default to )
filter_by_custom_fields_0_value_from = '' # str | Filter the results associating more than one parameter. This is just a sample using 'and' sintax. (optional) (default to )
count_0_filter_by_review_like = '' # str | Return the total records from a filterBy query. Ex.: count[0][filterBy][review][like]=Bla (optional) (default to )
count_1_filter_by_created_at_from = '' # str | Return the total records from createdFrom a specific date. Ex.: count[1][filterBy][createdAt][from]=2015-01-01T02:00:00.000Z (optional) (default to )

try:
    # List multiple reviews resources.
    api_response = api_instance.getreviewss(authorization, x_tenant, x_version, page=page, page_size=page_size, order_by=order_by, select_0=select_0, select_1=select_1, filter_by_review_like=filter_by_review_like, filter_by_user=filter_by_user, filter_by_applicant=filter_by_applicant, filter_by_position=filter_by_position, filter_by_created_at_from=filter_by_created_at_from, filter_by_created_at_to=filter_by_created_at_to, filter_by_custom_fields_0_field=filter_by_custom_fields_0_field, filter_by_custom_fields_0_value_from=filter_by_custom_fields_0_value_from, count_0_filter_by_review_like=count_0_filter_by_review_like, count_1_filter_by_created_at_from=count_1_filter_by_created_at_from)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReviewsApi->getreviewss: %s\n" % e)
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
 **filter_by_review_like** | **str**| Filter the results. This is just a sample. You can use a better tool like postman to try other filters. Ex: filterBy[fieldA]&#x3D;some value&amp;filterBy[fieldB][fieldDfromC]&#x3D;other value | [optional] [default to ]
 **filter_by_user** | **str**| Filter the results. This is just a sample. You can use a better tool like postman to try other filters. Ex: filterBy[fieldA]&#x3D;some value&amp;filterBy[fieldB][fieldDfromC]&#x3D;other value | [optional] [default to ]
 **filter_by_applicant** | **str**| Filter the results. This is just a sample. You can use a better tool like postman to try other filters. Ex: filterBy[fieldA]&#x3D;some value&amp;filterBy[fieldB][fieldDfromC]&#x3D;other value | [optional] [default to ]
 **filter_by_position** | **str**| Filter the results. This is just a sample. You can use a better tool like postman to try other filters. Ex: filterBy[fieldA]&#x3D;some value&amp;filterBy[fieldB][fieldDfromC]&#x3D;other value | [optional] [default to ]
 **filter_by_created_at_from** | **str**| Filter the results greatter than a given date | [optional] [default to 2015-01-01T02:00:00.000Z]
 **filter_by_created_at_to** | **str**| Filter the results lower than a given date | [optional] [default to 2017-01-01T02:00:00.000Z]
 **filter_by_custom_fields_0_field** | **str**| Filter the results associating more than one parameter. This is just a sample using &#39;and&#39; sintax. | [optional] [default to ]
 **filter_by_custom_fields_0_value_from** | **str**| Filter the results associating more than one parameter. This is just a sample using &#39;and&#39; sintax. | [optional] [default to ]
 **count_0_filter_by_review_like** | **str**| Return the total records from a filterBy query. Ex.: count[0][filterBy][review][like]&#x3D;Bla | [optional] [default to ]
 **count_1_filter_by_created_at_from** | **str**| Return the total records from createdFrom a specific date. Ex.: count[1][filterBy][createdAt][from]&#x3D;2015-01-01T02:00:00.000Z | [optional] [default to ]

### Return type

[**ReviewsList**](ReviewsList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updatereviews**
> Reviews updatereviews(authorization, x_tenant, x_version, reviews_id, body)

Update a specific review instance.

Update a specific review instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReviewsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
reviews_id = 'reviews_id_example' # str | The ID of the reviews that will be updated.
body = swagger_client.Reviews() # Reviews | Data used to update reviews

try:
    # Update a specific review instance.
    api_response = api_instance.updatereviews(authorization, x_tenant, x_version, reviews_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReviewsApi->updatereviews: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **reviews_id** | **str**| The ID of the reviews that will be updated. | 
 **body** | [**Reviews**](Reviews.md)| Data used to update reviews | 

### Return type

[**Reviews**](Reviews.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

