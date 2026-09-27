# neucore_api.ApplicationMCPApi

All URIs are relative to *https://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mcp_v1**](ApplicationMCPApi.md#mcp_v1) | **POST** /app/v1/mcp | The Neucore MCP server.


# **mcp_v1**
> str mcp_v1(mcp_protocol_version, mcp_method, mcp_name=mcp_name, body=body)

The Neucore MCP server.

Needs role: app-mcp.

### Example

* Bearer Authentication (BearerAuth):

```python
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
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with neucore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = neucore_api.ApplicationMCPApi(api_client)
    mcp_protocol_version = 'mcp_protocol_version_example' # str | The MCP protocol version for this request (e.g., \"2026-07-28\").
    mcp_method = 'mcp_method_example' # str | Must mirror the JSON-RPC method in the request body (e.g., \"tools/list\", \"tools/call\", \"server/discover\").
    mcp_name = 'mcp_name_example' # str | Required for tools/call and prompts/get: mirrors the tool or prompt name from the body. (optional)
    body = None # object | JSON encoded MCP request body. (optional)

    try:
        # The Neucore MCP server.
        api_response = api_instance.mcp_v1(mcp_protocol_version, mcp_method, mcp_name=mcp_name, body=body)
        print("The response of ApplicationMCPApi->mcp_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationMCPApi->mcp_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mcp_protocol_version** | **str**| The MCP protocol version for this request (e.g., \&quot;2026-07-28\&quot;). | 
 **mcp_method** | **str**| Must mirror the JSON-RPC method in the request body (e.g., \&quot;tools/list\&quot;, \&quot;tools/call\&quot;, \&quot;server/discover\&quot;). | 
 **mcp_name** | **str**| Required for tools/call and prompts/get: mirrors the tool or prompt name from the body. | [optional] 
 **body** | **object**| JSON encoded MCP request body. | [optional] 

### Return type

**str**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MCP response. |  -  |
**204** | Accepted. No outgoing messages at this time. |  -  |
**400** | Bad Request (e.g., unsupported protocol version). |  -  |
**403** | Not authorized. |  -  |
**429** | Too Many Requests. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

