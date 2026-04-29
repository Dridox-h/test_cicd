from fastapi import FastAPI

app = FastAPI(title="Mon App")


@app.get("/")
def root():
    return {"message": "Hello from Cloudeo!", "status": "ok"}


@app.get("/health")
def health():
    return {"status": "healthy"}
