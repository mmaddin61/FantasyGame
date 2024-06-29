
class IllegalStateError(RuntimeError):
    """Exception raised when the program is in an illegal state.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message="The program is in an invalid state."):
        self.message = message
        super().__init__(self.message)

class DialogueDataError(RuntimeError):
    """Exception raised when an error occurs while loading or parsing the dialogue data.
    
    Attributes:
        message -- explanation of the error
    """
    
    def __init__(self, message="Failed to load the dialogue data."):
        self.message = message
        super().__init__(self.message)

class ElementExistsError(RuntimeError):
    """Exception raised when an element already exists in a collection.
    
    Attributes:
        message -- explanation of the error
    """
    
    def __init__(self, message="The element already exists."):
        self.message = message
        super().__init__(self.message)

class ElementNotFoundError(RuntimeError):
    """Exception raised when an element is not found in a collection.
    
    Attributes:
        message -- explanation of the error
    """
    
    def __init__(self, message="The element was not found."):
        self.message = message
        super().__init__(self.message)