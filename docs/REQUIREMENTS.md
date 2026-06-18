<think>
Okay, I need to create a REQUIREMENTS.md file for the forecast-loom project. Let me start by understanding the context provided. The project is a time-series forecasting model that's scalable and efficient, integrated with data science tools. The user wants functional and non-functional requirements, constraints, and assumptions.

First, functional requirements. The main features should include data ingestion, preprocessing, model training, forecasting, integration with tools, and a user interface. Let me break these down. Data ingestion needs to support various formats and real-time streams. Preprocessing should handle missing data, normalization, etc. Model training must allow different algorithms and hyperparameter tuning. Forecasting needs to generate predictions and confidence intervals. Integration with tools like Python, R, TensorFlow, PyTorch is essential. The UI should have dashboards and visualization tools.

Non-functional requirements: Performance is crucial. The system should handle large datasets efficiently. Maybe specify processing time for 1 million data points. Scalability to handle increasing data. Security aspects like data encryption and access controls. Reliability with high availability and error handling. Usability for both experts and non-experts.

Constraints: Use existing frameworks like vLLM and SGLang. Leverage the Axentx BRAIN for datasets and knowledge. Avoid duplicating existing products like iceoryx2. Compliance with licenses of the datasets provided (Apache-2.0, MIT, etc.).

Assumptions: Availability of the BRAIN's datasets, sufficient computational resources, user familiarity with data science tools. Also, that the model can be validated for real-world use cases before shipping.

I need to structure all this into a markdown document with clear sections. Number the functional requirements as FR-1 to FR-6. Non-functional under their categories. Constraints and assumptions as bullet points. Make sure it's concrete and shippable, avoiding vague terms. Check for any missing aspects like error handling or specific integration APIs. Also, ensure that the requirements align with the existing portfolio and don't overlap with iceoryx2. Maybe mention the use of the Axentx RUNBOOK for deployment. Alright, time to put it all together in the correct format.
</think>

# REQUIREMENTS.md

## Functional Requirements

### FR-1: Data Ingestion & Integration
- Support ingestion of time-series data from CSV, Parquet, JSON, and real-time streaming sources (Kafka, AWS Kinesis)
- Provide Python SDK with Pandas/Numpy integration for data loading
- Implement automatic schema detection and type inference

### FR-2: Preprocessing Pipeline
- Include automated handling of missing values (interpolation, forward-fill)
- Support feature engineering (seasonality extraction, rolling windows)
- Implement normalization/scaling (Z-score, Min-Max)
- Provide configurable data validation rules

### FR-3: Model Training & Management
- Support multiple forecasting algorithms (ARIMA, Prophet, LSTM, Transformer)
- Enable automated hyperparameter tuning (Bayesian optimization)
- Maintain versioned model registry with metadata tracking
- Provide cross-validation framework for time-series data

### FR-4: Forecasting & Analysis
- Generate multi-step forecasts with confidence intervals
- Support scenario analysis (what-if simulations)
- Implement anomaly detection in forecasted data
- Export predictions in multiple formats (CSV, JSON, database)

### FR-5: Tool Integration
- Native integration with Jupyter Notebooks, MLflow, and DVC
- Provide REST API for programmatic access
- Implement TensorFlow/PyTorch compatibility layers
- Support deployment as Docker containers

### FR-6: User Interface
- Web-based dashboard for model monitoring and visualization
- Interactive time-series charting with zoom/pan capabilities
- Model performance metrics display (MAE, RMSE, MAPE)
- Alert configuration interface for forecast thresholds

## Non-Functional Requirements

### Performance
- Process 1 million time-series data points in <30 seconds (95th percentile)
- Maintain <200ms latency for API requests under 100 QPS load
- Support horizontal scaling to handle 10M+ time-series points

### Security
- Implement TLS 1.3 for all data transmissions
- Enforce role-based access control (RBAC) for model management
- Store sensitive data using AES-256 encryption at rest
- Regular vulnerability scanning of dependencies

### Reliability
- Achieve 99.9% system availability (SLA)
- Implement automated model retraining with version rollback capability
- Maintain 99.95% prediction accuracy consistency across deployments
- Comprehensive error logging and monitoring with Prometheus/Grafana

### Usability
- Provide interactive tutorials for new users
- Maintain API documentation with Swagger/OpenAPI
- Implement auto-complete suggestions in UI inputs
- Support dark/light theme toggle in web interface

## Constraints

- Must use vLLM (vllm-project/vllm) for inference acceleration
- Leverage Axentx BRAIN (pgvector) for dataset storage and retrieval
- Avoid duplicating functionality from existing Axentx products (e.g., iceoryx2 IPC capabilities)
- Comply with dataset licenses (Apache-2.0, MIT, CDLA-Permissive-2.0)
- Maintain compatibility with Axentx RUNBOOK deployment standards
- Use SGLang (sgl-project/sglang) for structured output generation

## Assumptions

- Axentx BRAIN contains sufficient time-series datasets for initial training
- Target environments have GPU acceleration available (NVIDIA A100+)
- Users have basic proficiency with Python and data science tools
- Forecast validation will be performed through Axentx's revenue-validation pipeline
- Model performance requirements can be met with current hardware constraints
- Integration with existing Axentx systems (HR/BD, QA) will follow standard protocols
