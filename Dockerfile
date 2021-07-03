FROM python:3.9.6-slim

RUN groupadd app && useradd app -g app

WORKDIR app

RUN mkdir venv && python -m venv /venv

COPY . .

RUN pip install -r requirements.txt

USER app

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]