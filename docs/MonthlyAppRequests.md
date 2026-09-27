# MonthlyAppRequests


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **int** |  | 
**app_name** | **str** |  | 
**requests** | **int** |  | 
**year** | **int** |  | 
**month** | **int** |  | 

## Example

```python
from neucore_api.models.monthly_app_requests import MonthlyAppRequests

# TODO update the JSON string below
json = "{}"
# create an instance of MonthlyAppRequests from a JSON string
monthly_app_requests_instance = MonthlyAppRequests.from_json(json)
# print the JSON string representation of the object
print(MonthlyAppRequests.to_json())

# convert the object into a dict
monthly_app_requests_dict = monthly_app_requests_instance.to_dict()
# create an instance of MonthlyAppRequests from a dict
monthly_app_requests_from_dict = MonthlyAppRequests.from_dict(monthly_app_requests_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


