import os

import uvicorn
from fastapi import FastAPI
from fastapi.exception_handlers import request_validation_exception_handler
from fastapi.exceptions import RequestValidationError

from pdf_builder.api import ROUTERS
from pdf_builder.config import PDF_BUILDER_API_VERSION


app = FastAPI(
    title="PdfBuilder",
    version="0.1.0",
    description="PdfBuilder OpenAPI",
)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    print("Got validation exception", exc)
    return await request_validation_exception_handler(request, exc)


for router_name, router in ROUTERS.items():
    app.include_router(router, prefix=f"/{router_name}", tags=[router_name])


def main():
    port = 8002 + PDF_BUILDER_API_VERSION
    if "PDF_BUILDER_SERVER_PORT" in os.environ:
        port = int(os.environ["PDF_BUILDER_SERVER_PORT"])
    uvicorn.run("pdf_builder.main:app", host="0.0.0.0", port=port, reload=False)
