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

from openapi_client.models.conversation import Conversation  # noqa: E501

class TestConversation(unittest.TestCase):
    """Conversation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Conversation:
        """Test Conversation
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Conversation`
        """
        model = Conversation()  # noqa: E501
        if include_optional:
            return Conversation(
                var_schema = openapi_client.models.embedded_model_schema.EmbeddedModelSchema(
                    migration = 56, 
                    semantic = 'MAJOR_0_MINOR_0_PATCH_1', ),
                id = '',
                name = '',
                created = openapi_client.models.grouped_timestamp.GroupedTimestamp(
                    schema = openapi_client.models.embedded_model_schema.EmbeddedModelSchema(
                        migration = 56, 
                        semantic = 'MAJOR_0_MINOR_0_PATCH_1', ), 
                    value = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    readable = 'Last week - June 3rd, 3:33 a.m.', ),
                updated = openapi_client.models.grouped_timestamp.GroupedTimestamp(
                    schema = openapi_client.models.embedded_model_schema.EmbeddedModelSchema(
                        migration = 56, 
                        semantic = 'MAJOR_0_MINOR_0_PATCH_1', ), 
                    value = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    readable = 'Last week - June 3rd, 3:33 a.m.', ),
                deleted = openapi_client.models.grouped_timestamp.GroupedTimestamp(
                    schema = openapi_client.models.embedded_model_schema.EmbeddedModelSchema(
                        migration = 56, 
                        semantic = 'MAJOR_0_MINOR_0_PATCH_1', ), 
                    value = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    readable = 'Last week - June 3rd, 3:33 a.m.', ),
                favorited = True,
                application = openapi_client.models.application.Application(
                    schema = openapi_client.models.embedded_model_schema.EmbeddedModelSchema(
                        migration = 56, 
                        semantic = 'MAJOR_0_MINOR_0_PATCH_1', ), 
                    id = '', 
                    name = 'SUBLIME', 
                    version = '', 
                    platform = 'WEB', 
                    onboarded = True, 
                    privacy = 'OPEN', 
                    capabilities = 'LOCAL', 
                    mechanism = 'MANUAL', 
                    automatic_unload = True, ),
                annotations = openapi_client.models.flattened_annotations.FlattenedAnnotations(
                    schema = openapi_client.models.embedded_model_schema.EmbeddedModelSchema(
                        migration = 56, 
                        semantic = 'MAJOR_0_MINOR_0_PATCH_1', ), 
                    iterable = [
                        openapi_client.models.referenced_annotation.ReferencedAnnotation(
                            id = '', 
                            reference = openapi_client.models.flattened_annotation.FlattenedAnnotation(
                                id = '', 
                                created = openapi_client.models.grouped_timestamp.GroupedTimestamp(
                                    value = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    readable = 'Last week - June 3rd, 3:33 a.m.', ), 
                                updated = openapi_client.models.grouped_timestamp.GroupedTimestamp(
                                    value = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    readable = 'Last week - June 3rd, 3:33 a.m.', ), 
                                deleted = , 
                                mechanism = 'MANUAL', 
                                asset = openapi_client.models.referenced_asset_[dag_safety].ReferencedAsset [DAG Safety](
                                    id = '2254f2c8-5797-40e8-ac56-41166dc0e159', ), 
                                person = openapi_client.models.referenced_person.ReferencedPerson(
                                    id = '', ), 
                                type = 'DESCRIPTION', 
                                text = '', 
                                model = openapi_client.models.referenced_model.ReferencedModel(
                                    id = '', ), 
                                pseudo = True, 
                                favorited = True, 
                                anchor = openapi_client.models.referenced_anchor.ReferencedAnchor(
                                    id = '', ), 
                                conversation = openapi_client.models.referenced_conversation.ReferencedConversation(
                                    id = '', ), 
                                score = openapi_client.models.score.Score(
                                    manual = 56, 
                                    automatic = 56, 
                                    priority = 56, 
                                    reuse = 56, 
                                    update = 56, ), 
                                messages = openapi_client.models.flattened_conversation_messages.FlattenedConversationMessages(
                                    iterable = [
                                        openapi_client.models.referenced_conversation_message.ReferencedConversationMessage(
                                            id = '', )
                                        ], 
                                    indices = {
                                        'key' : 56
                                        }, ), ), )
                        ], 
                    indices = {
                        'key' : 56
                        }, 
                    score = openapi_client.models.score.Score(
                        manual = 56, 
                        automatic = 56, 
                        priority = 56, 
                        reuse = 56, 
                        update = 56, ), ),
                messages = openapi_client.models.flattened_conversation_messages.FlattenedConversationMessages(
                    schema = openapi_client.models.embedded_model_schema.EmbeddedModelSchema(
                        migration = 56, 
                        semantic = 'MAJOR_0_MINOR_0_PATCH_1', ), 
                    iterable = [
                        openapi_client.models.referenced_conversation_message.ReferencedConversationMessage(
                            id = '', 
                            reference = openapi_client.models.flattened_conversation_message.FlattenedConversationMessage(
                                id = '', 
                                created = openapi_client.models.grouped_timestamp.GroupedTimestamp(
                                    value = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    readable = 'Last week - June 3rd, 3:33 a.m.', ), 
                                updated = openapi_client.models.grouped_timestamp.GroupedTimestamp(
                                    value = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    readable = 'Last week - June 3rd, 3:33 a.m.', ), 
                                deleted = , 
                                model = openapi_client.models.model.Model(
                                    id = '', 
                                    version = '', 
                                    created = , 
                                    name = '', 
                                    description = '', 
                                    cloud = True, 
                                    type = 'BALANCED', 
                                    usage = 'OCR', 
                                    bytes = openapi_client.models.byte_descriptor.ByteDescriptor(
                                        value = 33600, 
                                        readable = '33.6 KB', ), 
                                    ram = openapi_client.models.byte_descriptor.ByteDescriptor(
                                        value = 33600, 
                                        readable = '33.6 KB', ), 
                                    quantization = '', 
                                    foundation = 'GPT_3.5', 
                                    downloaded = True, 
                                    loaded = True, 
                                    unique = '', 
                                    parameters = 1.337, 
                                    provider = 'APPLE', 
                                    cpu = True, 
                                    downloading = True, ), 
                                fragment = openapi_client.models.fragment_format.FragmentFormat(
                                    string = openapi_client.models.transferable_string.TransferableString(
                                        raw = '', 
                                        base64 = '', 
                                        base64_url = '', 
                                        data_url = '', ), 
                                    metadata = openapi_client.models.fragment_metadata.FragmentMetadata(
                                        ext = 'csx', ), ), 
                                conversation = openapi_client.models.referenced_conversation.ReferencedConversation(
                                    id = '', ), 
                                sentiment = 'LIKE', 
                                role = 'USER', 
                                score = openapi_client.models.score.Score(
                                    manual = 56, 
                                    automatic = 56, 
                                    priority = 56, 
                                    reuse = 56, 
                                    update = 56, ), 
                                annotations = openapi_client.models.flattened_annotations.FlattenedAnnotations(
                                    iterable = [
                                        openapi_client.models.referenced_annotation.ReferencedAnnotation(
                                            id = '', )
                                        ], 
                                    indices = {
                                        'key' : 56
                                        }, ), ), )
                        ], 
                    indices = {
                        'key' : 56
                        }, 
                    score = openapi_client.models.score.Score(
                        manual = 56, 
                        automatic = 56, 
                        priority = 56, 
                        reuse = 56, 
                        update = 56, ), ),
                model = openapi_client.models.referenced_model.ReferencedModel(
                    schema = openapi_client.models.embedded_model_schema.EmbeddedModelSchema(
                        migration = 56, 
                        semantic = 'MAJOR_0_MINOR_0_PATCH_1', ), 
                    id = '', ),
                assets = openapi_client.models.flattened_assets_[dag_safety].FlattenedAssets [DAG Safety](
                    schema = openapi_client.models.embedded_model_schema.EmbeddedModelSchema(
                        migration = 56, 
                        semantic = 'MAJOR_0_MINOR_0_PATCH_1', ), 
                    iterable = [
                        openapi_client.models.referenced_asset_[dag_safety].ReferencedAsset [DAG Safety](
                            id = '2254f2c8-5797-40e8-ac56-41166dc0e159', 
                            reference = openapi_client.models.flattened_asset_[dag_safety].FlattenedAsset [DAG Safety](
                                id = '2254f2c8-5797-40e8-ac56-41166dc0e159', 
                                name = '', 
                                creator = '497f6eca-6276-4993-bfeb-53cbbbba6f08', 
                                created = openapi_client.models.grouped_timestamp.GroupedTimestamp(
                                    value = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    readable = 'Last week - June 3rd, 3:33 a.m.', ), 
                                updated = openapi_client.models.grouped_timestamp.GroupedTimestamp(
                                    value = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    readable = 'Last week - June 3rd, 3:33 a.m.', ), 
                                synced = , 
                                deleted = , 
                                formats = openapi_client.models.flattened_formats.FlattenedFormats(
                                    iterable = [
                                        openapi_client.models.referenced_format_[dag_safety].ReferencedFormat [DAG Safety](
                                            id = '102ff265-fdfb-4142-8d94-4932d400199c', )
                                        ], ), 
                                preview = openapi_client.models.flattened_preview.FlattenedPreview(
                                    base = '', 
                                    overlay = '', ), 
                                original = '0872ccbf-1d8f-4f46-9028-469794d72761', 
                                shares = openapi_client.models.flattened_shares_[dag_safe].FlattenedShares [DAG Safe](
                                    iterable = [
                                        openapi_client.models.flattened_share_[dag_safe].FlattenedShare [DAG SAFE](
                                            id = '', 
                                            asset = '', 
                                            user = '', 
                                            link = '', 
                                            access = 'PUBLIC', 
                                            accessors = openapi_client.models.accessors.Accessors(
                                                iterable = [
                                                    openapi_client.models.accessor.Accessor(
                                                        id = '', 
                                                        os = '', 
                                                        share = '', 
                                                        count = 56, 
                                                        user = openapi_client.models.flattened_user_profile.FlattenedUserProfile(
                                                            id = '', 
                                                            email = '', 
                                                            name = '', 
                                                            username = '', 
                                                            picture = '', 
                                                            vanityname = '', ), )
                                                    ], ), 
                                            created = , 
                                            short = '', 
                                            name = '', 
                                            distributions = openapi_client.models.flattened_distributions.FlattenedDistributions(
                                                iterable = [
                                                    openapi_client.models.referenced_distribution.ReferencedDistribution(
                                                        id = '', )
                                                    ], ), 
                                            score = openapi_client.models.score.Score(
                                                manual = 56, 
                                                automatic = 56, 
                                                priority = 56, 
                                                reuse = 56, 
                                                update = 56, ), )
                                        ], 
                                    score = openapi_client.models.score.Score(
                                        manual = 56, 
                                        automatic = 56, 
                                        priority = 56, 
                                        reuse = 56, 
                                        update = 56, ), ), 
                                mechanism = 'MANUAL', 
                                websites = openapi_client.models.flattened_websites.FlattenedWebsites(
                                    iterable = [
                                        openapi_client.models.referenced_website.ReferencedWebsite(
                                            id = '', )
                                        ], 
                                    indices = {
                                        'key' : 56
                                        }, ), 
                                interacted = , 
                                tags = openapi_client.models.flattened_tags.FlattenedTags(
                                    iterable = [
                                        openapi_client.models.referenced_tag.ReferencedTag(
                                            id = '', )
                                        ], ), 
                                sensitives = openapi_client.models.flattened_sensitives.FlattenedSensitives(
                                    iterable = [
                                        openapi_client.models.referenced_sensitive.ReferencedSensitive(
                                            id = '', )
                                        ], ), 
                                persons = openapi_client.models.flattened_persons.FlattenedPersons(
                                    iterable = [
                                        openapi_client.models.referenced_person.ReferencedPerson(
                                            id = '', )
                                        ], ), 
                                curated = True, 
                                discovered = True, 
                                activities = openapi_client.models.flattened_activities.FlattenedActivities(
                                    iterable = [
                                        openapi_client.models.referenced_activity.ReferencedActivity(
                                            id = '', )
                                        ], ), 
                                score = , 
                                favorited = True, 
                                pseudo = True, 
                                annotations = openapi_client.models.flattened_annotations.FlattenedAnnotations(
                                    iterable = [
                                        openapi_client.models.referenced_annotation.ReferencedAnnotation(
                                            id = '', )
                                        ], ), 
                                hints = openapi_client.models.flattened_hints.FlattenedHints(
                                    iterable = [
                                        openapi_client.models.referenced_hint.ReferencedHint(
                                            id = '', )
                                        ], ), 
                                anchors = openapi_client.models.flattened_anchors.FlattenedAnchors(
                                    iterable = [
                                        openapi_client.models.referenced_anchor.ReferencedAnchor(
                                            id = '', )
                                        ], ), 
                                conversations = openapi_client.models.flattened_conversations.FlattenedConversations(
                                    iterable = [
                                        openapi_client.models.referenced_conversation.ReferencedConversation(
                                            id = '', )
                                        ], ), ), )
                        ], 
                    indices = {
                        'key' : 56
                        }, 
                    score = , ),
                anchors = openapi_client.models.flattened_anchors.FlattenedAnchors(
                    schema = openapi_client.models.embedded_model_schema.EmbeddedModelSchema(
                        migration = 56, 
                        semantic = 'MAJOR_0_MINOR_0_PATCH_1', ), 
                    iterable = [
                        openapi_client.models.referenced_anchor.ReferencedAnchor(
                            id = '', 
                            reference = openapi_client.models.flattened_anchor.FlattenedAnchor(
                                id = '', 
                                type = 'FILE', 
                                watch = True, 
                                points = openapi_client.models.flattened_anchor_points.FlattenedAnchorPoints(
                                    iterable = [
                                        openapi_client.models.referenced_anchor_point.ReferencedAnchorPoint(
                                            id = '', )
                                        ], 
                                    indices = {
                                        'key' : 56
                                        }, 
                                    score = openapi_client.models.score.Score(
                                        manual = 56, 
                                        automatic = 56, 
                                        priority = 56, 
                                        reuse = 56, 
                                        update = 56, ), ), 
                                created = openapi_client.models.grouped_timestamp.GroupedTimestamp(
                                    value = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    readable = 'Last week - June 3rd, 3:33 a.m.', ), 
                                updated = openapi_client.models.grouped_timestamp.GroupedTimestamp(
                                    value = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    readable = 'Last week - June 3rd, 3:33 a.m.', ), 
                                deleted = , 
                                assets = openapi_client.models.flattened_assets_[dag_safety].FlattenedAssets [DAG Safety](), 
                                name = '', 
                                annotations = openapi_client.models.flattened_annotations.FlattenedAnnotations(
                                    iterable = [
                                        openapi_client.models.referenced_annotation.ReferencedAnnotation(
                                            id = '', )
                                        ], ), 
                                conversations = openapi_client.models.flattened_conversations.FlattenedConversations(
                                    iterable = [
                                        openapi_client.models.referenced_conversation.ReferencedConversation(
                                            id = '', )
                                        ], ), 
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
                    score = , ),
                type = 'COPILOT',
                grounding = openapi_client.models.conversation_grounding.ConversationGrounding(
                    schema = openapi_client.models.embedded_model_schema.EmbeddedModelSchema(
                        migration = 56, 
                        semantic = 'MAJOR_0_MINOR_0_PATCH_1', ), 
                    messages = openapi_client.models.flattened_conversation_messages.FlattenedConversationMessages(
                        iterable = [
                            openapi_client.models.referenced_conversation_message.ReferencedConversationMessage(
                                id = '', 
                                reference = openapi_client.models.flattened_conversation_message.FlattenedConversationMessage(
                                    id = '', 
                                    created = openapi_client.models.grouped_timestamp.GroupedTimestamp(
                                        value = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                        readable = 'Last week - June 3rd, 3:33 a.m.', ), 
                                    updated = openapi_client.models.grouped_timestamp.GroupedTimestamp(
                                        value = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                        readable = 'Last week - June 3rd, 3:33 a.m.', ), 
                                    deleted = , 
                                    model = openapi_client.models.model.Model(
                                        id = '', 
                                        version = '', 
                                        created = , 
                                        name = '', 
                                        description = '', 
                                        cloud = True, 
                                        type = 'BALANCED', 
                                        usage = 'OCR', 
                                        bytes = openapi_client.models.byte_descriptor.ByteDescriptor(
                                            value = 33600, 
                                            readable = '33.6 KB', ), 
                                        ram = openapi_client.models.byte_descriptor.ByteDescriptor(
                                            value = 33600, 
                                            readable = '33.6 KB', ), 
                                        quantization = '', 
                                        foundation = 'GPT_3.5', 
                                        downloaded = True, 
                                        loaded = True, 
                                        unique = '', 
                                        parameters = 1.337, 
                                        provider = 'APPLE', 
                                        cpu = True, 
                                        downloading = True, ), 
                                    fragment = openapi_client.models.fragment_format.FragmentFormat(
                                        string = openapi_client.models.transferable_string.TransferableString(
                                            raw = '', 
                                            base64 = '', 
                                            base64_url = '', 
                                            data_url = '', ), 
                                        metadata = openapi_client.models.fragment_metadata.FragmentMetadata(
                                            ext = 'csx', ), ), 
                                    conversation = openapi_client.models.referenced_conversation.ReferencedConversation(
                                        id = '', ), 
                                    sentiment = 'LIKE', 
                                    role = 'USER', 
                                    score = openapi_client.models.score.Score(
                                        manual = 56, 
                                        automatic = 56, 
                                        priority = 56, 
                                        reuse = 56, 
                                        update = 56, ), 
                                    annotations = openapi_client.models.flattened_annotations.FlattenedAnnotations(
                                        iterable = [
                                            openapi_client.models.referenced_annotation.ReferencedAnnotation(
                                                id = '', )
                                            ], 
                                        indices = {
                                            'key' : 56
                                            }, ), ), )
                            ], 
                        indices = {
                            'key' : 56
                            }, 
                        score = openapi_client.models.score.Score(
                            manual = 56, 
                            automatic = 56, 
                            priority = 56, 
                            reuse = 56, 
                            update = 56, ), ), ),
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
            return Conversation(
                id = '',
                created = openapi_client.models.grouped_timestamp.GroupedTimestamp(
                    schema = openapi_client.models.embedded_model_schema.EmbeddedModelSchema(
                        migration = 56, 
                        semantic = 'MAJOR_0_MINOR_0_PATCH_1', ), 
                    value = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    readable = 'Last week - June 3rd, 3:33 a.m.', ),
                updated = openapi_client.models.grouped_timestamp.GroupedTimestamp(
                    schema = openapi_client.models.embedded_model_schema.EmbeddedModelSchema(
                        migration = 56, 
                        semantic = 'MAJOR_0_MINOR_0_PATCH_1', ), 
                    value = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    readable = 'Last week - June 3rd, 3:33 a.m.', ),
                messages = openapi_client.models.flattened_conversation_messages.FlattenedConversationMessages(
                    schema = openapi_client.models.embedded_model_schema.EmbeddedModelSchema(
                        migration = 56, 
                        semantic = 'MAJOR_0_MINOR_0_PATCH_1', ), 
                    iterable = [
                        openapi_client.models.referenced_conversation_message.ReferencedConversationMessage(
                            id = '', 
                            reference = openapi_client.models.flattened_conversation_message.FlattenedConversationMessage(
                                id = '', 
                                created = openapi_client.models.grouped_timestamp.GroupedTimestamp(
                                    value = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    readable = 'Last week - June 3rd, 3:33 a.m.', ), 
                                updated = openapi_client.models.grouped_timestamp.GroupedTimestamp(
                                    value = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    readable = 'Last week - June 3rd, 3:33 a.m.', ), 
                                deleted = , 
                                model = openapi_client.models.model.Model(
                                    id = '', 
                                    version = '', 
                                    created = , 
                                    name = '', 
                                    description = '', 
                                    cloud = True, 
                                    type = 'BALANCED', 
                                    usage = 'OCR', 
                                    bytes = openapi_client.models.byte_descriptor.ByteDescriptor(
                                        value = 33600, 
                                        readable = '33.6 KB', ), 
                                    ram = openapi_client.models.byte_descriptor.ByteDescriptor(
                                        value = 33600, 
                                        readable = '33.6 KB', ), 
                                    quantization = '', 
                                    foundation = 'GPT_3.5', 
                                    downloaded = True, 
                                    loaded = True, 
                                    unique = '', 
                                    parameters = 1.337, 
                                    provider = 'APPLE', 
                                    cpu = True, 
                                    downloading = True, ), 
                                fragment = openapi_client.models.fragment_format.FragmentFormat(
                                    string = openapi_client.models.transferable_string.TransferableString(
                                        raw = '', 
                                        base64 = '', 
                                        base64_url = '', 
                                        data_url = '', ), 
                                    metadata = openapi_client.models.fragment_metadata.FragmentMetadata(
                                        ext = 'csx', ), ), 
                                conversation = openapi_client.models.referenced_conversation.ReferencedConversation(
                                    id = '', ), 
                                sentiment = 'LIKE', 
                                role = 'USER', 
                                score = openapi_client.models.score.Score(
                                    manual = 56, 
                                    automatic = 56, 
                                    priority = 56, 
                                    reuse = 56, 
                                    update = 56, ), 
                                annotations = openapi_client.models.flattened_annotations.FlattenedAnnotations(
                                    iterable = [
                                        openapi_client.models.referenced_annotation.ReferencedAnnotation(
                                            id = '', )
                                        ], 
                                    indices = {
                                        'key' : 56
                                        }, ), ), )
                        ], 
                    indices = {
                        'key' : 56
                        }, 
                    score = openapi_client.models.score.Score(
                        manual = 56, 
                        automatic = 56, 
                        priority = 56, 
                        reuse = 56, 
                        update = 56, ), ),
                type = 'COPILOT',
        )
        """

    def testConversation(self):
        """Test Conversation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()