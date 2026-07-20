import json
import re
from pathlib import Path
from collections import Counter


def test_report_exists():
    """Criterion 1: /app/report.json exists and is valid JSON."""
    assert Path("/app/report.json").exists(), "no report.json found"


def test_report_validity():
    """Criteria 2-4: total_requests, unique_ips and top_path match values recomputed from /app/access.log."""
    with open("/app/report.json") as f:
        data = json.load(f)

    assert "total_requests" in data, "Missing total_requests"
    assert "unique_ips" in data, "Missing unique_ips"
    assert "top_path" in data, "Missing top_path"

    # Recalcula os dados lendo o access.log diretamente para checar a precisão
    paths, ips, total = Counter(), set(), 0
    with open("/app/access.log") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            total += 1
            ips.add(line.split()[0])
            m = re.search(r'"(?:GET|POST|PUT|DELETE|HEAD|PATCH) (\S+) ', line)
            if m:
                paths[m.group(1)] += 1

    assert data["total_requests"] == total, (
        f"Expected {total}, got {data['total_requests']}"
    )
    assert data["unique_ips"] == len(ips), (
        f"Expected {len(ips)}, got {data['unique_ips']}"
    )
    assert data["top_path"] == paths.most_common(1)[0][0], "Top path mismatch"
