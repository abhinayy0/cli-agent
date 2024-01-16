# coding: utf-8

"""
    Pieces Isomorphic OpenAPI

    Endpoints for Assets, Formats, Users, Asset, Format, User.

    The version of the OpenAPI document: 1.0
    Contact: tsavo@pieces.app
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.conversation_messages_api import ConversationMessagesApi  # noqa: E501


class TestConversationMessagesApi(unittest.TestCase):
    """ConversationMessagesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ConversationMessagesApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_messages_create_specific_message(self) -> None:
        """Test case for messages_create_specific_message

        /messages/create [POST]  # noqa: E501
        """
        pass

    def test_messages_delete_specific_message(self) -> None:
        """Test case for messages_delete_specific_message

        /messages/{message}/delete [POST]  # noqa: E501
        """
        pass

    def test_messages_snapshot(self) -> None:
        """Test case for messages_snapshot

        /messages [GET]  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()