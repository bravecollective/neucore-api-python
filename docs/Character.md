# Character


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | EVE character ID. | 
**name** | **str** | EVE character name. | 
**main** | **bool** |  | [optional] 
**valid_token** | **bool, none_type** | Shows if character&#39;s refresh token is valid or not.  This is null if there is no refresh token (EVE SSOv1 only) or a valid token but without scopes (SSOv2). | [optional] 
**valid_token_time** | **datetime, none_type** | Date and time when that valid token property was last changed. | [optional] 
**created** | **datetime, none_type** |  | [optional] 
**last_update** | **datetime, none_type** | Last ESI update. | [optional] 
**corporation** | [**Corporation**](Corporation.md) |  | [optional] 
**character_name_changes** | [**[CharacterNameChange]**](CharacterNameChange.md) | List of previous character names (API: not included by default). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


