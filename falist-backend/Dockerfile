FROM python:3.11-slim

# set workdir
WORKDIR /app

# instalando dependências do SO para psycopg2
RUN apt-get update && apt-get install -y gcc libpq-dev --no-install-recommends \
&& rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

ENV PYTHONUNBUFFERED=1

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]