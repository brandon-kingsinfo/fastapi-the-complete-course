from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from typing import Optional
import uvicorn
from SQLConnection import get_db

app = FastAPI()


@app.get("/")
async def get_orders(db=Depends(get_db)):
    '''return all orders'''
    orders = db.session.query(db.order_detail).all()

    return orders


if __name__ == '__main__':
    uvicorn.run(app)
