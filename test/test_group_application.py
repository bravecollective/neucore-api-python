"""
    Neucore API

    Client library of Neucore API  # noqa: E501

    The version of the OpenAPI document: 1.21.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import neucore_api
from neucore_api.model.group import Group
from neucore_api.model.player import Player
globals()['Group'] = Group
globals()['Player'] = Player
from neucore_api.model.group_application import GroupApplication


class TestGroupApplication(unittest.TestCase):
    """GroupApplication unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGroupApplication(self):
        """Test GroupApplication"""
        # FIXME: construct object with mandatory attributes with example values
        # model = GroupApplication()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
