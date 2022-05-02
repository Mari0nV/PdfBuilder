from fileinput import filename
import os
from pathlib import Path
from pdf_builder.api.errors import ContentTypeNotSupported
from pdf_builder.utils.document import Document
from pdf_builder.utils.storage import save_to_bucket
from fastapi import APIRouter, Depends, Response, status

from pdf_builder.schemas.builder import BuilderInputs, ContentType
from pdf_builder.utils.authentication import verify_token

router = APIRouter(dependencies=[Depends(verify_token)])

@router.post("", status_code=status.HTTP_204_NO_CONTENT)
async def build_pdf(
    inputs: BuilderInputs
):
    if inputs.content_type == ContentType.Markdown:
        doc = Document.from_markdown(md_content=inputs.content, filename=inputs.filename)
    else:
        raise ContentTypeNotSupported(inputs.content_type)

    tmp_pdf_path = Path(os.path.dirname(__file__)) / f"../tmp/{inputs.filename}.pdf"
    doc.save_to_pdf(tmp_pdf_path)

    with open(tmp_pdf_path, "rb") as fd:
        save_to_bucket(f"{inputs.filename}.pdf", fd.read())
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)
