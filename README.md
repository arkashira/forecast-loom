# Forecast Loom

A simple Python project that emits metrics for every forecast executed.

## Usage

1. Run `python -m pytest` to run the tests.
2. Run `python src/forecast_loom.py` to execute the forecast loom.

## Metrics

The forecast loom emits the following metrics:

* `forecasts_executed`: the number of forecasts executed
* `latency_bucket`: the latency of each forecast execution
* `cost_estimation`: the estimated cost of each forecast execution
