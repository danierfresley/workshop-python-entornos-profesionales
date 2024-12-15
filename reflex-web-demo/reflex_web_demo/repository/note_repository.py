from ..model.note_model import Note
from .connection_db import connection
from sqlmodel import Session, select

def select_all():
    engine = connection()
    with Session(engine) as session:
        query = select(Note)
        return session.exec(query).all()

def select_note_by_date(date: str):
    engine = connection()
    with Session(engine) as session:
        query = select(Note).where(Note.date == date)
        return session.exec(query).all()

def create_note(note: Note):
    engine = connection()
    with Session(engine) as session:
        session.add(note)
        session.commit()
        query = select(Note)
        return session.exec(query).all()