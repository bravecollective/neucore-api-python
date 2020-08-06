# neucore_api.ApplicationCharactersApi

All URIs are relative to *https://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**character_list_v1**](ApplicationCharactersApi.md#character_list_v1) | **POST** /app/v1/character-list | Returns all known characters from the parameter list.
[**characters_v1**](ApplicationCharactersApi.md#characters_v1) | **GET** /app/v1/characters/{characterId} | Returns all characters of the player account to which the character ID belongs.
[**corporation_characters_v1**](ApplicationCharactersApi.md#corporation_characters_v1) | **GET** /app/v1/corp-characters/{corporationId} | Returns a list of all known characters from the corporation.
[**corporation_players_v1**](ApplicationCharactersApi.md#corporation_players_v1) | **GET** /app/v1/corp-players/{corporationId} | Returns a list of all players that have a character in the corporation.
[**incoming_characters_v1**](ApplicationCharactersApi.md#incoming_characters_v1) | **GET** /app/v1/incoming-characters/{characterId} | Returns all characters that were moved from another account to the player account to which the                     ID belongs.
[**main_v1**](ApplicationCharactersApi.md#main_v1) | **GET** /app/v1/main/{cid} | Returns the main character of the player account to which the character ID belongs.
[**main_v2**](ApplicationCharactersApi.md#main_v2) | **GET** /app/v2/main/{cid} | Returns the main character of the player account to which the character ID belongs.
[**player_characters_v1**](ApplicationCharactersApi.md#player_characters_v1) | **GET** /app/v1/player-chars/{playerId} | Returns all characters from the player account.
[**player_v1**](ApplicationCharactersApi.md#player_v1) | **GET** /app/v1/player/{characterId} | Returns the player account to which the character ID belongs.
[**player_with_characters_v1**](ApplicationCharactersApi.md#player_with_characters_v1) | **GET** /app/v1/player-with-characters/{characterId} | Returns the player account to which the character ID belongs with all characters.
[**removed_characters_v1**](ApplicationCharactersApi.md#removed_characters_v1) | **GET** /app/v1/removed-characters/{characterId} | Returns all characters that were removed from the player account to which the character ID                     belongs.


# **character_list_v1**
> list[Character] character_list_v1(request_body)

Returns all known characters from the parameter list.

Needs role: app-chars.

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import neucore_api
from neucore_api.rest import ApiException
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
    api_instance = neucore_api.ApplicationCharactersApi(api_client)
    request_body = [56] # list[int] | Array with EVE character IDs.

    try:
        # Returns all known characters from the parameter list.
        api_response = api_instance.character_list_v1(request_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationCharactersApi->character_list_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**list[int]**](int.md)| Array with EVE character IDs. | 

### Return type

[**list[Character]**](Character.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of characters (does not include the corporation property). |  -  |
**400** | Invalid body. |  -  |
**403** | Not authorized. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **characters_v1**
> list[Character] characters_v1(character_id)

Returns all characters of the player account to which the character ID belongs.

Needs role: app-chars.

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import neucore_api
from neucore_api.rest import ApiException
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
    api_instance = neucore_api.ApplicationCharactersApi(api_client)
    character_id = 56 # int | EVE character ID.

    try:
        # Returns all characters of the player account to which the character ID belongs.
        api_response = api_instance.characters_v1(character_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationCharactersApi->characters_v1: %s\n" % e)
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
**404** | Character not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **corporation_characters_v1**
> list[Character] corporation_characters_v1(corporation_id)

Returns a list of all known characters from the corporation.

Needs role: app-chars.

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import neucore_api
from neucore_api.rest import ApiException
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
    api_instance = neucore_api.ApplicationCharactersApi(api_client)
    corporation_id = 56 # int | EVE corporation ID.

    try:
        # Returns a list of all known characters from the corporation.
        api_response = api_instance.corporation_characters_v1(corporation_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationCharactersApi->corporation_characters_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corporation_id** | **int**| EVE corporation ID. | 

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
**200** | List of characters (does not include the corporation property). |  -  |
**403** | Not authorized. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **corporation_players_v1**
> list[Player] corporation_players_v1(corporation_id)

Returns a list of all players that have a character in the corporation.

Needs role: app-chars.

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import neucore_api
from neucore_api.rest import ApiException
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
    api_instance = neucore_api.ApplicationCharactersApi(api_client)
    corporation_id = 56 # int | EVE corporation ID.

    try:
        # Returns a list of all players that have a character in the corporation.
        api_response = api_instance.corporation_players_v1(corporation_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationCharactersApi->corporation_players_v1: %s\n" % e)
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

# **incoming_characters_v1**
> list[RemovedCharacter] incoming_characters_v1(character_id)

Returns all characters that were moved from another account to the player account to which the                     ID belongs.

Needs role: app-chars.

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import neucore_api
from neucore_api.rest import ApiException
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
    api_instance = neucore_api.ApplicationCharactersApi(api_client)
    character_id = 56 # int | EVE character ID.

    try:
        # Returns all characters that were moved from another account to the player account to which the                     ID belongs.
        api_response = api_instance.incoming_characters_v1(character_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationCharactersApi->incoming_characters_v1: %s\n" % e)
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
**404** | Character not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **main_v1**
> Character main_v1(cid)

Returns the main character of the player account to which the character ID belongs.

Needs role: app-chars.<br>It is possible that an account has no main character.

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import neucore_api
from neucore_api.rest import ApiException
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
    api_instance = neucore_api.ApplicationCharactersApi(api_client)
    cid = 56 # int | EVE character ID.

    try:
        # Returns the main character of the player account to which the character ID belongs.
        api_response = api_instance.main_v1(cid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationCharactersApi->main_v1: %s\n" % e)
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
**404** | Character not found. (default reason phrase) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **main_v2**
> Character main_v2(cid)

Returns the main character of the player account to which the character ID belongs.

Needs role: app-chars.<br>It is possible that an account has no main character.

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import neucore_api
from neucore_api.rest import ApiException
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
    api_instance = neucore_api.ApplicationCharactersApi(api_client)
    cid = 56 # int | EVE character ID.

    try:
        # Returns the main character of the player account to which the character ID belongs.
        api_response = api_instance.main_v2(cid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationCharactersApi->main_v2: %s\n" % e)
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

# **player_characters_v1**
> list[Character] player_characters_v1(player_id)

Returns all characters from the player account.

Needs role: app-chars.

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import neucore_api
from neucore_api.rest import ApiException
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
    api_instance = neucore_api.ApplicationCharactersApi(api_client)
    player_id = 56 # int | Player ID.

    try:
        # Returns all characters from the player account.
        api_response = api_instance.player_characters_v1(player_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationCharactersApi->player_characters_v1: %s\n" % e)
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

Returns the player account to which the character ID belongs.

Needs role: app-chars.

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import neucore_api
from neucore_api.rest import ApiException
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
    api_instance = neucore_api.ApplicationCharactersApi(api_client)
    character_id = 56 # int | EVE character ID.

    try:
        # Returns the player account to which the character ID belongs.
        api_response = api_instance.player_v1(character_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationCharactersApi->player_v1: %s\n" % e)
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

# **player_with_characters_v1**
> Player player_with_characters_v1(character_id)

Returns the player account to which the character ID belongs with all characters.

Needs role: app-chars.

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import neucore_api
from neucore_api.rest import ApiException
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
    api_instance = neucore_api.ApplicationCharactersApi(api_client)
    character_id = 56 # int | EVE character ID.

    try:
        # Returns the player account to which the character ID belongs with all characters.
        api_response = api_instance.player_with_characters_v1(character_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationCharactersApi->player_with_characters_v1: %s\n" % e)
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
**200** | The player, only id, name and characters properties are returned. |  -  |
**403** | Not authorized. |  -  |
**404** | Character not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **removed_characters_v1**
> list[RemovedCharacter] removed_characters_v1(character_id)

Returns all characters that were removed from the player account to which the character ID                     belongs.

Needs role: app-chars.

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import neucore_api
from neucore_api.rest import ApiException
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
    api_instance = neucore_api.ApplicationCharactersApi(api_client)
    character_id = 56 # int | EVE character ID.

    try:
        # Returns all characters that were removed from the player account to which the character ID                     belongs.
        api_response = api_instance.removed_characters_v1(character_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationCharactersApi->removed_characters_v1: %s\n" % e)
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
**404** | Character not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

