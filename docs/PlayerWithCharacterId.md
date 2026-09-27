# PlayerWithCharacterId


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**character_id** | **int** |  | 

## Example

```python
from neucore_api.models.player_with_character_id import PlayerWithCharacterId

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerWithCharacterId from a JSON string
player_with_character_id_instance = PlayerWithCharacterId.from_json(json)
# print the JSON string representation of the object
print(PlayerWithCharacterId.to_json())

# convert the object into a dict
player_with_character_id_dict = player_with_character_id_instance.to_dict()
# create an instance of PlayerWithCharacterId from a dict
player_with_character_id_from_dict = PlayerWithCharacterId.from_dict(player_with_character_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


