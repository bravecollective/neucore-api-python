# CorporationMember

The player property contains only id and name, character does not contain corporation.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**player** | [**Player**](Player.md) |  | [optional] 
**id** | **int** | EVE Character ID. | 
**name** | **str** | EVE Character name. | 
**location** | [**EsiLocation**](EsiLocation.md) |  | [optional] 
**logoff_date** | **datetime** |  | [optional] 
**logon_date** | **datetime** |  | [optional] 
**ship_type** | [**EsiType**](EsiType.md) |  | [optional] 
**start_date** | **datetime** |  | [optional] 
**character** | [**Character**](Character.md) |  | [optional] 
**missing_character_mail_sent_date** | **datetime** | Date and time of the last sent mail. | [optional] 
**missing_character_mail_sent_result** | **str** | Result of the last sent mail (OK, Blocked, CSPA charge &gt; 0) | [optional] 
**missing_character_mail_sent_number** | **int** | Number of mails sent, is reset when the character is added. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


