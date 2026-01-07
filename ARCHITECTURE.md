# X-Ray: Decision-Level Debugging for Non-Deterministic Pipelines

## Overview

X-Ray is a lightweight observability system designed to debug multi-step, non-deterministic decision pipelines such as competitor selection, ranking, categorization, and LLM-assisted workflows.

Traditional tracing explains what executed.  
X-Ray explains why a specific output was produced by making decision points first-class: what went in, what came out, and which step caused the collapse.

The system consists of:
- a minimal SDK developers embed into pipelines
- a simple API that ingests run- and step-level decision data

---

## Core Data Model

Run
 └── Step (many)
      ├── step_name
      ├── input
      ├── output
      └── metadata (optional)

### Rationale

A Run represents one execution of a pipeline.
A Step represents a single decision point (filtering, ranking, LLM evaluation).

Steps are normalized rather than stored as nested blobs to enable cross-run and cross-pipeline queries.

### Alternatives Considered

Storing the entire execution as a single nested JSON blob was rejected because it:
- makes querying difficult
- tightly couples schema to pipeline logic
- increases storage and parsing cost

---

## Debugging Walkthrough

A competitor selection pipeline returns a Laptop Stand for a Phone Case.

Using X-Ray:
1. Inspect the run
2. Identify the price_filter step
3. Observe candidate reduction from 4 to 2
4. Conclude the mismatch occurred during filtering, not ranking or LLM evaluation

This localizes the failure to a single decision point.

---

## Queryability

Because steps are first-class entities with explicit names, queries like:
“Show runs where price_filter eliminated more than 90% of candidates”
naturally emerge across pipelines.

---

## Performance & Scale

Capturing full candidate details is expensive.

X-Ray is lossy by default:
- captures summaries and counts
- allows opt-in verbosity for critical runs

Developers control the trade-off between completeness and cost.

---

## Developer Experience

Minimal instrumentation:
    run_id = start_run("pipeline")

Full instrumentation:
    @xray_step(name="price_filter", run_id=run_id)

Backend failures never block pipeline execution.

---

## Non-Goals

- No database
- No UI
- No authentication
- No async queues

---

## What Next

Future work includes batching, storage backends, richer queries, and visualization.
