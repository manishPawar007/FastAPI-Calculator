from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/addition/{a}/{b}")
async def add_numbers(a: int, b: int):
    result = a + b
    return {"result": result}

@app.get("/subtraction/{a}/{b}")
async def subtract_numbers(a: int, b: int):
    result = a - b
    return {"result": result}

@app.get("/multiplication/{a}/{b}")
async def multiply_numbers(a: int, b: int):
    result = a * b
    return {"result": result}

@app.get("/division/{a}/{b}")
async def divide_numbers(a: int, b: int):
    if b == 0:
        return {"error": "Division by zero is not allowed."}
    result = a / b
    return {"result": result}

@app.get("/modulus/{a}/{b}")
async def modulus_numbers(a: int, b: int):
    if b == 0:
        return {"error": "Modulus by zero is not allowed."}
    result = a % b
    return {"result": result}
