from ..model.note_model import Note
from .connection_db import connection
from sqlmodel import Session, select

def select_all():
    engine = connection()
    with Session(engine) as session:
        query = select(Note)
        return session.exec(query).all()