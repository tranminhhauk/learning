FROM python:3-slim

WORKDIR /main

COPY requirement.txt .

RUN pip install --no-cache-dir -r requirement.txt

COPY . .
 
EXPOSE 5000

CMD [ "python", "main.py" ]

