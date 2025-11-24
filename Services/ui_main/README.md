# FastAPI Controller


## 1. Clone repository

```bash
git clone https://github.com/JONNYDAN/UI---CNPM.git
cd UI---CNPM
```
## 2. Run code

```bash
yarn
yarn dev
```

## Healthcheck

This project exposes a minimal health endpoint at GET /health which returns a small JSON payload indicating the app is healthy.

To test locally (dev server):

```bash
# using curl
curl http://localhost:3000/health

# or using node
node -e "require('http').get('http://127.0.0.1:3000/health', res => res.pipe(process.stdout))"
```

Or use the included npm script (from the project root):

```bash
npm run healthcheck
```

The `docker-compose.yml` also contains a container healthcheck that hits this route so container orchestration can detect if the app is up.
