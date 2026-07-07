from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

app = FastAPI(title="FastAPI Calculator")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Get current directory
BASE_DIR = Path(__file__).resolve().parent


# Home Page
@app.get("/")
async def home():
    return FileResponse(BASE_DIR / "index.html")


# Addition
@app.get("/addition/{a}/{b}")
async def add_numbers(a: int, b: int):
    return {"result": a + b}


# Subtraction
@app.get("/subtraction/{a}/{b}")
async def subtract_numbers(a: int, b: int):
    return {"result": a - b}


# Multiplication
@app.get("/multiplication/{a}/{b}")
async def multiply_numbers(a: int, b: int):
    return {"result": a * b}


# Division
@app.get("/division/{a}/{b}")
async def divide_numbers(a: int, b: int):
    if b == 0:
        return {"error": "Division by zero is not allowed."}
    return {"result": a / b}


# Modulus
@app.get("/modulus/{a}/{b}")
async def modulus_numbers(a: int, b: int):
    if b == 0:
        return {"error": "Modulus by zero is not allowed."}
    return {"result": a % b}