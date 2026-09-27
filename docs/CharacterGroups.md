# CharacterGroups


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**character** | [**Character**](Character.md) |  | 
**groups** | [**List[Group]**](Group.md) |  | 
**deactivated** | **str** | Groups deactivation status. | 

## Example

```python
from neucore_api.models.character_groups import CharacterGroups

# TODO update the JSON string below
json = "{}"
# create an instance of CharacterGroups from a JSON string
character_groups_instance = CharacterGroups.from_json(json)
# print the JSON string representation of the object
print(CharacterGroups.to_json())

# convert the object into a dict
character_groups_dict = character_groups_instance.to_dict()
# create an instance of CharacterGroups from a dict
character_groups_from_dict = CharacterGroups.from_dict(character_groups_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


