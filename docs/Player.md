# Player


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_accounts** | [**List[ServiceAccount]**](ServiceAccount.md) | External service accounts (API: not included by default) | [optional] 
**character_id** | **int** | ID of main character (API: not included by default) | [optional] 
**corporation_name** | **str** | Corporation of main character (API: not included by default) | [optional] 
**alliance_name** | **str** | Alliance of main character (API: not included by default) | [optional] 
**id** | **int** |  | 
**name** | **str** | A name for the player.  This is the EVE character name of the current main character or the most recent main character, if there isn&#39;t one at the moment. | 
**status** | **str** | Player account status. | [optional] 
**roles** | [**List[Role]**](Role.md) | Roles for authorisation. | [optional] 
**characters** | [**List[Character]**](Character.md) |  | [optional] 
**groups** | [**List[Group]**](Group.md) | Group membership. | [optional] 
**manager_groups** | [**List[Group]**](Group.md) | Manager of groups. | [optional] 
**manager_apps** | [**List[App]**](App.md) | Manager of apps. | [optional] 
**removed_characters** | [**List[RemovedCharacter]**](RemovedCharacter.md) | Characters that were removed from a player (API: not included by default). | [optional] 
**incoming_characters** | [**List[RemovedCharacter]**](RemovedCharacter.md) | Characters that were moved from another player account to this account (API: not included by default). | [optional] 

## Example

```python
from neucore_api.models.player import Player

# TODO update the JSON string below
json = "{}"
# create an instance of Player from a JSON string
player_instance = Player.from_json(json)
# print the JSON string representation of the object
print(Player.to_json())

# convert the object into a dict
player_dict = player_instance.to_dict()
# create an instance of Player from a dict
player_from_dict = Player.from_dict(player_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


