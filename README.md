# Main_Prv_Repo

ServiceNow-style incident sample generator for server monitoring and observability exercises.

## Generate incident table (Excel input)

Run:

```bash
python3 incident_table_generator.py
```

The script creates an Excel-compatible CSV file under `output/` with incident fields such as:

- incident number and description
- category/subcategory and priority
- server/CI details
- opened/acknowledged/resolved timestamps
- metric thresholds and observed values
- observability signals (metrics/logs/traces)
- impacted service and business impact
