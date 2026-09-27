# EsiType

An EVE name from the category \"inventory_type\".

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 

## Example

```python
from neucore_api.models.esi_type import EsiType

# TODO update the JSON string below
json = "{}"
# create an instance of EsiType from a JSON string
esi_type_instance = EsiType.from_json(json)
# print the JSON string representation of the object
print(EsiType.to_json())

# convert the object into a dict
esi_type_dict = esi_type_instance.to_dict()
# create an instance of EsiType from a dict
esi_type_from_dict = EsiType.from_dict(esi_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


