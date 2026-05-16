"""Generate a ServiceNow-like incident table for server monitoring observability exercises.

Creates sample incident records and exports them to CSV, which can be opened
in Excel and used as an input sheet for observability concept checks.
"""

from __future__ import annotations

import csv
from dataclasses import asdict, dataclass
from datetime import UTC, datetime
from pathlib import Path


@dataclass(frozen=True)
class Incident:
    incident_number: str
    short_description: str
    category: str
    subcategory: str
    priority: str
    state: str
    assignment_group: str
    configuration_item: str
    opened_at_utc: str
    acknowledged_at_utc: str
    resolved_at_utc: str
    metric_name: str
    metric_threshold: str
    observed_value: str
    root_cause_hypothesis: str
    observability_signal: str
    source_tool: str
    impacted_service: str
    business_impact: str


INCIDENTS = [
    Incident("INC0012451", "CPU utilization spike on app-server-01", "Infrastructure", "CPU", "2 - High", "Resolved", "SRE Monitoring", "app-server-01", "2026-05-10T02:14:00Z", "2026-05-10T02:18:00Z", "2026-05-10T02:42:00Z", "cpu.utilization.percent", "> 85% for 5m", "93%", "Runaway Java process after batch release", "Metrics", "Datadog", "checkout-api", "Elevated API latency for checkout"),
    Incident("INC0012452", "Disk space critically low on db-server-02", "Infrastructure", "Storage", "1 - Critical", "Resolved", "Database Operations", "db-server-02", "2026-05-11T11:06:00Z", "2026-05-11T11:08:00Z", "2026-05-11T11:31:00Z", "disk.free.percent", "< 10%", "6%", "Unexpected log growth from failed replication", "Metrics + Logs", "Prometheus/Grafana", "orders-db", "Risk of write failures"),
    Incident("INC0012453", "Packet loss detected between web and cache nodes", "Network", "Connectivity", "2 - High", "In Progress", "Network Engineering", "edge-switch-03", "2026-05-12T17:45:00Z", "2026-05-12T17:48:00Z", "", "network.packet.loss.percent", "> 2% for 10m", "3.4%", "Intermittent switch port errors", "Metrics + Traces", "New Relic", "session-cache", "Intermittent session drops"),
    Incident("INC0012454", "Memory leak suspected on recommendation worker", "Application", "Memory", "3 - Moderate", "New", "Platform Engineering", "reco-worker-07", "2026-05-13T08:20:00Z", "", "", "memory.rss.bytes", "Increase > 30% hour-over-hour", "+47%", "Unreleased object references in consumer loop", "Metrics + Logs + Profiling", "Elastic + APM", "recommendation-engine", "Possible pod restarts and degraded recommendations"),
]


def write_csv(output_dir: Path) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(UTC).strftime("%Y%m%d_%H%M%S")
    csv_path = output_dir / f"servicenow_incidents_{timestamp}.csv"

    rows = [asdict(item) for item in INCIDENTS]
    with csv_path.open("w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    return csv_path


def main() -> None:
    csv_path = write_csv(Path("output"))
    print(f"Created {len(INCIDENTS)} incidents")
    print(f"CSV (Excel-compatible): {csv_path}")


if __name__ == "__main__":
    main()
