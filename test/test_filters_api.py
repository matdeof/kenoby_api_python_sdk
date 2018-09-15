# coding: utf-8

"""
    Kenoby

    Issues or Questions? <a href=\"mailto:devs@kenoby.com\" target=\"_blank\">Send us an e-mail</a>.<br>                      For better experience <a href=\"http://api.kenoby.com/swagger.json\" target=\"_blank\">Download our swagger.json</a>                      and use it on <a href=\"https://www.getpostman.com/\" target=\"_blank\">Postman</a>  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.filters_api import FiltersApi  # noqa: E501
from swagger_client.rest import ApiException


class TestFiltersApi(unittest.TestCase):
    """FiltersApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.filters_api.FiltersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_createfilters(self):
        """Test case for createfilters

        Create a new filters  # noqa: E501
        """
        pass

    def test_deletefilters(self):
        """Test case for deletefilters

        Delete a specific filter instance.  # noqa: E501
        """
        pass

    def test_getfilters(self):
        """Test case for getfilters

        Return a specific filter instance.  # noqa: E501
        """
        pass

    def test_getfilterss(self):
        """Test case for getfilterss

        List multiple filters resources.  # noqa: E501
        """
        pass

    def test_updatefilters(self):
        """Test case for updatefilters

        Update a specific filter instance.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()