FROM arm64v8/python:3.9-slim
WORKDIR /usr/app
RUN pip install -U pip && pip install mlflow==1.30.0 "fastapi[all]" pandas scikit-learn
COPY app.py app.py
COPY schemas.py schemas.py
COPY sk_model/ sk_model/
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--reload"]
