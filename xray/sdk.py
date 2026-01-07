import json
import uuid
import requests
from functools import wraps

XRAY_API_URL = "http://127.0.0.1:8000"

def start_run(pipeline: str):
    run_id = str(uuid.uuid4())
    payload = {
        "run_id": run_id,
        "pipeline": pipeline
    }

    try:
        requests.post(f"{XRAY_API_URL}/runs", json=payload, timeout=1)
    except Exception:
        pass

    return run_id

def xray_step(name: str, run_id: str):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            input_data = {
                "args": args,
                "kwargs": kwargs
            }

            result = fn(*args, **kwargs)

            payload = {
                "run_id": run_id,
                "step": name,
                "input": str(input_data),
                "output": str(result)
            }

            try:
                requests.post(f"{XRAY_API_URL}/steps", json=payload, timeout=1)
            except Exception:
                pass

            return result
        return wrapper
    return decorator

