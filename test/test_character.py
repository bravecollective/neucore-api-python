"""
    Neucore API

    Client library of Neucore API  # noqa: E501

    The version of the OpenAPI document: 1.21.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import neucore_api
from neucore_api.model.character_name_change import CharacterNameChange
from neucore_api.model.corporation import Corporation
globals()['CharacterNameChange'] = CharacterNameChange
globals()['Corporation'] = Corporation
from neucore_api.model.character import Character


class TestCharacter(unittest.TestCase):
    """Character unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCharacter(self):
        """Test Character"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Character()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
