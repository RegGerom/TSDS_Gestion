FROM python:3.10-slim

WORKDIR /app/

COPY . .

RUN apt update && apt install gcc -y

RUN pip install -r requirements.txt

EXPOSE 3000

CMD ["gunicorn", "estudiantes.wsgi:application"]