# EsiToken


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eve_login_id** | **int** | ID of EveLogin | 
**character_id** | **int** | ID of Character | 
**player_id** | **int** | ID of Player | 
**valid_token** | **bool, none_type** | Shows if the refresh token is valid or not.  This is null if there is no refresh token (EVE SSOv1 only) or a valid token but without scopes (SSOv2). | 
**valid_token_time** | **datetime, none_type** | Date and time when the valid token property was last changed. | 
**has_roles** | **bool, none_type** | Shows if the EVE character has all required roles for the login.  Null if the login does not require any roles or if the token is invalid. | 
**player_name** | **str** | Name of Player | [optional] 
**character** | [**Character**](Character.md) |  | [optional] 
**last_checked** | **datetime, none_type** | When the refresh token was last checked for validity. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


