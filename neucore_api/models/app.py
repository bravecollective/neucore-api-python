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


class App(object):
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
        'roles': 'list[Role]',
        'groups': 'list[Group]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'roles': 'roles',
        'groups': 'groups'
    }

    def __init__(self, id=None, name=None, roles=None, groups=None):  # noqa: E501
        """App - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._name = None
        self._roles = None
        self._groups = None
        self.discriminator = None

        self.id = id
        self.name = name
        if roles is not None:
            self.roles = roles
        if groups is not None:
            self.groups = groups

    @property
    def id(self):
        """Gets the id of this App.  # noqa: E501

        App ID  # noqa: E501

        :return: The id of this App.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this App.

        App ID  # noqa: E501

        :param id: The id of this App.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this App.  # noqa: E501

        App name  # noqa: E501

        :return: The name of this App.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this App.

        App name  # noqa: E501

        :param name: The name of this App.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501

        self._name = name

    @property
    def roles(self):
        """Gets the roles of this App.  # noqa: E501

        Roles for authorization.  # noqa: E501

        :return: The roles of this App.  # noqa: E501
        :rtype: list[Role]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this App.

        Roles for authorization.  # noqa: E501

        :param roles: The roles of this App.  # noqa: E501
        :type: list[Role]
        """

        self._roles = roles

    @property
    def groups(self):
        """Gets the groups of this App.  # noqa: E501

        Groups the app can see.  # noqa: E501

        :return: The groups of this App.  # noqa: E501
        :rtype: list[Group]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this App.

        Groups the app can see.  # noqa: E501

        :param groups: The groups of this App.  # noqa: E501
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
        if not isinstance(other, App):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
