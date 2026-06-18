# STORIES.md – forecast‑loom

## Overview
**forecast‑loom** is a scalable, high‑performance time‑series forecasting platform that ingests massive datasets, trains state‑of‑the‑art models, and serves predictions through familiar data‑science interfaces (Python API, REST, and SQL).  
The backlog below is organized into **Epics**, each containing **User Stories** written in the classic “As a \<role\>, I want \<goal\>, so that \<benefit\>” format, with concrete **Acceptance Criteria**. Stories are ordered to deliver a Minimum Viable Product (MVP) first, then extend functionality toward a production‑grade offering.

---

## EPIC 1 – Data Ingestion & Preparation  

| # | User Story | Acceptance Criteria |
|---|------------|---------------------|
| 1 | **As a Data Engineer, I want a CLI tool that registers a new time‑series dataset, so that analysts can start using the data without writing code.** | - `forecast-loom register <path> --name <dataset-id>` creates a dataset entry in the metadata store.<br>- Supports CSV, Parquet, and Arrow formats.<br>- Validates timestamp column presence and monotonicity.<br>- Returns a unique dataset‑ID and logs registration metadata (size, schema, source). |
| 2 | **As a Data Scientist, I want a Python SDK function `load_dataset(id)` that returns a lazy `dask`/`polars` DataFrame, so that I can explore and preprocess data at scale.** | - `load_dataset(id)` loads data from the storage backend (S3, GCS, or local) into a lazy DataFrame.<br>- Handles automatic type inference for timestamps and numeric columns.<br>- Provides `.head()`, `.describe()`, and `.visualize()` helpers.<br>- Raises a clear error if the dataset‑ID does not exist. |
| 3 | **As a Data Engineer, I want automatic schema versioning, so that downstream pipelines stay consistent when a dataset evolves.** | - Each registration creates a versioned schema entry (`v1`, `v2`, …).<br>- SDK exposes `list_versions(id)` and `load_dataset(id, version=…)`.<br>- Changing a schema without migration triggers a warning and blocks model training until resolved. |

---

## EPIC 2 – Model Definition & Training  

| # | User Story | Acceptance Criteria |
|---|------------|---------------------|
| 4 | **As an ML Engineer, I want a configurable training pipeline (YAML) that selects model architecture, hyper‑parameters, and compute resources, so that experiments are reproducible.** | - YAML schema includes `model: {type, layers, activation}`, `training: {epochs, batch_size, optimizer, learning_rate}`, `resources: {gpu, cpu, memory}`.<br>- `forecast-loom train --config <file.yaml>` launches a reproducible run and stores artefacts in the model registry.<br>- All run metadata (git SHA, container image, timestamps) are persisted. |
| 5 | **As a Data Scientist, I want built‑in support for popular architectures (DeepAR, N‑BEATS, Temporal Fusion Transformer) with sensible defaults, so that I can get baseline forecasts quickly.** | - `model: deep_ar` (or `nbeats`, `tft`) can be specified without extra code.<br>- Default hyper‑parameters are tuned for datasets up to 10 M rows.<br>- Training completes within 30 min on a single V100 for the benchmark dataset (provided in `examples/`). |
| 6 | **As an ML Engineer, I want distributed training via PyTorch Lightning + DDP, so that we can scale to >100 M rows without manual sharding.** | - `resources.distributed: true` triggers DDP launch.<br>- Training automatically shards the dataset using `torch.utils.data.DistributedSampler`.<br>- Logs per‑GPU utilization and verifies that total loss converges similarly to single‑GPU runs. |
| 7 | **As a Product Manager, I want early‑stopping based on a validation metric (e.g., MAE) with a configurable patience, so that we avoid over‑training and reduce compute cost.** | - `training.early_stopping.metric` and `training.early_stopping.patience` are respected.<br>- When patience is exceeded, training stops and the best checkpoint is promoted.<br>- A summary report shows the epoch where early‑stopping triggered. |

---

## EPIC 3 – Model Registry & Versioning  

| # | User Story | Acceptance Criteria |
|---|------------|---------------------|
| 8 | **As a DevOps Engineer, I want a central model registry (REST API) that stores model artefacts, metadata, and lineage, so that production services can fetch the exact version they need.** | - `POST /models` registers a new model version with fields: `model_id`, `dataset_id`, `config_hash`, `metrics`, `artifact_uri`.<br>- `GET /models/{model_id}?latest=true` returns the most recent approved version.<br>- Registry persists in PostgreSQL + object storage (e.g., S3). |
| 9 | **As a Data Scientist, I want to compare multiple model versions side‑by‑side (metrics table), so that I can select the best candidate for deployment.** | - `GET /models/{model_id}/comparisons` returns a JSON/HTML table with MAE, RMSE, MAPE, training time, and resource usage for each version.<br>- UI highlights the “dominant” version (lowest error, within resource budget). |

---

## EPIC 4 – Serving & Integration  

| # | User Story | Acceptance Criteria |
|---|------------|----------------
