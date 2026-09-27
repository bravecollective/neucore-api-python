# EsiAccessToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | 
**scopes** | **List[str]** |  | 
**expires** | **int** |  | 

## Example

```python
from neucore_api.models.esi_access_token import EsiAccessToken

# TODO update the JSON string below
json = "{}"
# create an instance of EsiAccessToken from a JSON string
esi_access_token_instance = EsiAccessToken.from_json(json)
# print the JSON string representation of the object
print(EsiAccessToken.to_json())

# convert the object into a dict
esi_access_token_dict = esi_access_token_instance.to_dict()
# create an instance of EsiAccessToken from a dict
esi_access_token_from_dict = EsiAccessToken.from_dict(esi_access_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


