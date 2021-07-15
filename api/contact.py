import os
from fastapi import FastAPI, Response, status, BackgroundTasks
from pydantic import BaseModel
import requests
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

HCAPTCHA_VERIFY_URL = "https://hcaptcha.com/siteverify"

app = FastAPI()


class ContactMeDetail(BaseModel):
    name: str
    email: str
    details: str
    token: str
    ekey: str


def post_email(detail: ContactMeDetail):
    html = f"""
            <h1>Contact me form submission details:</h1>
            <h2>Name: {detail.name}</h2>
            <h3>Email: <a href='mailto:{detail.email}'>{detail.email}</a></h3>
            <p>Details: {detail.details}</p>
        """
    message = Mail(
        from_email="contact@bimalghartimagar.com.np",
        to_emails="bimal.gharti.magar@gmail.com",
        subject="Somebody reached out to you from your portfolio",
        html_content=html,
    )
    try:
        sg = SendGridAPIClient(os.environ.get("SENDGRID_API_KEY"))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)


@app.post("/api/contact")
async def contactr(detail: ContactMeDetail, res: Response, task: BackgroundTasks):
    response = requests.post(
        HCAPTCHA_VERIFY_URL,
        data={
            "secret": os.environ.get("HCAPTCHA_SECRET_KEY"),
            "response": detail.token,
        },
    )

    response = response.json()

    if response["success"]:
        res.status_code = status.HTTP_200_OK
        task.add_task(post_email, detail)
        return {
            "success": True,
            "msg": "Thank you for your message. I'll reach out to you soon.",
        }

    res.status_code = status.HTTP_400_BAD_REQUEST
    return {"success": False, "msg": "Captcha Error"}
