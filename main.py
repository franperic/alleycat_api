from fastapi import FastAPI

app = FastAPI()


@app.get("/hello_there")
async def root():
    return {"message": "Harrow - das het klappet"}

@app.get("/horde_patorde")
async def root():
    return {"message": "Aloha - ja, au das gaht!"}

@app.get("/grande_terrazza")
async def root():
    return {"message": "Check!"}