import logging
import reflex as rx

from .model.note_model import Note
from .service.note_service import select_all_note_service, selec_user_by_date_service, create_note_service

from .notify_component import notify_component

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class State(rx.State):
    
    notes: list[Note]
    note_date: str
    
    @rx.background
    async def get_all_note(self):
        async with self:
            self.notes = select_all_note_service()

    @rx.background
    async def get_note_by_date(self):
        async with self:
            self.notes = selec_user_by_date_service(self.note_date)

    @rx.background
    async def create_note(self, data: dict):
        async with self:
           self.notes = create_note_service(notes=data["notes"], date=data["date"])
    
    @rx.event
    def find_on_change(self, value: str):
        self.note_date = value


@rx.page(title="Notes - Reflex", on_load = State.get_all_note)
def index() -> rx.Component:
    return rx.flex(
        rx.heading("Note", align="center"),
        rx.hstack(
            find_note_component(),
            create_note_dialogo_component(),
            style={"margin-top": "40px"}
         ),
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

def find_note_component() -> rx.Component:
    return rx.hstack(
        rx.input(placeholder="Ingresar la fecha", on_change=State.find_on_change),
        rx.button("Buscar nota", on_click=State.get_note_by_date)
    )

def create_user_form() -> rx.Component:
    return rx.form(
        rx.vstack(
            rx.input(
                placeholder="Notas",
                name="notes"
            ),
            rx.input(
                placeholder="Fecha",
                name="date"
            ),
            rx.dialog.close(
                rx.button("Guardar", type="submit")
            )
        ),
        on_submit=State.create_note
    )

def create_note_dialogo_component() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(rx.button("Crear Nota")),
        rx.dialog.content(
            rx.flex(
                rx.dialog.title("Crear Nota"),
                create_user_form(),
                justify="center",
                align="center",
                direction="column"
            ),
            rx.flex(
                rx.dialog.close(
                    rx.button("Cancelar", color_scheme="gray", variant="soft")
                ),
                spacing="3",
                margin_top="16px",
                justify="end"
            ),
            style={"width": "250px"}
        )
    )

app = rx.App()
app.add_page(index)
