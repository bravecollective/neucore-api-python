# neucore_api.ApplicationESIApi

All URIs are relative to *https://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**esi_access_token_v1**](ApplicationESIApi.md#esi_access_token_v1) | **GET** /app/v1/esi/access-token/{characterId} | Returns an access token for a character and EVE login.
[**esi_eve_login_characters_v1**](ApplicationESIApi.md#esi_eve_login_characters_v1) | **GET** /app/v1/esi/eve-login/{name}/characters | Returns character IDs of characters that have an ESI token (including invalid) of an EVE login.
[**esi_eve_login_token_data_v1**](ApplicationESIApi.md#esi_eve_login_token_data_v1) | **GET** /app/v1/esi/eve-login/{name}/token-data | Returns data for all valid tokens (roles are also checked if applicable) for an EVE login.
[**esi_post_v1**](ApplicationESIApi.md#esi_post_v1) | **POST** /app/v1/esi | See POST /app/v2/esi
[**esi_post_v2**](ApplicationESIApi.md#esi_post_v2) | **POST** /app/v2/esi | Same as GET /app/v2/esi, but for POST requests.
[**esi_v1**](ApplicationESIApi.md#esi_v1) | **GET** /app/v1/esi | See GET /app/v2/esi
[**esi_v2**](ApplicationESIApi.md#esi_v2) | **GET** /app/v2/esi | Makes an ESI GET request on behalf on an EVE character and returns the result.


# **esi_access_token_v1**
> EsiAccessToken esi_access_token_v1(character_id)

Returns an access token for a character and EVE login.

Needs role: app-esi-token

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import neucore_api
from neucore_api.api import application_esi_api
from neucore_api.model.esi_access_token import EsiAccessToken
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
    api_instance = application_esi_api.ApplicationESIApi(api_client)
    character_id = 1 # int | The EVE character ID.
    eve_login_name = "2" # str | Optional EVE login name, defaults to 'core.default'. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns an access token for a character and EVE login.
        api_response = api_instance.esi_access_token_v1(character_id)
        pprint(api_response)
    except neucore_api.ApiException as e:
        print("Exception when calling ApplicationESIApi->esi_access_token_v1: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns an access token for a character and EVE login.
        api_response = api_instance.esi_access_token_v1(character_id, eve_login_name=eve_login_name)
        pprint(api_response)
    except neucore_api.ApiException as e:
        print("Exception when calling ApplicationESIApi->esi_access_token_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| The EVE character ID. |
 **eve_login_name** | **str**| Optional EVE login name, defaults to &#39;core.default&#39;. | [optional]

### Return type

[**EsiAccessToken**](EsiAccessToken.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**204** | Invalid token. |  -  |
**403** | Forbidden |  -  |
**404** | ESI token not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esi_eve_login_characters_v1**
> [int] esi_eve_login_characters_v1(name)

Returns character IDs of characters that have an ESI token (including invalid) of an EVE login.

Needs role: app-esi-login.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import neucore_api
from neucore_api.api import application_esi_api
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
    api_instance = application_esi_api.ApplicationESIApi(api_client)
    name = "2" # str | EVE login name.

    # example passing only required values which don't have defaults set
    try:
        # Returns character IDs of characters that have an ESI token (including invalid) of an EVE login.
        api_response = api_instance.esi_eve_login_characters_v1(name)
        pprint(api_response)
    except neucore_api.ApiException as e:
        print("Exception when calling ApplicationESIApi->esi_eve_login_characters_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| EVE login name. |

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
**200** |  |  -  |
**403** | Forbidden |  -  |
**404** | EVE login not found. |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esi_eve_login_token_data_v1**
> [EsiTokenData] esi_eve_login_token_data_v1(name)

Returns data for all valid tokens (roles are also checked if applicable) for an EVE login.

Needs role: app-esi-login.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import neucore_api
from neucore_api.api import application_esi_api
from neucore_api.model.esi_token_data import EsiTokenData
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
    api_instance = application_esi_api.ApplicationESIApi(api_client)
    name = "2" # str | EVE login name, 'core.default' is not allowed.

    # example passing only required values which don't have defaults set
    try:
        # Returns data for all valid tokens (roles are also checked if applicable) for an EVE login.
        api_response = api_instance.esi_eve_login_token_data_v1(name)
        pprint(api_response)
    except neucore_api.ApiException as e:
        print("Exception when calling ApplicationESIApi->esi_eve_login_token_data_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| EVE login name, &#39;core.default&#39; is not allowed. |

### Return type

[**[EsiTokenData]**](EsiTokenData.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**403** | Forbidden |  -  |
**404** | EVE login not found. |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esi_post_v1**
> str esi_post_v1(esi_path_query, datasource, body)

See POST /app/v2/esi

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import neucore_api
from neucore_api.api import application_esi_api
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
    api_instance = application_esi_api.ApplicationESIApi(api_client)
    esi_path_query = "esi-path-query_example" # str | 
    datasource = "datasource_example" # str | 
    body = "body_example" # str | 
    neucore_eve_character = "Neucore-EveCharacter_example" # str | The EVE character ID those token should be used. Has priority over the query      *                       parameter 'datasource' (optional)
    neucore_eve_login = "Neucore-EveLogin_example" # str | The EVE login name from which the token should be used, defaults to core.default. (optional)

    # example passing only required values which don't have defaults set
    try:
        # See POST /app/v2/esi
        api_response = api_instance.esi_post_v1(esi_path_query, datasource, body)
        pprint(api_response)
    except neucore_api.ApiException as e:
        print("Exception when calling ApplicationESIApi->esi_post_v1: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # See POST /app/v2/esi
        api_response = api_instance.esi_post_v1(esi_path_query, datasource, body, neucore_eve_character=neucore_eve_character, neucore_eve_login=neucore_eve_login)
        pprint(api_response)
    except neucore_api.ApiException as e:
        print("Exception when calling ApplicationESIApi->esi_post_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **esi_path_query** | **str**|  |
 **datasource** | **str**|  |
 **body** | **str**|  |
 **neucore_eve_character** | **str**| The EVE character ID those token should be used. Has priority over the query      *                       parameter &#39;datasource&#39; | [optional]
 **neucore_eve_login** | **str**| The EVE login name from which the token should be used, defaults to core.default. | [optional]

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
**200** |  |  * Expires -  <br>  |
**304** |  |  * Expires -  <br>  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**420** |  |  -  |
**429** | Too many errors, see reason phrase for more. |  -  |
**500** |  |  -  |
**503** |  |  -  |
**504** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esi_post_v2**
> str esi_post_v2(esi_path_query, datasource, body)

Same as GET /app/v2/esi, but for POST requests.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import neucore_api
from neucore_api.api import application_esi_api
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
    api_instance = application_esi_api.ApplicationESIApi(api_client)
    esi_path_query = "esi-path-query_example" # str | 
    datasource = "datasource_example" # str | 
    body = "body_example" # str | JSON encoded data.
    neucore_eve_character = "Neucore-EveCharacter_example" # str | The EVE character ID those token should be used. Has priority over the query      *                       parameter 'datasource' (optional)
    neucore_eve_login = "Neucore-EveLogin_example" # str | The EVE login name from which the token should be used, defaults to core.default. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Same as GET /app/v2/esi, but for POST requests.
        api_response = api_instance.esi_post_v2(esi_path_query, datasource, body)
        pprint(api_response)
    except neucore_api.ApiException as e:
        print("Exception when calling ApplicationESIApi->esi_post_v2: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Same as GET /app/v2/esi, but for POST requests.
        api_response = api_instance.esi_post_v2(esi_path_query, datasource, body, neucore_eve_character=neucore_eve_character, neucore_eve_login=neucore_eve_login)
        pprint(api_response)
    except neucore_api.ApiException as e:
        print("Exception when calling ApplicationESIApi->esi_post_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **esi_path_query** | **str**|  |
 **datasource** | **str**|  |
 **body** | **str**| JSON encoded data. |
 **neucore_eve_character** | **str**| The EVE character ID those token should be used. Has priority over the query      *                       parameter &#39;datasource&#39; | [optional]
 **neucore_eve_login** | **str**| The EVE login name from which the token should be used, defaults to core.default. | [optional]

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
**200** |  |  * Expires -  <br>  |
**304** |  |  * Expires -  <br>  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**420** |  |  -  |
**429** |  |  * Retry-After - Delay in seconds. <br>  |
**500** |  |  -  |
**503** |  |  -  |
**504** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esi_v1**
> str esi_v1(esi_path_query, datasource)

See GET /app/v2/esi

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import neucore_api
from neucore_api.api import application_esi_api
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
    api_instance = application_esi_api.ApplicationESIApi(api_client)
    esi_path_query = "esi-path-query_example" # str | 
    datasource = "datasource_example" # str | 
    neucore_eve_character = "Neucore-EveCharacter_example" # str | The EVE character ID those token should be used. Has priority over the query      *                       parameter 'datasource' (optional)
    neucore_eve_login = "Neucore-EveLogin_example" # str | The EVE login name from which the token should be used, defaults to core.default. (optional)

    # example passing only required values which don't have defaults set
    try:
        # See GET /app/v2/esi
        api_response = api_instance.esi_v1(esi_path_query, datasource)
        pprint(api_response)
    except neucore_api.ApiException as e:
        print("Exception when calling ApplicationESIApi->esi_v1: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # See GET /app/v2/esi
        api_response = api_instance.esi_v1(esi_path_query, datasource, neucore_eve_character=neucore_eve_character, neucore_eve_login=neucore_eve_login)
        pprint(api_response)
    except neucore_api.ApiException as e:
        print("Exception when calling ApplicationESIApi->esi_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **esi_path_query** | **str**|  |
 **datasource** | **str**|  |
 **neucore_eve_character** | **str**| The EVE character ID those token should be used. Has priority over the query      *                       parameter &#39;datasource&#39; | [optional]
 **neucore_eve_login** | **str**| The EVE login name from which the token should be used, defaults to core.default. | [optional]

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
**200** |  |  * Expires -  <br>  |
**304** |  |  * Expires -  <br>  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**420** |  |  -  |
**429** | Too many errors, see reason phrase for more. |  -  |
**500** |  |  -  |
**503** |  |  -  |
**504** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esi_v2**
> str esi_v2(esi_path_query)

Makes an ESI GET request on behalf on an EVE character and returns the result.

Needs role: app-esi-proxy<br>      *         Either the header 'Neucore-EveCharacter' and optionally 'Neucore-EveLogin' or the query parameter                'datasource' is required.<br>      *         Public ESI routes are not allowed.<br>      *         The following headers from ESI are passed through to the response if they exist:                Content-Type Expires X-Esi-Error-Limit-Remain X-Esi-Error-Limit-Reset X-Pages warning, Warning<br>      *         The HTTP status code from ESI is also passed through, so there may be more than the documented ones.<br>      *         The ESI path and query parameters can alternatively be appended to the path of this endpoint,                this allows to use OpenAPI clients that were generated for the ESI API,                see doc/api-examples for more.

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import neucore_api
from neucore_api.api import application_esi_api
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
    api_instance = application_esi_api.ApplicationESIApi(api_client)
    esi_path_query = "esi-path-query_example" # str | The ESI path and query string (without the datasource parameter).
    neucore_eve_character = "Neucore-EveCharacter_example" # str | The EVE character ID those token should be used. Has priority over the query                             parameter 'datasource' (optional)
    neucore_eve_login = "Neucore-EveLogin_example" # str | The EVE login name from which the token should be used, defaults to core.default. (optional)
    datasource = "datasource_example" # str | The EVE character ID those token should be used from the default login to make the ESI                             request. Optionally followed by a colon and the name of an EVE login to use an alternative                             ESI token. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Makes an ESI GET request on behalf on an EVE character and returns the result.
        api_response = api_instance.esi_v2(esi_path_query)
        pprint(api_response)
    except neucore_api.ApiException as e:
        print("Exception when calling ApplicationESIApi->esi_v2: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Makes an ESI GET request on behalf on an EVE character and returns the result.
        api_response = api_instance.esi_v2(esi_path_query, neucore_eve_character=neucore_eve_character, neucore_eve_login=neucore_eve_login, datasource=datasource)
        pprint(api_response)
    except neucore_api.ApiException as e:
        print("Exception when calling ApplicationESIApi->esi_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **esi_path_query** | **str**| The ESI path and query string (without the datasource parameter). |
 **neucore_eve_character** | **str**| The EVE character ID those token should be used. Has priority over the query                             parameter &#39;datasource&#39; | [optional]
 **neucore_eve_login** | **str**| The EVE login name from which the token should be used, defaults to core.default. | [optional]
 **datasource** | **str**| The EVE character ID those token should be used from the default login to make the ESI                             request. Optionally followed by a colon and the name of an EVE login to use an alternative                             ESI token. | [optional]

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
**200** | The data from ESI.&lt;br&gt;                             Please note that the JSON schema type can be an object, array or number etc.,                             unfortunately there is no way to document this. |  * Expires -  <br>  |
**304** | Not modified |  * Expires -  <br>  |
**400** | Bad request, see reason phrase and/or body for more. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**420** | Error limited |  -  |
**429** | Too many errors, see body for more. |  * Retry-After - Delay in seconds. <br>  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

