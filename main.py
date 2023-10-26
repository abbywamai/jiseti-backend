from fastapi import FastAPI, HTTPException, Depends
from fastapi_users import FastAPIUsers, models
from fastapi_users.authentication import JWTAuthentication

from database import SessionLocal, engine
from models import Base, User, Red_flag, Intervention, Status

Base.metadata.create_all(bind=engine)

SECRET = "YOUR_SECRET_KEY"

users = FastAPIUsers(
    models.get_user_db,
    models.TortoiseBaseUserModel,
    models.UserCreate,
    models.UserUpdate,
    models.UserDB,
    SECRET,
)

app = FastAPI()

auth_backends = [JWTAuthentication(secret=SECRET, lifetime_seconds=3600)]

from database import get_db
from fastapi import Depends, HTTPException, Response, status

# Dependency for getting the DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/interventions/", dependencies=auth_backends, response_model=Intervention)
async def create_intervention(intervention: Intervention, current_user: models.UserDB = Depends(users.get_current_active_user)):
    intervention_db = Intervention(**intervention.dict(), userid=current_user.id)
    db.add(intervention_db)
    db.commit()
    db.refresh(intervention_db)
    return intervention_db

@app.get("/interventions/{intervention_id}", response_model=Intervention)
async def read_intervention(intervention_id: int):
    intervention = db.query(Intervention).filter(Intervention.id == intervention_id).first()
    if intervention is None:
        raise HTTPException(status_code=404, detail="Intervention not found")
    return intervention

@app.delete("/interventions/{intervention_id}", dependencies=auth_backends, response_model=Intervention)
async def delete_intervention(intervention_id: int, current_user: models.UserDB = Depends(users.get_current_active_user)):
    intervention = db.query(Intervention).filter(Intervention.id == intervention_id).first()
    if intervention is None:
        raise HTTPException(status_code=404, detail="Intervention not found")
    if intervention.userid != current_user.id:
        raise HTTPException(status_code=403, detail="You do not have permission to delete this intervention")
    db.delete(intervention)
    db.commit()
    return intervention

@app.post("/red_flags/", dependencies=auth_backends, response_model=Red_flag)
async def create_red_flag(red_flag: Red_flag, current_user: models.UserDB = Depends(users.get_current_active_user)):
    red_flag_db = Red_flag(**red_flag.dict(), userid=current_user.id)
    db.add(red_flag_db)
    db.commit()
    db.refresh(red_flag_db)
    return red_flag_db

@app.get("/red_flags/{red_flag_id}", response_model=Red_flag)
async def read_red_flag(red_flag_id: int):
    red_flag = db.query(Red_flag).filter(Red_flag.id == red_flag_id).first()
    if red_flag is None:
        raise HTTPException(status_code=404, detail="Red flag not found")
    return red_flag

@app.delete("/red_flags/{red_flag_id}", dependencies=auth_backends, response_model=Red_flag)
async def delete_red_flag(red_flag_id: int, current_user: models.UserDB = Depends(users.get_current_active_user)):
    red_flag = db.query(Red_flag).filter(Red_flag.id == red_flag_id).first()
    if red_flag is None:
        raise HTTPException(status_code=404, detail="Red flag not found")
    if red_flag.userid != current_user.id:
        raise HTTPException(status_code=403, detail="You do not have permission to delete this red flag")
    db.delete(red_flag)
    db.commit()
    return red_flag
