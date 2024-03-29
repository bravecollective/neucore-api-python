# neucore_api.ApplicationCharactersApi

All URIs are relative to *https://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**character_list_v1**](ApplicationCharactersApi.md#character_list_v1) | **POST** /app/v1/character-list | Returns all known characters from the parameter list.
[**characters_bulk_v1**](ApplicationCharactersApi.md#characters_bulk_v1) | **POST** /app/v1/characters | Returns all characters from multiple player accounts identified by character IDs.
[**characters_v1**](ApplicationCharactersApi.md#characters_v1) | **GET** /app/v1/characters/{characterId} | Returns all characters of the player account to which the character ID belongs.
[**corporation_characters_v1**](ApplicationCharactersApi.md#corporation_characters_v1) | **GET** /app/v1/corp-characters/{corporationId} | Returns a list of all known characters from the corporation.
[**corporation_players_v1**](ApplicationCharactersApi.md#corporation_players_v1) | **GET** /app/v1/corp-players/{corporationId} | Returns a list of all players that have a character in the corporation.
[**incoming_characters_v1**](ApplicationCharactersApi.md#incoming_characters_v1) | **GET** /app/v1/incoming-characters/{characterId} | Returns all characters that were moved from another account to the player account to which the                     ID belongs.
[**main_v1**](ApplicationCharactersApi.md#main_v1) | **GET** /app/v1/main/{cid} | Returns the main character of the player account to which the character ID belongs.
[**main_v2**](ApplicationCharactersApi.md#main_v2) | **GET** /app/v2/main/{cid} | Returns the main character of the player account to which the character ID belongs.
[**player_characters_v1**](ApplicationCharactersApi.md#player_characters_v1) | **GET** /app/v1/player-chars/{playerId} | Returns all characters from the player account.
[**player_v1**](ApplicationCharactersApi.md#player_v1) | **GET** /app/v1/player/{characterId} | Returns the player account to which the character ID belongs.
[**player_with_characters_v1**](ApplicationCharactersApi.md#player_with_characters_v1) | **GET** /app/v1/player-with-characters/{characterId} | Returns the player account to which the character ID belongs with all characters.
[**players_v1**](ApplicationCharactersApi.md#players_v1) | **POST** /app/v1/players | Returns player accounts identified by character IDs. Can contain the same player several times.
[**removed_characters_v1**](ApplicationCharactersApi.md#removed_characters_v1) | **GET** /app/v1/removed-characters/{characterId} | Returns all characters that were removed from the player account to which the character ID                     belongs.


# **character_list_v1**
> [Character] character_list_v1(request_body)

Returns all known characters from the parameter list.

Needs role: app-chars.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import neucore_api
from neucore_api.api import application_characters_api
from neucore_api.model.character import Character
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
    api_instance = application_characters_api.ApplicationCharactersApi(api_client)
    request_body = [
        1,
    ] # [int] | Array with EVE character IDs.

    # example passing only required values which don't have defaults set
    try:
        # Returns all known characters from the parameter list.
        api_response = api_instance.character_list_v1(request_body)
        pprint(api_response)
    except neucore_api.ApiException as e:
        print("Exception when calling ApplicationCharactersApi->character_list_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | **[int]**| Array with EVE character IDs. |

### Return type

[**[Character]**](Character.md)

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
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **characters_bulk_v1**
> [[int]] characters_bulk_v1(request_body)

Returns all characters from multiple player accounts identified by character IDs.

Needs role: app-chars.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import neucore_api
from neucore_api.api import application_characters_api
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
    api_instance = application_characters_api.ApplicationCharactersApi(api_client)
    request_body = [
        1,
    ] # [int] | EVE character IDs array.

    # example passing only required values which don't have defaults set
    try:
        # Returns all characters from multiple player accounts identified by character IDs.
        api_response = api_instance.characters_bulk_v1(request_body)
        pprint(api_response)
    except neucore_api.ApiException as e:
        print("Exception when calling ApplicationCharactersApi->characters_bulk_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | **[int]**| EVE character IDs array. |

### Return type

**[[int]]**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Invalid body. |  -  |
**200** | All characters from the player account. |  -  |
**403** | Not authorized. |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **characters_v1**
> [Character] characters_v1(character_id)

Returns all characters of the player account to which the character ID belongs.

Needs role: app-chars.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import neucore_api
from neucore_api.api import application_characters_api
from neucore_api.model.character import Character
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
    api_instance = application_characters_api.ApplicationCharactersApi(api_client)
    character_id = 1 # int | EVE character ID.

    # example passing only required values which don't have defaults set
    try:
        # Returns all characters of the player account to which the character ID belongs.
        api_response = api_instance.characters_v1(character_id)
        pprint(api_response)
    except neucore_api.ApiException as e:
        print("Exception when calling ApplicationCharactersApi->characters_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| EVE character ID. |

### Return type

[**[Character]**](Character.md)

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
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **corporation_characters_v1**
> [Character] corporation_characters_v1(corporation_id)

Returns a list of all known characters from the corporation.

Needs role: app-chars.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import neucore_api
from neucore_api.api import application_characters_api
from neucore_api.model.character import Character
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
    api_instance = application_characters_api.ApplicationCharactersApi(api_client)
    corporation_id = 1 # int | EVE corporation ID.

    # example passing only required values which don't have defaults set
    try:
        # Returns a list of all known characters from the corporation.
        api_response = api_instance.corporation_characters_v1(corporation_id)
        pprint(api_response)
    except neucore_api.ApiException as e:
        print("Exception when calling ApplicationCharactersApi->corporation_characters_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corporation_id** | **int**| EVE corporation ID. |

### Return type

[**[Character]**](Character.md)

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
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **corporation_players_v1**
> [Player] corporation_players_v1(corporation_id)

Returns a list of all players that have a character in the corporation.

Needs role: app-chars.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import neucore_api
from neucore_api.api import application_characters_api
from neucore_api.model.player import Player
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
    api_instance = application_characters_api.ApplicationCharactersApi(api_client)
    corporation_id = 1 # int | EVE corporation ID.

    # example passing only required values which don't have defaults set
    try:
        # Returns a list of all players that have a character in the corporation.
        api_response = api_instance.corporation_players_v1(corporation_id)
        pprint(api_response)
    except neucore_api.ApiException as e:
        print("Exception when calling ApplicationCharactersApi->corporation_players_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corporation_id** | **int**| EVE corporation ID. |

### Return type

[**[Player]**](Player.md)

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
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **incoming_characters_v1**
> [RemovedCharacter] incoming_characters_v1(character_id)

Returns all characters that were moved from another account to the player account to which the                     ID belongs.

Needs role: app-chars.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import neucore_api
from neucore_api.api import application_characters_api
from neucore_api.model.removed_character import RemovedCharacter
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
    api_instance = application_characters_api.ApplicationCharactersApi(api_client)
    character_id = 1 # int | EVE character ID.

    # example passing only required values which don't have defaults set
    try:
        # Returns all characters that were moved from another account to the player account to which the                     ID belongs.
        api_response = api_instance.incoming_characters_v1(character_id)
        pprint(api_response)
    except neucore_api.ApiException as e:
        print("Exception when calling ApplicationCharactersApi->incoming_characters_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| EVE character ID. |

### Return type

[**[RemovedCharacter]**](RemovedCharacter.md)

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
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **main_v1**
> Character main_v1(cid)

Returns the main character of the player account to which the character ID belongs.

Needs role: app-chars.<br>It is possible that an account has no main character.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import neucore_api
from neucore_api.api import application_characters_api
from neucore_api.model.character import Character
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
    api_instance = application_characters_api.ApplicationCharactersApi(api_client)
    cid = 1 # int | EVE character ID.

    # example passing only required values which don't have defaults set
    try:
        # Returns the main character of the player account to which the character ID belongs.
        api_response = api_instance.main_v1(cid)
        pprint(api_response)
    except neucore_api.ApiException as e:
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
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **main_v2**
> Character main_v2(cid)

Returns the main character of the player account to which the character ID belongs.

Needs role: app-chars.<br>It is possible that an account has no main character.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import neucore_api
from neucore_api.api import application_characters_api
from neucore_api.model.character import Character
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
    api_instance = application_characters_api.ApplicationCharactersApi(api_client)
    cid = 1 # int | EVE character ID.

    # example passing only required values which don't have defaults set
    try:
        # Returns the main character of the player account to which the character ID belongs.
        api_response = api_instance.main_v2(cid)
        pprint(api_response)
    except neucore_api.ApiException as e:
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
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **player_characters_v1**
> [Character] player_characters_v1(player_id)

Returns all characters from the player account.

Needs role: app-chars.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import neucore_api
from neucore_api.api import application_characters_api
from neucore_api.model.character import Character
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
    api_instance = application_characters_api.ApplicationCharactersApi(api_client)
    player_id = 1 # int | Player ID.

    # example passing only required values which don't have defaults set
    try:
        # Returns all characters from the player account.
        api_response = api_instance.player_characters_v1(player_id)
        pprint(api_response)
    except neucore_api.ApiException as e:
        print("Exception when calling ApplicationCharactersApi->player_characters_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **player_id** | **int**| Player ID. |

### Return type

[**[Character]**](Character.md)

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
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **player_v1**
> Player player_v1(character_id)

Returns the player account to which the character ID belongs.

Needs role: app-chars.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import neucore_api
from neucore_api.api import application_characters_api
from neucore_api.model.player import Player
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
    api_instance = application_characters_api.ApplicationCharactersApi(api_client)
    character_id = 1 # int | EVE character ID.

    # example passing only required values which don't have defaults set
    try:
        # Returns the player account to which the character ID belongs.
        api_response = api_instance.player_v1(character_id)
        pprint(api_response)
    except neucore_api.ApiException as e:
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
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **player_with_characters_v1**
> Player player_with_characters_v1(character_id)

Returns the player account to which the character ID belongs with all characters.

Needs role: app-chars.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import neucore_api
from neucore_api.api import application_characters_api
from neucore_api.model.player import Player
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
    api_instance = application_characters_api.ApplicationCharactersApi(api_client)
    character_id = 1 # int | EVE character ID.

    # example passing only required values which don't have defaults set
    try:
        # Returns the player account to which the character ID belongs with all characters.
        api_response = api_instance.player_with_characters_v1(character_id)
        pprint(api_response)
    except neucore_api.ApiException as e:
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
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **players_v1**
> [PlayerWithCharcterId] players_v1(request_body)

Returns player accounts identified by character IDs. Can contain the same player several times.

Needs role: app-chars.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import neucore_api
from neucore_api.api import application_characters_api
from neucore_api.model.player_with_charcter_id import PlayerWithCharcterId
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
    api_instance = application_characters_api.ApplicationCharactersApi(api_client)
    request_body = [
        1,
    ] # [int] | EVE character IDs array.

    # example passing only required values which don't have defaults set
    try:
        # Returns player accounts identified by character IDs. Can contain the same player several times.
        api_response = api_instance.players_v1(request_body)
        pprint(api_response)
    except neucore_api.ApiException as e:
        print("Exception when calling ApplicationCharactersApi->players_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | **[int]**| EVE character IDs array. |

### Return type

[**[PlayerWithCharcterId]**](PlayerWithCharcterId.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | One entry for each character ID that was provided and found. |  -  |
**400** | Invalid body. |  -  |
**403** | Not authorized. |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **removed_characters_v1**
> [RemovedCharacter] removed_characters_v1(character_id)

Returns all characters that were removed from the player account to which the character ID                     belongs.

Needs role: app-chars.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import neucore_api
from neucore_api.api import application_characters_api
from neucore_api.model.removed_character import RemovedCharacter
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
    api_instance = application_characters_api.ApplicationCharactersApi(api_client)
    character_id = 1 # int | EVE character ID.

    # example passing only required values which don't have defaults set
    try:
        # Returns all characters that were removed from the player account to which the character ID                     belongs.
        api_response = api_instance.removed_characters_v1(character_id)
        pprint(api_response)
    except neucore_api.ApiException as e:
        print("Exception when calling ApplicationCharactersApi->removed_characters_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| EVE character ID. |

### Return type

[**[RemovedCharacter]**](RemovedCharacter.md)

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
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

