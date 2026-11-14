# Endpoints

## GET /health
Liveness check.
```bash
curl http://localhost:8000/health
# {"status":"ok"}
```

## GET /health-details
Service status with name and version. Values are constants; no environment data is exposed.
```bash
curl http://localhost:8000/health-details
# {"status":"ok","service":"checkpoint-api","version":"0.1.0"}
```
