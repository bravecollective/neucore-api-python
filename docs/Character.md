# Character


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int, none_type** | EVE character ID. | 
**name** | **str** | EVE character name. | 
**valid_token** | **bool, none_type** | Shows if character&#39;s default refresh token is valid or not.                         This is null if there is no refresh token (EVE SSOv1 only)                         or a valid token but without scopes (SSOv2). | [optional] 
**valid_token_time** | **datetime, none_type** | Date and time when the valid token property of the default token was last changed. | [optional] 
**token_last_checked** | **datetime, none_type** | Date and time when the default token was last checked. | [optional] 
**main** | **bool** |  | [optional] 
**esi_tokens** | [**[EsiToken]**](EsiToken.md) | ESI tokens of the character (API: not included by default). | [optional] 
**created** | **datetime, none_type** |  | [optional] 
**last_update** | **datetime, none_type** | Last ESI update. | [optional] 
**corporation** | [**Corporation**](Corporation.md) |  | [optional] 
**character_name_changes** | [**[CharacterNameChange]**](CharacterNameChange.md) | List of previous character names (API: not included by default). | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


