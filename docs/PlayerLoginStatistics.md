# PlayerLoginStatistics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unique_logins** | **int** |  | 
**total_logins** | **int** |  | 
**year** | **int** |  | 
**month** | **int** |  | 

## Example

```python
from neucore_api.models.player_login_statistics import PlayerLoginStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerLoginStatistics from a JSON string
player_login_statistics_instance = PlayerLoginStatistics.from_json(json)
# print the JSON string representation of the object
print(PlayerLoginStatistics.to_json())

# convert the object into a dict
player_login_statistics_dict = player_login_statistics_instance.to_dict()
# create an instance of PlayerLoginStatistics from a dict
player_login_statistics_from_dict = PlayerLoginStatistics.from_dict(player_login_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


