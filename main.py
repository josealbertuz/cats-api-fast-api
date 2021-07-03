from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from repository import cat_repository
from schemas import cat_schemas

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/')
async def root():
    return {"message": "Hello world"}


@app.post('/cat', response_model=cat_schemas.Cat)
async def create_cat(cat: cat_schemas.CatCreate, db: Session = Depends(get_db)):
    return cat_repository.create_cat(db=db, cat=cat)


@app.get('/cat/{cat_id}')
async def get_cat(cat_id: int, db: Session = Depends(get_db)):
    cat_db = cat_repository.get_cat(db=db, cat_id=cat_id)
    if cat_db is None:
        raise HTTPException(status_code=404, detail="That cat does not exists")
    return cat_db


@app.delete('/cat/{cat_id}')
async def delete_cat(cat_id: int, db: Session = Depends(get_db)):
    if cat_repository.delete_cat(db=db, cat_id=cat_id):
        return {"details": "Cat deleted"}
    raise HTTPException(status_code=404, detail="That cat does not exists")
