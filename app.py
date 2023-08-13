from fastapi import FastAPI, HTTPException
from pynginx import *

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/add_route")
async def route_adder():
    return add_route()

@app.get("/add_rule")
async def relu_adder(rule_name: str = "", rule_location: str = "", rule_value: str = ""):
    try:
        result = add_rule(rule_name, rule_location, rule_value)
    except ValueError as e:
        raise HTTPException(
            status_code=500,
            detail=e.args,
        )

    return result