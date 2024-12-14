import logging
import reflex as rx

from .model.note_model import Note
from .service.note_service import select_all_note_service

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class State(rx.State):
    
    notes: list[Note]
    
    @rx.background
    async def get_all_note(self):
        async with self:
            self.notes = select_all_note_service()


@rx.page(title="Notes - Reflex", on_load = State.get_all_note)
def index() -> rx.Component:
    return rx.flex(
        rx.heading("Note", align="center"),
        table_note(State.notes),
        direction="column",
        style={"width":"60vw", "margin":"auto"}
    )

def table_note(list_note: list[Note]) -> rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Id"),
                rx.table.column_header_cell("Note"),
                rx.table.column_header_cell("Fecha"),
                rx.table.column_header_cell("Acción")
            )
        ),
        rx.table.body(
            rx.foreach(list_note, row_table)
        ),
    )

def row_table(note: Note) -> rx.Component:
    return rx.table.row(
        rx.table.cell(note.id),
        rx.table.cell(note.notes),
        rx.table.cell(note.date),
        rx.table.cell(rx.hstack(
            rx.button("Eliminar")
        ))
    )

app = rx.App()
app.add_page(index)
