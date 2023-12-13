FROM python:3.10-slim

COPY ./.secrets ./.secrets
COPY ./pyproject.toml .

RUN pip install --upgrade pip
RUN pip install pdm
RUN pdm install 

COPY requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 8080
 
CMD pdm run streamlit run --server.port 8080 --server.enableCORS false Generator.py 