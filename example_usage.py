from client import AgenticDevEnvironmentLiveTelemetryLoopClient

def main():
    client = AgenticDevEnvironmentLiveTelemetryLoopClient()
    state = {"active_branch": "agent-synthesis-v3", "memory_usage_mb": 420}
    res = client.monitor_dev_loop(state)
    print(f"Health Score: {res['execution_health_score'] * 100}%")
    print(f"Status: {res['loop_status']}")
    print(f"Anomalies: {len(res['live_anomalies_detected'])}")

if __name__ == "__main__":
    main()
