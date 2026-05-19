# DevSecOps Pipeline

A basic DevSecOps CI pipeline using GitHub Actions to perform automated security testing on every push for an intentionally vulnerable Flask Notes application.
## Security Checks

- **pip-audit** → Scans dependencies for known CVEs
- **Bandit** → Performs SAST on Python code
- **Trivy** → Scans filesystem for vulnerabilities, secrets, and misconfigurations

## Workflow

```text

Push Code → Install Dependencies → Security Scans → Pass/Fail Build
```
scan result :
<img width="1299" height="432" alt="image" src="https://github.com/user-attachments/assets/c3de41c5-0eea-4213-ace6-d3fa674dbf1b" />
