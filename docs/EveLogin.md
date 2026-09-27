# EveLogin


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** | Names starting with &#39;core.&#39; are reserved for internal use. | 
**description** | **str** |  | 
**esi_scopes** | **str** |  | 
**eve_roles** | **List[str]** | Maximum length of all roles separated by comma: 1024. | 

## Example

```python
from neucore_api.models.eve_login import EveLogin

# TODO update the JSON string below
json = "{}"
# create an instance of EveLogin from a JSON string
eve_login_instance = EveLogin.from_json(json)
# print the JSON string representation of the object
print(EveLogin.to_json())

# convert the object into a dict
eve_login_dict = eve_login_instance.to_dict()
# create an instance of EveLogin from a dict
eve_login_from_dict = EveLogin.from_dict(eve_login_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


