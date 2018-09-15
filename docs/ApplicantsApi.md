# swagger_client.ApplicantsApi

All URIs are relative to *https://api.kenoby.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activateapplication**](ApplicantsApi.md#activateapplication) | **PUT** /applicants/job/apply/activate | Applicant activating his application for a specific position.
[**applypositions**](ApplicantsApi.md#applypositions) | **PUT** /applicants/job/apply | Applicant applying for a specific position.
[**cachescreeningtest**](ApplicantsApi.md#cachescreeningtest) | **GET** /screening-tests/cache | Save and return a specific application screening test which already started the test.
[**checkpreviousapplicant**](ApplicantsApi.md#checkpreviousapplicant) | **GET** /applicants/jobs/check-previous | Validade if applicant exists for login.
[**checkpreviousapplicant_0**](ApplicantsApi.md#checkpreviousapplicant_0) | **GET** /applicants/jobs/restore-previous | Validade if applicant exists and send an email to the applicant for login.
[**createapplicants**](ApplicantsApi.md#createapplicants) | **POST** /applicants | Create a new applicants
[**createapplicantsreferral**](ApplicantsApi.md#createapplicantsreferral) | **POST** /applicants/referral | Create a new applicant based on a referral from an employee
[**deleteapplicants**](ApplicantsApi.md#deleteapplicants) | **DELETE** /applicants/{applicantsId} | Delete a specific applicant instance.
[**exportapplicants**](ApplicantsApi.md#exportapplicants) | **GET** /applicants/export | Export applicants to CSV
[**getallapplicantssreferral**](ApplicantsApi.md#getallapplicantssreferral) | **GET** /applicants/referrals-list | List multiple referral resources.
[**getapplicantassessments**](ApplicantsApi.md#getapplicantassessments) | **GET** /applicants/{applicantsId}/mindsight | Return mindsight assessments of a specific applicant instance.
[**getapplicants**](ApplicantsApi.md#getapplicants) | **GET** /applicants/{applicantsId} | Return a specific applicant instance.
[**getapplicantss**](ApplicantsApi.md#getapplicantss) | **GET** /applicants | List multiple applicants resources.
[**getapplicantssreferral**](ApplicantsApi.md#getapplicantssreferral) | **GET** /applicants/referrals | List multiple referral applicants resources.
[**getapplication**](ApplicantsApi.md#getapplication) | **GET** /applicants/jobs/restore | Return a specific application instance which already started applying.
[**getapplication_0**](ApplicantsApi.md#getapplication_0) | **GET** /applicants/jobs/cache | Return a specific application instance which already started applying.
[**parse_cv**](ApplicantsApi.md#parse_cv) | **GET** /applicants/any/parse-cv | Return a parsed applicant from a given CV.
[**sendapplicantxerpa**](ApplicantsApi.md#sendapplicantxerpa) | **GET** /applicants/send-to-xerpa | Send applicant to Xerpa
[**sendlogintokenapplicant**](ApplicantsApi.md#sendlogintokenapplicant) | **GET** /applicants/jobs/send-login-token | Send an email to the applicant for login.
[**updateapplicants**](ApplicantsApi.md#updateapplicants) | **PUT** /applicants/{applicantsId} | Update a specific applicant instance.
[**updateapplicantscustomfields**](ApplicantsApi.md#updateapplicantscustomfields) | **PUT** /applicants/{applicantsId}/custom-fields | Update a specific customFields of an applicant instance.
[**updateapplicantsreferralmapping**](ApplicantsApi.md#updateapplicantsreferralmapping) | **PUT** /applicants/referral/mapping | Update a referral setting the mapping after creation
[**updateapplicantsscreeningtest**](ApplicantsApi.md#updateapplicantsscreeningtest) | **PUT** /applicants/{applicantsId}/screeningTest | Update and evaluate a specific applicant screeningTest instance.


# **activateapplication**
> Applicants activateapplication(application, sign_up_token, position=position)

Applicant activating his application for a specific position.

Applicant activating his application for a specific position.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicantsApi()
application = 'application_example' # str | The ID of the application that will be activated.
sign_up_token = 'sign_up_token_example' # str | The token encrypted that gives permission to activate.
position = 'position_example' # str | The ID of the position that will be updated. (optional)

try:
    # Applicant activating his application for a specific position.
    api_response = api_instance.activateapplication(application, sign_up_token, position=position)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicantsApi->activateapplication: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | **str**| The ID of the application that will be activated. | 
 **sign_up_token** | **str**| The token encrypted that gives permission to activate. | 
 **position** | **str**| The ID of the position that will be updated. | [optional] 

### Return type

[**Applicants**](Applicants.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applypositions**
> Applicants applypositions(x_tenant, x_version, position, captcha_token, body)

Applicant applying for a specific position.

Applicant applying for a specific position.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicantsApi()
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
position = 'position_example' # str | The ID of the positions that will be updated.
captcha_token = 'captcha_token_example' # str | The captcha token.
body = swagger_client.Applicants() # Applicants | Applicant that is applying for this position

try:
    # Applicant applying for a specific position.
    api_response = api_instance.applypositions(x_tenant, x_version, position, captcha_token, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicantsApi->applypositions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **position** | **str**| The ID of the positions that will be updated. | 
 **captcha_token** | **str**| The captcha token. | 
 **body** | [**Applicants**](Applicants.md)| Applicant that is applying for this position | 

### Return type

[**Applicants**](Applicants.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cachescreeningtest**
> ApplicantsscreeningTests cachescreeningtest(applicant_id)

Save and return a specific application screening test which already started the test.

Save and return a specific application screening test which already started the test.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicantsApi()
applicant_id = 'applicant_id_example' # str | The ID of the application that will be retrieved.

try:
    # Save and return a specific application screening test which already started the test.
    api_response = api_instance.cachescreeningtest(applicant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicantsApi->cachescreeningtest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicant_id** | **str**| The ID of the application that will be retrieved. | 

### Return type

[**ApplicantsscreeningTests**](ApplicantsscreeningTests.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checkpreviousapplicant**
> Applicants checkpreviousapplicant(email, tenant)

Validade if applicant exists for login.

Validade if applicant exists for login.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicantsApi()
email = 'email_example' # str | The email of the application that will be checked.
tenant = 'tenant_example' # str | The ID of the tenant that will be checked.

try:
    # Validade if applicant exists for login.
    api_response = api_instance.checkpreviousapplicant(email, tenant)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicantsApi->checkpreviousapplicant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| The email of the application that will be checked. | 
 **tenant** | **str**| The ID of the tenant that will be checked. | 

### Return type

[**Applicants**](Applicants.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checkpreviousapplicant_0**
> Applicants checkpreviousapplicant_0(applicant, tenant)

Validade if applicant exists and send an email to the applicant for login.

Validade if applicant exists and send an email to the applicant for login.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicantsApi()
applicant = 'applicant_example' # str | The ID of the application that will be retrieved.
tenant = 'tenant_example' # str | The ID of the tenant that will be retrieved.

try:
    # Validade if applicant exists and send an email to the applicant for login.
    api_response = api_instance.checkpreviousapplicant_0(applicant, tenant)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicantsApi->checkpreviousapplicant_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicant** | **str**| The ID of the application that will be retrieved. | 
 **tenant** | **str**| The ID of the tenant that will be retrieved. | 

### Return type

[**Applicants**](Applicants.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **createapplicants**
> createapplicants(authorization, x_tenant, x_version, body)

Create a new applicants

Create a new applicants

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicantsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
body = swagger_client.Applicants() # Applicants | Data used to create a new applicants

try:
    # Create a new applicants
    api_instance.createapplicants(authorization, x_tenant, x_version, body)
except ApiException as e:
    print("Exception when calling ApplicantsApi->createapplicants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **body** | [**Applicants**](Applicants.md)| Data used to create a new applicants | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **createapplicantsreferral**
> createapplicantsreferral(authorization, x_tenant, x_version, body)

Create a new applicant based on a referral from an employee

Create a new applicant based on a referral from an employee

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicantsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
body = swagger_client.Applicants() # Applicants | Data used to create a new applicant based on a referral from an employee

try:
    # Create a new applicant based on a referral from an employee
    api_instance.createapplicantsreferral(authorization, x_tenant, x_version, body)
except ApiException as e:
    print("Exception when calling ApplicantsApi->createapplicantsreferral: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **body** | [**Applicants**](Applicants.md)| Data used to create a new applicant based on a referral from an employee | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deleteapplicants**
> Applicants deleteapplicants(authorization, x_tenant, x_version, applicants_id, body)

Delete a specific applicant instance.

Delete a specific applicant instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicantsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
applicants_id = 'applicants_id_example' # str | The ID of the applicants that will be deleted.
body = swagger_client.Applicants() # Applicants | Data used to update applicants

try:
    # Delete a specific applicant instance.
    api_response = api_instance.deleteapplicants(authorization, x_tenant, x_version, applicants_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicantsApi->deleteapplicants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **applicants_id** | **str**| The ID of the applicants that will be deleted. | 
 **body** | [**Applicants**](Applicants.md)| Data used to update applicants | 

### Return type

[**Applicants**](Applicants.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exportapplicants**
> ApplicantsList exportapplicants(authorization, x_tenant, x_version)

Export applicants to CSV

This operation allows you to export applicants to CSV using an ElastiSearch Query.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicantsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)

try:
    # Export applicants to CSV
    api_response = api_instance.exportapplicants(authorization, x_tenant, x_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicantsApi->exportapplicants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]

### Return type

[**ApplicantsList**](ApplicantsList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getallapplicantssreferral**
> ApplicantsList getallapplicantssreferral(authorization, x_tenant, x_version)

List multiple referral resources.

This operation allows you to list referral resources.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicantsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)

try:
    # List multiple referral resources.
    api_response = api_instance.getallapplicantssreferral(authorization, x_tenant, x_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicantsApi->getallapplicantssreferral: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]

### Return type

[**ApplicantsList**](ApplicantsList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getapplicantassessments**
> Applicants getapplicantassessments(x_tenant, x_version, applicants_id, token, mapping)

Return mindsight assessments of a specific applicant instance.

Return mindsight assessments of a specific applicant instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicantsApi()
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
applicants_id = 'applicants_id_example' # str | The ID of the applicants that will be retrieved.
token = 'token_example' # str | The token generated in screening test.
mapping = 'mapping_example' # str | The ID of mapping that applicant is requiring the test.

try:
    # Return mindsight assessments of a specific applicant instance.
    api_response = api_instance.getapplicantassessments(x_tenant, x_version, applicants_id, token, mapping)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicantsApi->getapplicantassessments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **applicants_id** | **str**| The ID of the applicants that will be retrieved. | 
 **token** | **str**| The token generated in screening test. | 
 **mapping** | **str**| The ID of mapping that applicant is requiring the test. | 

### Return type

[**Applicants**](Applicants.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getapplicants**
> Applicants getapplicants(authorization, x_tenant, x_version, applicants_id)

Return a specific applicant instance.

Return a specific applicant instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicantsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
applicants_id = 'applicants_id_example' # str | The ID of the applicants that will be retrieved.

try:
    # Return a specific applicant instance.
    api_response = api_instance.getapplicants(authorization, x_tenant, x_version, applicants_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicantsApi->getapplicants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **applicants_id** | **str**| The ID of the applicants that will be retrieved. | 

### Return type

[**Applicants**](Applicants.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getapplicantss**
> ApplicantsList getapplicantss(authorization, x_tenant, x_version, page=page, page_size=page_size, order_by=order_by, select_0=select_0, select_1=select_1, filter_by_name_like=filter_by_name_like, filter_by_created_at_from=filter_by_created_at_from, filter_by_created_at_to=filter_by_created_at_to, filter_by_or_0_name_like=filter_by_or_0_name_like, filter_by_or_1_email_like=filter_by_or_1_email_like, filter_by_custom_fields_0_field=filter_by_custom_fields_0_field, filter_by_custom_fields_0_value_from=filter_by_custom_fields_0_value_from, count_0_filter_by_name_like=count_0_filter_by_name_like, count_1_filter_by_created_at_from=count_1_filter_by_created_at_from, search_by=search_by)

List multiple applicants resources.

This operation allows you to list and search for applicants resources provided query arguments.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicantsApi()
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
filter_by_or_0_name_like = '' # str | Filter the results associating more than one parameter. This is just a sample using 'or' sintax. (optional) (default to )
filter_by_or_1_email_like = '' # str | Filter the results associating more than one parameter. This is just a sample using 'or' sintax. (optional) (default to )
filter_by_custom_fields_0_field = '' # str | Filter the results associating more than one parameter. This is just a sample using 'and' sintax. (optional) (default to )
filter_by_custom_fields_0_value_from = '' # str | Filter the results associating more than one parameter. This is just a sample using 'and' sintax. (optional) (default to )
count_0_filter_by_name_like = '' # str | Return the total records from a filterBy query. Ex.: count[0][filterBy][name][like]=Ricardo (optional) (default to )
count_1_filter_by_created_at_from = '' # str | Return the total records from createdFrom a specific date. Ex.: count[1][filterBy][createdAt][from]=2015-01-01T02:00:00.000Z (optional) (default to )
search_by = '' # str | Make a text search on main fields. Name and e-mail have higher scores. (optional) (default to )

try:
    # List multiple applicants resources.
    api_response = api_instance.getapplicantss(authorization, x_tenant, x_version, page=page, page_size=page_size, order_by=order_by, select_0=select_0, select_1=select_1, filter_by_name_like=filter_by_name_like, filter_by_created_at_from=filter_by_created_at_from, filter_by_created_at_to=filter_by_created_at_to, filter_by_or_0_name_like=filter_by_or_0_name_like, filter_by_or_1_email_like=filter_by_or_1_email_like, filter_by_custom_fields_0_field=filter_by_custom_fields_0_field, filter_by_custom_fields_0_value_from=filter_by_custom_fields_0_value_from, count_0_filter_by_name_like=count_0_filter_by_name_like, count_1_filter_by_created_at_from=count_1_filter_by_created_at_from, search_by=search_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicantsApi->getapplicantss: %s\n" % e)
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
 **filter_by_or_0_name_like** | **str**| Filter the results associating more than one parameter. This is just a sample using &#39;or&#39; sintax. | [optional] [default to ]
 **filter_by_or_1_email_like** | **str**| Filter the results associating more than one parameter. This is just a sample using &#39;or&#39; sintax. | [optional] [default to ]
 **filter_by_custom_fields_0_field** | **str**| Filter the results associating more than one parameter. This is just a sample using &#39;and&#39; sintax. | [optional] [default to ]
 **filter_by_custom_fields_0_value_from** | **str**| Filter the results associating more than one parameter. This is just a sample using &#39;and&#39; sintax. | [optional] [default to ]
 **count_0_filter_by_name_like** | **str**| Return the total records from a filterBy query. Ex.: count[0][filterBy][name][like]&#x3D;Ricardo | [optional] [default to ]
 **count_1_filter_by_created_at_from** | **str**| Return the total records from createdFrom a specific date. Ex.: count[1][filterBy][createdAt][from]&#x3D;2015-01-01T02:00:00.000Z | [optional] [default to ]
 **search_by** | **str**| Make a text search on main fields. Name and e-mail have higher scores. | [optional] [default to ]

### Return type

[**ApplicantsList**](ApplicantsList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getapplicantssreferral**
> ApplicantsList getapplicantssreferral(authorization, x_tenant, x_version)

List multiple referral applicants resources.

This operation allows you to list referral applicants resources.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicantsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)

try:
    # List multiple referral applicants resources.
    api_response = api_instance.getapplicantssreferral(authorization, x_tenant, x_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicantsApi->getapplicantssreferral: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]

### Return type

[**ApplicantsList**](ApplicantsList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getapplication**
> Applicants getapplication(application)

Return a specific application instance which already started applying.

Return a specific application instance which already started applying.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicantsApi()
application = 'application_example' # str | The ID of the application that will be retrieved.

try:
    # Return a specific application instance which already started applying.
    api_response = api_instance.getapplication(application)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicantsApi->getapplication: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | **str**| The ID of the application that will be retrieved. | 

### Return type

[**Applicants**](Applicants.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getapplication_0**
> Applicants getapplication_0(application)

Return a specific application instance which already started applying.

Return a specific application instance which already started applying.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicantsApi()
application = 'application_example' # str | The ID of the application that will be retrieved.

try:
    # Return a specific application instance which already started applying.
    api_response = api_instance.getapplication_0(application)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicantsApi->getapplication_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | **str**| The ID of the application that will be retrieved. | 

### Return type

[**Applicants**](Applicants.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **parse_cv**
> Applicants parse_cv(authorization, x_tenant, x_version, file, captcha_token=captcha_token)

Return a parsed applicant from a given CV.

Return a parsed applicant from a given CV.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicantsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
file = 'file_example' # str | The full path of file that will be parsed.
captcha_token = 'captcha_token_example' # str | The captcha token. It will be required in case the user is not logged in when parsing a file. (optional)

try:
    # Return a parsed applicant from a given CV.
    api_response = api_instance.parse_cv(authorization, x_tenant, x_version, file, captcha_token=captcha_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicantsApi->parse_cv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **file** | **str**| The full path of file that will be parsed. | 
 **captcha_token** | **str**| The captcha token. It will be required in case the user is not logged in when parsing a file. | [optional] 

### Return type

[**Applicants**](Applicants.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sendapplicantxerpa**
> ApplicantsList sendapplicantxerpa(authorization, x_tenant, x_version)

Send applicant to Xerpa

This operation allows you to send an applicant to Xerpa.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicantsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)

try:
    # Send applicant to Xerpa
    api_response = api_instance.sendapplicantxerpa(authorization, x_tenant, x_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicantsApi->sendapplicantxerpa: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]

### Return type

[**ApplicantsList**](ApplicantsList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sendlogintokenapplicant**
> Applicants sendlogintokenapplicant(email, tenant)

Send an email to the applicant for login.

Send an email to the applicant for login.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicantsApi()
email = 'email_example' # str | The email of the application that will be send.
tenant = 'tenant_example' # str | The ID of the tenant that will be retrieved.

try:
    # Send an email to the applicant for login.
    api_response = api_instance.sendlogintokenapplicant(email, tenant)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicantsApi->sendlogintokenapplicant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| The email of the application that will be send. | 
 **tenant** | **str**| The ID of the tenant that will be retrieved. | 

### Return type

[**Applicants**](Applicants.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updateapplicants**
> Applicants updateapplicants(authorization, x_tenant, x_version, applicants_id, body)

Update a specific applicant instance.

Update a specific applicant instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicantsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
applicants_id = 'applicants_id_example' # str | The ID of the applicants that will be updated.
body = swagger_client.Applicants() # Applicants | Data used to update applicants

try:
    # Update a specific applicant instance.
    api_response = api_instance.updateapplicants(authorization, x_tenant, x_version, applicants_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicantsApi->updateapplicants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **applicants_id** | **str**| The ID of the applicants that will be updated. | 
 **body** | [**Applicants**](Applicants.md)| Data used to update applicants | 

### Return type

[**Applicants**](Applicants.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updateapplicantscustomfields**
> Applicants updateapplicantscustomfields(authorization, x_tenant, x_version, applicants_id, body)

Update a specific customFields of an applicant instance.

Update a specific customFields of an applicant instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicantsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
applicants_id = 'applicants_id_example' # str | The ID of the applicants that will be updated.
body = swagger_client.Applicants() # Applicants | Data used to update applicants

try:
    # Update a specific customFields of an applicant instance.
    api_response = api_instance.updateapplicantscustomfields(authorization, x_tenant, x_version, applicants_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicantsApi->updateapplicantscustomfields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **applicants_id** | **str**| The ID of the applicants that will be updated. | 
 **body** | [**Applicants**](Applicants.md)| Data used to update applicants | 

### Return type

[**Applicants**](Applicants.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updateapplicantsreferralmapping**
> updateapplicantsreferralmapping(authorization, x_tenant, x_version, body)

Update a referral setting the mapping after creation

Update a referral setting the mapping after creation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicantsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
body = swagger_client.Applicants() # Applicants | Data used to create a new applicant based on a referral from an employee

try:
    # Update a referral setting the mapping after creation
    api_instance.updateapplicantsreferralmapping(authorization, x_tenant, x_version, body)
except ApiException as e:
    print("Exception when calling ApplicantsApi->updateapplicantsreferralmapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **body** | [**Applicants**](Applicants.md)| Data used to create a new applicant based on a referral from an employee | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updateapplicantsscreeningtest**
> Applicants updateapplicantsscreeningtest(authorization, x_tenant, x_version, applicants_id, body)

Update and evaluate a specific applicant screeningTest instance.

Update and evaluate a specific applicant screeningTest instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicantsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
applicants_id = 'applicants_id_example' # str | The ID of the applicants that will be updated.
body = swagger_client.Applicants() # Applicants | Data used to update applicants screeningTest

try:
    # Update and evaluate a specific applicant screeningTest instance.
    api_response = api_instance.updateapplicantsscreeningtest(authorization, x_tenant, x_version, applicants_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicantsApi->updateapplicantsscreeningtest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **applicants_id** | **str**| The ID of the applicants that will be updated. | 
 **body** | [**Applicants**](Applicants.md)| Data used to update applicants screeningTest | 

### Return type

[**Applicants**](Applicants.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

