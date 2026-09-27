# Corporation

EVE corporation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | EVE corporation ID. | 
**name** | **str** | EVE corporation name. | 
**ticker** | **str** | Corporation ticker. | 
**alliance** | [**Alliance**](Alliance.md) |  | [optional] 
**groups** | [**List[Group]**](Group.md) | Groups for automatic assignment (API: not included by default). | [optional] 
**tracking_last_update** | **datetime** | Last update of corporation member tracking data (API: not included by default). | [optional] 
**auto_allowlist** | **bool** | True if this corporation was automatically placed on the allowlist of a watchlist (API: not included by default). | [optional] 

## Example

```python
from neucore_api.models.corporation import Corporation

# TODO update the JSON string below
json = "{}"
# create an instance of Corporation from a JSON string
corporation_instance = Corporation.from_json(json)
# print the JSON string representation of the object
print(Corporation.to_json())

# convert the object into a dict
corporation_dict = corporation_instance.to_dict()
# create an instance of Corporation from a dict
corporation_from_dict = Corporation.from_dict(corporation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


