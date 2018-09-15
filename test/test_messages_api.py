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
from swagger_client.api.messages_api import MessagesApi  # noqa: E501
from swagger_client.rest import ApiException


class TestMessagesApi(unittest.TestCase):
    """MessagesApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.messages_api.MessagesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_createabulkmessages(self):
        """Test case for createabulkmessages

        Create a bulk of new messages  # noqa: E501
        """
        pass

    def test_createamassmessages(self):
        """Test case for createamassmessages

        Create a mass new messages  # noqa: E501
        """
        pass

    def test_createmessages(self):
        """Test case for createmessages

        Create a new messages  # noqa: E501
        """
        pass

    def test_getmessages(self):
        """Test case for getmessages

        Return a specific message instance.  # noqa: E501
        """
        pass

    def test_getmessages_0(self):
        """Test case for getmessages_0

        Return sent messages to applicants.  # noqa: E501
        """
        pass

    def test_getmessagess(self):
        """Test case for getmessagess

        List multiple messages resources.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()