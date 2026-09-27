# EsiLocation

An EVE location (System, Station, Structure, ...)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**category** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from neucore_api.models.esi_location import EsiLocation

# TODO update the JSON string below
json = "{}"
# create an instance of EsiLocation from a JSON string
esi_location_instance = EsiLocation.from_json(json)
# print the JSON string representation of the object
print(EsiLocation.to_json())

# convert the object into a dict
esi_location_dict = esi_location_instance.to_dict()
# create an instance of EsiLocation from a dict
esi_location_from_dict = EsiLocation.from_dict(esi_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


