"""
    Neucore API

    Client library of Neucore API  # noqa: E501

    The version of the OpenAPI document: 1.21.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import neucore_api
from neucore_api.model.character import Character
from neucore_api.model.group import Group
globals()['Character'] = Character
globals()['Group'] = Group
from neucore_api.model.character_groups import CharacterGroups


class TestCharacterGroups(unittest.TestCase):
    """CharacterGroups unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCharacterGroups(self):
        """Test CharacterGroups"""
        # FIXME: construct object with mandatory attributes with example values
        # model = CharacterGroups()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
