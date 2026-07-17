# Marchetti Project OS

A focused production system for creating identity-consistent Kaia Marchetti content with Markdown, JSON, and Python.

## Production flow

1. Kaia's permanent identity loads from `01_IDENTITY/`.
2. A content job is created under `04_CONTENT/JOBS/`.
3. The job is validated against locked identity rules.
4. A final provider-ready prompt is assembled from the job and canon.
5. The generated asset receives a QC report.
6. Approved assets are registered in `05_ASSETS/ASSET_MANIFEST.json`.
7. Repeated drift is recorded in `07_ANALYTICS/DRIFT_LOG.json`.

## First commands

From the repository root in PowerShell:

```powershell
python 02_PIPELINE\scripts\create_job.py --slug miami-morning-walk
python 02_PIPELINE\scripts\validate_job.py 04_CONTENT\JOBS\miami-morning-walk\GENERATION_JOB.json
python 02_PIPELINE\scripts\build_prompt.py 04_CONTENT\JOBS\miami-morning-walk\GENERATION_JOB.json
```

Then open:

```text
04_CONTENT/JOBS/miami-morning-walk/FINAL_PROMPT.md
```

Attach the approved Kaia anchor image and paste that prompt into the image generator. Complete `QC_REPORT.json` before approving the asset.
