# PluginConfigurationFile

Plugin configuration from YAML file.  API: The required properties are necessary for the service page where users register their account. The rest is necessary for the admin page.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**directory_name** | **str** | Directory where the plugin.yml file is stored.  Only from database but always set when the data from the file is read. | [optional] 
**urls** | [**List[PluginConfigurationURL]**](PluginConfigurationURL.md) |  | [optional] 
**text_top** | **str** |  | [optional] 
**text_account** | **str** |  | [optional] 
**text_register** | **str** |  | [optional] 
**text_pending** | **str** |  | [optional] 
**configuration_data** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**types** | **List[str]** | Not part of the file but will be set when the plugin implementation is loaded. | [optional] 
**one_account** | **bool** |  | [optional] 
**properties** | **List[str]** |  | 
**show_password** | **bool** |  | [optional] 
**actions** | **List[str]** |  | 

## Example

```python
from neucore_api.models.plugin_configuration_file import PluginConfigurationFile

# TODO update the JSON string below
json = "{}"
# create an instance of PluginConfigurationFile from a JSON string
plugin_configuration_file_instance = PluginConfigurationFile.from_json(json)
# print the JSON string representation of the object
print(PluginConfigurationFile.to_json())

# convert the object into a dict
plugin_configuration_file_dict = plugin_configuration_file_instance.to_dict()
# create an instance of PluginConfigurationFile from a dict
plugin_configuration_file_from_dict = PluginConfigurationFile.from_dict(plugin_configuration_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


