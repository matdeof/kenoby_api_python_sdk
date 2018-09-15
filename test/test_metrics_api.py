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
from swagger_client.api.metrics_api import MetricsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestMetricsApi(unittest.TestCase):
    """MetricsApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.metrics_api.MetricsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_createmetrics(self):
        """Test case for createmetrics

        Create a new metrics  # noqa: E501
        """
        pass

    def test_getmetricss(self):
        """Test case for getmetricss

        List multiple metrics resources.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
