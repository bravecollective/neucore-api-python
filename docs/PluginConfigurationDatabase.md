# PluginConfigurationDatabase

Plugin configuration stored in database.  API: The required properties are necessary for the service page where users register their account. The rest is necessary for the admin page.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**urls** | [**[PluginConfigurationURL]**](PluginConfigurationURL.md) |  | 
**text_top** | **str** |  | 
**text_account** | **str** |  | 
**text_register** | **str** |  | 
**text_pending** | **str** |  | 
**configuration_data** | **str** |  | 
**directory_name** | **str** | Directory where the plugin.yml file is stored.  Only from database but always set when the data from the file is read. | [optional] 
**active** | **bool** | Inactive plugins are neither updated by the cron job nor displayed to the user.  From admin UI. | [optional] 
**required_groups** | **[int]** | From admin UI. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


