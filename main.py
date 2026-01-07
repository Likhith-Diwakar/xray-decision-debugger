from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok"}

from pydantic import BaseModel

class RunIn(BaseModel):
    run_id: str
    pipeline: str


@app.post("/runs")
def create_run(run: RunIn):
    print("XRAY RUN STARTED:", run.run_id, run.pipeline)
    return {"ok": True}

class StepIn(BaseModel):
    run_id: str
    step: str
    input: str
    output: str


@app.post("/steps")
def create_step(step: StepIn):
    print(
        "XRAY STEP:",
        step.run_id,
        step.step,
        "INPUT:",
        step.input,
        "OUTPUT:",
        step.output
    )
    return {"ok": True}
