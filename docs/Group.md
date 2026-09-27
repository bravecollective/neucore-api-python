# Group


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Group ID. | 
**name** | **str** | A unique group name (can be changed). | 
**description** | **str** |  | [optional] 
**visibility** | **str** |  | [optional] 
**auto_accept** | **bool** |  | [optional] 
**is_default** | **bool** |  | [optional] 
**is_auto_managed** | **bool** | API: The value of this property is not always set. | [optional] 

## Example

```python
from neucore_api.models.group import Group

# TODO update the JSON string below
json = "{}"
# create an instance of Group from a JSON string
group_instance = Group.from_json(json)
# print the JSON string representation of the object
print(Group.to_json())

# convert the object into a dict
group_dict = group_instance.to_dict()
# create an instance of Group from a dict
group_from_dict = Group.from_dict(group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


