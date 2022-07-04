from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.faces import router

tags_metadata = [
    {
        "name": "Faces",
        "description": "Read and Write to Employee Face Encodings.",
    }
]

app = FastAPI(
    docs_url="/",
    title="Three Tier System - Faces REST API ",
    description="REST API for Three Tier System Faces",
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Ashley T Shumba",
        "url": "https://ashleytshumba.co.zw",
        "email": "ashleytshumba@gmail.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
    openapi_url="/api/v1/openapi.json",
    openapi_tags=tags_metadata,
)


origins = [
    "http://localhost:3000",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# @app.get("/")
# async def read_root():
#     return {"Hello": "World"}


app.include_router(
    router,
    prefix="/api",
)
