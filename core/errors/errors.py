class CustomError:
    """Custom Error class"""

    ALLOWED_TYPES = ["TypeError", "ValueError", "UnassignedError"]

    def __init__(self, error_type: str, message: str) -> None:
        if error_type in self.ALLOWED_TYPES:
            self.error_type = error_type
            self.message = message
            print(self)  

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.error_type}, {self.message!r})"

    def __str__(self) -> str:
        return f"{self.error_type}: {self.message}"


