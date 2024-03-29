# neucore_api.ApplicationGroupsApi

All URIs are relative to *https://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**alliance_groups_bulk_v1**](ApplicationGroupsApi.md#alliance_groups_bulk_v1) | **POST** /app/v1/alliance-groups | Return groups of multiple alliances.
[**alliance_groups_v1**](ApplicationGroupsApi.md#alliance_groups_v1) | **GET** /app/v1/alliance-groups/{aid} | Return groups of the alliance.
[**alliance_groups_v2**](ApplicationGroupsApi.md#alliance_groups_v2) | **GET** /app/v2/alliance-groups/{aid} | Return groups of the alliance.
[**corp_groups_bulk_v1**](ApplicationGroupsApi.md#corp_groups_bulk_v1) | **POST** /app/v1/corp-groups | Return groups of multiple corporations.
[**corp_groups_v1**](ApplicationGroupsApi.md#corp_groups_v1) | **GET** /app/v1/corp-groups/{cid} | Return groups of the corporation.
[**corp_groups_v2**](ApplicationGroupsApi.md#corp_groups_v2) | **GET** /app/v2/corp-groups/{cid} | Return groups of the corporation.
[**group_members_v1**](ApplicationGroupsApi.md#group_members_v1) | **GET** /app/v1/group-members/{groupId} | Returns the main character IDs from all group members.
[**groups_bulk_v1**](ApplicationGroupsApi.md#groups_bulk_v1) | **POST** /app/v1/groups | Return groups of multiple players, identified by one of their character IDs.
[**groups_v1**](ApplicationGroupsApi.md#groups_v1) | **GET** /app/v1/groups/{cid} | Return groups of the character&#39;s player account.
[**groups_v2**](ApplicationGroupsApi.md#groups_v2) | **GET** /app/v2/groups/{cid} | Return groups of the character&#39;s player account.
[**groups_with_fallback_v1**](ApplicationGroupsApi.md#groups_with_fallback_v1) | **GET** /app/v1/groups-with-fallback | Returns groups from the character&#39;s account, if available, or the corporation and alliance.


# **alliance_groups_bulk_v1**
> [Alliance] alliance_groups_bulk_v1(request_body)

Return groups of multiple alliances.

Needs role: app-groups.<br>      *                  Returns only groups that have been added to the app as well.      *                  Skips alliances that are not found in the local database.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import neucore_api
from neucore_api.api import application_groups_api
from neucore_api.model.alliance import Alliance
from pprint import pprint
# Defining the host is optional and defaults to https://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neucore_api.Configuration(
    host = "https://localhost/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = neucore_api.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with neucore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = application_groups_api.ApplicationGroupsApi(api_client)
    request_body = [
        1,
    ] # [int] | EVE alliance IDs array.

    # example passing only required values which don't have defaults set
    try:
        # Return groups of multiple alliances.
        api_response = api_instance.alliance_groups_bulk_v1(request_body)
        pprint(api_response)
    except neucore_api.ApiException as e:
        print("Exception when calling ApplicationGroupsApi->alliance_groups_bulk_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | **[int]**| EVE alliance IDs array. |

### Return type

[**[Alliance]**](Alliance.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of alliances with groups. |  -  |
**400** | Invalid body. |  -  |
**403** | Not authorized. |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alliance_groups_v1**
> [Group] alliance_groups_v1(aid)

Return groups of the alliance.

Needs role: app-groups.<br>Returns only groups that have been added to the app as well.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import neucore_api
from neucore_api.api import application_groups_api
from neucore_api.model.group import Group
from pprint import pprint
# Defining the host is optional and defaults to https://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neucore_api.Configuration(
    host = "https://localhost/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = neucore_api.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with neucore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = application_groups_api.ApplicationGroupsApi(api_client)
    aid = 1 # int | EVE alliance ID.

    # example passing only required values which don't have defaults set
    try:
        # Return groups of the alliance.
        api_response = api_instance.alliance_groups_v1(aid)
        pprint(api_response)
    except neucore_api.ApiException as e:
        print("Exception when calling ApplicationGroupsApi->alliance_groups_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **int**| EVE alliance ID. |

### Return type

[**[Group]**](Group.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of groups. |  -  |
**403** | Not authorized. |  -  |
**404** | Alliance not found. (default reason phrase) |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alliance_groups_v2**
> [Group] alliance_groups_v2(aid)

Return groups of the alliance.

Needs role: app-groups.<br>Returns only groups that have been added to the app as well.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import neucore_api
from neucore_api.api import application_groups_api
from neucore_api.model.group import Group
from pprint import pprint
# Defining the host is optional and defaults to https://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neucore_api.Configuration(
    host = "https://localhost/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = neucore_api.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with neucore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = application_groups_api.ApplicationGroupsApi(api_client)
    aid = 1 # int | EVE alliance ID.

    # example passing only required values which don't have defaults set
    try:
        # Return groups of the alliance.
        api_response = api_instance.alliance_groups_v2(aid)
        pprint(api_response)
    except neucore_api.ApiException as e:
        print("Exception when calling ApplicationGroupsApi->alliance_groups_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **int**| EVE alliance ID. |

### Return type

[**[Group]**](Group.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of groups. |  -  |
**403** | Not authorized. |  -  |
**404** | Reason phrase: Alliance not found. |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **corp_groups_bulk_v1**
> [Corporation] corp_groups_bulk_v1(request_body)

Return groups of multiple corporations.

Needs role: app-groups.<br>      *                  Returns only groups that have been added to the app as well.      *                  Skips corporations that are not found in the local database.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import neucore_api
from neucore_api.api import application_groups_api
from neucore_api.model.corporation import Corporation
from pprint import pprint
# Defining the host is optional and defaults to https://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neucore_api.Configuration(
    host = "https://localhost/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = neucore_api.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with neucore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = application_groups_api.ApplicationGroupsApi(api_client)
    request_body = [
        1,
    ] # [int] | EVE corporation IDs array.

    # example passing only required values which don't have defaults set
    try:
        # Return groups of multiple corporations.
        api_response = api_instance.corp_groups_bulk_v1(request_body)
        pprint(api_response)
    except neucore_api.ApiException as e:
        print("Exception when calling ApplicationGroupsApi->corp_groups_bulk_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | **[int]**| EVE corporation IDs array. |

### Return type

[**[Corporation]**](Corporation.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of corporations with groups but without alliance. |  -  |
**400** | Invalid body. |  -  |
**403** | Not authorized. |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **corp_groups_v1**
> [Group] corp_groups_v1(cid)

Return groups of the corporation.

Needs role: app-groups.<br>Returns only groups that have been added to the app as well.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import neucore_api
from neucore_api.api import application_groups_api
from neucore_api.model.group import Group
from pprint import pprint
# Defining the host is optional and defaults to https://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neucore_api.Configuration(
    host = "https://localhost/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = neucore_api.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with neucore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = application_groups_api.ApplicationGroupsApi(api_client)
    cid = 1 # int | EVE corporation ID.

    # example passing only required values which don't have defaults set
    try:
        # Return groups of the corporation.
        api_response = api_instance.corp_groups_v1(cid)
        pprint(api_response)
    except neucore_api.ApiException as e:
        print("Exception when calling ApplicationGroupsApi->corp_groups_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cid** | **int**| EVE corporation ID. |

### Return type

[**[Group]**](Group.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of groups. |  -  |
**403** | Not authorized. |  -  |
**404** | Corporation not found. (default reason phrase) |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **corp_groups_v2**
> [Group] corp_groups_v2(cid)

Return groups of the corporation.

Needs role: app-groups.<br>Returns only groups that have been added to the app as well.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import neucore_api
from neucore_api.api import application_groups_api
from neucore_api.model.group import Group
from pprint import pprint
# Defining the host is optional and defaults to https://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neucore_api.Configuration(
    host = "https://localhost/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = neucore_api.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with neucore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = application_groups_api.ApplicationGroupsApi(api_client)
    cid = 1 # int | EVE corporation ID.

    # example passing only required values which don't have defaults set
    try:
        # Return groups of the corporation.
        api_response = api_instance.corp_groups_v2(cid)
        pprint(api_response)
    except neucore_api.ApiException as e:
        print("Exception when calling ApplicationGroupsApi->corp_groups_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cid** | **int**| EVE corporation ID. |

### Return type

[**[Group]**](Group.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of groups. |  -  |
**403** | Not authorized. |  -  |
**404** | Reason phrase: Corporation not found. |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_members_v1**
> [int] group_members_v1(group_id)

Returns the main character IDs from all group members.

Needs role: app-groups.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import neucore_api
from neucore_api.api import application_groups_api
from pprint import pprint
# Defining the host is optional and defaults to https://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neucore_api.Configuration(
    host = "https://localhost/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = neucore_api.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with neucore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = application_groups_api.ApplicationGroupsApi(api_client)
    group_id = 1 # int | Group ID.
    corporation = 1 # int | Limit to characters that are a member of this corporation. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns the main character IDs from all group members.
        api_response = api_instance.group_members_v1(group_id)
        pprint(api_response)
    except neucore_api.ApiException as e:
        print("Exception when calling ApplicationGroupsApi->group_members_v1: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns the main character IDs from all group members.
        api_response = api_instance.group_members_v1(group_id, corporation=corporation)
        pprint(api_response)
    except neucore_api.ApiException as e:
        print("Exception when calling ApplicationGroupsApi->group_members_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| Group ID. |
 **corporation** | **int**| Limit to characters that are a member of this corporation. | [optional]

### Return type

**[int]**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of character IDs. |  -  |
**403** | Not authorized. |  -  |
**404** | Group was not found or app may not see it. |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_bulk_v1**
> [CharacterGroups] groups_bulk_v1(request_body)

Return groups of multiple players, identified by one of their character IDs.

Needs role: app-groups.<br>      *                  Returns only groups that have been added to the app as well.      *                  Skips characters that are not found in the local database.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import neucore_api
from neucore_api.api import application_groups_api
from neucore_api.model.character_groups import CharacterGroups
from pprint import pprint
# Defining the host is optional and defaults to https://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neucore_api.Configuration(
    host = "https://localhost/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = neucore_api.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with neucore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = application_groups_api.ApplicationGroupsApi(api_client)
    request_body = [
        1,
    ] # [int] | EVE character IDs array.

    # example passing only required values which don't have defaults set
    try:
        # Return groups of multiple players, identified by one of their character IDs.
        api_response = api_instance.groups_bulk_v1(request_body)
        pprint(api_response)
    except neucore_api.ApiException as e:
        print("Exception when calling ApplicationGroupsApi->groups_bulk_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | **[int]**| EVE character IDs array. |

### Return type

[**[CharacterGroups]**](CharacterGroups.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of characters (id, name and corporation properties only) with groups. |  -  |
**400** | Invalid body. |  -  |
**403** | Not authorized. |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_v1**
> [Group] groups_v1(cid)

Return groups of the character's player account.

Needs role: app-groups.<br>Returns only groups that have been added to the app as well.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import neucore_api
from neucore_api.api import application_groups_api
from neucore_api.model.group import Group
from pprint import pprint
# Defining the host is optional and defaults to https://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neucore_api.Configuration(
    host = "https://localhost/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = neucore_api.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with neucore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = application_groups_api.ApplicationGroupsApi(api_client)
    cid = 1 # int | EVE character ID.

    # example passing only required values which don't have defaults set
    try:
        # Return groups of the character's player account.
        api_response = api_instance.groups_v1(cid)
        pprint(api_response)
    except neucore_api.ApiException as e:
        print("Exception when calling ApplicationGroupsApi->groups_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cid** | **int**| EVE character ID. |

### Return type

[**[Group]**](Group.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of groups. |  -  |
**403** | Not authorized. |  -  |
**404** | Character not found. (default reason phrase) |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_v2**
> [Group] groups_v2(cid)

Return groups of the character's player account.

Needs role: app-groups.<br>Returns only groups that have been added to the app as well.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import neucore_api
from neucore_api.api import application_groups_api
from neucore_api.model.group import Group
from pprint import pprint
# Defining the host is optional and defaults to https://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neucore_api.Configuration(
    host = "https://localhost/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = neucore_api.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with neucore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = application_groups_api.ApplicationGroupsApi(api_client)
    cid = 1 # int | EVE character ID.

    # example passing only required values which don't have defaults set
    try:
        # Return groups of the character's player account.
        api_response = api_instance.groups_v2(cid)
        pprint(api_response)
    except neucore_api.ApiException as e:
        print("Exception when calling ApplicationGroupsApi->groups_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cid** | **int**| EVE character ID. |

### Return type

[**[Group]**](Group.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of groups. |  -  |
**403** | Not authorized. |  -  |
**404** | Reason phrase: Character not found. |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_with_fallback_v1**
> [Group] groups_with_fallback_v1(character, corporation)

Returns groups from the character's account, if available, or the corporation and alliance.

Needs role: app-groups.<br>      *                  Returns only groups that have been added to the app as well.<br>      *                  It is not checked if character, corporation and alliance match.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import neucore_api
from neucore_api.api import application_groups_api
from neucore_api.model.group import Group
from pprint import pprint
# Defining the host is optional and defaults to https://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neucore_api.Configuration(
    host = "https://localhost/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = neucore_api.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with neucore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = application_groups_api.ApplicationGroupsApi(api_client)
    character = 1 # int | EVE character ID.
    corporation = 1 # int | EVE corporation ID.
    alliance = 1 # int | EVE alliance ID. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns groups from the character's account, if available, or the corporation and alliance.
        api_response = api_instance.groups_with_fallback_v1(character, corporation)
        pprint(api_response)
    except neucore_api.ApiException as e:
        print("Exception when calling ApplicationGroupsApi->groups_with_fallback_v1: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns groups from the character's account, if available, or the corporation and alliance.
        api_response = api_instance.groups_with_fallback_v1(character, corporation, alliance=alliance)
        pprint(api_response)
    except neucore_api.ApiException as e:
        print("Exception when calling ApplicationGroupsApi->groups_with_fallback_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character** | **int**| EVE character ID. |
 **corporation** | **int**| EVE corporation ID. |
 **alliance** | **int**| EVE alliance ID. | [optional]

### Return type

[**[Group]**](Group.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of groups. |  -  |
**403** | Not authorized. |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

