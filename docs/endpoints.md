# API Endpoints

## GET /health

Simple liveness check.

```bash
curl http://127.0.0.1:8000/health
```

Response:

```json
{ "status": "ok" }
```

## GET /health-details

Status plus service name and version.

```bash
curl http://127.0.0.1:8000/health-details
```

Response:

```json
{
  "status": "ok",
  "service": "checkpoint-api",
  "version": "0.1.0"
}
```

The service name and version are hard-coded constants in `app/main.py` and must be updated manually when the version changes.
