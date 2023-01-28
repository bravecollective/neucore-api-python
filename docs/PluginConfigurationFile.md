# PluginConfigurationFile

Plugin configuration from YAML file.  API: The required properties are necessary for the service page where users register their account. The rest is necessary for the admin page.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**properties** | **[str]** |  | 
**actions** | **[str]** |  | 
**directory_name** | **str** | Directory where the plugin.yml file is stored.  Only from database but always set when the data from the file is read. | [optional] 
**urls** | [**[PluginConfigurationURL]**](PluginConfigurationURL.md) |  | [optional] 
**text_top** | **str** |  | [optional] 
**text_account** | **str** |  | [optional] 
**text_register** | **str** |  | [optional] 
**text_pending** | **str** |  | [optional] 
**configuration_data** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**types** | **[str]** | Not part of the file but will be set when the plugin implementation is loaded. | [optional] 
**one_account** | **bool** |  | [optional] 
**show_password** | **bool** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


