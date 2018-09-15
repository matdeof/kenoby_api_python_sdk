# swagger_client.ApplicantUsersApi

All URIs are relative to *https://api.kenoby.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**applicantuserforgotpassword**](ApplicantUsersApi.md#applicantuserforgotpassword) | **GET** /applicant-user/forgot-password | Send an email for the applicant with the link to change password.
[**approve_applicantion_position**](ApplicantUsersApi.md#approve_applicantion_position) | **POST** /applicant-user/:applicant/:position/approve | Approve applied position for internal jobsite an determinated applicant.
[**check_applicant_user_credentials**](ApplicantUsersApi.md#check_applicant_user_credentials) | **POST** /applicant-user/auth | Check applicant-user credentials
[**check_applicant_user_credentials_0**](ApplicantUsersApi.md#check_applicant_user_credentials_0) | **POST** /applicant-user/credentials | Check applicant-user credentials
[**check_applicant_user_credentials_1**](ApplicantUsersApi.md#check_applicant_user_credentials_1) | **POST** /applicant-user/{applicantUser}/magic-link | Request magic link to access web portal
[**find_applicant_user_by_email**](ApplicantUsersApi.md#find_applicant_user_by_email) | **GET** /applicant-user/auth | Check if the email is already in use.
[**get_applicant_user_applications**](ApplicantUsersApi.md#get_applicant_user_applications) | **GET** /applicant-user/applications | Request the applications of a applicant user from a tenant.
[**getapplicantuser**](ApplicantUsersApi.md#getapplicantuser) | **GET** /applicant-user/{applicantUserId} | Return a specific applicant user instance.
[**new_applicant_user**](ApplicantUsersApi.md#new_applicant_user) | **POST** /applicant-user | Create a new applicant user
[**reject_applicantion_position**](ApplicantUsersApi.md#reject_applicantion_position) | **POST** /applicant-user/:applicant/:position/reject | Reject applied position for internal jobsite an determinated applicant.
[**resend_email_verification**](ApplicantUsersApi.md#resend_email_verification) | **POST** /applicant-user/{applicantUser}/resend-email-verification | Resend the email verification for applicantUser
[**save_partial**](ApplicantUsersApi.md#save_partial) | **POST** /applicant-user/save-partial | Save the minimum data of ApplicantUser case his not exist in database


# **applicantuserforgotpassword**
> ApplicantUser applicantuserforgotpassword(x_tenant, x_portal_token, email)

Send an email for the applicant with the link to change password.

Send an email for the applicant with the link to change password.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicantUsersApi()
x_tenant = '' # str | Tenant ID. (default to )
x_portal_token = '' # str | Login Token/Magic Link token (not required if Authorization is send). (default to )
email = 'email_example' # str | The applicant user email.

try:
    # Send an email for the applicant with the link to change password.
    api_response = api_instance.applicantuserforgotpassword(x_tenant, x_portal_token, email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicantUsersApi->applicantuserforgotpassword: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**| Tenant ID. | [default to ]
 **x_portal_token** | **str**| Login Token/Magic Link token (not required if Authorization is send). | [default to ]
 **email** | **str**| The applicant user email. | 

### Return type

[**ApplicantUser**](ApplicantUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **approve_applicantion_position**
> approve_applicantion_position(applicant, position)

Approve applied position for internal jobsite an determinated applicant.

Approve applied position for internal jobsite an determinated applicant.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicantUsersApi()
applicant = 'applicant_example' # str | The applicant id.
position = 'position_example' # str | The position id.

try:
    # Approve applied position for internal jobsite an determinated applicant.
    api_instance.approve_applicantion_position(applicant, position)
except ApiException as e:
    print("Exception when calling ApplicantUsersApi->approve_applicantion_position: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicant** | **str**| The applicant id. | 
 **position** | **str**| The position id. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_applicant_user_credentials**
> check_applicant_user_credentials(x_tenant, authorization, x_portal_token, x_portal=x_portal)

Check applicant-user credentials

Check applicant-user credentials

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicantUsersApi()
x_tenant = '' # str | Tenant ID. (default to )
authorization = 'Basic ' # str | Basic Authentication (not required if x-portal-token is send). (default to Basic )
x_portal_token = '' # str | Login Token/Magic Link token (not required if Authorization is send). (default to )
x_portal = false # bool | Flag to determine that we are using web portal (optional) (default to false)

try:
    # Check applicant-user credentials
    api_instance.check_applicant_user_credentials(x_tenant, authorization, x_portal_token, x_portal=x_portal)
except ApiException as e:
    print("Exception when calling ApplicantUsersApi->check_applicant_user_credentials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**| Tenant ID. | [default to ]
 **authorization** | **str**| Basic Authentication (not required if x-portal-token is send). | [default to Basic ]
 **x_portal_token** | **str**| Login Token/Magic Link token (not required if Authorization is send). | [default to ]
 **x_portal** | **bool**| Flag to determine that we are using web portal | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_applicant_user_credentials_0**
> check_applicant_user_credentials_0(authorization, x_portal_token, x_portal=x_portal)

Check applicant-user credentials

Check applicant-user credentials

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicantUsersApi()
authorization = 'Basic ' # str | Basic Authentication (not required if x-portal-token is send). (default to Basic )
x_portal_token = '' # str | Login Token/Magic Link token (not required if Authorization is send). (default to )
x_portal = false # bool | Flag to determine that we are using web portal (optional) (default to false)

try:
    # Check applicant-user credentials
    api_instance.check_applicant_user_credentials_0(authorization, x_portal_token, x_portal=x_portal)
except ApiException as e:
    print("Exception when calling ApplicantUsersApi->check_applicant_user_credentials_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication (not required if x-portal-token is send). | [default to Basic ]
 **x_portal_token** | **str**| Login Token/Magic Link token (not required if Authorization is send). | [default to ]
 **x_portal** | **bool**| Flag to determine that we are using web portal | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_applicant_user_credentials_1**
> check_applicant_user_credentials_1(x_tenant, id)

Request magic link to access web portal

Request magic link to access web portal

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicantUsersApi()
x_tenant = '' # str | Tenant ID. (default to )
id = 'id_example' # str | The ID of the applicant users that will be retrieved.

try:
    # Request magic link to access web portal
    api_instance.check_applicant_user_credentials_1(x_tenant, id)
except ApiException as e:
    print("Exception when calling ApplicantUsersApi->check_applicant_user_credentials_1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**| Tenant ID. | [default to ]
 **id** | **str**| The ID of the applicant users that will be retrieved. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_applicant_user_by_email**
> find_applicant_user_by_email(x_tenant, authorization, x_portal_token, email)

Check if the email is already in use.

Check if the email is already in use.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicantUsersApi()
x_tenant = '' # str | Tenant ID. (default to )
authorization = 'Basic ' # str | Basic Authentication (not required if x-portal-token is send). (default to Basic )
x_portal_token = '' # str | Login Token/Magic Link token (not required if Authorization is send). (default to )
email = 'email_example' # str | The email of the applicant users that will be checked.

try:
    # Check if the email is already in use.
    api_instance.find_applicant_user_by_email(x_tenant, authorization, x_portal_token, email)
except ApiException as e:
    print("Exception when calling ApplicantUsersApi->find_applicant_user_by_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**| Tenant ID. | [default to ]
 **authorization** | **str**| Basic Authentication (not required if x-portal-token is send). | [default to Basic ]
 **x_portal_token** | **str**| Login Token/Magic Link token (not required if Authorization is send). | [default to ]
 **email** | **str**| The email of the applicant users that will be checked. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_applicant_user_applications**
> get_applicant_user_applications(x_tenant, authorization, x_portal_token, x_portal=x_portal)

Request the applications of a applicant user from a tenant.

Request the applications of a applicant user from a tenant.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicantUsersApi()
x_tenant = '' # str | Tenant ID. (default to )
authorization = 'Basic ' # str | Basic Authentication (not required if x-portal-token is send). (default to Basic )
x_portal_token = '' # str | Login Token/Magic Link token (not required if Authorization is send). (default to )
x_portal = false # bool | Flag to determine that we are using web portal (optional) (default to false)

try:
    # Request the applications of a applicant user from a tenant.
    api_instance.get_applicant_user_applications(x_tenant, authorization, x_portal_token, x_portal=x_portal)
except ApiException as e:
    print("Exception when calling ApplicantUsersApi->get_applicant_user_applications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**| Tenant ID. | [default to ]
 **authorization** | **str**| Basic Authentication (not required if x-portal-token is send). | [default to Basic ]
 **x_portal_token** | **str**| Login Token/Magic Link token (not required if Authorization is send). | [default to ]
 **x_portal** | **bool**| Flag to determine that we are using web portal | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getapplicantuser**
> ApplicantUser getapplicantuser(x_tenant, authorization, x_portal_token, id)

Return a specific applicant user instance.

Return a specific applicant user instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicantUsersApi()
x_tenant = '' # str | Tenant ID. (default to )
authorization = 'Basic ' # str | Basic Authentication (not required if x-portal-token is send). (default to Basic )
x_portal_token = '' # str | Login Token/Magic Link token (not required if Authorization is send). (default to )
id = 'id_example' # str | The ID of the applicant users that will be retrieved.

try:
    # Return a specific applicant user instance.
    api_response = api_instance.getapplicantuser(x_tenant, authorization, x_portal_token, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicantUsersApi->getapplicantuser: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**| Tenant ID. | [default to ]
 **authorization** | **str**| Basic Authentication (not required if x-portal-token is send). | [default to Basic ]
 **x_portal_token** | **str**| Login Token/Magic Link token (not required if Authorization is send). | [default to ]
 **id** | **str**| The ID of the applicant users that will be retrieved. | 

### Return type

[**ApplicantUser**](ApplicantUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **new_applicant_user**
> new_applicant_user(x_tenant, body, jobsite, position=position)

Create a new applicant user

Create a new applicant user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicantUsersApi()
x_tenant = '' # str | Tenant ID. (default to )
body = swagger_client.ApplicantUser() # ApplicantUser | Data used to create a new applicant user
jobsite = swagger_client.null() #  | The ID of the jobsite to create applicant.
position = swagger_client.null() #  | The ID of the position to register applicant (not required for talent base). (optional)

try:
    # Create a new applicant user
    api_instance.new_applicant_user(x_tenant, body, jobsite, position=position)
except ApiException as e:
    print("Exception when calling ApplicantUsersApi->new_applicant_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**| Tenant ID. | [default to ]
 **body** | [**ApplicantUser**](ApplicantUser.md)| Data used to create a new applicant user | 
 **jobsite** | [****](.md)| The ID of the jobsite to create applicant. | 
 **position** | [****](.md)| The ID of the position to register applicant (not required for talent base). | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reject_applicantion_position**
> reject_applicantion_position(applicant, position)

Reject applied position for internal jobsite an determinated applicant.

Reject applied position for internal jobsite an determinated applicant.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicantUsersApi()
applicant = 'applicant_example' # str | The applicant id.
position = 'position_example' # str | The position id.

try:
    # Reject applied position for internal jobsite an determinated applicant.
    api_instance.reject_applicantion_position(applicant, position)
except ApiException as e:
    print("Exception when calling ApplicantUsersApi->reject_applicantion_position: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicant** | **str**| The applicant id. | 
 **position** | **str**| The position id. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resend_email_verification**
> resend_email_verification(x_tenant, id, jobsite)

Resend the email verification for applicantUser

Resend the email verification for applicantUser

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicantUsersApi()
x_tenant = '' # str | Tenant ID. (default to )
id = 'id_example' # str | The ID of the applicant users that will be resend email.
jobsite = swagger_client.null() #  | The ID of the jobsite.

try:
    # Resend the email verification for applicantUser
    api_instance.resend_email_verification(x_tenant, id, jobsite)
except ApiException as e:
    print("Exception when calling ApplicantUsersApi->resend_email_verification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**| Tenant ID. | [default to ]
 **id** | **str**| The ID of the applicant users that will be resend email. | 
 **jobsite** | [****](.md)| The ID of the jobsite. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_partial**
> save_partial(name, email, password)

Save the minimum data of ApplicantUser case his not exist in database

Save the minimum data of ApplicantUser case his not exist in database

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicantUsersApi()
name = swagger_client.null() #  | The applicantUser name
email = swagger_client.null() #  | The applicantUser email
password = swagger_client.null() #  | The applicantUser password

try:
    # Save the minimum data of ApplicantUser case his not exist in database
    api_instance.save_partial(name, email, password)
except ApiException as e:
    print("Exception when calling ApplicantUsersApi->save_partial: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | [****](.md)| The applicantUser name | 
 **email** | [****](.md)| The applicantUser email | 
 **password** | [****](.md)| The applicantUser password | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

