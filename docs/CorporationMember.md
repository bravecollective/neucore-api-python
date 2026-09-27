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

## Example

```python
from neucore_api.models.corporation_member import CorporationMember

# TODO update the JSON string below
json = "{}"
# create an instance of CorporationMember from a JSON string
corporation_member_instance = CorporationMember.from_json(json)
# print the JSON string representation of the object
print(CorporationMember.to_json())

# convert the object into a dict
corporation_member_dict = corporation_member_instance.to_dict()
# create an instance of CorporationMember from a dict
corporation_member_from_dict = CorporationMember.from_dict(corporation_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


