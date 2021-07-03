from sqlalchemy.orm import Session
from models import cat_model
from schemas import cat_schemas


def get_cat(db: Session, cat_id: int):
    return db.get(cat_model.Cat, cat_id)


def create_cat(db: Session, cat: cat_schemas.CatCreate):
    db_cat = cat_model.Cat(name=cat.name, age=cat.age, breed=cat.breed)
    db.add(db_cat)
    db.commit()
    db.refresh(db_cat)
    return db_cat


def delete_cat(db: Session, cat_id: int):
    db_cat = db.get(cat_model.Cat, cat_id)
    if db_cat is None:
        return False
    db.delete(db_cat)
    db.commit()
    return True
