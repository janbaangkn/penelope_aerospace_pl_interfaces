class ToBeDeveloped(Exception):
    """Raised if the code still needs to be developed."""

    def __init__(self):
        message = "This functionality still needs to be developed."
        super().__init__(message)
