from sqlmodel import Field, Session, create_engine, SQLModel
from ..model import Note


def connection():
    sqlite_file_name = "reflex.db"
    sqlite_url = f"sqlite:///{sqlite_file_name}"
    engine = create_engine(sqlite_url, echo=True)

#     SQLModel.metadata.create_all(engine)
#     note1: Note = Note(notes = "Estudiar Python", date = "2024-12-13")
#     note2: Note = Note(notes = "Leer Articulos Ing Software", date = "2024-12-14")

#     with Session(engine) as session:
#          session.add(note1)
#          session.add(note2)

#          session.commit()

    return engine