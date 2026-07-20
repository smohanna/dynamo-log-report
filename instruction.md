There is an Apache-style access log at /app/access.log. Parse it and write a JSON summary report to /app/report.json.

The report must be a single JSON object with exactly these keys: total_requests (integer), unique_ips (integer), and top_path (string).

Success criteria:

1. /app/report.json exists and is valid JSON.
2. total_requests equals the exact number of non-empty lines in /app/access.log.
3. unique_ips equals the number of distinct client IPs (first whitespace-separated field of each line).
4. top_path equals the request path that appears most often among GET/POST/PUT/DELETE/HEAD/PATCH requests.
