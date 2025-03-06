"""
Extractors for different data types.
"""

from .email import extract_emails
from .table import extract_tables
from .links import extract_links

# Registry of available extractors
EXTRACTORS = {
    "email": extract_emails,
    "table": extract_tables,
    "links": extract_links,
    # Add more extractors as they are implemented
}

class ExtractorNotFoundError(ValueError):
    """Exception raised when an extractor doesn't exist for a specified data type."""
    def __init__(self, data_type):
        self.data_type = data_type
        message = f"No extractor available for data type: '{data_type}'. Available extractors are: {', '.join(EXTRACTORS.keys())}"
        super().__init__(message)


def get_extractor(data_type):
    """
    Get the appropriate extractor function for the specified data type.

    Args:
        data_type: Type of data to extract.

    Returns:
        Extractor function.

    Raises:
        ExtractorNotFoundError: If no extractor exists for the specified data type.
    """
    if data_type not in EXTRACTORS:
        raise ExtractorNotFoundError(data_type)

    return EXTRACTORS[data_type]


__all__ = ["get_extractor", "EXTRACTORS", "ExtractorNotFoundError"]