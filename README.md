# Marchetti Project OS

A focused production system for creating identity-consistent Kaia Marchetti content with Markdown, JSON, and Python.

## Production flow

1. Kaia's permanent identity loads from `01_IDENTITY/`.
2. A content job is created under `04_CONTENT/JOBS/`.
3. The job is validated against locked identity rules.
4. A final provider-ready prompt is assembled from the job and canon.
5. The generated asset receives a QC report.
6. Approved assets are registered in `05_ASSETS/ASSET_MANIFEST.json`.
7.