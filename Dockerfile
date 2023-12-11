FROM python:3.10-slim

COPY ./.secrets ./.secrets
COPY ./requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8501

CMD python run streamlit run --server.port 8501 --server.enableCORS false ./src/app.py 