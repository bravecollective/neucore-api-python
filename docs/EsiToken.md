# EsiToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eve_login_id** | **int** | ID of EveLogin | 
**character_id** | **int** | ID of Character | 
**player_id** | **int** | ID of Player | 
**player_name** | **str** | Name of Player | [optional] 
**character** | [**Character**](Character.md) |  | [optional] 
**valid_token** | **bool** | Shows if the refresh token is valid or not.  This is null if there is no refresh token (EVE SSOv1 only) or a valid token but without scopes (SSOv2). | 
**valid_token_time** | **datetime** | Date and time when the valid token property was last changed. | 
**has_roles** | **bool** | Shows if the EVE character has all required roles for the login.  Null if the login does not require any roles or if the token is invalid. | 
**last_checked** | **datetime** | When the refresh token was last checked for validity. | [optional] 

## Example

```python
from neucore_api.models.esi_token import EsiToken

# TODO update the JSON string below
json = "{}"
# create an instance of EsiToken from a JSON string
esi_token_instance = EsiToken.from_json(json)
# print the JSON string representation of the object
print(EsiToken.to_json())

# convert the object into a dict
esi_token_dict = esi_token_instance.to_dict()
# create an instance of EsiToken from a dict
esi_token_from_dict = EsiToken.from_dict(esi_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


