# App


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | App ID | 
**name** | **str** | App name | 
**roles** | [**List[Role]**](Role.md) | Roles for authorisation. | [optional] 
**groups** | [**List[Group]**](Group.md) | Groups the app can see. | [optional] 
**eve_logins** | [**List[EveLogin]**](EveLogin.md) |  | [optional] 

## Example

```python
from neucore_api.models.app import App

# TODO update the JSON string below
json = "{}"
# create an instance of App from a JSON string
app_instance = App.from_json(json)
# print the JSON string representation of the object
print(App.to_json())

# convert the object into a dict
app_dict = app_instance.to_dict()
# create an instance of App from a dict
app_from_dict = App.from_dict(app_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


