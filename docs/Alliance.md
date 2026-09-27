# Alliance

EVE Alliance.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | EVE alliance ID. | 
**name** | **str** | EVE alliance name. | 
**ticker** | **str** | Alliance ticker. | 
**groups** | [**List[Group]**](Group.md) | Groups for automatic assignment (API: not included by default). | [optional] 

## Example

```python
from neucore_api.models.alliance import Alliance

# TODO update the JSON string below
json = "{}"
# create an instance of Alliance from a JSON string
alliance_instance = Alliance.from_json(json)
# print the JSON string representation of the object
print(Alliance.to_json())

# convert the object into a dict
alliance_dict = alliance_instance.to_dict()
# create an instance of Alliance from a dict
alliance_from_dict = Alliance.from_dict(alliance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


