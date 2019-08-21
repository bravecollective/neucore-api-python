# coding: utf-8

"""
    Neucore API

    Client library of Neucore API  # noqa: E501

    The version of the OpenAPI document: 1.4.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class Alliance(object):
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
        'id': 'int',
        'name': 'str',
        'ticker': 'str',
        'groups': 'list[Group]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'ticker': 'ticker',
        'groups': 'groups'
    }

    def __init__(self, id=None, name=None, ticker=None, groups=None):  # noqa: E501
        """Alliance - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._name = None
        self._ticker = None
        self._groups = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.ticker = ticker
        if groups is not None:
            self.groups = groups

    @property
    def id(self):
        """Gets the id of this Alliance.  # noqa: E501

        EVE alliance ID.  # noqa: E501

        :return: The id of this Alliance.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Alliance.

        EVE alliance ID.  # noqa: E501

        :param id: The id of this Alliance.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this Alliance.  # noqa: E501

        EVE alliance name.  # noqa: E501

        :return: The name of this Alliance.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Alliance.

        EVE alliance name.  # noqa: E501

        :param name: The name of this Alliance.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def ticker(self):
        """Gets the ticker of this Alliance.  # noqa: E501

        Alliance ticker.  # noqa: E501

        :return: The ticker of this Alliance.  # noqa: E501
        :rtype: str
        """
        return self._ticker

    @ticker.setter
    def ticker(self, ticker):
        """Sets the ticker of this Alliance.

        Alliance ticker.  # noqa: E501

        :param ticker: The ticker of this Alliance.  # noqa: E501
        :type: str
        """

        self._ticker = ticker

    @property
    def groups(self):
        """Gets the groups of this Alliance.  # noqa: E501

        Groups for automatic assignment (API: not included by default).  # noqa: E501

        :return: The groups of this Alliance.  # noqa: E501
        :rtype: list[Group]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this Alliance.

        Groups for automatic assignment (API: not included by default).  # noqa: E501

        :param groups: The groups of this Alliance.  # noqa: E501
        :type: list[Group]
        """

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
        if not isinstance(other, Alliance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
