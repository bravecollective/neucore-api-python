"""
    Neucore API

    Client library of Neucore API  # noqa: E501

    The version of the OpenAPI document: 1.33.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import neucore_api
from neucore_api.api.application_api import ApplicationApi  # noqa: E501


class TestApplicationApi(unittest.TestCase):
    """ApplicationApi unit test stubs"""

    def setUp(self):
        self.api = ApplicationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_show_v1(self):
        """Test case for show_v1

        Show app information.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
