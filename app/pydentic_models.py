from pydantic import BaseModel


class categoryitem(BaseModel):
    name: str
    description: str




class Subcategory(BaseModel):
    name: str
    description: str