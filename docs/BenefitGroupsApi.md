# swagger_client.BenefitGroupsApi

All URIs are relative to *https://api.kenoby.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createbenefit_groups**](BenefitGroupsApi.md#createbenefit_groups) | **POST** /benefit-groups | Create a new benefit-groups
[**deletebenefit_groups**](BenefitGroupsApi.md#deletebenefit_groups) | **DELETE** /benefit-groups/{benefit-groupsId} | Delete a specific benefitGroup instance.
[**getbenefit_groups**](BenefitGroupsApi.md#getbenefit_groups) | **GET** /benefit-groups/{benefit-groupsId} | Return a specific benefit-group instance.
[**getbenefit_groupss**](BenefitGroupsApi.md#getbenefit_groupss) | **GET** /benefit-groups | List multiple benefit-groups resources.
[**updatebenefit_groups**](BenefitGroupsApi.md#updatebenefit_groups) | **PUT** /benefit-groups/{benefitGroupsId} | Update a specific benefit-group instance.


# **createbenefit_groups**
> createbenefit_groups(authorization, x_tenant, x_version, body)

Create a new benefit-groups

Create a new benefit-groups

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BenefitGroupsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
body = swagger_client.BenefitGroups() # BenefitGroups | Data used to create a new benefit-groups

try:
    # Create a new benefit-groups
    api_instance.createbenefit_groups(authorization, x_tenant, x_version, body)
except ApiException as e:
    print("Exception when calling BenefitGroupsApi->createbenefit_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **body** | [**BenefitGroups**](BenefitGroups.md)| Data used to create a new benefit-groups | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deletebenefit_groups**
> BenefitGroups deletebenefit_groups(authorization, x_tenant, x_version, benefit_groups_id, body)

Delete a specific benefitGroup instance.

Delete a specific benefitGroup instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BenefitGroupsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
benefit_groups_id = 'benefit_groups_id_example' # str | The ID of the benefit-groups that will be updated.
body = swagger_client.BenefitGroups() # BenefitGroups | Data used to delete benefitGroup

try:
    # Delete a specific benefitGroup instance.
    api_response = api_instance.deletebenefit_groups(authorization, x_tenant, x_version, benefit_groups_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BenefitGroupsApi->deletebenefit_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **benefit_groups_id** | **str**| The ID of the benefit-groups that will be updated. | 
 **body** | [**BenefitGroups**](BenefitGroups.md)| Data used to delete benefitGroup | 

### Return type

[**BenefitGroups**](BenefitGroups.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getbenefit_groups**
> BenefitGroups getbenefit_groups(authorization, x_tenant, benefit_groups_id, x_version)

Return a specific benefit-group instance.

Return a specific benefit-group instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BenefitGroupsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
benefit_groups_id = 'benefit_groups_id_example' # str | The ID of the benefit-groups that will be updated.
x_version = '3.0.0' # str | The API version. (default to 3.0.0)

try:
    # Return a specific benefit-group instance.
    api_response = api_instance.getbenefit_groups(authorization, x_tenant, benefit_groups_id, x_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BenefitGroupsApi->getbenefit_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **benefit_groups_id** | **str**| The ID of the benefit-groups that will be updated. | 
 **x_version** | **str**| The API version. | [default to 3.0.0]

### Return type

[**BenefitGroups**](BenefitGroups.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getbenefit_groupss**
> BenefitGroupsList getbenefit_groupss(authorization, x_tenant, x_version, page=page, page_size=page_size, order_by=order_by, select_0=select_0, select_1=select_1, filter_by_name_like=filter_by_name_like, filter_by_created_at_from=filter_by_created_at_from, filter_by_created_at_to=filter_by_created_at_to, count_0_filter_by_name_like=count_0_filter_by_name_like, count_1_filter_by_created_at_from=count_1_filter_by_created_at_from)

List multiple benefit-groups resources.

This operation allows you to list and search for benefit-groups resources provided query arguments.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BenefitGroupsApi()
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
count_0_filter_by_name_like = '' # str | Return the total records from a filterBy query. Ex.: count[0][filterBy][name][like]=Loren Ipsun (optional) (default to )
count_1_filter_by_created_at_from = '' # str | Return the total records from createdFrom a specific date. Ex.: count[1][filterBy][createdAt][from]=2015-01-01T02:00:00.000Z (optional) (default to )

try:
    # List multiple benefit-groups resources.
    api_response = api_instance.getbenefit_groupss(authorization, x_tenant, x_version, page=page, page_size=page_size, order_by=order_by, select_0=select_0, select_1=select_1, filter_by_name_like=filter_by_name_like, filter_by_created_at_from=filter_by_created_at_from, filter_by_created_at_to=filter_by_created_at_to, count_0_filter_by_name_like=count_0_filter_by_name_like, count_1_filter_by_created_at_from=count_1_filter_by_created_at_from)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BenefitGroupsApi->getbenefit_groupss: %s\n" % e)
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
 **count_0_filter_by_name_like** | **str**| Return the total records from a filterBy query. Ex.: count[0][filterBy][name][like]&#x3D;Loren Ipsun | [optional] [default to ]
 **count_1_filter_by_created_at_from** | **str**| Return the total records from createdFrom a specific date. Ex.: count[1][filterBy][createdAt][from]&#x3D;2015-01-01T02:00:00.000Z | [optional] [default to ]

### Return type

[**BenefitGroupsList**](BenefitGroupsList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updatebenefit_groups**
> BenefitGroups updatebenefit_groups(authorization, x_tenant, x_version, benefit_groups_id, body)

Update a specific benefit-group instance.

Update a specific benefit-group instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BenefitGroupsApi()
authorization = 'Basic ' # str | Basic Authentication. (default to Basic )
x_tenant = '' # str | The tenant id. (default to )
x_version = '3.0.0' # str | The API version. (default to 3.0.0)
benefit_groups_id = 'benefit_groups_id_example' # str | The ID of the benefit-groups that will be updated.
body = swagger_client.BenefitGroups() # BenefitGroups | Data used to update benefit-groups

try:
    # Update a specific benefit-group instance.
    api_response = api_instance.updatebenefit_groups(authorization, x_tenant, x_version, benefit_groups_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BenefitGroupsApi->updatebenefit_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Basic Authentication. | [default to Basic ]
 **x_tenant** | **str**| The tenant id. | [default to ]
 **x_version** | **str**| The API version. | [default to 3.0.0]
 **benefit_groups_id** | **str**| The ID of the benefit-groups that will be updated. | 
 **body** | [**BenefitGroups**](BenefitGroups.md)| Data used to update benefit-groups | 

### Return type

[**BenefitGroups**](BenefitGroups.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

