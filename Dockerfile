FROM python:3.8.12-slim-buster
WORKDIR /tema10/src
COPY . .
RUN python -m pip install -r requirements.txt
EXPOSE 8082
CMD ["python", "envpar.py"]
