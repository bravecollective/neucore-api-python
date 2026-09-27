# Character


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**valid_token** | **bool** | Shows if character&#39;s default refresh token is valid or not. This is null if there is no refresh token (EVE SSOv1 only) or a valid token but without scopes (SSOv2). | [optional] 
**valid_token_time** | **datetime** | Date and time when the valid token property of the default token was last changed. | [optional] 
**token_last_checked** | **datetime** | Date and time when the default token was last checked. | [optional] 
**id** | **int** | EVE character ID. | 
**name** | **str** | EVE character name. | 
**main** | **bool** |  | [optional] 
**esi_tokens** | [**List[EsiToken]**](EsiToken.md) | ESI tokens of the character (API: not included by default). | [optional] 
**created** | **datetime** |  | [optional] 
**last_update** | **datetime** | Last ESI update. | [optional] 
**corporation** | [**Corporation**](Corporation.md) |  | [optional] 
**character_name_changes** | [**List[CharacterNameChange]**](CharacterNameChange.md) | List of previous character names (API: not included by default). | [optional] 

## Example

```python
from neucore_api.models.character import Character

# TODO update the JSON string below
json = "{}"
# create an instance of Character from a JSON string
character_instance = Character.from_json(json)
# print the JSON string representation of the object
print(Character.to_json())

# convert the object into a dict
character_dict = character_instance.to_dict()
# create an instance of Character from a dict
character_from_dict = Character.from_dict(character_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


