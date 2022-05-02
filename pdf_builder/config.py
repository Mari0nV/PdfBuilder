from pdf_builder.utils.environ import get_environ


PDF_BUILDER_API_URL = get_environ(
    "PDF_BUILDER_API_URL",
    message_on_failure="Missing PDF Builder API URL",
)
PDF_BUILDER_API_VERSION = 0
