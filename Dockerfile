FROM python:3.12
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
RUN pip install pydantic['email']
COPY app /app
COPY .env /.env
COPY main.py /main.py
COPY alembic.ini /alembic.ini
COPY alembic /alembic
CMD ["uvicorn", "main:app","--host","0.0.0.0","--port","8000" ]
EXPOSE 8000