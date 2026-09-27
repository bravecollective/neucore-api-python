# HourlyAppRequests


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **int** |  | 
**app_name** | **str** |  | 
**requests** | **int** |  | 
**year** | **int** |  | 
**month** | **int** |  | 
**day_of_month** | **int** |  | 
**hour** | **int** |  | 

## Example

```python
from neucore_api.models.hourly_app_requests import HourlyAppRequests

# TODO update the JSON string below
json = "{}"
# create an instance of HourlyAppRequests from a JSON string
hourly_app_requests_instance = HourlyAppRequests.from_json(json)
# print the JSON string representation of the object
print(HourlyAppRequests.to_json())

# convert the object into a dict
hourly_app_requests_dict = hourly_app_requests_instance.to_dict()
# create an instance of HourlyAppRequests from a dict
hourly_app_requests_from_dict = HourlyAppRequests.from_dict(hourly_app_requests_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


