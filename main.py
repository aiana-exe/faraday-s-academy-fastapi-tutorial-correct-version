from fastapi import FastAPI, Depends

from api import users, courses, sections
from db.db_setup import engine, get_db
from db.models import user, course

from sqlalchemy.ext.asyncio import AsyncSession

user.Base.metadata.create_all(bind=engine)
course.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Fast API LMS",
    description="LMS for managing students and courses.",
    version="0.0.1",
    contact={
        "name": "Gwen",
        "email": "gwen@example.com",
    },
    license_info={
        "name": "MIT",
    },
)

app.include_router(users.router)
app.include_router(courses.router)
app.include_router(sections.router)


# test route
# @app.get("/")
# async def root():
#     print("Hello")
#     return {"message": "Hello World"}



# async
# @app.get("/")
# async def read_root(db: AsyncSession = Depends(get_db)):
#     result = await db.execute(select(course.Course))
#     items = result.scalars().all()
#     return items