# coding: utf-8

"""
    Neucore API

    Client library of Neucore API  # noqa: E501

    OpenAPI spec version: 0.8.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class RemovedCharacter(object):
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
        'new_player_id': 'int',
        'new_player_name': 'str',
        'character_id': 'int',
        'character_name': 'str',
        'removed_date': 'datetime',
        'reason': 'str'
    }

    attribute_map = {
        'new_player_id': 'newPlayerId',
        'new_player_name': 'newPlayerName',
        'character_id': 'characterId',
        'character_name': 'characterName',
        'removed_date': 'removedDate',
        'reason': 'reason'
    }

    def __init__(self, new_player_id=None, new_player_name=None, character_id=None, character_name=None, removed_date=None, reason=None):  # noqa: E501
        """RemovedCharacter - a model defined in OpenAPI"""  # noqa: E501

        self._new_player_id = None
        self._new_player_name = None
        self._character_id = None
        self._character_name = None
        self._removed_date = None
        self._reason = None
        self.discriminator = None

        if new_player_id is not None:
            self.new_player_id = new_player_id
        if new_player_name is not None:
            self.new_player_name = new_player_name
        self.character_id = character_id
        self.character_name = character_name
        self.removed_date = removed_date
        self.reason = reason

    @property
    def new_player_id(self):
        """Gets the new_player_id of this RemovedCharacter.  # noqa: E501


        :return: The new_player_id of this RemovedCharacter.  # noqa: E501
        :rtype: int
        """
        return self._new_player_id

    @new_player_id.setter
    def new_player_id(self, new_player_id):
        """Sets the new_player_id of this RemovedCharacter.


        :param new_player_id: The new_player_id of this RemovedCharacter.  # noqa: E501
        :type: int
        """

        self._new_player_id = new_player_id

    @property
    def new_player_name(self):
        """Gets the new_player_name of this RemovedCharacter.  # noqa: E501


        :return: The new_player_name of this RemovedCharacter.  # noqa: E501
        :rtype: str
        """
        return self._new_player_name

    @new_player_name.setter
    def new_player_name(self, new_player_name):
        """Sets the new_player_name of this RemovedCharacter.


        :param new_player_name: The new_player_name of this RemovedCharacter.  # noqa: E501
        :type: str
        """

        self._new_player_name = new_player_name

    @property
    def character_id(self):
        """Gets the character_id of this RemovedCharacter.  # noqa: E501

        EVE character ID.  # noqa: E501

        :return: The character_id of this RemovedCharacter.  # noqa: E501
        :rtype: int
        """
        return self._character_id

    @character_id.setter
    def character_id(self, character_id):
        """Sets the character_id of this RemovedCharacter.

        EVE character ID.  # noqa: E501

        :param character_id: The character_id of this RemovedCharacter.  # noqa: E501
        :type: int
        """
        if character_id is None:
            raise ValueError("Invalid value for `character_id`, must not be `None`")  # noqa: E501

        self._character_id = character_id

    @property
    def character_name(self):
        """Gets the character_name of this RemovedCharacter.  # noqa: E501

        EVE character name.  # noqa: E501

        :return: The character_name of this RemovedCharacter.  # noqa: E501
        :rtype: str
        """
        return self._character_name

    @character_name.setter
    def character_name(self, character_name):
        """Sets the character_name of this RemovedCharacter.

        EVE character name.  # noqa: E501

        :param character_name: The character_name of this RemovedCharacter.  # noqa: E501
        :type: str
        """
        if character_name is None:
            raise ValueError("Invalid value for `character_name`, must not be `None`")  # noqa: E501

        self._character_name = character_name

    @property
    def removed_date(self):
        """Gets the removed_date of this RemovedCharacter.  # noqa: E501

        Date of removal.  # noqa: E501

        :return: The removed_date of this RemovedCharacter.  # noqa: E501
        :rtype: datetime
        """
        return self._removed_date

    @removed_date.setter
    def removed_date(self, removed_date):
        """Sets the removed_date of this RemovedCharacter.

        Date of removal.  # noqa: E501

        :param removed_date: The removed_date of this RemovedCharacter.  # noqa: E501
        :type: datetime
        """
        if removed_date is None:
            raise ValueError("Invalid value for `removed_date`, must not be `None`")  # noqa: E501

        self._removed_date = removed_date

    @property
    def reason(self):
        """Gets the reason of this RemovedCharacter.  # noqa: E501

        How it was removed (deleted or moved to another account).  # noqa: E501

        :return: The reason of this RemovedCharacter.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this RemovedCharacter.

        How it was removed (deleted or moved to another account).  # noqa: E501

        :param reason: The reason of this RemovedCharacter.  # noqa: E501
        :type: str
        """
        if reason is None:
            raise ValueError("Invalid value for `reason`, must not be `None`")  # noqa: E501

        self._reason = reason

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
        if not isinstance(other, RemovedCharacter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other