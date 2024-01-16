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
import datetime

from openapi_client.models.flattened_anchor_points import FlattenedAnchorPoints  # noqa: E501

class TestFlattenedAnchorPoints(unittest.TestCase):
    """FlattenedAnchorPoints unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FlattenedAnchorPoints:
        """Test FlattenedAnchorPoints
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FlattenedAnchorPoints`
        """
        model = FlattenedAnchorPoints()  # noqa: E501
        if include_optional:
            return FlattenedAnchorPoints(
                var_schema = openapi_client.models.embedded_model_schema.EmbeddedModelSchema(
                    migration = 56, 
                    semantic = 'MAJOR_0_MINOR_0_PATCH_1', ),
                iterable = [
                    openapi_client.models.referenced_anchor_point.ReferencedAnchorPoint(
                        schema = openapi_client.models.embedded_model_schema.EmbeddedModelSchema(
                            migration = 56, 
                            semantic = 'MAJOR_0_MINOR_0_PATCH_1', ), 
                        id = '', 
                        reference = openapi_client.models.flattened_anchor_point.FlattenedAnchorPoint(
                            id = '', 
                            verified = True, 
                            fullpath = '', 
                            created = openapi_client.models.grouped_timestamp.GroupedTimestamp(
                                value = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                readable = 'Last week - June 3rd, 3:33 a.m.', ), 
                            updated = openapi_client.models.grouped_timestamp.GroupedTimestamp(
                                value = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                readable = 'Last week - June 3rd, 3:33 a.m.', ), 
                            deleted = , 
                            platform = 'WEB', 
                            anchor = openapi_client.models.referenced_anchor.ReferencedAnchor(
                                id = '', ), 
                            score = openapi_client.models.score.Score(
                                manual = 56, 
                                automatic = 56, 
                                priority = 56, 
                                reuse = 56, 
                                update = 56, ), ), )
                    ],
                indices = {
                    'key' : 56
                    },
                score = openapi_client.models.score.Score(
                    schema = openapi_client.models.embedded_model_schema.EmbeddedModelSchema(
                        migration = 56, 
                        semantic = 'MAJOR_0_MINOR_0_PATCH_1', ), 
                    manual = 56, 
                    automatic = 56, 
                    priority = 56, 
                    reuse = 56, 
                    update = 56, 
                    reference = 56, )
            )
        else:
            return FlattenedAnchorPoints(
                iterable = [
                    openapi_client.models.referenced_anchor_point.ReferencedAnchorPoint(
                        schema = openapi_client.models.embedded_model_schema.EmbeddedModelSchema(
                            migration = 56, 
                            semantic = 'MAJOR_0_MINOR_0_PATCH_1', ), 
                        id = '', 
                        reference = openapi_client.models.flattened_anchor_point.FlattenedAnchorPoint(
                            id = '', 
                            verified = True, 
                            fullpath = '', 
                            created = openapi_client.models.grouped_timestamp.GroupedTimestamp(
                                value = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                readable = 'Last week - June 3rd, 3:33 a.m.', ), 
                            updated = openapi_client.models.grouped_timestamp.GroupedTimestamp(
                                value = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                readable = 'Last week - June 3rd, 3:33 a.m.', ), 
                            deleted = , 
                            platform = 'WEB', 
                            anchor = openapi_client.models.referenced_anchor.ReferencedAnchor(
                                id = '', ), 
                            score = openapi_client.models.score.Score(
                                manual = 56, 
                                automatic = 56, 
                                priority = 56, 
                                reuse = 56, 
                                update = 56, ), ), )
                    ],
        )
        """

    def testFlattenedAnchorPoints(self):
        """Test FlattenedAnchorPoints"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()