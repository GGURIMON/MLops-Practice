# ARM 아키텍처를 위한 Python 이미지 사용
# 윈도우 환경에서는 amd64/python:3.9-slim를 사용함. 내가 맥북이라 이렇게 사용하는 것.
FROM arm64v8/python:3.9-slim

# PostgreSQL 클라이언트 설치
RUN apt-get update && apt-get install -y \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# 작업 디렉토리 설정
WORKDIR /usr/app

# pip와 필요한 Python 라이브러리 설치
RUN pip install -U pip && \
    pip install scikit-learn pandas psycopg2-binary

# Python 스크립트 복사
COPY data_generator.py data_generator.py

# ENTRYPOINT로 Python 스크립트 실행
ENTRYPOINT ["python", "data_generator.py", "--db-host"]

# 기본값으로 localhost 설정
CMD ["postgres-server"]
