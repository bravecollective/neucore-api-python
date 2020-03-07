# coding: utf-8

"""
    Neucore API

    Client library of Neucore API  # noqa: E501

    The version of the OpenAPI document: 1.9.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from neucore_api.configuration import Configuration


class Corporation(object):
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
        'alliance': 'Alliance',
        'groups': 'list[Group]',
        'tracking_last_update': 'datetime',
        'auto_whitelist': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'ticker': 'ticker',
        'alliance': 'alliance',
        'groups': 'groups',
        'tracking_last_update': 'trackingLastUpdate',
        'auto_whitelist': 'autoWhitelist'
    }

    def __init__(self, id=None, name=None, ticker=None, alliance=None, groups=None, tracking_last_update=None, auto_whitelist=None, local_vars_configuration=None):  # noqa: E501
        """Corporation - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._ticker = None
        self._alliance = None
        self._groups = None
        self._tracking_last_update = None
        self._auto_whitelist = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.ticker = ticker
        if alliance is not None:
            self.alliance = alliance
        if groups is not None:
            self.groups = groups
        self.tracking_last_update = tracking_last_update
        if auto_whitelist is not None:
            self.auto_whitelist = auto_whitelist

    @property
    def id(self):
        """Gets the id of this Corporation.  # noqa: E501

        EVE corporation ID.  # noqa: E501

        :return: The id of this Corporation.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Corporation.

        EVE corporation ID.  # noqa: E501

        :param id: The id of this Corporation.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this Corporation.  # noqa: E501

        EVE corporation name.  # noqa: E501

        :return: The name of this Corporation.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Corporation.

        EVE corporation name.  # noqa: E501

        :param name: The name of this Corporation.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def ticker(self):
        """Gets the ticker of this Corporation.  # noqa: E501

        Corporation ticker.  # noqa: E501

        :return: The ticker of this Corporation.  # noqa: E501
        :rtype: str
        """
        return self._ticker

    @ticker.setter
    def ticker(self, ticker):
        """Sets the ticker of this Corporation.

        Corporation ticker.  # noqa: E501

        :param ticker: The ticker of this Corporation.  # noqa: E501
        :type: str
        """

        self._ticker = ticker

    @property
    def alliance(self):
        """Gets the alliance of this Corporation.  # noqa: E501


        :return: The alliance of this Corporation.  # noqa: E501
        :rtype: Alliance
        """
        return self._alliance

    @alliance.setter
    def alliance(self, alliance):
        """Sets the alliance of this Corporation.


        :param alliance: The alliance of this Corporation.  # noqa: E501
        :type: Alliance
        """

        self._alliance = alliance

    @property
    def groups(self):
        """Gets the groups of this Corporation.  # noqa: E501

        Groups for automatic assignment (API: not included by default).  # noqa: E501

        :return: The groups of this Corporation.  # noqa: E501
        :rtype: list[Group]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this Corporation.

        Groups for automatic assignment (API: not included by default).  # noqa: E501

        :param groups: The groups of this Corporation.  # noqa: E501
        :type: list[Group]
        """

        self._groups = groups

    @property
    def tracking_last_update(self):
        """Gets the tracking_last_update of this Corporation.  # noqa: E501

        Last update of corporation member tracking data (API: not included by default).  # noqa: E501

        :return: The tracking_last_update of this Corporation.  # noqa: E501
        :rtype: datetime
        """
        return self._tracking_last_update

    @tracking_last_update.setter
    def tracking_last_update(self, tracking_last_update):
        """Sets the tracking_last_update of this Corporation.

        Last update of corporation member tracking data (API: not included by default).  # noqa: E501

        :param tracking_last_update: The tracking_last_update of this Corporation.  # noqa: E501
        :type: datetime
        """

        self._tracking_last_update = tracking_last_update

    @property
    def auto_whitelist(self):
        """Gets the auto_whitelist of this Corporation.  # noqa: E501

        True if this corporation was automatically placed on the whitelist of a watchlist (API: not included by default).  # noqa: E501

        :return: The auto_whitelist of this Corporation.  # noqa: E501
        :rtype: bool
        """
        return self._auto_whitelist

    @auto_whitelist.setter
    def auto_whitelist(self, auto_whitelist):
        """Sets the auto_whitelist of this Corporation.

        True if this corporation was automatically placed on the whitelist of a watchlist (API: not included by default).  # noqa: E501

        :param auto_whitelist: The auto_whitelist of this Corporation.  # noqa: E501
        :type: bool
        """

        self._auto_whitelist = auto_whitelist

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
        if not isinstance(other, Corporation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Corporation):
            return True

        return self.to_dict() != other.to_dict()
