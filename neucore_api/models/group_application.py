# coding: utf-8

"""
    Neucore API

    Client library of Neucore API  # noqa: E501

    OpenAPI spec version: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class GroupApplication(object):
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
        'player': 'Player',
        'group': 'Group',
        'created': 'datetime',
        'status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'player': 'player',
        'group': 'group',
        'created': 'created',
        'status': 'status'
    }

    def __init__(self, id=None, player=None, group=None, created=None, status=None):  # noqa: E501
        """GroupApplication - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._player = None
        self._group = None
        self._created = None
        self._status = None
        self.discriminator = None

        self.id = id
        self.player = player
        self.group = group
        self.created = created
        if status is not None:
            self.status = status

    @property
    def id(self):
        """Gets the id of this GroupApplication.  # noqa: E501


        :return: The id of this GroupApplication.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GroupApplication.


        :param id: The id of this GroupApplication.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def player(self):
        """Gets the player of this GroupApplication.  # noqa: E501


        :return: The player of this GroupApplication.  # noqa: E501
        :rtype: Player
        """
        return self._player

    @player.setter
    def player(self, player):
        """Sets the player of this GroupApplication.


        :param player: The player of this GroupApplication.  # noqa: E501
        :type: Player
        """
        if player is None:
            raise ValueError("Invalid value for `player`, must not be `None`")  # noqa: E501

        self._player = player

    @property
    def group(self):
        """Gets the group of this GroupApplication.  # noqa: E501


        :return: The group of this GroupApplication.  # noqa: E501
        :rtype: Group
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this GroupApplication.


        :param group: The group of this GroupApplication.  # noqa: E501
        :type: Group
        """
        if group is None:
            raise ValueError("Invalid value for `group`, must not be `None`")  # noqa: E501

        self._group = group

    @property
    def created(self):
        """Gets the created of this GroupApplication.  # noqa: E501


        :return: The created of this GroupApplication.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this GroupApplication.


        :param created: The created of this GroupApplication.  # noqa: E501
        :type: datetime
        """
        if created is None:
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def status(self):
        """Gets the status of this GroupApplication.  # noqa: E501

        Group application status.  # noqa: E501

        :return: The status of this GroupApplication.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GroupApplication.

        Group application status.  # noqa: E501

        :param status: The status of this GroupApplication.  # noqa: E501
        :type: str
        """
        allowed_values = ["pending", "accepted", "denied"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

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
        if not isinstance(other, GroupApplication):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
