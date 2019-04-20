# Player

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** | A name for the player.  This is the EVE character name of the current main character or of the last main character if there is currently none. | 
**status** | **str** | Player account status. | [optional] 
**roles** | [**list[Role]**](Role.md) | Roles for authorization. | [optional] 
**characters** | [**list[Character]**](Character.md) |  | [optional] 
**groups** | [**list[Group]**](Group.md) | Group membership. | [optional] 
**manager_groups** | [**list[Group]**](Group.md) | Manager of groups. | [optional] 
**manager_apps** | [**list[App]**](App.md) | Manager of apps. | [optional] 
**removed_characters** | [**list[RemovedCharacter]**](RemovedCharacter.md) | Characters that were removed from a player (API: not included by default). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


