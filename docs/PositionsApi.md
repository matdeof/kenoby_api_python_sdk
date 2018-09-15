# swagger_client.PositionsApi

All URIs are relative to *https://api.kenoby.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancelpositions**](PositionsApi.md#cancelpositions) | **PUT** /positions/{positionsId}/cancel | Cancel a specific position instance.
[**checkpositionstage**](PositionsApi.md#checkpositionstage) | **GET** /positions/{positionsId}/has-candidates | Check if stage in a position has candidates.
[**closepositions**](PositionsApi.md#closepositions) | **PUT** /positions/{positionsId}/close | Close a specific position instance.
[**createpositions**](PositionsApi.md#createpositions) | **POST** /positions | Create a new positions
[**delete**](PositionsApi.md#delete) | **DELETE** /positions/{positionsId} | Delete a specific position instance.
[**exportcandidatesposition**](PositionsApi.md#exportcandidatesposition) | **GET** /positions/{positionsId}/export-candidates | Generate CSV that contains candidate information for a specific position
[**generatetokenposition**](PositionsApi.md#generatetokenposition) | **PUT** /positions/{positionsId}/generate-token-internal | Generate internal token for a Position.
[**getpositiongeolocationapplicants**](PositionsApi.md#getpositiongeolocationapplicants) | **GET** /positions/{positionsId}/status-geolocation | Returns the status of geo located applicants for the position.
[**getpositionhasparser**](PositionsApi.md#getpositionhasparser) | **GET** /positions/{positionsId}/has-parser | Returns if parser is available for a specific position
[**getpositionhistory**](PositionsApi.md#getpositionhistory) | **GET** /positions/{positionsId}/history | Returns the position history for a specific position
[**getpositions**](PositionsApi.md#getpositions) | **GET** /positions/{positionsId} | Return a specific position instance.
[**getpositionsreferral**](PositionsApi.md#getpositionsreferral) | **GET** /positions | List multiple positions resources for referral.
[**getpositionwebportal**](PositionsApi.md#getpositionwebportal) | **GET** /positions/{positionsId}/portal | Return a specific position instance for web portal.
[**startpositiongeolocationapplicants**](PositionsApi.md#startpositiongeolocationapplicants) | **GET** /positions/{positionsId}/start-geolocation | Starts indexing geo located applicants for the position.
[**startpositions**](PositionsApi.md#startpositions) | **PUT** /positions/{positionsId}/start | Start/unfreeze a specific position instance.
[**stoppositions**](PositionsApi.md#stoppositions) | **PUT** /positions/{positionsId}/stop | Stop/freeze a specific position instance.
[**updatepositionfeedback**](PositionsApi.md#updatepositionfeedback) | **PUT** /positions/{positionsId}/update-feedback | Update a email template feedback.
[**updatepositiongeolocation**](PositionsApi.md#updatepositiongeolocation) | **PUT** /positions/{positionsId}/toggle-geolocation | Update a specific position geolocation feature.
[**updatepositions**](PositionsApi.md#updatepositions) | **PUT** /positions/{positionsId} | Update a specific position instance.
[**updatepositionsaccess**](PositionsApi.md#updatepositionsaccess) | **PUT** /positions/{positionsId}/update-access | Update a specific position access instance.


# **cancelpositions**
> Positions cancelpositions(authorization, x_tenant, x_version, positions_id)

Cancel a specific position instance.

Cancel a specific position instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PositionsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
positions_id = 'positions_id_example' # str | The ID of the positions that will be updated.

try:
    # Cancel a specific position instance.
    api_response = api_instance.cancelpositions(authorization, x_tenant, x_version, positions_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PositionsApi->cancelpositions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **positions_id** | **str**| The ID of the positions that will be updated. | 

### Return type

[**Positions**](Positions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checkpositionstage**
> Positions checkpositionstage(authorization, x_tenant, x_version, positions_id, body=body)

Check if stage in a position has candidates.

Check if stage in a position has candidates.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PositionsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
positions_id = 'positions_id_example' # str | The ID of the positions that will be deleted.
body = swagger_client.Positions() # Positions | Data used to check the stage in position (optional)

try:
    # Check if stage in a position has candidates.
    api_response = api_instance.checkpositionstage(authorization, x_tenant, x_version, positions_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PositionsApi->checkpositionstage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **positions_id** | **str**| The ID of the positions that will be deleted. | 
 **body** | [**Positions**](Positions.md)| Data used to check the stage in position | [optional] 

### Return type

[**Positions**](Positions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **closepositions**
> Positions closepositions(authorization, x_tenant, x_version, positions_id)

Close a specific position instance.

Close a specific position instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PositionsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
positions_id = 'positions_id_example' # str | The ID of the positions that will be updated.

try:
    # Close a specific position instance.
    api_response = api_instance.closepositions(authorization, x_tenant, x_version, positions_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PositionsApi->closepositions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **positions_id** | **str**| The ID of the positions that will be updated. | 

### Return type

[**Positions**](Positions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **createpositions**
> createpositions(authorization, x_tenant, x_version, body)

Create a new positions

Create a new positions

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PositionsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
body = swagger_client.Positions() # Positions | Data used to create a new positions

try:
    # Create a new positions
    api_instance.createpositions(authorization, x_tenant, x_version, body)
except ApiException as e:
    print("Exception when calling PositionsApi->createpositions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **body** | [**Positions**](Positions.md)| Data used to create a new positions | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> delete(authorization, x_tenant, x_version, positions_id, body=body)

Delete a specific position instance.

Delete a specific position instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PositionsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
positions_id = 'positions_id_example' # str | The ID of the positions that will be deleted.
body = swagger_client.Positions() # Positions | Data used to delete positions (optional)

try:
    # Delete a specific position instance.
    api_instance.delete(authorization, x_tenant, x_version, positions_id, body=body)
except ApiException as e:
    print("Exception when calling PositionsApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **positions_id** | **str**| The ID of the positions that will be deleted. | 
 **body** | [**Positions**](Positions.md)| Data used to delete positions | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exportcandidatesposition**
> Positions exportcandidatesposition(authorization, x_tenant, x_version, positions_id)

Generate CSV that contains candidate information for a specific position

Generate CSV that contains candidate information for a specific position

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PositionsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
positions_id = 'positions_id_example' # str | The ID of the positions that the token will be generated.

try:
    # Generate CSV that contains candidate information for a specific position
    api_response = api_instance.exportcandidatesposition(authorization, x_tenant, x_version, positions_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PositionsApi->exportcandidatesposition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **positions_id** | **str**| The ID of the positions that the token will be generated. | 

### Return type

[**Positions**](Positions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generatetokenposition**
> Positions generatetokenposition(authorization, x_tenant, x_version, positions_id)

Generate internal token for a Position.

Generates a token to be used in an internal position (not public)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PositionsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
positions_id = 'positions_id_example' # str | The ID of the positions that the token will be generated.

try:
    # Generate internal token for a Position.
    api_response = api_instance.generatetokenposition(authorization, x_tenant, x_version, positions_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PositionsApi->generatetokenposition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **positions_id** | **str**| The ID of the positions that the token will be generated. | 

### Return type

[**Positions**](Positions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getpositiongeolocationapplicants**
> Positions getpositiongeolocationapplicants(authorization, x_tenant, x_version, positions_id)

Returns the status of geo located applicants for the position.

Returns the status of geo located applicants for the position.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PositionsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
positions_id = 'positions_id_example' # str | The ID of the positions that will be updated.

try:
    # Returns the status of geo located applicants for the position.
    api_response = api_instance.getpositiongeolocationapplicants(authorization, x_tenant, x_version, positions_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PositionsApi->getpositiongeolocationapplicants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **positions_id** | **str**| The ID of the positions that will be updated. | 

### Return type

[**Positions**](Positions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getpositionhasparser**
> getpositionhasparser(authorization, x_tenant, x_version, positions_id)

Returns if parser is available for a specific position

Returns if parser is available for a specific position

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PositionsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
positions_id = 'positions_id_example' # str | The ID of the positions that the token will be generated.

try:
    # Returns if parser is available for a specific position
    api_instance.getpositionhasparser(authorization, x_tenant, x_version, positions_id)
except ApiException as e:
    print("Exception when calling PositionsApi->getpositionhasparser: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **positions_id** | **str**| The ID of the positions that the token will be generated. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getpositionhistory**
> Positions getpositionhistory(authorization, x_tenant, x_version, positions_id)

Returns the position history for a specific position

Returns the position history for a specific position

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PositionsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
positions_id = 'positions_id_example' # str | The ID of the positions that the token will be generated.

try:
    # Returns the position history for a specific position
    api_response = api_instance.getpositionhistory(authorization, x_tenant, x_version, positions_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PositionsApi->getpositionhistory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **positions_id** | **str**| The ID of the positions that the token will be generated. | 

### Return type

[**Positions**](Positions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getpositions**
> Positions getpositions(authorization, x_tenant, x_version, positions_id)

Return a specific position instance.

Return a specific position instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PositionsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
positions_id = 'positions_id_example' # str | The ID of the positions that will be retrieved.

try:
    # Return a specific position instance.
    api_response = api_instance.getpositions(authorization, x_tenant, x_version, positions_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PositionsApi->getpositions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **positions_id** | **str**| The ID of the positions that will be retrieved. | 

### Return type

[**Positions**](Positions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getpositionsreferral**
> PositionsList getpositionsreferral(authorization, x_tenant, x_version)

List multiple positions resources for referral.

This operation allows you to list for positions resources for referral.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PositionsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)

try:
    # List multiple positions resources for referral.
    api_response = api_instance.getpositionsreferral(authorization, x_tenant, x_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PositionsApi->getpositionsreferral: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]

### Return type

[**PositionsList**](PositionsList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getpositionwebportal**
> Positions getpositionwebportal(x_tenant, authorization, x_portal_token, position_id, x_portal=x_portal)

Return a specific position instance for web portal.

Return a specific position instance web portal.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PositionsApi()
x_tenant = '' # str | The tenant id. (default to )
authorization = 'Basic ' # str | Basic Authentication (not required if x-portal-token is send). (default to Basic )
x_portal_token = '' # str | Login Token/Magic Link token (not required if Authorization is send). (default to )
position_id = 'position_id_example' # str | The ID of the position that will be retrieved.
x_portal = false # bool | Flag to determine that we are using web portal (optional) (default to false)

try:
    # Return a specific position instance for web portal.
    api_response = api_instance.getpositionwebportal(x_tenant, authorization, x_portal_token, position_id, x_portal=x_portal)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PositionsApi->getpositionwebportal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**| The tenant id. | [default to ]
 **authorization** | **str**| Basic Authentication (not required if x-portal-token is send). | [default to Basic ]
 **x_portal_token** | **str**| Login Token/Magic Link token (not required if Authorization is send). | [default to ]
 **position_id** | **str**| The ID of the position that will be retrieved. | 
 **x_portal** | **bool**| Flag to determine that we are using web portal | [optional] [default to false]

### Return type

[**Positions**](Positions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **startpositiongeolocationapplicants**
> Positions startpositiongeolocationapplicants(authorization, x_tenant, x_version, positions_id)

Starts indexing geo located applicants for the position.

Starts indexing geo located applicants for the position.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PositionsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
positions_id = 'positions_id_example' # str | The ID of the positions that will be updated.

try:
    # Starts indexing geo located applicants for the position.
    api_response = api_instance.startpositiongeolocationapplicants(authorization, x_tenant, x_version, positions_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PositionsApi->startpositiongeolocationapplicants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **positions_id** | **str**| The ID of the positions that will be updated. | 

### Return type

[**Positions**](Positions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **startpositions**
> Positions startpositions(authorization, x_tenant, x_version, positions_id)

Start/unfreeze a specific position instance.

Start/unfreeze a specific position instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PositionsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
positions_id = 'positions_id_example' # str | The ID of the positions that will be updated.

try:
    # Start/unfreeze a specific position instance.
    api_response = api_instance.startpositions(authorization, x_tenant, x_version, positions_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PositionsApi->startpositions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **positions_id** | **str**| The ID of the positions that will be updated. | 

### Return type

[**Positions**](Positions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stoppositions**
> Positions stoppositions(authorization, x_tenant, x_version, positions_id)

Stop/freeze a specific position instance.

Stop/freeze a specific position instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PositionsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
positions_id = 'positions_id_example' # str | The ID of the positions that will be updated.

try:
    # Stop/freeze a specific position instance.
    api_response = api_instance.stoppositions(authorization, x_tenant, x_version, positions_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PositionsApi->stoppositions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **positions_id** | **str**| The ID of the positions that will be updated. | 

### Return type

[**Positions**](Positions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updatepositionfeedback**
> Positions updatepositionfeedback(authorization, x_tenant, x_version, positions_id)

Update a email template feedback.

Update a email template feedback.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PositionsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
positions_id = 'positions_id_example' # str | The ID of the positions that will be updated.

try:
    # Update a email template feedback.
    api_response = api_instance.updatepositionfeedback(authorization, x_tenant, x_version, positions_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PositionsApi->updatepositionfeedback: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **positions_id** | **str**| The ID of the positions that will be updated. | 

### Return type

[**Positions**](Positions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updatepositiongeolocation**
> Positions updatepositiongeolocation(authorization, x_tenant, x_version, positions_id)

Update a specific position geolocation feature.

Update a specific position geolocation feature.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PositionsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
positions_id = 'positions_id_example' # str | The ID of the positions that will be updated.

try:
    # Update a specific position geolocation feature.
    api_response = api_instance.updatepositiongeolocation(authorization, x_tenant, x_version, positions_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PositionsApi->updatepositiongeolocation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **positions_id** | **str**| The ID of the positions that will be updated. | 

### Return type

[**Positions**](Positions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updatepositions**
> Positions updatepositions(authorization, x_tenant, x_version, positions_id, body)

Update a specific position instance.

Update a specific position instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PositionsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
positions_id = 'positions_id_example' # str | The ID of the positions that will be updated.
body = swagger_client.Positions() # Positions | Data used to update positions

try:
    # Update a specific position instance.
    api_response = api_instance.updatepositions(authorization, x_tenant, x_version, positions_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PositionsApi->updatepositions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **positions_id** | **str**| The ID of the positions that will be updated. | 
 **body** | [**Positions**](Positions.md)| Data used to update positions | 

### Return type

[**Positions**](Positions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updatepositionsaccess**
> Positions updatepositionsaccess(authorization, x_tenant, x_version, positions_id, body)

Update a specific position access instance.

Update a specific position access instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PositionsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
positions_id = 'positions_id_example' # str | The ID of the positions that will be updated.
body = swagger_client.Positions() # Positions | Data used to update positions

try:
    # Update a specific position access instance.
    api_response = api_instance.updatepositionsaccess(authorization, x_tenant, x_version, positions_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PositionsApi->updatepositionsaccess: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **positions_id** | **str**| The ID of the positions that will be updated. | 
 **body** | [**Positions**](Positions.md)| Data used to update positions | 

### Return type

[**Positions**](Positions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

