# neucore_api.ApplicationApi

All URIs are relative to *https://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**alliance_groups_bulk_v1**](ApplicationApi.md#alliance_groups_bulk_v1) | **POST** /app/v1/alliance-groups | Return groups of multiple alliances.
[**alliance_groups_v1**](ApplicationApi.md#alliance_groups_v1) | **GET** /app/v1/alliance-groups/{aid} | Return groups of the alliance.
[**alliance_groups_v2**](ApplicationApi.md#alliance_groups_v2) | **GET** /app/v2/alliance-groups/{aid} | Return groups of the alliance.
[**characters_v1**](ApplicationApi.md#characters_v1) | **GET** /app/v1/characters/{characterId} | Return all characters of the player account to which the character ID belongs.
[**corp_groups_bulk_v1**](ApplicationApi.md#corp_groups_bulk_v1) | **POST** /app/v1/corp-groups | Return groups of multiple corporations.
[**corp_groups_v1**](ApplicationApi.md#corp_groups_v1) | **GET** /app/v1/corp-groups/{cid} | Return groups of the corporation.
[**corp_groups_v2**](ApplicationApi.md#corp_groups_v2) | **GET** /app/v2/corp-groups/{cid} | Return groups of the corporation.
[**corporation_players_v1**](ApplicationApi.md#corporation_players_v1) | **GET** /app/v1/corp-players/{corporationId} | Return a list of all players that have a character in the corporation.
[**esi_post_v1**](ApplicationApi.md#esi_post_v1) | **POST** /app/v1/esi | Same as GET ​/app​/v1​/esi, but for POST requests.
[**esi_v1**](ApplicationApi.md#esi_v1) | **GET** /app/v1/esi | Makes an ESI GET request on behalf on an EVE character and returns the result.
[**groups_bulk_v1**](ApplicationApi.md#groups_bulk_v1) | **POST** /app/v1/groups | Return groups of multiple players, identified by one of their character IDs.
[**groups_v1**](ApplicationApi.md#groups_v1) | **GET** /app/v1/groups/{cid} | Return groups of the character&#39;s player account.
[**groups_v2**](ApplicationApi.md#groups_v2) | **GET** /app/v2/groups/{cid} | Return groups of the character&#39;s player account.
[**groups_with_fallback_v1**](ApplicationApi.md#groups_with_fallback_v1) | **GET** /app/v1/groups-with-fallback | Returns groups from the character&#39;s account, if available, or the corporation and alliance.
[**incoming_characters_v1**](ApplicationApi.md#incoming_characters_v1) | **GET** /app/v1/incoming-characters/{characterId} | Return all characters that were moved from another account to the player account to which the                     ID belongs.
[**main_v1**](ApplicationApi.md#main_v1) | **GET** /app/v1/main/{cid} | Return the main character of the player account to which the character ID belongs.
[**main_v2**](ApplicationApi.md#main_v2) | **GET** /app/v2/main/{cid} | Return the main character of the player account to which the character ID belongs.
[**member_tracking_v1**](ApplicationApi.md#member_tracking_v1) | **GET** /app/v1/corporation/{id}/member-tracking | Return corporation member tracking data.
[**player_characters_v1**](ApplicationApi.md#player_characters_v1) | **GET** /app/v1/player-chars/{playerId} | Return all characters from the player account.
[**player_v1**](ApplicationApi.md#player_v1) | **GET** /app/v1/player/{characterId} | Return the player account to which the character ID belongs.
[**removed_characters_v1**](ApplicationApi.md#removed_characters_v1) | **GET** /app/v1/removed-characters/{characterId} | Return all characters that were removed from the player account to which the character ID belongs.
[**show_v1**](ApplicationApi.md#show_v1) | **GET** /app/v1/show | Show app information.


# **alliance_groups_bulk_v1**
> list[Alliance] alliance_groups_bulk_v1(request_body)

Return groups of multiple alliances.

Needs role: app-groups.<br>      *                  Returns only groups that have been added to the app as well.      *                  Skips alliances that are not found in the local database.

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import neucore_api
from neucore_api.rest import ApiException
from pprint import pprint
configuration = neucore_api.Configuration()
# Configure Bearer authorization: BearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://localhost/api
configuration.host = "https://localhost/api"
# Enter a context with an instance of the API client
with neucore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = neucore_api.ApplicationApi(api_client)
    request_body = [56] # list[int] | EVE alliance IDs array.

    try:
        # Return groups of multiple alliances.
        api_response = api_instance.alliance_groups_bulk_v1(request_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationApi->alliance_groups_bulk_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**list[int]**](int.md)| EVE alliance IDs array. | 

### Return type

[**list[Alliance]**](Alliance.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alliance_groups_v1**
> list[Group] alliance_groups_v1(aid)

Return groups of the alliance.

Needs role: app-groups.<br>Returns only groups that have been added to the app as well.

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import neucore_api
from neucore_api.rest import ApiException
from pprint import pprint
configuration = neucore_api.Configuration()
# Configure Bearer authorization: BearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://localhost/api
configuration.host = "https://localhost/api"
# Enter a context with an instance of the API client
with neucore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = neucore_api.ApplicationApi(api_client)
    aid = 56 # int | EVE alliance ID.

    try:
        # Return groups of the alliance.
        api_response = api_instance.alliance_groups_v1(aid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationApi->alliance_groups_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **int**| EVE alliance ID. | 

### Return type

[**list[Group]**](Group.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alliance_groups_v2**
> list[Group] alliance_groups_v2(aid)

Return groups of the alliance.

Needs role: app-groups.<br>Returns only groups that have been added to the app as well.

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import neucore_api
from neucore_api.rest import ApiException
from pprint import pprint
configuration = neucore_api.Configuration()
# Configure Bearer authorization: BearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://localhost/api
configuration.host = "https://localhost/api"
# Enter a context with an instance of the API client
with neucore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = neucore_api.ApplicationApi(api_client)
    aid = 56 # int | EVE alliance ID.

    try:
        # Return groups of the alliance.
        api_response = api_instance.alliance_groups_v2(aid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationApi->alliance_groups_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **int**| EVE alliance ID. | 

### Return type

[**list[Group]**](Group.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **characters_v1**
> list[Character] characters_v1(character_id)

Return all characters of the player account to which the character ID belongs.

Needs role: app-chars.

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import neucore_api
from neucore_api.rest import ApiException
from pprint import pprint
configuration = neucore_api.Configuration()
# Configure Bearer authorization: BearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://localhost/api
configuration.host = "https://localhost/api"
# Enter a context with an instance of the API client
with neucore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = neucore_api.ApplicationApi(api_client)
    character_id = 56 # int | EVE character ID.

    try:
        # Return all characters of the player account to which the character ID belongs.
        api_response = api_instance.characters_v1(character_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationApi->characters_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| EVE character ID. | 

### Return type

[**list[Character]**](Character.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All characters from the player account. |  -  |
**403** | Not authorized. |  -  |
**404** | Character (or player) not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **corp_groups_bulk_v1**
> list[Corporation] corp_groups_bulk_v1(request_body)

Return groups of multiple corporations.

Needs role: app-groups.<br>      *                  Returns only groups that have been added to the app as well.      *                  Skips corporations that are not found in the local database.

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import neucore_api
from neucore_api.rest import ApiException
from pprint import pprint
configuration = neucore_api.Configuration()
# Configure Bearer authorization: BearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://localhost/api
configuration.host = "https://localhost/api"
# Enter a context with an instance of the API client
with neucore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = neucore_api.ApplicationApi(api_client)
    request_body = [56] # list[int] | EVE corporation IDs array.

    try:
        # Return groups of multiple corporations.
        api_response = api_instance.corp_groups_bulk_v1(request_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationApi->corp_groups_bulk_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**list[int]**](int.md)| EVE corporation IDs array. | 

### Return type

[**list[Corporation]**](Corporation.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **corp_groups_v1**
> list[Group] corp_groups_v1(cid)

Return groups of the corporation.

Needs role: app-groups.<br>Returns only groups that have been added to the app as well.

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import neucore_api
from neucore_api.rest import ApiException
from pprint import pprint
configuration = neucore_api.Configuration()
# Configure Bearer authorization: BearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://localhost/api
configuration.host = "https://localhost/api"
# Enter a context with an instance of the API client
with neucore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = neucore_api.ApplicationApi(api_client)
    cid = 56 # int | EVE corporation ID.

    try:
        # Return groups of the corporation.
        api_response = api_instance.corp_groups_v1(cid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationApi->corp_groups_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cid** | **int**| EVE corporation ID. | 

### Return type

[**list[Group]**](Group.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **corp_groups_v2**
> list[Group] corp_groups_v2(cid)

Return groups of the corporation.

Needs role: app-groups.<br>Returns only groups that have been added to the app as well.

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import neucore_api
from neucore_api.rest import ApiException
from pprint import pprint
configuration = neucore_api.Configuration()
# Configure Bearer authorization: BearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://localhost/api
configuration.host = "https://localhost/api"
# Enter a context with an instance of the API client
with neucore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = neucore_api.ApplicationApi(api_client)
    cid = 56 # int | EVE corporation ID.

    try:
        # Return groups of the corporation.
        api_response = api_instance.corp_groups_v2(cid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationApi->corp_groups_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cid** | **int**| EVE corporation ID. | 

### Return type

[**list[Group]**](Group.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **corporation_players_v1**
> list[Player] corporation_players_v1(corporation_id)

Return a list of all players that have a character in the corporation.

Needs role: app-chars.

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import neucore_api
from neucore_api.rest import ApiException
from pprint import pprint
configuration = neucore_api.Configuration()
# Configure Bearer authorization: BearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://localhost/api
configuration.host = "https://localhost/api"
# Enter a context with an instance of the API client
with neucore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = neucore_api.ApplicationApi(api_client)
    corporation_id = 56 # int | EVE corporation ID.

    try:
        # Return a list of all players that have a character in the corporation.
        api_response = api_instance.corporation_players_v1(corporation_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationApi->corporation_players_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corporation_id** | **int**| EVE corporation ID. | 

### Return type

[**list[Player]**](Player.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of players, only id and name properties are returned. |  -  |
**403** | Not authorized. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esi_post_v1**
> str esi_post_v1(esi_path_query, datasource, body)

Same as GET ​/app​/v1​/esi, but for POST requests.

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import neucore_api
from neucore_api.rest import ApiException
from pprint import pprint
configuration = neucore_api.Configuration()
# Configure Bearer authorization: BearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://localhost/api
configuration.host = "https://localhost/api"
# Enter a context with an instance of the API client
with neucore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = neucore_api.ApplicationApi(api_client)
    esi_path_query = 'esi_path_query_example' # str | The ESI path and query string (without the datasource parameter).
datasource = 'datasource_example' # str | The EVE character ID those token should be used to make the ESI request
body = 'body_example' # str | JSON encoded data.

    try:
        # Same as GET ​/app​/v1​/esi, but for POST requests.
        api_response = api_instance.esi_post_v1(esi_path_query, datasource, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationApi->esi_post_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **esi_path_query** | **str**| The ESI path and query string (without the datasource parameter). | 
 **datasource** | **str**| The EVE character ID those token should be used to make the ESI request | 
 **body** | **str**| JSON encoded data. | 

### Return type

**str**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Same as GET ​/app​/v1​/esi, see there for details. |  * Expires - RFC7231 formatted datetime string <br>  |
**304** | Not modified |  * Expires - RFC7231 formatted datetime string <br>  |
**400** | Bad request, see reason phrase and/or body for more. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**420** | Error limited |  -  |
**429** | Maximum permissible ESI error limit reached (X-Esi-Error-Limit-Remain &lt;&#x3D; 20). |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esi_v1**
> str esi_v1(esi_path_query, datasource)

Makes an ESI GET request on behalf on an EVE character and returns the result.

Needs role: app-esi<br>      *         Public ESI routes are not allowed.<br>      *         The following headers from ESI are passed through to the response:                Content-Type Expires X-Esi-Error-Limit-Remain X-Esi-Error-Limit-Reset X-Pages warning<br>      *         The HTTP status code from ESI is also passed through, so maybe there's more than the documented.<br>      *         The ESI path and query parameters can alternatively be appended to the path of this endpoint,                this allows to use OpenAPI clients that were generated for the ESI API,                see doc/app-esi-examples.php for more.

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import neucore_api
from neucore_api.rest import ApiException
from pprint import pprint
configuration = neucore_api.Configuration()
# Configure Bearer authorization: BearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://localhost/api
configuration.host = "https://localhost/api"
# Enter a context with an instance of the API client
with neucore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = neucore_api.ApplicationApi(api_client)
    esi_path_query = 'esi_path_query_example' # str | The ESI path and query string (without the datasource parameter).
datasource = 'datasource_example' # str | The EVE character ID those token should be used to make the ESI request

    try:
        # Makes an ESI GET request on behalf on an EVE character and returns the result.
        api_response = api_instance.esi_v1(esi_path_query, datasource)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationApi->esi_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **esi_path_query** | **str**| The ESI path and query string (without the datasource parameter). | 
 **datasource** | **str**| The EVE character ID those token should be used to make the ESI request | 

### Return type

**str**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The data from ESI.&lt;br&gt;                             Please note that the JSON schema type can be an object, array or number etc.,                             unfortunately there is no way to document this. |  * Expires - RFC7231 formatted datetime string <br>  |
**304** | Not modified |  * Expires - RFC7231 formatted datetime string <br>  |
**400** | Bad request, see reason phrase and/or body for more. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**420** | Error limited |  -  |
**429** | Maximum permissible ESI error limit reached (X-Esi-Error-Limit-Remain &lt;&#x3D; 20). |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_bulk_v1**
> list[CharacterGroups] groups_bulk_v1(request_body)

Return groups of multiple players, identified by one of their character IDs.

Needs role: app-groups.<br>      *                  Returns only groups that have been added to the app as well.      *                  Skips characters that are not found in the local database.

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import neucore_api
from neucore_api.rest import ApiException
from pprint import pprint
configuration = neucore_api.Configuration()
# Configure Bearer authorization: BearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://localhost/api
configuration.host = "https://localhost/api"
# Enter a context with an instance of the API client
with neucore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = neucore_api.ApplicationApi(api_client)
    request_body = [56] # list[int] | EVE character IDs array.

    try:
        # Return groups of multiple players, identified by one of their character IDs.
        api_response = api_instance.groups_bulk_v1(request_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationApi->groups_bulk_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**list[int]**](int.md)| EVE character IDs array. | 

### Return type

[**list[CharacterGroups]**](CharacterGroups.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_v1**
> list[Group] groups_v1(cid)

Return groups of the character's player account.

Needs role: app-groups.<br>Returns only groups that have been added to the app as well.

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import neucore_api
from neucore_api.rest import ApiException
from pprint import pprint
configuration = neucore_api.Configuration()
# Configure Bearer authorization: BearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://localhost/api
configuration.host = "https://localhost/api"
# Enter a context with an instance of the API client
with neucore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = neucore_api.ApplicationApi(api_client)
    cid = 56 # int | EVE character ID.

    try:
        # Return groups of the character's player account.
        api_response = api_instance.groups_v1(cid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationApi->groups_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cid** | **int**| EVE character ID. | 

### Return type

[**list[Group]**](Group.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_v2**
> list[Group] groups_v2(cid)

Return groups of the character's player account.

Needs role: app-groups.<br>Returns only groups that have been added to the app as well.

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import neucore_api
from neucore_api.rest import ApiException
from pprint import pprint
configuration = neucore_api.Configuration()
# Configure Bearer authorization: BearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://localhost/api
configuration.host = "https://localhost/api"
# Enter a context with an instance of the API client
with neucore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = neucore_api.ApplicationApi(api_client)
    cid = 56 # int | EVE character ID.

    try:
        # Return groups of the character's player account.
        api_response = api_instance.groups_v2(cid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationApi->groups_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cid** | **int**| EVE character ID. | 

### Return type

[**list[Group]**](Group.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_with_fallback_v1**
> list[Group] groups_with_fallback_v1(character, corporation, alliance=alliance)

Returns groups from the character's account, if available, or the corporation and alliance.

Needs role: app-groups.<br>      *                  Returns only groups that have been added to the app as well.<br>      *                  It is not checked if character, corporation and alliance match.

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import neucore_api
from neucore_api.rest import ApiException
from pprint import pprint
configuration = neucore_api.Configuration()
# Configure Bearer authorization: BearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://localhost/api
configuration.host = "https://localhost/api"
# Enter a context with an instance of the API client
with neucore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = neucore_api.ApplicationApi(api_client)
    character = 56 # int | EVE character ID.
corporation = 56 # int | EVE corporation ID.
alliance = 56 # int | EVE alliance ID. (optional)

    try:
        # Returns groups from the character's account, if available, or the corporation and alliance.
        api_response = api_instance.groups_with_fallback_v1(character, corporation, alliance=alliance)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationApi->groups_with_fallback_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character** | **int**| EVE character ID. | 
 **corporation** | **int**| EVE corporation ID. | 
 **alliance** | **int**| EVE alliance ID. | [optional] 

### Return type

[**list[Group]**](Group.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **incoming_characters_v1**
> list[RemovedCharacter] incoming_characters_v1(character_id)

Return all characters that were moved from another account to the player account to which the                     ID belongs.

Needs role: app-chars.

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import neucore_api
from neucore_api.rest import ApiException
from pprint import pprint
configuration = neucore_api.Configuration()
# Configure Bearer authorization: BearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://localhost/api
configuration.host = "https://localhost/api"
# Enter a context with an instance of the API client
with neucore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = neucore_api.ApplicationApi(api_client)
    character_id = 56 # int | EVE character ID.

    try:
        # Return all characters that were moved from another account to the player account to which the                     ID belongs.
        api_response = api_instance.incoming_characters_v1(character_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationApi->incoming_characters_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| EVE character ID. | 

### Return type

[**list[RemovedCharacter]**](RemovedCharacter.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All incoming characters from the player account. |  -  |
**403** | Not authorized. |  -  |
**404** | Character (or player) not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **main_v1**
> Character main_v1(cid)

Return the main character of the player account to which the character ID belongs.

Needs role: app-chars.<br>It is possible that an account has no main character.

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import neucore_api
from neucore_api.rest import ApiException
from pprint import pprint
configuration = neucore_api.Configuration()
# Configure Bearer authorization: BearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://localhost/api
configuration.host = "https://localhost/api"
# Enter a context with an instance of the API client
with neucore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = neucore_api.ApplicationApi(api_client)
    cid = 56 # int | EVE character ID.

    try:
        # Return the main character of the player account to which the character ID belongs.
        api_response = api_instance.main_v1(cid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationApi->main_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cid** | **int**| EVE character ID. | 

### Return type

[**Character**](Character.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The main character |  -  |
**204** | No main character found. |  -  |
**403** | Not authorized. |  -  |
**404** | Character (or player) not found. (default reason phrase) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **main_v2**
> Character main_v2(cid)

Return the main character of the player account to which the character ID belongs.

Needs role: app-chars.<br>It is possible that an account has no main character.

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import neucore_api
from neucore_api.rest import ApiException
from pprint import pprint
configuration = neucore_api.Configuration()
# Configure Bearer authorization: BearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://localhost/api
configuration.host = "https://localhost/api"
# Enter a context with an instance of the API client
with neucore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = neucore_api.ApplicationApi(api_client)
    cid = 56 # int | EVE character ID.

    try:
        # Return the main character of the player account to which the character ID belongs.
        api_response = api_instance.main_v2(cid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationApi->main_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cid** | **int**| EVE character ID. | 

### Return type

[**Character**](Character.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The main character |  -  |
**204** | No main character found. |  -  |
**403** | Not authorized. |  -  |
**404** | Reason phrase: Character not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **member_tracking_v1**
> list[CorporationMember] member_tracking_v1(id, inactive=inactive, active=active, account=account)

Return corporation member tracking data.

Needs role: app-tracking

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import neucore_api
from neucore_api.rest import ApiException
from pprint import pprint
configuration = neucore_api.Configuration()
# Configure Bearer authorization: BearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://localhost/api
configuration.host = "https://localhost/api"
# Enter a context with an instance of the API client
with neucore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = neucore_api.ApplicationApi(api_client)
    id = 56 # int | EVE corporation ID.
inactive = 56 # int | Limit to members who have been inactive for x days or longer. (optional)
active = 56 # int | Limit to members who were active in the last x days. (optional)
account = 'account_example' # str | Limit to members with (true) or without (false) an account. (optional)

    try:
        # Return corporation member tracking data.
        api_response = api_instance.member_tracking_v1(id, inactive=inactive, active=active, account=account)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationApi->member_tracking_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| EVE corporation ID. | 
 **inactive** | **int**| Limit to members who have been inactive for x days or longer. | [optional] 
 **active** | **int**| Limit to members who were active in the last x days. | [optional] 
 **account** | **str**| Limit to members with (true) or without (false) an account. | [optional] 

### Return type

[**list[CorporationMember]**](CorporationMember.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Members ordered by logonDate descending (character and player properties excluded). |  -  |
**403** | Not authorized. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **player_characters_v1**
> list[Character] player_characters_v1(player_id)

Return all characters from the player account.

Needs role: app-chars.

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import neucore_api
from neucore_api.rest import ApiException
from pprint import pprint
configuration = neucore_api.Configuration()
# Configure Bearer authorization: BearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://localhost/api
configuration.host = "https://localhost/api"
# Enter a context with an instance of the API client
with neucore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = neucore_api.ApplicationApi(api_client)
    player_id = 56 # int | Player ID.

    try:
        # Return all characters from the player account.
        api_response = api_instance.player_characters_v1(player_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationApi->player_characters_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **player_id** | **int**| Player ID. | 

### Return type

[**list[Character]**](Character.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All characters from the player account. |  -  |
**403** | Not authorized. |  -  |
**404** | Player not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **player_v1**
> Player player_v1(character_id)

Return the player account to which the character ID belongs.

Needs role: app-chars.

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import neucore_api
from neucore_api.rest import ApiException
from pprint import pprint
configuration = neucore_api.Configuration()
# Configure Bearer authorization: BearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://localhost/api
configuration.host = "https://localhost/api"
# Enter a context with an instance of the API client
with neucore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = neucore_api.ApplicationApi(api_client)
    character_id = 56 # int | EVE character ID.

    try:
        # Return the player account to which the character ID belongs.
        api_response = api_instance.player_v1(character_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationApi->player_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| EVE character ID. | 

### Return type

[**Player**](Player.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The player, only id and name properties are returned. |  -  |
**403** | Not authorized. |  -  |
**404** | Character not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **removed_characters_v1**
> list[RemovedCharacter] removed_characters_v1(character_id)

Return all characters that were removed from the player account to which the character ID belongs.

Needs role: app-chars.

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import neucore_api
from neucore_api.rest import ApiException
from pprint import pprint
configuration = neucore_api.Configuration()
# Configure Bearer authorization: BearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://localhost/api
configuration.host = "https://localhost/api"
# Enter a context with an instance of the API client
with neucore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = neucore_api.ApplicationApi(api_client)
    character_id = 56 # int | EVE character ID.

    try:
        # Return all characters that were removed from the player account to which the character ID belongs.
        api_response = api_instance.removed_characters_v1(character_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationApi->removed_characters_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| EVE character ID. | 

### Return type

[**list[RemovedCharacter]**](RemovedCharacter.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All removed characters from the player account. |  -  |
**403** | Not authorized. |  -  |
**404** | Character (or player) not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_v1**
> App show_v1()

Show app information.

Needs role: app

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import neucore_api
from neucore_api.rest import ApiException
from pprint import pprint
configuration = neucore_api.Configuration()
# Configure Bearer authorization: BearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://localhost/api
configuration.host = "https://localhost/api"
# Enter a context with an instance of the API client
with neucore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = neucore_api.ApplicationApi(api_client)
    
    try:
        # Show app information.
        api_response = api_instance.show_v1()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationApi->show_v1: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**App**](App.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The app information |  -  |
**403** | Not authorized. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

