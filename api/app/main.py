from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import router
from routers.validate import router as validate_router

app = FastAPI(title="Word Validation API")

# CORS สำหรับทุกที่
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# รวม router
app.include_router(validate_router, prefix="/api")



# Optional: endpoint รับ webhook จาก n8n (ถ้าต้องการ)
@app.post("/api/webhook/worddee_event")
async def receive_webhook(data: dict):
    print("🔥 Received from n8n:", data)
    return {"status": "ok", "received": data}

@app.get("/")
def root():
    return {"message": "API is running"}