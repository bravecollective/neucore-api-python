# GroupApplication

The player property contains only id and name.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**player** | [**Player**](Player.md) |  | 
**group** | [**Group**](Group.md) |  | 
**created** | **datetime** |  | 
**status** | **str** | Group application status. | [optional] 

## Example

```python
from neucore_api.models.group_application import GroupApplication

# TODO update the JSON string below
json = "{}"
# create an instance of GroupApplication from a JSON string
group_application_instance = GroupApplication.from_json(json)
# print the JSON string representation of the object
print(GroupApplication.to_json())

# convert the object into a dict
group_application_dict = group_application_instance.to_dict()
# create an instance of GroupApplication from a dict
group_application_from_dict = GroupApplication.from_dict(group_application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


