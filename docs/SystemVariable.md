# SystemVariable

A system settings variable.  This is also used as a storage for Storage\\Variables with the prefix \"__storage__\" if APCu is not available.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Variable name. | 
**value** | **str** | Variable value. | 

## Example

```python
from neucore_api.models.system_variable import SystemVariable

# TODO update the JSON string below
json = "{}"
# create an instance of SystemVariable from a JSON string
system_variable_instance = SystemVariable.from_json(json)
# print the JSON string representation of the object
print(SystemVariable.to_json())

# convert the object into a dict
system_variable_dict = system_variable_instance.to_dict()
# create an instance of SystemVariable from a dict
system_variable_from_dict = SystemVariable.from_dict(system_variable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


