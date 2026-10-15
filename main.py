from fastapi import FastAPI

app = FastAPI()


@app.get("/healthz")
def healthz():
    return {"status": "probe-healthz-ok"}


@app.get("/")
def root():
    return {"app": "probe-with-healthz"}
