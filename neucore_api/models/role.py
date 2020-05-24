# coding: utf-8

"""
    Neucore API

    Client library of Neucore API  # noqa: E501

    The version of the OpenAPI document: 1.12.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from neucore_api.configuration import Configuration


class Role(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    APP = "app"
    APP_GROUPS = "app-groups"
    APP_CHARS = "app-chars"
    APP_TRACKING = "app-tracking"
    APP_ESI = "app-esi"
    USER = "user"
    USER_ADMIN = "user-admin"
    USER_MANAGER = "user-manager"
    APP_ADMIN = "app-admin"
    APP_MANAGER = "app-manager"
    GROUP_ADMIN = "group-admin"
    GROUP_MANAGER = "group-manager"
    ESI = "esi"
    SETTINGS = "settings"
    TRACKING = "tracking"

    allowable_values = [APP, APP_GROUPS, APP_CHARS, APP_TRACKING, APP_ESI, USER, USER_ADMIN, USER_MANAGER, APP_ADMIN, APP_MANAGER, GROUP_ADMIN, GROUP_MANAGER, ESI, SETTINGS, TRACKING]  # noqa: E501

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
    }

    attribute_map = {
    }

    def __init__(self, local_vars_configuration=None):  # noqa: E501
        """Role - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self.discriminator = None

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
        if not isinstance(other, Role):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Role):
            return True

        return self.to_dict() != other.to_dict()
