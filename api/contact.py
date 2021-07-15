import os
from fastapi import FastAPI, Response, status
from pydantic import BaseModel
import httpx

HCAPTCHA_VERIFY_URL = "https://hcaptcha.com/siteverify"

app = FastAPI()


class ContactMeDetail(BaseModel):
    name: str
    email: str
    details: str
    token: str
    ekey: str


@app.post("/api/contact")
async def contact(detail: ContactMeDetail, res: Response):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            HCAPTCHA_VERIFY_URL,
            data={
                "secret": os.environ.get("HCAPTCHA_SECRET_KEY"),
                "response": detail.token,
            },
        )

        response = response.json()

        if response["success"]:
            res.status_code = status.HTTP_200_OK
            return detail

    res.status_code = status.HTTP_400_BAD_REQUEST
    return {"message": "Invalid captcha"}
