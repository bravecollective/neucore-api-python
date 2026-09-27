# CharacterNameChange

A previous character name.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**old_name** | **str** |  | 
**change_date** | **datetime** |  | 

## Example

```python
from neucore_api.models.character_name_change import CharacterNameChange

# TODO update the JSON string below
json = "{}"
# create an instance of CharacterNameChange from a JSON string
character_name_change_instance = CharacterNameChange.from_json(json)
# print the JSON string representation of the object
print(CharacterNameChange.to_json())

# convert the object into a dict
character_name_change_dict = character_name_change_instance.to_dict()
# create an instance of CharacterNameChange from a dict
character_name_change_from_dict = CharacterNameChange.from_dict(character_name_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


