# neucore_api.ApplicationESIApi

All URIs are relative to *https://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**esi_post_v1**](ApplicationESIApi.md#esi_post_v1) | **POST** /app/v1/esi | Same as GET /app/v1/esi, but for POST requests.
[**esi_v1**](ApplicationESIApi.md#esi_v1) | **GET** /app/v1/esi | Makes an ESI GET request on behalf on an EVE character and returns the result.


# **esi_post_v1**
> str esi_post_v1(esi_path_query, datasource, body)

Same as GET /app/v1/esi, but for POST requests.

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
    api_instance = neucore_api.ApplicationESIApi(api_client)
    esi_path_query = 'esi_path_query_example' # str | The ESI path and query string (without the datasource parameter).
datasource = 'datasource_example' # str | The EVE character ID those token should be used to make the ESI request
body = 'body_example' # str | JSON encoded data.

    try:
        # Same as GET /app/v1/esi, but for POST requests.
        api_response = api_instance.esi_post_v1(esi_path_query, datasource, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationESIApi->esi_post_v1: %s\n" % e)
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
**429** | Maximum permissible ESI error limit reached (X-Esi-Error-Limit-Remain &lt;&#x3D; 20)                             or API rate limit exceeded. |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esi_v1**
> str esi_v1(esi_path_query, datasource)

Makes an ESI GET request on behalf on an EVE character and returns the result.

Needs role: app-esi<br>      *         Public ESI routes are not allowed.<br>      *         The following headers from ESI are passed through to the response if they exist:                Content-Type Expires X-Esi-Error-Limit-Remain X-Esi-Error-Limit-Reset X-Pages warning, Warning<br>      *         The HTTP status code from ESI is also passed through, so there may be more than the documented ones.<br>      *         The ESI path and query parameters can alternatively be appended to the path of this endpoint,                this allows to use OpenAPI clients that were generated for the ESI API,                see doc/app-esi-examples.php for more.

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
    api_instance = neucore_api.ApplicationESIApi(api_client)
    esi_path_query = 'esi_path_query_example' # str | The ESI path and query string (without the datasource parameter).
datasource = 'datasource_example' # str | The EVE character ID those token should be used to make the ESI request

    try:
        # Makes an ESI GET request on behalf on an EVE character and returns the result.
        api_response = api_instance.esi_v1(esi_path_query, datasource)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationESIApi->esi_v1: %s\n" % e)
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
**429** | Maximum permissible ESI error limit reached (X-Esi-Error-Limit-Remain &lt;&#x3D; 20)                             or API rate limit exceeded. |  -  |
**500** | Internal server error |  -  |
**503** | Service unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

