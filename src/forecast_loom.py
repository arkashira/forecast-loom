import time
from dataclasses import dataclass
from typing import Dict

@dataclass
class Metrics:
    forecasts_executed: int = 0
    latency: Dict[float, int] = None
    cost_estimation: float = 0.0

    def __post_init__(self):
        self.latency = {}

    def increment_forecasts_executed(self):
        self.forecasts_executed += 1

    def update_latency(self, latency: float):
        if latency not in self.latency:
            self.latency[latency] = 1
        else:
            self.latency[latency] += 1

    def update_cost_estimation(self, cpu_usage: float):
        self.cost_estimation = cpu_usage * 0.01  # assume $0.01 per CPU unit

    def to_prometheus(self):
        metrics = f"forecasts_executed {self.forecasts_executed}\n"
        for latency, count in self.latency.items():
            metrics += f"latency_bucket{{le=\"{latency}\"}} {count}\n"
        metrics += f"cost_estimation {self.cost_estimation}\n"
        return metrics

class ForecastLoom:
    def __init__(self):
        self.metrics = Metrics()

    def execute_forecast(self, cpu_usage: float):
        start_time = time.time()
        # simulate forecast execution
        time.sleep(0.1)
        end_time = time.time()
        latency = end_time - start_time
        self.metrics.increment_forecasts_executed()
        self.metrics.update_latency(latency)
        self.metrics.update_cost_estimation(cpu_usage)
        return latency

    def get_metrics(self):
        return self.metrics.to_prometheus()
