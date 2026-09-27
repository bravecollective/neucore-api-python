# Watchlist


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**lock_watchlist_settings** | **bool** |  | [optional] 

## Example

```python
from neucore_api.models.watchlist import Watchlist

# TODO update the JSON string below
json = "{}"
# create an instance of Watchlist from a JSON string
watchlist_instance = Watchlist.from_json(json)
# print the JSON string representation of the object
print(Watchlist.to_json())

# convert the object into a dict
watchlist_dict = watchlist_instance.to_dict()
# create an instance of Watchlist from a dict
watchlist_from_dict = Watchlist.from_dict(watchlist_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


