# coding: utf-8

"""
    Neucore API

    Client library of Neucore API  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class CharacterGroups(object):
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
        'character': 'Character',
        'groups': 'list[Group]'
    }

    attribute_map = {
        'character': 'character',
        'groups': 'groups'
    }

    def __init__(self, character=None, groups=None):  # noqa: E501
        """CharacterGroups - a model defined in OpenAPI"""  # noqa: E501

        self._character = None
        self._groups = None
        self.discriminator = None

        self.character = character
        self.groups = groups

    @property
    def character(self):
        """Gets the character of this CharacterGroups.  # noqa: E501


        :return: The character of this CharacterGroups.  # noqa: E501
        :rtype: Character
        """
        return self._character

    @character.setter
    def character(self, character):
        """Sets the character of this CharacterGroups.


        :param character: The character of this CharacterGroups.  # noqa: E501
        :type: Character
        """
        if character is None:
            raise ValueError("Invalid value for `character`, must not be `None`")  # noqa: E501

        self._character = character

    @property
    def groups(self):
        """Gets the groups of this CharacterGroups.  # noqa: E501


        :return: The groups of this CharacterGroups.  # noqa: E501
        :rtype: list[Group]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this CharacterGroups.


        :param groups: The groups of this CharacterGroups.  # noqa: E501
        :type: list[Group]
        """
        if groups is None:
            raise ValueError("Invalid value for `groups`, must not be `None`")  # noqa: E501

        self._groups = groups

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
        if not isinstance(other, CharacterGroups):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
