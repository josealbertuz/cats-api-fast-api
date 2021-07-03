from pydantic import BaseModel


class CatBase(BaseModel):
    name: str
    age: int
    breed: str


class CatCreate(CatBase):
    pass


class Cat(CatBase):
    id: int

    class Config:
        orm_mode = True
