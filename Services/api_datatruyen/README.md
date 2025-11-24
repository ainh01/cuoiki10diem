# FastAPI Controller


## 1. Clone repository

```bash
git clone https://github.com/JONNYDAN/API---CNPM.git
cd API---CNPM
```

## 2. Tạo môi trường ảo

Trên Windows
```bash
python -m venv venv
venv\Scripts\activate
```

Trên macOS/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

## 3. Cài đặt dependencies
```bash
pip install -r requirements.txt
```

## 4. Chạy ứng dụng
```bash
uvicorn main:app --reload --port 8000
```

> If your FastAPI app is defined in `server.py` instead of `main.py`, run:

```bash
uvicorn server:app --reload --port 8000
```

## 5. Health check

After the application is running you can verify it with the health-check endpoint:

```bash
# returns 200 and JSON {"status": "ok"} when the app can reach MongoDB
curl -i http://localhost:8000/health
```

## 6. Running tests

Install pytest and run the test suite (the basic health endpoint test doesn't require a running MongoDB; it accepts 200 or 503):

```bash
pip install -r requirements.txt pytest
pytest -q
```