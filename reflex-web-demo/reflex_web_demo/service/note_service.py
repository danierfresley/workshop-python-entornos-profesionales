from ..repository.note_repository import select_all

def select_all_note_service():
    notes = select_all()
    print(notes)
    return notes    