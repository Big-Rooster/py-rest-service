"""PyRest Service API module.

This module provides the business contracts layer including:
- Service interfaces
- Data transfer objects (DTOs)
- Business exceptions
"""

from .py_rest_service import PyRestService
from .models import (
    PyRestDto,
    GetPyRestRequest,
    GetPyRestResponse,
    GetPyRestsRequest,
    GetPyRestsResponse,
    CreatePyRestResponse,
    UpdatePyRestResponse,
    DeletePyRestRequest,
    DeletePyRestResponse,
)
from .exception.error_code import ErrorCode
from .exception.service_exception import ServiceException

__all__ = [
    # Service interface
    "PyRestService",
    
    # DTOs
    "PyRestDto",
    "GetPyRestRequest",
    "GetPyRestResponse", 
    "GetPyRestsRequest",
    "GetPyRestsResponse",
    "CreatePyRestResponse",
    "UpdatePyRestResponse",
    "DeletePyRestRequest",
    "DeletePyRestResponse",
    
    # Exceptions
    "ErrorCode",
    "ServiceException",
] 