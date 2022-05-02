import os

from pdf_builder.exceptions import MissingEnvironmentVariable


def get_environ(variable_name: str, default_value=None, message_on_failure: str = ""):
    if variable_name in os.environ:
        return os.environ[variable_name]
    elif default_value is not None:
        return default_value
    else:
        raise MissingEnvironmentVariable(variable_name, message_on_failure)
