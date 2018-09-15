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
from swagger_client.api.notifications_api import NotificationsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestNotificationsApi(unittest.TestCase):
    """NotificationsApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.notifications_api.NotificationsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_getnotificationss(self):
        """Test case for getnotificationss

        List multiple notifications resources.  # noqa: E501
        """
        pass

    def test_markallasreadnotifications(self):
        """Test case for markallasreadnotifications

        Mark as read all notifications.  # noqa: E501
        """
        pass

    def test_markasreadnotifications(self):
        """Test case for markasreadnotifications

        Mark as read a specific notification instance.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
