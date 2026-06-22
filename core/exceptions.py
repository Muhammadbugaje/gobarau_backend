class BusinessLogicError(Exception):
    """Raised when a business rule is violated."""
    pass
class DuplicateRecordError(Exception):
    """Raised when attempting to create a duplicate record."""
    pass
class LifecycleError(Exception):
    """Raised when an invalid lifecycle transition is attempted."""
    pass
class SecurityError(Exception):
    """Raised when a security violation is detected."""
    pass