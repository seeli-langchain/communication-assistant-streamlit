from pydantic import BaseModel

class PersonaItem(BaseModel):
    id: int
    title: str
    apellido: str