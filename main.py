from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError

from app.config import settings
from app.error_formatter import validation_exception_handler


app = FastAPI(title=settings.app_name, version=settings.app_version)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
