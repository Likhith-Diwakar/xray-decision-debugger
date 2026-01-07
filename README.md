# X-Ray: Decision-Level Debugging SDK

X-Ray is a lightweight SDK and API for debugging non-deterministic, multi-step decision systems by making decision reasoning observable.

---

## How to Review This Submission

1. Read ARCHITECTURE.md to understand the data model and trade-offs
2. Run the demo to see a real debugging example
3. Watch the video walkthrough for design reasoning

---

## Setup

python -m venv venv
venv\Scripts\activate
pip install fastapi uvicorn requests

---

## Run the Demo

Start the API:
uvicorn main:app --reload

Run the demo pipeline:
python -m xray.pipeline_demo

---

## What This Shows

- Run-level visibility
- Step-level decision transparency
- Why specific candidates were eliminated

---

## Known Limitations

- No persistent storage
- No query UI
- Simplified data capture

These are intentional to keep focus on decision-level debugging.
