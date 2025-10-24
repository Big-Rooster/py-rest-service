"""Service interface definition for the PyRest Service."""

from abc import ABC, abstractmethod

from .models import (
    CreatePyRestResponse,
    DeletePyRestRequest,
    DeletePyRestResponse,
    PyRestDto,
    GetPyRestRequest,
    GetPyRestResponse,
    GetPyRestsRequest,
    GetPyRestsResponse,
    UpdatePyRestResponse,
)


class PyRestService(ABC):
    """Abstract interface for the PyRest Service business logic."""

    @abstractmethod
    async def create_py_rest(self, py_rest: PyRestDto) -> CreatePyRestResponse:
        """Create a new py-rest.
        
        Args:
            py_rest: The py-rest data to create
            
        Returns:
            Response containing the created py-rest
            
        Raises:
            ServiceException: If creation fails
        """
        pass

    @abstractmethod
    async def get_py_rests(self, request: GetPyRestsRequest) -> GetPyRestsResponse:
        """Get a paginated list of py-rests.
        
        Args:
            request: Pagination request parameters
            
        Returns:
            Response containing py-rests and pagination metadata
            
        Raises:
            ServiceException: If retrieval fails
        """
        pass

    @abstractmethod
    async def get_py_rest(self, request: GetPyRestRequest) -> GetPyRestResponse:
        """Get a single py-rest by ID.
        
        Args:
            request: Request containing the py-rest ID
            
        Returns:
            Response containing the requested py-rest
            
        Raises:
            ServiceException: If py-rest not found or retrieval fails
        """
        pass

    @abstractmethod
    async def update_py_rest(self, py_rest: PyRestDto) -> UpdatePyRestResponse:
        """Update an existing py-rest.
        
        Args:
            py_rest: The updated py-rest data
            
        Returns:
            Response containing the updated py-rest
            
        Raises:
            ServiceException: If py-rest not found or update fails
        """
        pass

    @abstractmethod
    async def delete_py_rest(self, request: DeletePyRestRequest) -> DeletePyRestResponse:
        """Delete a py-rest by ID.
        
        Args:
            request: Request containing the py-rest ID to delete
            
        Returns:
            Response with confirmation message
            
        Raises:
            ServiceException: If py-rest not found or deletion fails
        """
        pass 