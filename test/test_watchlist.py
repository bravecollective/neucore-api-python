# coding: utf-8

"""
    Neucore API

    Client library of Neucore API  # noqa: E501

    The version of the OpenAPI document: 1.12.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import neucore_api
from neucore_api.models.watchlist import Watchlist  # noqa: E501
from neucore_api.rest import ApiException

class TestWatchlist(unittest.TestCase):
    """Watchlist unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Watchlist
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = neucore_api.models.watchlist.Watchlist()  # noqa: E501
        if include_optional :
            return Watchlist(
                id = 56, 
                name = '0'
            )
        else :
            return Watchlist(
                id = 56,
                name = '0',
        )

    def testWatchlist(self):
        """Test Watchlist"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
