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
[**esi_post_v1**](ApplicationApi.md#esi_post_v1) | **POST** /app/v1/esi | Makes an ESI POST request on behalf on an EVE character and returns the result.
[**esi_v1**](ApplicationApi.md#esi_v1) | **GET** /app/v1/esi | Makes an ESI GET request on behalf on an EVE character and returns the result.
[**groups_bulk_v1**](ApplicationApi.md#groups_bulk_v1) | **POST** /app/v1/groups | Return groups of multiple players, identified by one of their character IDs.
[**groups_v1**](ApplicationApi.md#groups_v1) | **GET** /app/v1/groups/{cid} | Return groups of the character&#39;s player account.
[**groups_v2**](ApplicationApi.md#groups_v2) | **GET** /app/v2/groups/{cid} | Return groups of the character&#39;s player account.
[**groups_with_fallback_v1**](ApplicationApi.md#groups_with_fallback_v1) | **GET** /app/v1/groups-with-fallback | Returns groups from the character&#39;s account, if available, or the corporation and alliance.
[**main_v1**](ApplicationApi.md#main_v1) | **GET** /app/v1/main/{cid} | Returns the main character of the player account to which the character ID belongs.
[**main_v2**](ApplicationApi.md#main_v2) | **GET** /app/v2/main/{cid} | Return the main character of the player account to which the character ID belongs.
[**member_tracking_v1**](ApplicationApi.md#member_tracking_v1) | **GET** /app/v1/corporation/{id}/member-tracking | Return corporation member tracking data.
[**removed_characters_v1**](ApplicationApi.md#removed_characters_v1) | **GET** /app/v1/removed-characters/{characterId} | Return all characters that were removed from the player account to which the character ID belongs.
[**show_v1**](ApplicationApi.md#show_v1) | **GET** /app/v1/show | Show app information.


# **alliance_groups_bulk_v1**
> list[Alliance] alliance_groups_bulk_v1(request_body)

Return groups of multiple alliances.

Needs role: app-groups.<br>      *                  Returns only groups that have been added to the app as well.      *                  Skips alliances that are not found in the local database.

### Example

* Api Key Authentication (Bearer): 
```python
from __future__ import print_function
import time
import neucore_api
from neucore_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = neucore_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = neucore_api.ApplicationApi(neucore_api.ApiClient(configuration))
request_body = NULL # list[int] | EVE alliance IDs array.

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
 **request_body** | [**list[int]**](list.md)| EVE alliance IDs array. | 

### Return type

[**list[Alliance]**](Alliance.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alliance_groups_v1**
> list[Group] alliance_groups_v1(aid)

Return groups of the alliance.

Needs role: app-groups.<br>Returns only groups that have been added to the app as well.

### Example

* Api Key Authentication (Bearer): 
```python
from __future__ import print_function
import time
import neucore_api
from neucore_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = neucore_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = neucore_api.ApplicationApi(neucore_api.ApiClient(configuration))
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

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alliance_groups_v2**
> list[Group] alliance_groups_v2(aid)

Return groups of the alliance.

Needs role: app-groups.<br>Returns only groups that have been added to the app as well.

### Example

* Api Key Authentication (Bearer): 
```python
from __future__ import print_function
import time
import neucore_api
from neucore_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = neucore_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = neucore_api.ApplicationApi(neucore_api.ApiClient(configuration))
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

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **characters_v1**
> list[Character] characters_v1(character_id)

Return all characters of the player account to which the character ID belongs.

Needs role: app-chars.

### Example

* Api Key Authentication (Bearer): 
```python
from __future__ import print_function
import time
import neucore_api
from neucore_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = neucore_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = neucore_api.ApplicationApi(neucore_api.ApiClient(configuration))
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

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **corp_groups_bulk_v1**
> list[Corporation] corp_groups_bulk_v1(request_body)

Return groups of multiple corporations.

Needs role: app-groups.<br>      *                  Returns only groups that have been added to the app as well.      *                  Skips corporations that are not found in the local database.

### Example

* Api Key Authentication (Bearer): 
```python
from __future__ import print_function
import time
import neucore_api
from neucore_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = neucore_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = neucore_api.ApplicationApi(neucore_api.ApiClient(configuration))
request_body = NULL # list[int] | EVE corporation IDs array.

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
 **request_body** | [**list[int]**](list.md)| EVE corporation IDs array. | 

### Return type

[**list[Corporation]**](Corporation.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **corp_groups_v1**
> list[Group] corp_groups_v1(cid)

Return groups of the corporation.

Needs role: app-groups.<br>Returns only groups that have been added to the app as well.

### Example

* Api Key Authentication (Bearer): 
```python
from __future__ import print_function
import time
import neucore_api
from neucore_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = neucore_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = neucore_api.ApplicationApi(neucore_api.ApiClient(configuration))
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

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **corp_groups_v2**
> list[Group] corp_groups_v2(cid)

Return groups of the corporation.

Needs role: app-groups.<br>Returns only groups that have been added to the app as well.

### Example

* Api Key Authentication (Bearer): 
```python
from __future__ import print_function
import time
import neucore_api
from neucore_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = neucore_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = neucore_api.ApplicationApi(neucore_api.ApiClient(configuration))
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

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esi_post_v1**
> str esi_post_v1(esi_path_query, datasource, body)

Makes an ESI POST request on behalf on an EVE character and returns the result.

Needs role: app-esi<br>      *         Public ESI routes are not allowed.<br>      *         The following headers from ESI are passed through to the response:                Content-Type Expires X-Esi-Error-Limit-Remain X-Esi-Error-Limit-Reset X-Pages warning<br>      *         The HTTP status code from ESI is also passed through, so maybe there's more than the documented.<br>      *         The ESI path and query parameters can alternatively be appended to the path of this endpoint,                see doc/app-esi-examples.php for more.

### Example

* Api Key Authentication (Bearer): 
```python
from __future__ import print_function
import time
import neucore_api
from neucore_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = neucore_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = neucore_api.ApplicationApi(neucore_api.ApiClient(configuration))
esi_path_query = 'esi_path_query_example' # str | The ESI path and query string (without the datasource parameter).
datasource = 'datasource_example' # str | The EVE character ID those token should be used to make the ESI request
body = 'body_example' # str | JSON encoded data.

try:
    # Makes an ESI POST request on behalf on an EVE character and returns the result.
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

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esi_v1**
> str esi_v1(esi_path_query, datasource)

Makes an ESI GET request on behalf on an EVE character and returns the result.

Needs role: app-esi<br>      *         Public ESI routes are not allowed.<br>      *         The following headers from ESI are passed through to the response:                Content-Type Expires X-Esi-Error-Limit-Remain X-Esi-Error-Limit-Reset X-Pages warning<br>      *         The HTTP status code from ESI is also passed through, so maybe there's more than the documented.<br>      *         The ESI path and query parameters can alternatively be appended to the path of this endpoint,                see doc/app-esi-examples.php for more.

### Example

* Api Key Authentication (Bearer): 
```python
from __future__ import print_function
import time
import neucore_api
from neucore_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = neucore_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = neucore_api.ApplicationApi(neucore_api.ApiClient(configuration))
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

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_bulk_v1**
> list[CharacterGroups] groups_bulk_v1(request_body)

Return groups of multiple players, identified by one of their character IDs.

Needs role: app-groups.<br>      *                  Returns only groups that have been added to the app as well.      *                  Skips characters that are not found in the local database.

### Example

* Api Key Authentication (Bearer): 
```python
from __future__ import print_function
import time
import neucore_api
from neucore_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = neucore_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = neucore_api.ApplicationApi(neucore_api.ApiClient(configuration))
request_body = NULL # list[int] | EVE character IDs array.

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
 **request_body** | [**list[int]**](list.md)| EVE character IDs array. | 

### Return type

[**list[CharacterGroups]**](CharacterGroups.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_v1**
> list[Group] groups_v1(cid)

Return groups of the character's player account.

Needs role: app-groups.<br>Returns only groups that have been added to the app as well.

### Example

* Api Key Authentication (Bearer): 
```python
from __future__ import print_function
import time
import neucore_api
from neucore_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = neucore_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = neucore_api.ApplicationApi(neucore_api.ApiClient(configuration))
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

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_v2**
> list[Group] groups_v2(cid)

Return groups of the character's player account.

Needs role: app-groups.<br>Returns only groups that have been added to the app as well.

### Example

* Api Key Authentication (Bearer): 
```python
from __future__ import print_function
import time
import neucore_api
from neucore_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = neucore_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = neucore_api.ApplicationApi(neucore_api.ApiClient(configuration))
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

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_with_fallback_v1**
> list[Group] groups_with_fallback_v1(character, corporation, alliance=alliance)

Returns groups from the character's account, if available, or the corporation and alliance.

Needs role: app-groups.<br>      *                  Returns only groups that have been added to the app as well.<br>      *                  It is not checked if character, corporation and alliance match.

### Example

* Api Key Authentication (Bearer): 
```python
from __future__ import print_function
import time
import neucore_api
from neucore_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = neucore_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = neucore_api.ApplicationApi(neucore_api.ApiClient(configuration))
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

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **main_v1**
> Character main_v1(cid)

Returns the main character of the player account to which the character ID belongs.

Needs role: app-chars.<br>It is possible that an account has no main character.

### Example

* Api Key Authentication (Bearer): 
```python
from __future__ import print_function
import time
import neucore_api
from neucore_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = neucore_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = neucore_api.ApplicationApi(neucore_api.ApiClient(configuration))
cid = 56 # int | EVE character ID.

try:
    # Returns the main character of the player account to which the character ID belongs.
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

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **main_v2**
> Character main_v2(cid)

Return the main character of the player account to which the character ID belongs.

Needs role: app-chars.<br>It is possible that an account has no main character.

### Example

* Api Key Authentication (Bearer): 
```python
from __future__ import print_function
import time
import neucore_api
from neucore_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = neucore_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = neucore_api.ApplicationApi(neucore_api.ApiClient(configuration))
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

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **member_tracking_v1**
> list[CorporationMember] member_tracking_v1(id, inactive=inactive, active=active)

Return corporation member tracking data.

Needs role: app-tracking

### Example

* Api Key Authentication (Bearer): 
```python
from __future__ import print_function
import time
import neucore_api
from neucore_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = neucore_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = neucore_api.ApplicationApi(neucore_api.ApiClient(configuration))
id = 56 # int | EVE corporation ID.
inactive = 56 # int | Limit to members who have been inactive for x days or longer. (optional)
active = 56 # int | Limit to members who were active in the last x days. (optional)

try:
    # Return corporation member tracking data.
    api_response = api_instance.member_tracking_v1(id, inactive=inactive, active=active)
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

### Return type

[**list[CorporationMember]**](CorporationMember.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **removed_characters_v1**
> list[RemovedCharacter] removed_characters_v1(character_id)

Return all characters that were removed from the player account to which the character ID belongs.

Needs role: app-chars.

### Example

* Api Key Authentication (Bearer): 
```python
from __future__ import print_function
import time
import neucore_api
from neucore_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = neucore_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = neucore_api.ApplicationApi(neucore_api.ApiClient(configuration))
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

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_v1**
> App show_v1()

Show app information.

Needs role: app

### Example

* Api Key Authentication (Bearer): 
```python
from __future__ import print_function
import time
import neucore_api
from neucore_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = neucore_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = neucore_api.ApplicationApi(neucore_api.ApiClient(configuration))

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

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

