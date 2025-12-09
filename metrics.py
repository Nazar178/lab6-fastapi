from prometheus_client import Counter

request_counter = Counter("app_requests_total", "Total requests")
