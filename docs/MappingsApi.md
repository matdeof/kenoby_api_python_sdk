# swagger_client.MappingsApi

All URIs are relative to *https://api.kenoby.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**approvemappings**](MappingsApi.md#approvemappings) | **PUT** /mappings/{mappingsId}/approve | Approve an applicant to next stage.
[**approvemappings_0**](MappingsApi.md#approvemappings_0) | **POST** /mappings/approve | Approve applicants to next stage.
[**cancelmappings**](MappingsApi.md#cancelmappings) | **PUT** /mappings/{mappingsId}/cancel | Rollback the applicant to previews stage.
[**createmappingsreferral**](MappingsApi.md#createmappingsreferral) | **POST** /mappings | Create a new mapping based on a referral from an employee
[**deletemappings**](MappingsApi.md#deletemappings) | **DELETE** /mappings/{mappingsId} | Delete a specific mappings
[**generateandsendtests**](MappingsApi.md#generateandsendtests) | **POST** /screening-tests/generate-and-send | Generate tests if needed and send by email.
[**generateandsendtests_0**](MappingsApi.md#generateandsendtests_0) | **POST** /screening-tests/send-reminder | Generate tests if needed and send a reminder.
[**getcurrentquestiontest**](MappingsApi.md#getcurrentquestiontest) | **POST** /screening-tests/current-question | Validate token and return current question data.
[**getmappings**](MappingsApi.md#getmappings) | **GET** /mappings/{mappingsId} | Return a specific mapping instance.
[**getmappings_0**](MappingsApi.md#getmappings_0) | **GET** /mappings/{mappingsId}/list-tests | Return a specific mapping instance with focus on tests.
[**getmappingss**](MappingsApi.md#getmappingss) | **GET** /mappings | List multiple mappings resources.
[**incompatiblemappings**](MappingsApi.md#incompatiblemappings) | **POST** /mappings/incompatible-progress | Send mappings to incompatible in position.
[**rejectmapping**](MappingsApi.md#rejectmapping) | **PUT** /mappings/{mappingsId}/reject | Reject the applicant.
[**rejectmappings**](MappingsApi.md#rejectmappings) | **PUT** /mappings/reject | Reject the applicant.
[**removemappings**](MappingsApi.md#removemappings) | **POST** /mappings/remove | Remove mappings from position.
[**savecurrentquestiontest**](MappingsApi.md#savecurrentquestiontest) | **POST** /screening-tests/save-current-question | Validate token and save current question answer.
[**setignoretestsenrolledmapping**](MappingsApi.md#setignoretestsenrolledmapping) | **PUT** /mappings/:id/set-ignore-tests-enrolled | Update the flag to ignore tests on Enrolled stage
[**triagemappings**](MappingsApi.md#triagemappings) | **POST** /mappings/triage-progress | Triage all applicants by position in progress page
[**triagemappings_0**](MappingsApi.md#triagemappings_0) | **POST** /mappings/triage | Triage all applicants by position
[**undotriagemappings**](MappingsApi.md#undotriagemappings) | **POST** /mappings/undo-triage | Send mappings to enrolled stage from position, undo triage.
[**updatemappings**](MappingsApi.md#updatemappings) | **PUT** /mappings/{mappingsId} | Update a specific mapping instance.
[**updatestageorder**](MappingsApi.md#updatestageorder) | **PUT** /mappings/{positionId}/update-stage-order | Update mapping manual order.


# **approvemappings**
> Mappings approvemappings(authorization, x_tenant, x_version, mappings_id, body)

Approve an applicant to next stage.

Approve an applicant to next stage.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MappingsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
mappings_id = 'mappings_id_example' # str | The ID of the mappings that will be updated.
body = swagger_client.Mappings() # Mappings | Data used to update mappings

try:
    # Approve an applicant to next stage.
    api_response = api_instance.approvemappings(authorization, x_tenant, x_version, mappings_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MappingsApi->approvemappings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **mappings_id** | **str**| The ID of the mappings that will be updated. | 
 **body** | [**Mappings**](Mappings.md)| Data used to update mappings | 

### Return type

[**Mappings**](Mappings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **approvemappings_0**
> Mappings approvemappings_0(authorization, x_tenant, x_version, mappings_id, body)

Approve applicants to next stage.

Approve applicants to next stage.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MappingsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
mappings_id = 'mappings_id_example' # str | The ID of the mappings that will be updated.
body = swagger_client.Mappings() # Mappings | Data used to update mappings

try:
    # Approve applicants to next stage.
    api_response = api_instance.approvemappings_0(authorization, x_tenant, x_version, mappings_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MappingsApi->approvemappings_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **mappings_id** | **str**| The ID of the mappings that will be updated. | 
 **body** | [**Mappings**](Mappings.md)| Data used to update mappings | 

### Return type

[**Mappings**](Mappings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancelmappings**
> Mappings cancelmappings(authorization, x_tenant, x_version, mappings_id, body)

Rollback the applicant to previews stage.

Rollback the applicant to previews stage.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MappingsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
mappings_id = 'mappings_id_example' # str | The ID of the mappings that will be updated.
body = swagger_client.Mappings() # Mappings | Data used to update mappings

try:
    # Rollback the applicant to previews stage.
    api_response = api_instance.cancelmappings(authorization, x_tenant, x_version, mappings_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MappingsApi->cancelmappings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **mappings_id** | **str**| The ID of the mappings that will be updated. | 
 **body** | [**Mappings**](Mappings.md)| Data used to update mappings | 

### Return type

[**Mappings**](Mappings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **createmappingsreferral**
> createmappingsreferral(authorization, x_tenant, x_version, body)

Create a new mapping based on a referral from an employee

Create a new mapping based on a referral from an employee

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MappingsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
body = swagger_client.Mappings() # Mappings | Data used to create a new mappings

try:
    # Create a new mapping based on a referral from an employee
    api_instance.createmappingsreferral(authorization, x_tenant, x_version, body)
except ApiException as e:
    print("Exception when calling MappingsApi->createmappingsreferral: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **body** | [**Mappings**](Mappings.md)| Data used to create a new mappings | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deletemappings**
> deletemappings(authorization, x_tenant, x_version, mappings_id)

Delete a specific mappings

Delete a specific mappings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MappingsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
mappings_id = 'mappings_id_example' # str | The ID of the mappings that will be deleted.

try:
    # Delete a specific mappings
    api_instance.deletemappings(authorization, x_tenant, x_version, mappings_id)
except ApiException as e:
    print("Exception when calling MappingsApi->deletemappings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **mappings_id** | **str**| The ID of the mappings that will be deleted. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generateandsendtests**
> Mappings generateandsendtests(x_tenant, x_version, position_id, mappings, stage_id, body)

Generate tests if needed and send by email.

Generate tests if needed and send by email.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MappingsApi()
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
position_id = 'position_id_example' # str | The ID of the position that will be used.
mappings = 'mappings_example' # str | The ID of the mappings that will be sent.
stage_id = 'stage_id_example' # str | The ID of the stage that will be used.
body = swagger_client.Mappings() # Mappings | Data used to check mapping

try:
    # Generate tests if needed and send by email.
    api_response = api_instance.generateandsendtests(x_tenant, x_version, position_id, mappings, stage_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MappingsApi->generateandsendtests: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **position_id** | **str**| The ID of the position that will be used. | 
 **mappings** | **str**| The ID of the mappings that will be sent. | 
 **stage_id** | **str**| The ID of the stage that will be used. | 
 **body** | [**Mappings**](Mappings.md)| Data used to check mapping | 

### Return type

[**Mappings**](Mappings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generateandsendtests_0**
> Mappings generateandsendtests_0(x_tenant, x_version, position_id, mappings, stage_id, body)

Generate tests if needed and send a reminder.

Generate tests if needed and send a reminder.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MappingsApi()
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
position_id = 'position_id_example' # str | The ID of the position that will be used.
mappings = 'mappings_example' # str | The ID of the mappings that will be sent.
stage_id = 'stage_id_example' # str | The ID of the stage that will be used.
body = swagger_client.Mappings() # Mappings | Data used to check mapping

try:
    # Generate tests if needed and send a reminder.
    api_response = api_instance.generateandsendtests_0(x_tenant, x_version, position_id, mappings, stage_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MappingsApi->generateandsendtests_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **position_id** | **str**| The ID of the position that will be used. | 
 **mappings** | **str**| The ID of the mappings that will be sent. | 
 **stage_id** | **str**| The ID of the stage that will be used. | 
 **body** | [**Mappings**](Mappings.md)| Data used to check mapping | 

### Return type

[**Mappings**](Mappings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getcurrentquestiontest**
> Mappings getcurrentquestiontest(x_tenant, x_version, mappings_id, token, stage_id, original_test, body)

Validate token and return current question data.

Validate token and return current question data.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MappingsApi()
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
mappings_id = 'mappings_id_example' # str | The ID of the mappings that will be checked.
token = 'token_example' # str | The ID of the mappings that will be checked.
stage_id = 'stage_id_example' # str | The ID of the stage that will be checked.
original_test = 'original_test_example' # str | The ID of the position's test that will be checked.
body = swagger_client.Mappings() # Mappings | Data used to check mapping

try:
    # Validate token and return current question data.
    api_response = api_instance.getcurrentquestiontest(x_tenant, x_version, mappings_id, token, stage_id, original_test, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MappingsApi->getcurrentquestiontest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **mappings_id** | **str**| The ID of the mappings that will be checked. | 
 **token** | **str**| The ID of the mappings that will be checked. | 
 **stage_id** | **str**| The ID of the stage that will be checked. | 
 **original_test** | **str**| The ID of the position&#39;s test that will be checked. | 
 **body** | [**Mappings**](Mappings.md)| Data used to check mapping | 

### Return type

[**Mappings**](Mappings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getmappings**
> Mappings getmappings(authorization, x_tenant, x_version, mappings_id)

Return a specific mapping instance.

Return a specific mapping instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MappingsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
mappings_id = 'mappings_id_example' # str | The ID of the mappings that will be retrieved.

try:
    # Return a specific mapping instance.
    api_response = api_instance.getmappings(authorization, x_tenant, x_version, mappings_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MappingsApi->getmappings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **mappings_id** | **str**| The ID of the mappings that will be retrieved. | 

### Return type

[**Mappings**](Mappings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getmappings_0**
> Mappings getmappings_0(authorization, x_tenant, x_version, mappings_id)

Return a specific mapping instance with focus on tests.

Return a specific mapping instance with focus on tests.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MappingsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
mappings_id = 'mappings_id_example' # str | The ID of the mappings that will be retrieved.

try:
    # Return a specific mapping instance with focus on tests.
    api_response = api_instance.getmappings_0(authorization, x_tenant, x_version, mappings_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MappingsApi->getmappings_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **mappings_id** | **str**| The ID of the mappings that will be retrieved. | 

### Return type

[**Mappings**](Mappings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getmappingss**
> MappingsList getmappingss(authorization, x_tenant, x_version, page=page, page_size=page_size, order_by=order_by, select_0=select_0, select_1=select_1, filter_by_position=filter_by_position, filter_by_applicant=filter_by_applicant, filter_by_created_at_from=filter_by_created_at_from, filter_by_created_at_to=filter_by_created_at_to, filter_by_custom_fields_0_field=filter_by_custom_fields_0_field, filter_by_custom_fields_0_value_from=filter_by_custom_fields_0_value_from, count_0_filter_by_created_at_from=count_0_filter_by_created_at_from)

List multiple mappings resources.

This operation allows you to list and search for mappings resources provided query arguments.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MappingsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
page = 1 # int | The page of records. Used for pagination. (optional) (default to 1)
page_size = 20 # int | How many records to limit the output. (optional) (default to 20)
order_by = 'name' # str | Which fields to sort the records on. You can use minus sign to have a reverse order. Ex.: orderBy=-name (optional) (default to name)
select_0 = '' # str | Select which fields will be returned by the query. (optional) (default to )
select_1 = '' # str | Select which fields will be returned by the query. One select for each field (optional) (default to )
filter_by_position = '' # str | Filter the results. This is just a sample. You can use a better tool like postman to try other filters. Ex: filterBy[fieldA]=some value&filterBy[fieldB][fieldDfromC]=other value (optional) (default to )
filter_by_applicant = '' # str | Filter the results. This is just a sample. You can use a better tool like postman to try other filters. Ex: filterBy[fieldA]=some value&filterBy[fieldB][fieldDfromC]=other value (optional) (default to )
filter_by_created_at_from = '2015-01-01T02:00:00.000Z' # str | Filter the results greatter than a given date (optional) (default to 2015-01-01T02:00:00.000Z)
filter_by_created_at_to = '2017-01-01T02:00:00.000Z' # str | Filter the results lower than a given date (optional) (default to 2017-01-01T02:00:00.000Z)
filter_by_custom_fields_0_field = '' # str | Filter the results associating more than one parameter. This is just a sample using 'and' sintax. (optional) (default to )
filter_by_custom_fields_0_value_from = '' # str | Filter the results associating more than one parameter. This is just a sample using 'and' sintax. (optional) (default to )
count_0_filter_by_created_at_from = '' # str | Return the total records from createdFrom a specific date. Ex.: count[1][filterBy][createdAt][from]=2015-01-01T02:00:00.000Z (optional) (default to )

try:
    # List multiple mappings resources.
    api_response = api_instance.getmappingss(authorization, x_tenant, x_version, page=page, page_size=page_size, order_by=order_by, select_0=select_0, select_1=select_1, filter_by_position=filter_by_position, filter_by_applicant=filter_by_applicant, filter_by_created_at_from=filter_by_created_at_from, filter_by_created_at_to=filter_by_created_at_to, filter_by_custom_fields_0_field=filter_by_custom_fields_0_field, filter_by_custom_fields_0_value_from=filter_by_custom_fields_0_value_from, count_0_filter_by_created_at_from=count_0_filter_by_created_at_from)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MappingsApi->getmappingss: %s\n" % e)
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
 **filter_by_applicant** | **str**| Filter the results. This is just a sample. You can use a better tool like postman to try other filters. Ex: filterBy[fieldA]&#x3D;some value&amp;filterBy[fieldB][fieldDfromC]&#x3D;other value | [optional] [default to ]
 **filter_by_created_at_from** | **str**| Filter the results greatter than a given date | [optional] [default to 2015-01-01T02:00:00.000Z]
 **filter_by_created_at_to** | **str**| Filter the results lower than a given date | [optional] [default to 2017-01-01T02:00:00.000Z]
 **filter_by_custom_fields_0_field** | **str**| Filter the results associating more than one parameter. This is just a sample using &#39;and&#39; sintax. | [optional] [default to ]
 **filter_by_custom_fields_0_value_from** | **str**| Filter the results associating more than one parameter. This is just a sample using &#39;and&#39; sintax. | [optional] [default to ]
 **count_0_filter_by_created_at_from** | **str**| Return the total records from createdFrom a specific date. Ex.: count[1][filterBy][createdAt][from]&#x3D;2015-01-01T02:00:00.000Z | [optional] [default to ]

### Return type

[**MappingsList**](MappingsList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **incompatiblemappings**
> Mappings incompatiblemappings(authorization, x_tenant, x_version, applicants_id, body)

Send mappings to incompatible in position.

Send mappings to incompatible in position.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MappingsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
applicants_id = 'applicants_id_example' # str | The ID of the applicants that will be updated.
body = swagger_client.Mappings() # Mappings | Data used to update mappings

try:
    # Send mappings to incompatible in position.
    api_response = api_instance.incompatiblemappings(authorization, x_tenant, x_version, applicants_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MappingsApi->incompatiblemappings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **applicants_id** | **str**| The ID of the applicants that will be updated. | 
 **body** | [**Mappings**](Mappings.md)| Data used to update mappings | 

### Return type

[**Mappings**](Mappings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rejectmapping**
> Mappings rejectmapping(authorization, x_tenant, x_version, mappings_id, body)

Reject the applicant.

Reject the applicant.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MappingsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
mappings_id = 'mappings_id_example' # str | The ID of the mappings that will be updated.
body = swagger_client.Mappings() # Mappings | Data used to update mappings

try:
    # Reject the applicant.
    api_response = api_instance.rejectmapping(authorization, x_tenant, x_version, mappings_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MappingsApi->rejectmapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **mappings_id** | **str**| The ID of the mappings that will be updated. | 
 **body** | [**Mappings**](Mappings.md)| Data used to update mappings | 

### Return type

[**Mappings**](Mappings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rejectmappings**
> Mappings rejectmappings(authorization, x_tenant, x_version, body)

Reject the applicant.

Reject the applicant.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MappingsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
body = swagger_client.Mappings() # Mappings | Data used to update mappings

try:
    # Reject the applicant.
    api_response = api_instance.rejectmappings(authorization, x_tenant, x_version, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MappingsApi->rejectmappings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **body** | [**Mappings**](Mappings.md)| Data used to update mappings | 

### Return type

[**Mappings**](Mappings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **removemappings**
> Mappings removemappings(authorization, x_tenant, x_version, applicants_id, body)

Remove mappings from position.

Remove mappings from position.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MappingsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
applicants_id = 'applicants_id_example' # str | The ID of the applicants that will be updated.
body = swagger_client.Mappings() # Mappings | Data used to update mappings

try:
    # Remove mappings from position.
    api_response = api_instance.removemappings(authorization, x_tenant, x_version, applicants_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MappingsApi->removemappings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **applicants_id** | **str**| The ID of the applicants that will be updated. | 
 **body** | [**Mappings**](Mappings.md)| Data used to update mappings | 

### Return type

[**Mappings**](Mappings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **savecurrentquestiontest**
> Mappings savecurrentquestiontest(x_tenant, x_version, mappings_id, token, body)

Validate token and save current question answer.

Validate token and save current question answer.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MappingsApi()
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
mappings_id = 'mappings_id_example' # str | The ID of the mappings that will be checked.
token = 'token_example' # str | The ID of the mappings that will be checked.
body = swagger_client.Mappings() # Mappings | Data used to check mapping

try:
    # Validate token and save current question answer.
    api_response = api_instance.savecurrentquestiontest(x_tenant, x_version, mappings_id, token, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MappingsApi->savecurrentquestiontest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **mappings_id** | **str**| The ID of the mappings that will be checked. | 
 **token** | **str**| The ID of the mappings that will be checked. | 
 **body** | [**Mappings**](Mappings.md)| Data used to check mapping | 

### Return type

[**Mappings**](Mappings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setignoretestsenrolledmapping**
> Mappings setignoretestsenrolledmapping(authorization, x_tenant, x_version, body)

Update the flag to ignore tests on Enrolled stage

Update the flag to ignore tests on Enrolled stage

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MappingsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
body = swagger_client.Mappings() # Mappings | Body needs the ignoreEnrolledTests flag to be true or false

try:
    # Update the flag to ignore tests on Enrolled stage
    api_response = api_instance.setignoretestsenrolledmapping(authorization, x_tenant, x_version, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MappingsApi->setignoretestsenrolledmapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **body** | [**Mappings**](Mappings.md)| Body needs the ignoreEnrolledTests flag to be true or false | 

### Return type

[**Mappings**](Mappings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **triagemappings**
> triagemappings(authorization, x_tenant, x_version)

Triage all applicants by position in progress page

Triage all applicants by position in progress page

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MappingsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)

try:
    # Triage all applicants by position in progress page
    api_instance.triagemappings(authorization, x_tenant, x_version)
except ApiException as e:
    print("Exception when calling MappingsApi->triagemappings: %s\n" % e)
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

# **triagemappings_0**
> triagemappings_0(authorization, x_tenant, x_version)

Triage all applicants by position

Triage all applicants

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MappingsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)

try:
    # Triage all applicants by position
    api_instance.triagemappings_0(authorization, x_tenant, x_version)
except ApiException as e:
    print("Exception when calling MappingsApi->triagemappings_0: %s\n" % e)
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

# **undotriagemappings**
> Mappings undotriagemappings(authorization, x_tenant, x_version, applicants_id, body)

Send mappings to enrolled stage from position, undo triage.

Send mappings to enrolled stage from position, undo triage.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MappingsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
applicants_id = 'applicants_id_example' # str | The ID of the applicants that will be updated.
body = swagger_client.Mappings() # Mappings | Data used to update mappings

try:
    # Send mappings to enrolled stage from position, undo triage.
    api_response = api_instance.undotriagemappings(authorization, x_tenant, x_version, applicants_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MappingsApi->undotriagemappings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **applicants_id** | **str**| The ID of the applicants that will be updated. | 
 **body** | [**Mappings**](Mappings.md)| Data used to update mappings | 

### Return type

[**Mappings**](Mappings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updatemappings**
> Mappings updatemappings(authorization, x_tenant, x_version, mappings_id, undo, body)

Update a specific mapping instance.

Update a specific mapping instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MappingsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
mappings_id = 'mappings_id_example' # str | The ID of the mappings that will be updated.
undo = 'undo_example' # str | Send true if you need to decrease the mapped property
body = swagger_client.Mappings() # Mappings | Data used to update mappings

try:
    # Update a specific mapping instance.
    api_response = api_instance.updatemappings(authorization, x_tenant, x_version, mappings_id, undo, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MappingsApi->updatemappings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **mappings_id** | **str**| The ID of the mappings that will be updated. | 
 **undo** | **str**| Send true if you need to decrease the mapped property | 
 **body** | [**Mappings**](Mappings.md)| Data used to update mappings | 

### Return type

[**Mappings**](Mappings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updatestageorder**
> updatestageorder(authorization, x_tenant, x_version, position_id, body)

Update mapping manual order.

Update mapping manual order.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MappingsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
position_id = 'position_id_example' # str | The ID of the position that will be updated.
body = swagger_client.Mappings() # Mappings | Array of Mappings ID that will be updated.

try:
    # Update mapping manual order.
    api_instance.updatestageorder(authorization, x_tenant, x_version, position_id, body)
except ApiException as e:
    print("Exception when calling MappingsApi->updatestageorder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **position_id** | **str**| The ID of the position that will be updated. | 
 **body** | [**Mappings**](Mappings.md)| Array of Mappings ID that will be updated. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

