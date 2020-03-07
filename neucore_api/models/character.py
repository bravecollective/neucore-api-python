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


class Character(object):
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
        'main': 'bool',
        'valid_token': 'bool',
        'valid_token_time': 'datetime',
        'created': 'datetime',
        'last_update': 'datetime',
        'corporation': 'Corporation'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'main': 'main',
        'valid_token': 'validToken',
        'valid_token_time': 'validTokenTime',
        'created': 'created',
        'last_update': 'lastUpdate',
        'corporation': 'corporation'
    }

    def __init__(self, id=None, name=None, main=None, valid_token=None, valid_token_time=None, created=None, last_update=None, corporation=None, local_vars_configuration=None):  # noqa: E501
        """Character - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._main = None
        self._valid_token = None
        self._valid_token_time = None
        self._created = None
        self._last_update = None
        self._corporation = None
        self.discriminator = None

        self.id = id
        self.name = name
        if main is not None:
            self.main = main
        self.valid_token = valid_token
        self.valid_token_time = valid_token_time
        self.created = created
        self.last_update = last_update
        if corporation is not None:
            self.corporation = corporation

    @property
    def id(self):
        """Gets the id of this Character.  # noqa: E501

        EVE character ID.  # noqa: E501

        :return: The id of this Character.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Character.

        EVE character ID.  # noqa: E501

        :param id: The id of this Character.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this Character.  # noqa: E501

        EVE character name.  # noqa: E501

        :return: The name of this Character.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Character.

        EVE character name.  # noqa: E501

        :param name: The name of this Character.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def main(self):
        """Gets the main of this Character.  # noqa: E501


        :return: The main of this Character.  # noqa: E501
        :rtype: bool
        """
        return self._main

    @main.setter
    def main(self, main):
        """Sets the main of this Character.


        :param main: The main of this Character.  # noqa: E501
        :type: bool
        """

        self._main = main

    @property
    def valid_token(self):
        """Gets the valid_token of this Character.  # noqa: E501

        Shows if character's refresh token is valid or not.  This is null if there is no refresh token (EVE SSOv1 only) or a valid token but without scopes (SSOv2).  # noqa: E501

        :return: The valid_token of this Character.  # noqa: E501
        :rtype: bool
        """
        return self._valid_token

    @valid_token.setter
    def valid_token(self, valid_token):
        """Sets the valid_token of this Character.

        Shows if character's refresh token is valid or not.  This is null if there is no refresh token (EVE SSOv1 only) or a valid token but without scopes (SSOv2).  # noqa: E501

        :param valid_token: The valid_token of this Character.  # noqa: E501
        :type: bool
        """

        self._valid_token = valid_token

    @property
    def valid_token_time(self):
        """Gets the valid_token_time of this Character.  # noqa: E501

        Date and time when that valid token property was last changed.  # noqa: E501

        :return: The valid_token_time of this Character.  # noqa: E501
        :rtype: datetime
        """
        return self._valid_token_time

    @valid_token_time.setter
    def valid_token_time(self, valid_token_time):
        """Sets the valid_token_time of this Character.

        Date and time when that valid token property was last changed.  # noqa: E501

        :param valid_token_time: The valid_token_time of this Character.  # noqa: E501
        :type: datetime
        """

        self._valid_token_time = valid_token_time

    @property
    def created(self):
        """Gets the created of this Character.  # noqa: E501


        :return: The created of this Character.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Character.


        :param created: The created of this Character.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def last_update(self):
        """Gets the last_update of this Character.  # noqa: E501

        Last ESI update.  # noqa: E501

        :return: The last_update of this Character.  # noqa: E501
        :rtype: datetime
        """
        return self._last_update

    @last_update.setter
    def last_update(self, last_update):
        """Sets the last_update of this Character.

        Last ESI update.  # noqa: E501

        :param last_update: The last_update of this Character.  # noqa: E501
        :type: datetime
        """

        self._last_update = last_update

    @property
    def corporation(self):
        """Gets the corporation of this Character.  # noqa: E501


        :return: The corporation of this Character.  # noqa: E501
        :rtype: Corporation
        """
        return self._corporation

    @corporation.setter
    def corporation(self, corporation):
        """Sets the corporation of this Character.


        :param corporation: The corporation of this Character.  # noqa: E501
        :type: Corporation
        """

        self._corporation = corporation

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
        if not isinstance(other, Character):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Character):
            return True

        return self.to_dict() != other.to_dict()
