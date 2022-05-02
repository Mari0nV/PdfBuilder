import markdown2
import os.path
from subprocess import call
from pathlib import Path


class Document(object):
    def __init__(self, body: str, filename: str, stylesheet: str = None):
        self.body = body
        self.filename = filename
        self._html_filename = None
        self._stylesheet = stylesheet

    @staticmethod
    def from_markdown(md_content: str, filename: str, stylesheet: str = None):
        return Document(
            markdown2.markdown(md_content, extras=["tables"]),
            filename,
            stylesheet
        )

    @property
    def template(self):
        fn = Path(os.path.dirname(__file__)) / '../../res/template.html'
        return fn.open().read()

    @property
    def stylesheet(self):
        if self._stylesheet is not None:
            fn = self._stylesheet
        else:
            fn = Path(os.path.dirname(__file__)) / '../../res/css/github.css'
        assert fn.is_file()
        return fn.open().read()

    @property
    def html_filename(self):
        return Path(os.path.dirname(__file__)) / f"../tmp/{self.filename}.temp.html"

    def save_to_html(self):
        fn = Path(os.path.dirname(__file__)) / self.html_filename
        fn.open("w")
        fn.write_text(self.template.format(
            **{
                'title': self.filename,
                'body': self.body,
                'custom_style': self.stylesheet
            }
        ))

    def save_to_pdf(self, pdf_path: str):
        self.save_to_html()
        call(["wkhtmltopdf",
              "-B", "25",
              "-L", "25",
              "-R", "25",
              "-T", "25",
              "-q",
              "--title", self.filename,
              "--user-style-sheet", "pdf.css",
              self.html_filename,
              pdf_path])
