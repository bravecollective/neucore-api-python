# neucore_api.ApplicationApi

All URIs are relative to *https://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**show_v1**](ApplicationApi.md#show_v1) | **GET** /app/v1/show | Show app information.


# **show_v1**
> App show_v1()

Show app information.

Needs role: app

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import neucore_api
from neucore_api.api import application_api
from neucore_api.model.app import App
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
    api_instance = application_api.ApplicationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Show app information.
        api_response = api_instance.show_v1()
        pprint(api_response)
    except neucore_api.ApiException as e:
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

