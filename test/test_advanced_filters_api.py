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
from swagger_client.api.advanced_filters_api import AdvancedFiltersApi  # noqa: E501
from swagger_client.rest import ApiException


class TestAdvancedFiltersApi(unittest.TestCase):
    """AdvancedFiltersApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.advanced_filters_api.AdvancedFiltersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_createadvancedfilters(self):
        """Test case for createadvancedfilters

        Create a specific advanced-filter instance.  # noqa: E501
        """
        pass

    def test_deleteadvancedfilters(self):
        """Test case for deleteadvancedfilters

        Delete a specific advanced-filter instance.  # noqa: E501
        """
        pass

    def test_getadvancedfilter(self):
        """Test case for getadvancedfilter

        List multiple advanced-filters resources.  # noqa: E501
        """
        pass

    def test_getadvancedfilters(self):
        """Test case for getadvancedfilters

        Return a specific advanced-filter instance.  # noqa: E501
        """
        pass

    def test_updateadvancedfilters(self):
        """Test case for updateadvancedfilters

        Update a specific advanced-filter instance.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
