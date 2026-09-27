# PluginConfigurationDatabase

Plugin configuration stored in database.  API: The required properties are necessary for the service page where users register their account. The rest is necessary for the admin page.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**directory_name** | **str** | Directory where the plugin.yml file is stored.  Only from database but always set when the data from the file is read. | [optional] 
**urls** | [**List[PluginConfigurationURL]**](PluginConfigurationURL.md) |  | 
**text_top** | **str** |  | 
**text_account** | **str** |  | 
**text_register** | **str** |  | 
**text_pending** | **str** |  | 
**configuration_data** | **str** |  | 
**active** | **bool** | Inactive plugins are neither updated by the cron job nor displayed to the user.  From admin UI. | [optional] 
**required_groups** | **List[int]** | From admin UI. | [optional] 

## Example

```python
from neucore_api.models.plugin_configuration_database import PluginConfigurationDatabase

# TODO update the JSON string below
json = "{}"
# create an instance of PluginConfigurationDatabase from a JSON string
plugin_configuration_database_instance = PluginConfigurationDatabase.from_json(json)
# print the JSON string representation of the object
print(PluginConfigurationDatabase.to_json())

# convert the object into a dict
plugin_configuration_database_dict = plugin_configuration_database_instance.to_dict()
# create an instance of PluginConfigurationDatabase from a dict
plugin_configuration_database_from_dict = PluginConfigurationDatabase.from_dict(plugin_configuration_database_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


