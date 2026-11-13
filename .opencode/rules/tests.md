# Test rules (apply whenever you create or edit files in tests/)
- Use pytest and fastapi.testclient.TestClient.
- One test file per feature: tests/test_<feature>.py
- Assert both the status code and the response body.
- Cover at least one success case and one edge case for new endpoints.
- Never delete or weaken a test just to make it pass.
- Tests must not read .env files or use real secrets.
