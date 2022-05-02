class MissingEnvironmentVariable(Exception):
    def __init__(self, variable_name: str, detail: str = ""):
        super().__init__(
            f"Missing environment variable '{variable_name}'"
            + (f' : "{detail}"' if detail else "")
        )
