# neucore_api.ApplicationTrackingApi

All URIs are relative to *https://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**member_tracking_v1**](ApplicationTrackingApi.md#member_tracking_v1) | **GET** /app/v1/corporation/{id}/member-tracking | Return corporation member tracking data.


# **member_tracking_v1**
> [CorporationMember] member_tracking_v1(id)

Return corporation member tracking data.

Needs role: app-tracking

### Example

* Bearer Authentication (BearerAuth):

```python
import time
import neucore_api
from neucore_api.api import application_tracking_api
from neucore_api.model.corporation_member import CorporationMember
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
    api_instance = application_tracking_api.ApplicationTrackingApi(api_client)
    id = 1 # int | EVE corporation ID.
    inactive = 1 # int | Limit to members who have been inactive for x days or longer. (optional)
    active = 1 # int | Limit to members who were active in the last x days. (optional)
    account = "true" # str | Limit to members with (true) or without (false) an account. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Return corporation member tracking data.
        api_response = api_instance.member_tracking_v1(id)
        pprint(api_response)
    except neucore_api.ApiException as e:
        print("Exception when calling ApplicationTrackingApi->member_tracking_v1: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Return corporation member tracking data.
        api_response = api_instance.member_tracking_v1(id, inactive=inactive, active=active, account=account)
        pprint(api_response)
    except neucore_api.ApiException as e:
        print("Exception when calling ApplicationTrackingApi->member_tracking_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| EVE corporation ID. |
 **inactive** | **int**| Limit to members who have been inactive for x days or longer. | [optional]
 **active** | **int**| Limit to members who were active in the last x days. | [optional]
 **account** | **str**| Limit to members with (true) or without (false) an account. | [optional]

### Return type

[**[CorporationMember]**](CorporationMember.md)

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
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

