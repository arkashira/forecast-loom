import pytest
from forecast_loom import ForecastLoom, Metrics

def test_forecasts_executed():
    loom = ForecastLoom()
    assert loom.metrics.forecasts_executed == 0
    loom.execute_forecast(0.5)
    assert loom.metrics.forecasts_executed == 1

def test_latency():
    loom = ForecastLoom()
    latency = loom.execute_forecast(0.5)
    assert latency > 0
    assert latency in loom.metrics.latency

def test_cost_estimation():
    loom = ForecastLoom()
    loom.execute_forecast(0.5)
    assert loom.metrics.cost_estimation > 0

def test_to_prometheus():
    loom = ForecastLoom()
    loom.execute_forecast(0.5)
    metrics = loom.get_metrics()
    assert "forecasts_executed" in metrics
    assert "latency_bucket" in metrics
    assert "cost_estimation" in metrics

def test_edge_case_zero_cpu_usage():
    loom = ForecastLoom()
    loom.execute_forecast(0.0)
    assert loom.metrics.cost_estimation == 0.0
