# ARM 아키텍처를 위한 Python 이미지 사용
FROM arm64v8/python:3.9-slim

# 필요한 패키지 설치 및 패키지 목록 삭제
RUN apt-get update && apt-get install -y \
    git \
    wget \
    && rm -rf /var/lib/apt/lists/*

# 최신 pip 설치 및 필요한 Python 패키지 설치
RUN pip install -U pip && \
    pip install mlflow psycopg2-binary boto3

# MinIO 클라이언트 설치
RUN cd /tmp && \
    wget https://dl.min.io/client/mc/release/linux-arm64/mc && \
    chmod +x mc && \
    mv mc /usr/bin/mc
