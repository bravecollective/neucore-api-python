# RemovedCharacter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_player_id** | **int** |  | [optional] 
**new_player_name** | **str** |  | [optional] 
**player** | [**Player**](Player.md) |  | [optional] 
**character_id** | **int** | EVE character ID. | 
**character_name** | **str** | EVE character name. | 
**removed_date** | **datetime** | Date of removal. | 
**reason** | **str** | How it was removed (deleted or moved to another account). | 
**deleted_by** | [**Player**](Player.md) |  | [optional] 

## Example

```python
from neucore_api.models.removed_character import RemovedCharacter

# TODO update the JSON string below
json = "{}"
# create an instance of RemovedCharacter from a JSON string
removed_character_instance = RemovedCharacter.from_json(json)
# print the JSON string representation of the object
print(RemovedCharacter.to_json())

# convert the object into a dict
removed_character_dict = removed_character_instance.to_dict()
# create an instance of RemovedCharacter from a dict
removed_character_from_dict = RemovedCharacter.from_dict(removed_character_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


