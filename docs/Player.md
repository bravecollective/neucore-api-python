# Player


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int, none_type** |  | 
**name** | **str** | A name for the player.  This is the EVE character name of the current main character or of the last main character if there is currently none. | 
**service_accounts** | [**[ServiceAccount]**](ServiceAccount.md) | External service accounts (API: not included by default) | [optional] 
**corporation_name** | **str** | Corporation of main character (API: not included by default) | [optional] 
**status** | **str** | Player account status. | [optional] 
**roles** | [**[Role]**](Role.md) | Roles for authorization. | [optional] 
**characters** | [**[Character]**](Character.md) |  | [optional] 
**groups** | [**[Group]**](Group.md) | Group membership. | [optional] 
**manager_groups** | [**[Group]**](Group.md) | Manager of groups. | [optional] 
**manager_apps** | [**[App]**](App.md) | Manager of apps. | [optional] 
**removed_characters** | [**[RemovedCharacter]**](RemovedCharacter.md) | Characters that were removed from a player (API: not included by default). | [optional] 
**incoming_characters** | [**[RemovedCharacter]**](RemovedCharacter.md) | Characters that were moved from another player account to this account (API: not included by default). | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


