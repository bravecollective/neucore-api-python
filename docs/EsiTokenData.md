# EsiTokenData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_checked** | **str** |  | 
**character_id** | **int** |  | 
**character_name** | **str** |  | 
**corporation_id** | **int** |  | 
**alliance_id** | **int** |  | 

## Example

```python
from neucore_api.models.esi_token_data import EsiTokenData

# TODO update the JSON string below
json = "{}"
# create an instance of EsiTokenData from a JSON string
esi_token_data_instance = EsiTokenData.from_json(json)
# print the JSON string representation of the object
print(EsiTokenData.to_json())

# convert the object into a dict
esi_token_data_dict = esi_token_data_instance.to_dict()
# create an instance of EsiTokenData from a dict
esi_token_data_from_dict = EsiTokenData.from_dict(esi_token_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


