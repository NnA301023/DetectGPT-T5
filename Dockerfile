FROM python:3.9
WORKDIR /DetectGPT-T5

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .
