# Tech Spec: Forecast-Loom v1
## Stack

* Language: Python 3.9+
* Framework: FastAPI (async web framework)
* Runtime: Docker (containerization)
* Database: PostgreSQL (relational database)
* Time-series database: TimescaleDB (columnar storage for time-series data)
* Data science libraries: pandas, NumPy, scikit-learn, statsmodels
* Integration libraries: Apache Airflow, Apache Beam

## Hosting

* Free-tier-first hosting: Heroku (free dyno, PostgreSQL, and add-ons)
* Specific platforms: AWS (EC2, RDS, S3), GCP (Compute Engine, Cloud SQL, Cloud Storage)
* Containerization: Docker Hub (image repository)

## Data Model

* Tables/Collections:
	+ `forecasts`: stores forecasted values for each time series
		- `id` (primary key): UUID
		- `time_series_id`: foreign key referencing `time_series`
		- `forecast_date`: timestamp
		- `value`: forecasted value
	+ `time_series`: stores metadata for each time series
		- `id` (primary key): UUID
		- `name`: string
		- `description`: string
		- `data_source`: string
	+ `models`: stores metadata for each trained model
		- `id` (primary key): UUID
		- `name`: string
		- `description`: string
		- `model_type`: string (e.g. ARIMA, Prophet)
* Key fields:
	+ `id`: UUID for each table/collection

## API Surface

* Endpoints:
	1. `GET /time-series`: retrieve list of time series
		- Response: JSON array of time series objects
	2. `GET /time-series/{id}`: retrieve time series by ID
		- Response: JSON object representing time series
	3. `POST /time-series`: create new time series
		- Request: JSON object with time series metadata
		- Response: JSON object representing created time series
	4. `GET /forecasts`: retrieve list of forecasts
		- Response: JSON array of forecast objects
	5. `GET /forecasts/{id}`: retrieve forecast by ID
		- Response: JSON object representing forecast
	6. `POST /forecasts`: create new forecast
		- Request: JSON object with forecast metadata
		- Response: JSON object representing created forecast
	7. `GET /models`: retrieve list of models
		- Response: JSON array of model objects
	8. `GET /models/{id}`: retrieve model by ID
		- Response: JSON object representing model
	9. `POST /models`: create new model
		- Request: JSON object with model metadata
		- Response: JSON object representing created model
	10. `GET /status`: retrieve system status
		- Response: JSON object with system status

## Security Model

* Authentication: OAuth 2.0 with JWT tokens
* Authorization: role-based access control (RBAC)
* Secrets management: Hashicorp Vault (secrets storage)
* IAM: AWS IAM (identity and access management)

## Observability

* Logging: Loggly (centralized logging)
* Metrics: Prometheus (metrics collection)
* Traces: Jaeger (distributed tracing)
* Monitoring: New Relic (application performance monitoring)

## Build/CI

* Build tool: Docker (containerization)
* CI tool: GitHub Actions (continuous integration)
* Testing framework: Pytest (unit testing)
* Code coverage: codecov (code coverage analysis)
* Code quality: SonarQube (code quality analysis)