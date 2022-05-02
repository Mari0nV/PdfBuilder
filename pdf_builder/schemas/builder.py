from enum import Enum
from pydantic import BaseModel

class ContentType(Enum):
    Markdown = "markdown"

class BuilderInputs(BaseModel):
    content: str
    content_type: ContentType
    filename: str