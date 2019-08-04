The version numbers correspond to the Neucore version numbers.

When updating, check the generator version in .openapi-generator/VERSION, 
a new version may break backwards compatibility.

**Breaking changes**

- 1.4.0:  
  Generated from OpenAPI v3 definition file.  
  The authorization configuration changed, use `access_token` instead of `api_key`, see below. 

# neucore-api
Client library of Neucore API

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.3.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/bravecollective/neucore-api-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/bravecollective/neucore-api-python.git`)

Then import the package:
```python
import neucore_api 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import neucore_api
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import neucore_api
from neucore_api.rest import ApiException
from pprint import pprint

configuration = neucore_api.Configuration()
# Configure Bearer authorization: BearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://localhost/api
configuration.host = "https://localhost/api"
# Create an instance of the API class
api_instance = neucore_api.ApplicationApi(neucore_api.ApiClient(configuration))
request_body = [56] # list[int] | EVE alliance IDs array.

try:
    # Return groups of multiple alliances.
    api_response = api_instance.alliance_groups_bulk_v1(request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->alliance_groups_bulk_v1: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://localhost/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ApplicationApi* | [**alliance_groups_bulk_v1**](docs/ApplicationApi.md#alliance_groups_bulk_v1) | **POST** /app/v1/alliance-groups | Return groups of multiple alliances.
*ApplicationApi* | [**alliance_groups_v1**](docs/ApplicationApi.md#alliance_groups_v1) | **GET** /app/v1/alliance-groups/{aid} | Return groups of the alliance.
*ApplicationApi* | [**alliance_groups_v2**](docs/ApplicationApi.md#alliance_groups_v2) | **GET** /app/v2/alliance-groups/{aid} | Return groups of the alliance.
*ApplicationApi* | [**characters_v1**](docs/ApplicationApi.md#characters_v1) | **GET** /app/v1/characters/{characterId} | Return all characters of the player account to which the character ID belongs.
*ApplicationApi* | [**corp_groups_bulk_v1**](docs/ApplicationApi.md#corp_groups_bulk_v1) | **POST** /app/v1/corp-groups | Return groups of multiple corporations.
*ApplicationApi* | [**corp_groups_v1**](docs/ApplicationApi.md#corp_groups_v1) | **GET** /app/v1/corp-groups/{cid} | Return groups of the corporation.
*ApplicationApi* | [**corp_groups_v2**](docs/ApplicationApi.md#corp_groups_v2) | **GET** /app/v2/corp-groups/{cid} | Return groups of the corporation.
*ApplicationApi* | [**corporation_players_v1**](docs/ApplicationApi.md#corporation_players_v1) | **GET** /app/v1/corp-players/{corporationId} | Return a list of all players that have a character in the corporation.
*ApplicationApi* | [**esi_post_v1**](docs/ApplicationApi.md#esi_post_v1) | **POST** /app/v1/esi | Makes an ESI POST request on behalf on an EVE character and returns the result.
*ApplicationApi* | [**esi_v1**](docs/ApplicationApi.md#esi_v1) | **GET** /app/v1/esi | Makes an ESI GET request on behalf on an EVE character and returns the result.
*ApplicationApi* | [**groups_bulk_v1**](docs/ApplicationApi.md#groups_bulk_v1) | **POST** /app/v1/groups | Return groups of multiple players, identified by one of their character IDs.
*ApplicationApi* | [**groups_v1**](docs/ApplicationApi.md#groups_v1) | **GET** /app/v1/groups/{cid} | Return groups of the character&#39;s player account.
*ApplicationApi* | [**groups_v2**](docs/ApplicationApi.md#groups_v2) | **GET** /app/v2/groups/{cid} | Return groups of the character&#39;s player account.
*ApplicationApi* | [**groups_with_fallback_v1**](docs/ApplicationApi.md#groups_with_fallback_v1) | **GET** /app/v1/groups-with-fallback | Returns groups from the character&#39;s account, if available, or the corporation and alliance.
*ApplicationApi* | [**main_v1**](docs/ApplicationApi.md#main_v1) | **GET** /app/v1/main/{cid} | Return the main character of the player account to which the character ID belongs.
*ApplicationApi* | [**main_v2**](docs/ApplicationApi.md#main_v2) | **GET** /app/v2/main/{cid} | Return the main character of the player account to which the character ID belongs.
*ApplicationApi* | [**member_tracking_v1**](docs/ApplicationApi.md#member_tracking_v1) | **GET** /app/v1/corporation/{id}/member-tracking | Return corporation member tracking data.
*ApplicationApi* | [**player_characters_v1**](docs/ApplicationApi.md#player_characters_v1) | **GET** /app/v1/player-chars/{playerId} | Return all characters from the player account.
*ApplicationApi* | [**player_v1**](docs/ApplicationApi.md#player_v1) | **GET** /app/v1/player/{characterId} | Return the player account to which the character ID belongs.
*ApplicationApi* | [**removed_characters_v1**](docs/ApplicationApi.md#removed_characters_v1) | **GET** /app/v1/removed-characters/{characterId} | Return all characters that were removed from the player account to which the character ID belongs.
*ApplicationApi* | [**show_v1**](docs/ApplicationApi.md#show_v1) | **GET** /app/v1/show | Show app information.


## Documentation For Models

 - [Alliance](docs/Alliance.md)
 - [App](docs/App.md)
 - [Character](docs/Character.md)
 - [CharacterGroups](docs/CharacterGroups.md)
 - [Corporation](docs/Corporation.md)
 - [CorporationMember](docs/CorporationMember.md)
 - [Group](docs/Group.md)
 - [GroupApplication](docs/GroupApplication.md)
 - [Player](docs/Player.md)
 - [RemovedCharacter](docs/RemovedCharacter.md)
 - [Role](docs/Role.md)
 - [SystemVariable](docs/SystemVariable.md)


## Documentation For Authorization


## BearerAuth

- **Type**: Bearer authentication


## Author




