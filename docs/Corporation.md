# Corporation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | EVE corporation ID. | 
**name** | **str, none_type** | EVE corporation name. | 
**ticker** | **str, none_type** | Corporation ticker. | 
**alliance** | [**Alliance**](Alliance.md) |  | [optional] 
**groups** | [**[Group]**](Group.md) | Groups for automatic assignment (API: not included by default). | [optional] 
**tracking_last_update** | **datetime, none_type** | Last update of corporation member tracking data (API: not included by default). | [optional] 
**auto_allowlist** | **bool** | True if this corporation was automatically placed on the allowlist of a watchlist (API: not included by default). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


