# TotalDailyAppRequests


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requests** | **int** |  | 
**year** | **int** |  | 
**month** | **int** |  | 
**day_of_month** | **int** |  | 

## Example

```python
from neucore_api.models.total_daily_app_requests import TotalDailyAppRequests

# TODO update the JSON string below
json = "{}"
# create an instance of TotalDailyAppRequests from a JSON string
total_daily_app_requests_instance = TotalDailyAppRequests.from_json(json)
# print the JSON string representation of the object
print(TotalDailyAppRequests.to_json())

# convert the object into a dict
total_daily_app_requests_dict = total_daily_app_requests_instance.to_dict()
# create an instance of TotalDailyAppRequests from a dict
total_daily_app_requests_from_dict = TotalDailyAppRequests.from_dict(total_daily_app_requests_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


