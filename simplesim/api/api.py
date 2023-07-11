"""Main API module"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/{data}")
async def main(data):
    """Accepts the Data from the Sims"""
    print(data)
