# swagger_client.UsersApi

All URIs are relative to *https://api.kenoby.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activateusers**](UsersApi.md#activateusers) | **PUT** /users/{usersId}/activate | Activate a specific user instance and set the roles.
[**createusers**](UsersApi.md#createusers) | **POST** /users | Create a new users
[**deactivateusers**](UsersApi.md#deactivateusers) | **PUT** /users/{usersId}/deactivate | Deactivate a specific user instance.
[**generatetoken**](UsersApi.md#generatetoken) | **GET** /users/:_id/generate-token | Generate a login token for the user.
[**getusermanagers**](UsersApi.md#getusermanagers) | **GET** /users/{usersId}/manager | Return a specific user manager instance.
[**getusers**](UsersApi.md#getusers) | **GET** /users/{usersId} | Return a specific user instance.
[**getuserss**](UsersApi.md#getuserss) | **GET** /users | List multiple users resources.
[**importusers**](UsersApi.md#importusers) | **POST** /users/import | Import a new users
[**internalusers**](UsersApi.md#internalusers) | **POST** /users/internal | Get user by token or authorization
[**passwordrecoveryusers**](UsersApi.md#passwordrecoveryusers) | **POST** /users/me/password-recovery | Recover the password. Just send user&#39;s e-mail.
[**updateusers**](UsersApi.md#updateusers) | **PUT** /users/{usersId} | Update a specific user instance.


# **activateusers**
> Users activateusers(authorization, x_tenant, x_version, users_id, body)

Activate a specific user instance and set the roles.

Activate a specific user instance and set the roles.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
users_id = 'users_id_example' # str | The ID of the users that will be updated.
body = swagger_client.Users() # Users | Data used to update users

try:
    # Activate a specific user instance and set the roles.
    api_response = api_instance.activateusers(authorization, x_tenant, x_version, users_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->activateusers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **users_id** | **str**| The ID of the users that will be updated. | 
 **body** | [**Users**](Users.md)| Data used to update users | 

### Return type

[**Users**](Users.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **createusers**
> createusers(authorization, x_tenant, x_version, body)

Create a new users

Create a new users

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
body = swagger_client.Users() # Users | Data used to create a new users

try:
    # Create a new users
    api_instance.createusers(authorization, x_tenant, x_version, body)
except ApiException as e:
    print("Exception when calling UsersApi->createusers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **body** | [**Users**](Users.md)| Data used to create a new users | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deactivateusers**
> Users deactivateusers(authorization, x_tenant, x_version, users_id)

Deactivate a specific user instance.

Deactivate a specific user instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
users_id = 'users_id_example' # str | The ID of the users that will be updated.

try:
    # Deactivate a specific user instance.
    api_response = api_instance.deactivateusers(authorization, x_tenant, x_version, users_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->deactivateusers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **users_id** | **str**| The ID of the users that will be updated. | 

### Return type

[**Users**](Users.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generatetoken**
> generatetoken(authorization, x_tenant, x_version)

Generate a login token for the user.

Generate a login token for the user.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)

try:
    # Generate a login token for the user.
    api_instance.generatetoken(authorization, x_tenant, x_version)
except ApiException as e:
    print("Exception when calling UsersApi->generatetoken: %s\n" % e)
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

# **getusermanagers**
> Users getusermanagers(authorization, x_tenant, x_version, users_id)

Return a specific user manager instance.

Return a specific user manager instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
users_id = 'users_id_example' # str | The ID of the users that will be retrieved.

try:
    # Return a specific user manager instance.
    api_response = api_instance.getusermanagers(authorization, x_tenant, x_version, users_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->getusermanagers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **users_id** | **str**| The ID of the users that will be retrieved. | 

### Return type

[**Users**](Users.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getusers**
> Users getusers(authorization, x_tenant, x_version, users_id)

Return a specific user instance.

Return a specific user instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
users_id = 'users_id_example' # str | The ID of the users that will be retrieved.

try:
    # Return a specific user instance.
    api_response = api_instance.getusers(authorization, x_tenant, x_version, users_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->getusers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **users_id** | **str**| The ID of the users that will be retrieved. | 

### Return type

[**Users**](Users.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getuserss**
> UsersList getuserss(authorization, x_tenant, x_version, page=page, page_size=page_size, order_by=order_by, select_0=select_0, select_1=select_1, filter_by_name_like=filter_by_name_like, filter_by_email_like=filter_by_email_like, filter_by_created_at_from=filter_by_created_at_from, filter_by_created_at_to=filter_by_created_at_to, filter_by_or_0_name_like=filter_by_or_0_name_like, filter_by_or_1_email_like=filter_by_or_1_email_like, filter_by_custom_fields_0_field=filter_by_custom_fields_0_field, filter_by_custom_fields_0_value_from=filter_by_custom_fields_0_value_from, count_0_filter_by_or_0_name_like=count_0_filter_by_or_0_name_like, count_0_filter_by_or_1_email_like=count_0_filter_by_or_1_email_like)

List multiple users resources.

This operation allows you to list and search for users resources provided query arguments.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
page = 1 # int | The page of records. Used for pagination. (optional) (default to 1)
page_size = 20 # int | How many records to limit the output. (optional) (default to 20)
order_by = 'name' # str | Which fields to sort the records on. You can use minus sign to have a reverse order. Ex.: orderBy=-name (optional) (default to name)
select_0 = '' # str | Select which fields will be returned by the query. (optional) (default to )
select_1 = '' # str | Select which fields will be returned by the query. One select for each field (optional) (default to )
filter_by_name_like = '' # str | Filter the results. This is just a sample. You can use a better tool like postman to try other filters. Ex: filterBy[fieldA]=some value&filterBy[fieldB][fieldDfromC]=other value (optional) (default to )
filter_by_email_like = '' # str | Filter the results. This is just a sample. You can use a better tool like postman to try other filters. Ex: filterBy[fieldA]=some value&filterBy[fieldB][fieldDfromC]=other value (optional) (default to )
filter_by_created_at_from = '2015-01-01T02:00:00.000Z' # str | Filter the results greatter than a given date (optional) (default to 2015-01-01T02:00:00.000Z)
filter_by_created_at_to = '2017-01-01T02:00:00.000Z' # str | Filter the results lower than a given date (optional) (default to 2017-01-01T02:00:00.000Z)
filter_by_or_0_name_like = '' # str | Filter the results associating more than one parameter. This is just a sample using 'or' sintax. (optional) (default to )
filter_by_or_1_email_like = '' # str | Filter the results associating more than one parameter. This is just a sample using 'or' sintax. (optional) (default to )
filter_by_custom_fields_0_field = '' # str | Filter the results associating more than one parameter. This is just a sample using 'and' sintax. (optional) (default to )
filter_by_custom_fields_0_value_from = '' # str | Filter the results associating more than one parameter. This is just a sample using 'and' sintax. (optional) (default to )
count_0_filter_by_or_0_name_like = '' # str | Return the total records from a filterBy query. Ex.: count[0][filterBy][name][like]=Ricardo (optional) (default to )
count_0_filter_by_or_1_email_like = '' # str | Return the total records from createdFrom a specific date. Ex.: count[1][filterBy][createdAt][from]=2015-01-01T02:00:00.000Z (optional) (default to )

try:
    # List multiple users resources.
    api_response = api_instance.getuserss(authorization, x_tenant, x_version, page=page, page_size=page_size, order_by=order_by, select_0=select_0, select_1=select_1, filter_by_name_like=filter_by_name_like, filter_by_email_like=filter_by_email_like, filter_by_created_at_from=filter_by_created_at_from, filter_by_created_at_to=filter_by_created_at_to, filter_by_or_0_name_like=filter_by_or_0_name_like, filter_by_or_1_email_like=filter_by_or_1_email_like, filter_by_custom_fields_0_field=filter_by_custom_fields_0_field, filter_by_custom_fields_0_value_from=filter_by_custom_fields_0_value_from, count_0_filter_by_or_0_name_like=count_0_filter_by_or_0_name_like, count_0_filter_by_or_1_email_like=count_0_filter_by_or_1_email_like)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->getuserss: %s\n" % e)
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
 **filter_by_email_like** | **str**| Filter the results. This is just a sample. You can use a better tool like postman to try other filters. Ex: filterBy[fieldA]&#x3D;some value&amp;filterBy[fieldB][fieldDfromC]&#x3D;other value | [optional] [default to ]
 **filter_by_created_at_from** | **str**| Filter the results greatter than a given date | [optional] [default to 2015-01-01T02:00:00.000Z]
 **filter_by_created_at_to** | **str**| Filter the results lower than a given date | [optional] [default to 2017-01-01T02:00:00.000Z]
 **filter_by_or_0_name_like** | **str**| Filter the results associating more than one parameter. This is just a sample using &#39;or&#39; sintax. | [optional] [default to ]
 **filter_by_or_1_email_like** | **str**| Filter the results associating more than one parameter. This is just a sample using &#39;or&#39; sintax. | [optional] [default to ]
 **filter_by_custom_fields_0_field** | **str**| Filter the results associating more than one parameter. This is just a sample using &#39;and&#39; sintax. | [optional] [default to ]
 **filter_by_custom_fields_0_value_from** | **str**| Filter the results associating more than one parameter. This is just a sample using &#39;and&#39; sintax. | [optional] [default to ]
 **count_0_filter_by_or_0_name_like** | **str**| Return the total records from a filterBy query. Ex.: count[0][filterBy][name][like]&#x3D;Ricardo | [optional] [default to ]
 **count_0_filter_by_or_1_email_like** | **str**| Return the total records from createdFrom a specific date. Ex.: count[1][filterBy][createdAt][from]&#x3D;2015-01-01T02:00:00.000Z | [optional] [default to ]

### Return type

[**UsersList**](UsersList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **importusers**
> importusers(authorization, x_tenant, x_version, body)

Import a new users

Import a new users

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
body = swagger_client.Users() # Users | Data used to import a new users

try:
    # Import a new users
    api_instance.importusers(authorization, x_tenant, x_version, body)
except ApiException as e:
    print("Exception when calling UsersApi->importusers: %s\n" % e)
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

# **internalusers**
> internalusers(authorization=authorization, token=token)

Get user by token or authorization

Get user by token or authorization

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
authorization = 'authorization_example' # str | The authorization basic string. (optional)
token = 'token_example' # str | The generated token for login. (optional)

try:
    # Get user by token or authorization
    api_instance.internalusers(authorization=authorization, token=token)
except ApiException as e:
    print("Exception when calling UsersApi->internalusers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| The authorization basic string. | [optional] 
 **token** | **str**| The generated token for login. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **passwordrecoveryusers**
> Users passwordrecoveryusers(authorization, x_tenant, x_version, body)

Recover the password. Just send user's e-mail.

Recover the password. Just send user's e-mail.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
body = swagger_client.Users() # Users | Data used to update users

try:
    # Recover the password. Just send user's e-mail.
    api_response = api_instance.passwordrecoveryusers(authorization, x_tenant, x_version, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->passwordrecoveryusers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **body** | [**Users**](Users.md)| Data used to update users | 

### Return type

[**Users**](Users.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updateusers**
> Users updateusers(authorization, x_tenant, x_version, users_id, body)

Update a specific user instance.

Update a specific user instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
users_id = 'users_id_example' # str | The ID of the users that will be updated.
body = swagger_client.Users() # Users | Data used to update users

try:
    # Update a specific user instance.
    api_response = api_instance.updateusers(authorization, x_tenant, x_version, users_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->updateusers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **users_id** | **str**| The ID of the users that will be updated. | 
 **body** | [**Users**](Users.md)| Data used to update users | 

### Return type

[**Users**](Users.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

