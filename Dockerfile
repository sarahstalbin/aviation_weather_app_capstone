FROM python:3.9-slim-bullseye
ARG DEBIAN_FRONTEND=noninteractive
RUN pip3 install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY templates /usr/local/bin/templates
COPY app.py /usr/local/bin/app.py
COPY assets /usr/local/bin/static
COPY api_sfo.py /usr/local/bin/api_sfo.py
COPY models.py /usr/local/bin/models.py
COPY forms.py /usr/local/bin/forms.py
WORKDIR /usr/local/bin
CMD ["python3", "app.py"]
