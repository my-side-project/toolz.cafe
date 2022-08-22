FROM python:3.8

EXPOSE 5000

COPY . .

RUN python -m pip install -r requirements.txt

ENTRYPOINT [ "python", "app.py" ]
