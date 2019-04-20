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


class Group(object):
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
        'visibility': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'visibility': 'visibility'
    }

    def __init__(self, id=None, name=None, visibility=None):  # noqa: E501
        """Group - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._name = None
        self._visibility = None
        self.discriminator = None

        self.id = id
        self.name = name
        if visibility is not None:
            self.visibility = visibility

    @property
    def id(self):
        """Gets the id of this Group.  # noqa: E501

        Group ID.  # noqa: E501

        :return: The id of this Group.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Group.

        Group ID.  # noqa: E501

        :param id: The id of this Group.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this Group.  # noqa: E501

        A unique group name (can be changed).  # noqa: E501

        :return: The name of this Group.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Group.

        A unique group name (can be changed).  # noqa: E501

        :param name: The name of this Group.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 64:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `64`")  # noqa: E501
        if name is not None and not re.search(r'^[-._a-zA-Z0-9]+$', name):  # noqa: E501
            raise ValueError(r"Invalid value for `name`, must be a follow pattern or equal to `/^[-._a-zA-Z0-9]+$/`")  # noqa: E501

        self._name = name

    @property
    def visibility(self):
        """Gets the visibility of this Group.  # noqa: E501


        :return: The visibility of this Group.  # noqa: E501
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        """Sets the visibility of this Group.


        :param visibility: The visibility of this Group.  # noqa: E501
        :type: str
        """
        allowed_values = ["private", "public", "conditioned"]  # noqa: E501
        if visibility not in allowed_values:
            raise ValueError(
                "Invalid value for `visibility` ({0}), must be one of {1}"  # noqa: E501
                .format(visibility, allowed_values)
            )

        self._visibility = visibility

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
        if not isinstance(other, Group):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
