FROM python:3

COPY ./requirements.txt /requirements.txt
COPY ./ /
WORKDIR /

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /requirements.txt

CMD ["/py/bin/uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
