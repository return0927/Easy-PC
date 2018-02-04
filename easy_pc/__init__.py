from .db import PgSQL
from .settings import SetManager

settings = SetManager()
db = PgSQL(settings)
