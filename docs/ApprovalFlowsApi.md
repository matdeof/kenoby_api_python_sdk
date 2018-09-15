# swagger_client.ApprovalFlowsApi

All URIs are relative to *https://api.kenoby.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_approval_flow**](ApprovalFlowsApi.md#create_approval_flow) | **POST** /approval-flows | Create a new approval flow
[**delete_approval_flow**](ApprovalFlowsApi.md#delete_approval_flow) | **DELETE** /approval-flows/{approvalFlowId} | Delete a specific approval flow instance
[**get_approval_flow**](ApprovalFlowsApi.md#get_approval_flow) | **GET** /approval-flows/{approvalFlowId} | Return a specific approval flow instance.
[**get_approval_flows**](ApprovalFlowsApi.md#get_approval_flows) | **GET** /approval-flows | List multiple approval flow resources.
[**update_approval_flow**](ApprovalFlowsApi.md#update_approval_flow) | **PUT** /approval-flows/{approvalFlowId} | Update a specific approval flow instance.


# **create_approval_flow**
> create_approval_flow(authorization, x_tenant, x_version, body)

Create a new approval flow

Create a new approval flow

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApprovalFlowsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
body = swagger_client.ApprovalFlow() # ApprovalFlow | Data used to create a new approval flow

try:
    # Create a new approval flow
    api_instance.create_approval_flow(authorization, x_tenant, x_version, body)
except ApiException as e:
    print("Exception when calling ApprovalFlowsApi->create_approval_flow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **body** | [**ApprovalFlow**](ApprovalFlow.md)| Data used to create a new approval flow | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_approval_flow**
> delete_approval_flow(authorization, x_tenant, x_version, approval_flow_id)

Delete a specific approval flow instance

Delete a specific approval flow instance

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApprovalFlowsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
approval_flow_id = 'approval_flow_id_example' # str | The ID of the approval flow that will be deleted.

try:
    # Delete a specific approval flow instance
    api_instance.delete_approval_flow(authorization, x_tenant, x_version, approval_flow_id)
except ApiException as e:
    print("Exception when calling ApprovalFlowsApi->delete_approval_flow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **approval_flow_id** | **str**| The ID of the approval flow that will be deleted. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_approval_flow**
> ApprovalFlow get_approval_flow(authorization, x_tenant, x_version, approval_flow_id)

Return a specific approval flow instance.

Return a specific approval flow instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApprovalFlowsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
approval_flow_id = 'approval_flow_id_example' # str | The ID of the approval flow that will be retrieved.

try:
    # Return a specific approval flow instance.
    api_response = api_instance.get_approval_flow(authorization, x_tenant, x_version, approval_flow_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApprovalFlowsApi->get_approval_flow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **approval_flow_id** | **str**| The ID of the approval flow that will be retrieved. | 

### Return type

[**ApprovalFlow**](ApprovalFlow.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_approval_flows**
> ApprovalFlowsList get_approval_flows(authorization, x_tenant, x_version, page=page, page_size=page_size, order_by=order_by, select_0=select_0, select_1=select_1, filter_by_name_like=filter_by_name_like, count_0_filter_by_name_like=count_0_filter_by_name_like, count_1_filter_by_created_at_from=count_1_filter_by_created_at_from, search_by=search_by)

List multiple approval flow resources.

This operation allows you to list and search for approval flow resources provided query arguments.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApprovalFlowsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
page = 1 # int | The page of records. Used for pagination. (optional) (default to 1)
page_size = 20 # int | How many records to limit the output. (optional) (default to 20)
order_by = 'name' # str | Which fields to sort the records on. You can use minus sign to have a reverse order. Ex.: orderBy=-name (optional) (default to name)
select_0 = '' # str | Select which fields will be returned by the query. (optional) (default to )
select_1 = '' # str | Select which fields will be returned by the query. One select for each field (optional) (default to )
filter_by_name_like = '' # str | Filter the results. This is just a sample. You can use a better tool like postman to try other filters. Ex: filterBy[fieldA]=some value&filterBy[fieldB][fieldDfromC]=other value (optional) (default to )
count_0_filter_by_name_like = '' # str | Return the total records from a filterBy query. Ex.: count[0][filterBy][name][like]=My Position Template (optional) (default to )
count_1_filter_by_created_at_from = '' # str | Return the total records from createdFrom a specific date. Ex.: count[1][filterBy][createdAt][from]=2015-01-01T02:00:00.000Z (optional) (default to )
search_by = '' # str | Make a text search on main fields. (optional) (default to )

try:
    # List multiple approval flow resources.
    api_response = api_instance.get_approval_flows(authorization, x_tenant, x_version, page=page, page_size=page_size, order_by=order_by, select_0=select_0, select_1=select_1, filter_by_name_like=filter_by_name_like, count_0_filter_by_name_like=count_0_filter_by_name_like, count_1_filter_by_created_at_from=count_1_filter_by_created_at_from, search_by=search_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApprovalFlowsApi->get_approval_flows: %s\n" % e)
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
 **count_0_filter_by_name_like** | **str**| Return the total records from a filterBy query. Ex.: count[0][filterBy][name][like]&#x3D;My Position Template | [optional] [default to ]
 **count_1_filter_by_created_at_from** | **str**| Return the total records from createdFrom a specific date. Ex.: count[1][filterBy][createdAt][from]&#x3D;2015-01-01T02:00:00.000Z | [optional] [default to ]
 **search_by** | **str**| Make a text search on main fields. | [optional] [default to ]

### Return type

[**ApprovalFlowsList**](ApprovalFlowsList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_approval_flow**
> ApprovalFlow update_approval_flow(authorization, x_tenant, x_version, approval_flow_id, body)

Update a specific approval flow instance.

Update a specific approval flow instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApprovalFlowsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
approval_flow_id = 'approval_flow_id_example' # str | The ID of the approval flow that will be updated.
body = swagger_client.ApprovalFlow() # ApprovalFlow | Data used to update approval flow

try:
    # Update a specific approval flow instance.
    api_response = api_instance.update_approval_flow(authorization, x_tenant, x_version, approval_flow_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApprovalFlowsApi->update_approval_flow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **approval_flow_id** | **str**| The ID of the approval flow that will be updated. | 
 **body** | [**ApprovalFlow**](ApprovalFlow.md)| Data used to update approval flow | 

### Return type

[**ApprovalFlow**](ApprovalFlow.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

