# PluginConfigurationURL


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | placeholders: {plugin_id}, {username}, {password}, {email} | 
**title** | **str** |  | 
**target** | **str** |  | 

## Example

```python
from neucore_api.models.plugin_configuration_url import PluginConfigurationURL

# TODO update the JSON string below
json = "{}"
# create an instance of PluginConfigurationURL from a JSON string
plugin_configuration_url_instance = PluginConfigurationURL.from_json(json)
# print the JSON string representation of the object
print(PluginConfigurationURL.to_json())

# convert the object into a dict
plugin_configuration_url_dict = plugin_configuration_url_instance.to_dict()
# create an instance of PluginConfigurationURL from a dict
plugin_configuration_url_from_dict = PluginConfigurationURL.from_dict(plugin_configuration_url_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


