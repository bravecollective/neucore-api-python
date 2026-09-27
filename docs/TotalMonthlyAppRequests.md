# TotalMonthlyAppRequests


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requests** | **int** |  | 
**year** | **int** |  | 
**month** | **int** |  | 

## Example

```python
from neucore_api.models.total_monthly_app_requests import TotalMonthlyAppRequests

# TODO update the JSON string below
json = "{}"
# create an instance of TotalMonthlyAppRequests from a JSON string
total_monthly_app_requests_instance = TotalMonthlyAppRequests.from_json(json)
# print the JSON string representation of the object
print(TotalMonthlyAppRequests.to_json())

# convert the object into a dict
total_monthly_app_requests_dict = total_monthly_app_requests_instance.to_dict()
# create an instance of TotalMonthlyAppRequests from a dict
total_monthly_app_requests_from_dict = TotalMonthlyAppRequests.from_dict(total_monthly_app_requests_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


