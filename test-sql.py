from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from typing import Optional
import uvicorn
from SQLConnection import SQLConnect

app = FastAPI()


@app.get("/")
async def get_orders(db=Depends(SQLConnect)):
    '''return all orders'''
    orders = db.session.query(db.order_master).all()

    return orders


if __name__ == '__main__':
    uvicorn.run(app)
