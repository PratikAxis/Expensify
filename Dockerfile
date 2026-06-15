FROM python:3.11-slim
COPY . /main
WORKDIR /main
RUN pip install -r requirements.txt
WORKDIR /main/backend
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]