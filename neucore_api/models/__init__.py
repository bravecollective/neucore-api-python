# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from neucore_api.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from neucore_api.model.alliance import Alliance
from neucore_api.model.app import App
from neucore_api.model.character import Character
from neucore_api.model.character_groups import CharacterGroups
from neucore_api.model.character_name_change import CharacterNameChange
from neucore_api.model.corporation import Corporation
from neucore_api.model.corporation_member import CorporationMember
from neucore_api.model.esi_location import EsiLocation
from neucore_api.model.esi_token import EsiToken
from neucore_api.model.esi_token_data import EsiTokenData
from neucore_api.model.esi_type import EsiType
from neucore_api.model.eve_login import EveLogin
from neucore_api.model.group import Group
from neucore_api.model.group_application import GroupApplication
from neucore_api.model.hourly_app_requests import HourlyAppRequests
from neucore_api.model.monthly_app_requests import MonthlyAppRequests
from neucore_api.model.player import Player
from neucore_api.model.player_login_statistics import PlayerLoginStatistics
from neucore_api.model.player_with_charcter_id import PlayerWithCharcterId
from neucore_api.model.plugin import Plugin
from neucore_api.model.plugin_configuration_database import PluginConfigurationDatabase
from neucore_api.model.plugin_configuration_file import PluginConfigurationFile
from neucore_api.model.plugin_configuration_url import PluginConfigurationURL
from neucore_api.model.removed_character import RemovedCharacter
from neucore_api.model.role import Role
from neucore_api.model.search_result import SearchResult
from neucore_api.model.service_account import ServiceAccount
from neucore_api.model.system_variable import SystemVariable
from neucore_api.model.total_daily_app_requests import TotalDailyAppRequests
from neucore_api.model.total_monthly_app_requests import TotalMonthlyAppRequests
from neucore_api.model.watchlist import Watchlist
