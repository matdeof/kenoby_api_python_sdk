# swagger_client.MentionsApi

All URIs are relative to *https://api.kenoby.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deletefavoritementions**](MentionsApi.md#deletefavoritementions) | **DELETE** /mentions/{mentionId}/favorite | remove from favorite mention.
[**deletementions**](MentionsApi.md#deletementions) | **DELETE** /mentions/{mentionId} | delete mention.
[**getmentions**](MentionsApi.md#getmentions) | **GET** /mentions | List multiple mentions resources.
[**getunderedmentions**](MentionsApi.md#getunderedmentions) | **GET** /mentions/unread | List multiple mentions unreads.
[**postmentions**](MentionsApi.md#postmentions) | **POST** /mentions | Save mention.
[**putfavoritementions**](MentionsApi.md#putfavoritementions) | **PUT** /mentions/{mentionId}/favorite | add to favorite mention.
[**putreadmentions**](MentionsApi.md#putreadmentions) | **PUT** /mentions/read | read all mentions.


# **deletefavoritementions**
> MappingsList deletefavoritementions(authorization, x_tenant, x_version, mention_id)

remove from favorite mention.

This operation remove favorited mention.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MentionsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
mention_id = 'mention_id_example' # str | The ID of the mentions that will be retrieved.

try:
    # remove from favorite mention.
    api_response = api_instance.deletefavoritementions(authorization, x_tenant, x_version, mention_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MentionsApi->deletefavoritementions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **mention_id** | **str**| The ID of the mentions that will be retrieved. | 

### Return type

[**MappingsList**](MappingsList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deletementions**
> MappingsList deletementions(authorization, x_tenant, x_version, mention_id)

delete mention.

This operation delete one mention.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MentionsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
mention_id = 'mention_id_example' # str | The ID of the mentions that will be retrieved.

try:
    # delete mention.
    api_response = api_instance.deletementions(authorization, x_tenant, x_version, mention_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MentionsApi->deletementions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **mention_id** | **str**| The ID of the mentions that will be retrieved. | 

### Return type

[**MappingsList**](MappingsList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getmentions**
> MappingsList getmentions(authorization, x_tenant, x_version, filter_by=filter_by)

List multiple mentions resources.

This operation allows you to list and search for mentions resources provided query arguments.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MentionsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
filter_by = 'filter_by_example' # str | The API version. (optional)

try:
    # List multiple mentions resources.
    api_response = api_instance.getmentions(authorization, x_tenant, x_version, filter_by=filter_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MentionsApi->getmentions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **filter_by** | **str**| The API version. | [optional] 

### Return type

[**MappingsList**](MappingsList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getunderedmentions**
> MappingsList getunderedmentions(authorization, x_tenant, x_version)

List multiple mentions unreads.

This operation allows you to list and search for mentions unread resources provided query arguments.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MentionsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)

try:
    # List multiple mentions unreads.
    api_response = api_instance.getunderedmentions(authorization, x_tenant, x_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MentionsApi->getunderedmentions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]

### Return type

[**MappingsList**](MappingsList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **postmentions**
> MappingsList postmentions(authorization, x_tenant, x_version, body)

Save mention.

This operation save and send mention.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MentionsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
body = swagger_client.Mentions() # Mentions | Data used to create a new mention

try:
    # Save mention.
    api_response = api_instance.postmentions(authorization, x_tenant, x_version, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MentionsApi->postmentions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **body** | [**Mentions**](Mentions.md)| Data used to create a new mention | 

### Return type

[**MappingsList**](MappingsList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **putfavoritementions**
> MappingsList putfavoritementions(authorization, x_tenant, x_version, mention_id)

add to favorite mention.

This operation add to favorite mention.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MentionsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
mention_id = 'mention_id_example' # str | The ID of the mentions that will be retrieved.

try:
    # add to favorite mention.
    api_response = api_instance.putfavoritementions(authorization, x_tenant, x_version, mention_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MentionsApi->putfavoritementions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **mention_id** | **str**| The ID of the mentions that will be retrieved. | 

### Return type

[**MappingsList**](MappingsList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **putreadmentions**
> MappingsList putreadmentions(authorization, x_tenant, x_version)

read all mentions.

This operation read all mention.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MentionsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)

try:
    # read all mentions.
    api_response = api_instance.putreadmentions(authorization, x_tenant, x_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MentionsApi->putreadmentions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]

### Return type

[**MappingsList**](MappingsList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

