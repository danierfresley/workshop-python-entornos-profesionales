from ..repository.note_repository import select_all, select_note_by_date, create_note
from ..model.note_model import Note

def select_all_note_service():
    notes = select_all()
    print(notes)
    return notes    

def selec_user_by_date_service(date: str):
    if(len(date) !=0):
        return select_note_by_date(date)
    else:
        return select_all()

def create_note_service(notes: str, date: str):
    note_save: Note = Note(notes=notes, date=date)
    return create_note(note_save)
