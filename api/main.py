from fastapi import FastAPI

from .routers import auth_router, users_router

app = FastAPI()


app.include_router(auth_router, prefix="/auth")
app.include_router(users_router, prefix="/users")



# make all migrations
Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return "Hello!"
