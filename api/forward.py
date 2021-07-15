from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)


@app.post("/webhook/forward-email")
async def webhook_forward_email(req: Request):
    print("webhook received")
    body = await req.body()
    return {"status": "ok", "result": body}
