# coding: utf-8

"""
    Pieces Isomorphic OpenAPI

    Endpoints for Assets, Formats, Users, Asset, Format, User.

    The version of the OpenAPI document: 1.0
    Contact: tsavo@pieces.app
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr
from openapi_client.models.qgpt_question_output import QGPTQuestionOutput
from openapi_client.models.qgpt_relevance_output import QGPTRelevanceOutput
from openapi_client.models.qgpt_stream_enum import QGPTStreamEnum

class QGPTStreamOutput(BaseModel):
    """
    This is the out for the /qgpt/stream endpoint.  # noqa: E501
    """
    request: Optional[StrictStr] = Field(None, description="This is the id used to represent the stream of response. this will always be present. We will use the value passed inby the client, or we will generate one.")
    relevance: Optional[QGPTRelevanceOutput] = None
    question: Optional[QGPTQuestionOutput] = None
    status: Optional[QGPTStreamEnum] = None
    conversation: StrictStr = Field(..., description="This is the ID of a predefined persisted conversation, if this is not present we will create a new conversation for the input/output.(in the case of a question)")
    __properties = ["request", "relevance", "question", "status", "conversation"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> QGPTStreamOutput:
        """Create an instance of QGPTStreamOutput from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of relevance
        if self.relevance:
            _dict['relevance'] = self.relevance.to_dict()
        # override the default output from pydantic by calling `to_dict()` of question
        if self.question:
            _dict['question'] = self.question.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> QGPTStreamOutput:
        """Create an instance of QGPTStreamOutput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return QGPTStreamOutput.parse_obj(obj)

        _obj = QGPTStreamOutput.parse_obj({
            "request": obj.get("request"),
            "relevance": QGPTRelevanceOutput.from_dict(obj.get("relevance")) if obj.get("relevance") is not None else None,
            "question": QGPTQuestionOutput.from_dict(obj.get("question")) if obj.get("question") is not None else None,
            "status": obj.get("status"),
            "conversation": obj.get("conversation")
        })
        return _obj

