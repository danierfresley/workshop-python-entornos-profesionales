import reflex as rx
from typing import Optional
from sqlmodel import Field 

class Note(rx.Model, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    notes: str
    date: str