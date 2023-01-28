# CorporationMember

The player property contains only id and name, character does not contain corporation.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int, none_type** | EVE Character ID. | 
**name** | **str, none_type** | EVE Character name. | 
**player** | [**Player**](Player.md) |  | [optional] 
**location** | [**EsiLocation**](EsiLocation.md) |  | [optional] 
**logoff_date** | **datetime, none_type** |  | [optional] 
**logon_date** | **datetime, none_type** |  | [optional] 
**ship_type** | [**EsiType**](EsiType.md) |  | [optional] 
**start_date** | **datetime, none_type** |  | [optional] 
**character** | [**Character**](Character.md) |  | [optional] 
**missing_character_mail_sent_date** | **datetime, none_type** | Date and time of the last sent mail. | [optional] 
**missing_character_mail_sent_result** | **str, none_type** | Result of the last sent mail (OK, Blocked, CSPA charge &gt; 0) | [optional] 
**missing_character_mail_sent_number** | **int** | Number of mails sent, is reset when the character is added. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


