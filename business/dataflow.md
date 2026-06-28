# dataflow.md

## System Dataflow Architecture – *forecast‑loom*

```
+-------------------+          +-------------------+          +-------------------+
|  External Data    |          |  Ingestion Layer  |          |  Processing/      |
|  Sources (API,    |  --->    |  (Kafka / Kinesis)|  --->    |  Transform Layer  |
|  File, DB, IoT)   |          |  (Kafka Connect,  |          |  (Spark / Flink)  |
|                   |          |  Flume, Debezium) |          |  (ML Pipelines)   |
+-------------------+          +-------------------+          +-------------------+
          |                           |                           |
          |                           |                           |
          v                           v                           v
+-------------------+          +-------------------+          +-------------------+
|  Storage Tier     |          |  Query / Serving  |          |  Egress to User   |
|  (S3 / GCS / HDFS)|          |  Layer (Presto,   |          |  (REST / GraphQL) |
|  (Delta Lake /    |          |  Trino, Athena)   |          |  (SDK, CLI)       |
|  Parquet)         |          |  (Auth: JWT, RBAC)|          |  (Auth: OAuth2)   |
+-------------------+          +-------------------+          +-------------------+
```

### 1. External Data Sources
- **Public APIs** – Weather, economic indicators, market feeds (e.g., Alpha Vantage, OpenWeatherMap).
- **Enterprise Databases** – SQL/NoSQL (PostgreSQL, MongoDB, Cassandra) via CDC connectors.
- **File Stores** – S3, GCS, Azure Blob (CSV, Parquet, JSON).
- **IoT Streams** – MQTT, Kafka topics from sensors, edge devices.
- **User‑Uploaded Datasets** – CSV/Parquet via web portal or SFTP.

### 2. Ingestion Layer
| Component | Role | Key Features |
|-----------|------|--------------|
| **Kafka / Kinesis** | Stream broker | Low‑latency, high‑throughput, partitioned topics. |
| **Kafka Connect** | Source connectors | Pull from JDBC, MongoDB, S3, HTTP APIs. |
| **Flume / Debezium** | CDC for relational DBs | Capture change events in near‑real time. |
| **Schema Registry** | Avro/Protobuf schemas | Enforce data contracts, versioning. |
| **Auth** | OAuth2 / API keys | Secure source credentials, token rotation. |

### 3. Processing / Transform Layer
| Component | Role | Key Features |
|-----------|------|--------------|
| **Spark Structured Streaming / Flink** | Batch & stream ETL | Windowing, aggregation, feature engineering. |
| **ML Pipelines (MLflow / Kubeflow)** | Model training & inference | Auto‑ML, hyper‑parameter tuning, model registry. |
| **Delta Lake / Iceberg** | ACID transactions | Schema evolution, time travel, upserts. |
| **Feature Store (Feast)** | Centralized feature repository | Real‑time & batch feature serving. |
| **Auth** | Service‑to‑service | Mutual TLS, JWT validation, role‑based access. |

### 4. Storage Tier
| Storage | Format | Use Case |
|---------|--------|----------|
| **Object Store (S3 / GCS)** | Parquet / ORC | Raw & curated datasets, long‑term archival. |
| **Delta Lake** | Parquet + transaction log | Versioned, updatable tables for training data. |
| **Data Warehouse (Snowflake / BigQuery)** | Columnar | Analytical queries, reporting dashboards. |
| **Cache (Redis / Memcached)** | In‑memory | Low‑latency feature lookup for inference. |
| **Auth** | IAM policies, bucket ACLs | Fine‑grained access control. |

### 5. Query / Serving Layer
| Component | Role | Key Features |
|-----------|------|--------------|
| **Presto / Trino** | SQL query engine | Federated queries across Delta Lake, S3, DBs. |
| **Athena / BigQuery** | Serverless SQL | Pay‑per‑query, no provisioning. |
| **GraphQL / REST API** | Front‑end gateway | Aggregated endpoints for forecasts, metrics. |
| **Auth** | JWT, OAuth2, RBAC | Token validation, scope checks, audit logging. |

### 6. Egress to User
| Delivery | Interface | Auth |
|----------|-----------|------|
| **Web UI** | React + Ant Design | OAuth2, SSO (Okta, Auth0). |
| **CLI Tool** | Python SDK | API keys, OAuth2 refresh tokens. |
| **SDK** | Python / R / Java | OAuth2, client‑credentials flow. |
| **Webhook** | JSON payload | HMAC signature verification. |
| **Export** | CSV / Parquet | Signed URLs, S3 pre‑signed links. |

---

#### Auth Boundaries Summary
1. **External ↔ Ingestion** – OAuth2 tokens or API keys per source.
2. **Ingestion ↔ Processing** – Mutual TLS + JWT signed by ingestion service.
3. **Processing ↔ Storage** – IAM roles on object store, Kerberos for HDFS.
4. **Storage ↔ Query** – IAM policies + Presto/Trino role mapping.
5. **Query ↔ Egress** – OAuth2 scopes (`forecast:read`, `forecast:write`).
6. **Egress ↔ User** – SSO + MFA, audit trail in CloudTrail / GCP Audit Logs.

This architecture ensures **scalability**, **data integrity**, and **secure access** throughout the forecasting pipeline, aligning with the *forecast‑loom* hypothesis of a high‑performance, large‑dataset time‑series forecasting service.