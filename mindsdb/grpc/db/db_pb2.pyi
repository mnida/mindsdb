from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HandlerContext(_message.Message):
    __slots__ = ["context", "handler_params", "handler_type"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    HANDLER_PARAMS_FIELD_NUMBER: _ClassVar[int]
    HANDLER_TYPE_FIELD_NUMBER: _ClassVar[int]
    context: str
    handler_params: str
    handler_type: str
    def __init__(self, context: _Optional[str] = ..., handler_type: _Optional[str] = ..., handler_params: _Optional[str] = ...) -> None: ...

class NativeQueryContext(_message.Message):
    __slots__ = ["context", "query"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    context: HandlerContext
    query: str
    def __init__(self, context: _Optional[_Union[HandlerContext, _Mapping]] = ..., query: _Optional[str] = ...) -> None: ...

class Response(_message.Message):
    __slots__ = ["data_frame", "error_code", "error_message", "query", "type"]
    DATA_FRAME_FIELD_NUMBER: _ClassVar[int]
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    data_frame: bytes
    error_code: int
    error_message: str
    query: int
    type: str
    def __init__(self, type: _Optional[str] = ..., data_frame: _Optional[bytes] = ..., query: _Optional[int] = ..., error_code: _Optional[int] = ..., error_message: _Optional[str] = ...) -> None: ...

class StatusResponse(_message.Message):
    __slots__ = ["error_message", "success"]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    error_message: str
    success: bool
    def __init__(self, success: bool = ..., error_message: _Optional[str] = ...) -> None: ...
