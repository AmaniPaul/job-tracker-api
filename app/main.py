from fastapi import FastAPI

app = FastAPI(title="Job Tracker Api")

@app.get("/health")
def health():
    return {"status": "ok"}