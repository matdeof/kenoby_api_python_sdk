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
from swagger_client.api.mentions_api import MentionsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestMentionsApi(unittest.TestCase):
    """MentionsApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.mentions_api.MentionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_deletefavoritementions(self):
        """Test case for deletefavoritementions

        remove from favorite mention.  # noqa: E501
        """
        pass

    def test_deletementions(self):
        """Test case for deletementions

        delete mention.  # noqa: E501
        """
        pass

    def test_getmentions(self):
        """Test case for getmentions

        List multiple mentions resources.  # noqa: E501
        """
        pass

    def test_getunderedmentions(self):
        """Test case for getunderedmentions

        List multiple mentions unreads.  # noqa: E501
        """
        pass

    def test_postmentions(self):
        """Test case for postmentions

        Save mention.  # noqa: E501
        """
        pass

    def test_putfavoritementions(self):
        """Test case for putfavoritementions

        add to favorite mention.  # noqa: E501
        """
        pass

    def test_putreadmentions(self):
        """Test case for putreadmentions

        read all mentions.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()