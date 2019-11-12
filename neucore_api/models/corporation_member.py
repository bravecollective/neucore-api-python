# coding: utf-8

"""
    Neucore API

    Client library of Neucore API  # noqa: E501

    The version of the OpenAPI document: 1.6.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class CorporationMember(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'player': 'Player',
        'id': 'int',
        'name': 'str',
        'location': 'EsiLocation',
        'logoff_date': 'datetime',
        'logon_date': 'datetime',
        'ship_type': 'EsiType',
        'start_date': 'datetime',
        'character': 'Character'
    }

    attribute_map = {
        'player': 'player',
        'id': 'id',
        'name': 'name',
        'location': 'location',
        'logoff_date': 'logoffDate',
        'logon_date': 'logonDate',
        'ship_type': 'shipType',
        'start_date': 'startDate',
        'character': 'character'
    }

    def __init__(self, player=None, id=None, name=None, location=None, logoff_date=None, logon_date=None, ship_type=None, start_date=None, character=None):  # noqa: E501
        """CorporationMember - a model defined in OpenAPI"""  # noqa: E501

        self._player = None
        self._id = None
        self._name = None
        self._location = None
        self._logoff_date = None
        self._logon_date = None
        self._ship_type = None
        self._start_date = None
        self._character = None
        self.discriminator = None

        if player is not None:
            self.player = player
        self.id = id
        self.name = name
        if location is not None:
            self.location = location
        self.logoff_date = logoff_date
        self.logon_date = logon_date
        if ship_type is not None:
            self.ship_type = ship_type
        self.start_date = start_date
        if character is not None:
            self.character = character

    @property
    def player(self):
        """Gets the player of this CorporationMember.  # noqa: E501


        :return: The player of this CorporationMember.  # noqa: E501
        :rtype: Player
        """
        return self._player

    @player.setter
    def player(self, player):
        """Sets the player of this CorporationMember.


        :param player: The player of this CorporationMember.  # noqa: E501
        :type: Player
        """

        self._player = player

    @property
    def id(self):
        """Gets the id of this CorporationMember.  # noqa: E501

        EVE Character ID.  # noqa: E501

        :return: The id of this CorporationMember.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CorporationMember.

        EVE Character ID.  # noqa: E501

        :param id: The id of this CorporationMember.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this CorporationMember.  # noqa: E501

        EVE Character name.  # noqa: E501

        :return: The name of this CorporationMember.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CorporationMember.

        EVE Character name.  # noqa: E501

        :param name: The name of this CorporationMember.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def location(self):
        """Gets the location of this CorporationMember.  # noqa: E501


        :return: The location of this CorporationMember.  # noqa: E501
        :rtype: EsiLocation
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this CorporationMember.


        :param location: The location of this CorporationMember.  # noqa: E501
        :type: EsiLocation
        """

        self._location = location

    @property
    def logoff_date(self):
        """Gets the logoff_date of this CorporationMember.  # noqa: E501


        :return: The logoff_date of this CorporationMember.  # noqa: E501
        :rtype: datetime
        """
        return self._logoff_date

    @logoff_date.setter
    def logoff_date(self, logoff_date):
        """Sets the logoff_date of this CorporationMember.


        :param logoff_date: The logoff_date of this CorporationMember.  # noqa: E501
        :type: datetime
        """

        self._logoff_date = logoff_date

    @property
    def logon_date(self):
        """Gets the logon_date of this CorporationMember.  # noqa: E501


        :return: The logon_date of this CorporationMember.  # noqa: E501
        :rtype: datetime
        """
        return self._logon_date

    @logon_date.setter
    def logon_date(self, logon_date):
        """Sets the logon_date of this CorporationMember.


        :param logon_date: The logon_date of this CorporationMember.  # noqa: E501
        :type: datetime
        """

        self._logon_date = logon_date

    @property
    def ship_type(self):
        """Gets the ship_type of this CorporationMember.  # noqa: E501


        :return: The ship_type of this CorporationMember.  # noqa: E501
        :rtype: EsiType
        """
        return self._ship_type

    @ship_type.setter
    def ship_type(self, ship_type):
        """Sets the ship_type of this CorporationMember.


        :param ship_type: The ship_type of this CorporationMember.  # noqa: E501
        :type: EsiType
        """

        self._ship_type = ship_type

    @property
    def start_date(self):
        """Gets the start_date of this CorporationMember.  # noqa: E501


        :return: The start_date of this CorporationMember.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this CorporationMember.


        :param start_date: The start_date of this CorporationMember.  # noqa: E501
        :type: datetime
        """

        self._start_date = start_date

    @property
    def character(self):
        """Gets the character of this CorporationMember.  # noqa: E501


        :return: The character of this CorporationMember.  # noqa: E501
        :rtype: Character
        """
        return self._character

    @character.setter
    def character(self, character):
        """Sets the character of this CorporationMember.


        :param character: The character of this CorporationMember.  # noqa: E501
        :type: Character
        """

        self._character = character

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CorporationMember):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
