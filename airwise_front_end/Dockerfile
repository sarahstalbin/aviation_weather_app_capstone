FROM python:3.9-slim-bullseye
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y python3 python3-pip curl nano procps sqlite3
RUN pip3 install --upgrade pip && pip3 install flask
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY templates /usr/local/bin/templates
COPY app.py /usr/local/bin/app.py
COPY assets /usr/local/bin/static
COPY api_sfo.py /usr/local/bin/api_sfo.py
COPY api_metars.py /usr/local/bin/api_metars.py
COPY models.py /usr/local/bin/models.py
COPY forms.py /usr/local/bin/forms.py
EXPOSE 5000
WORKDIR /usr/local/bin
CMD ["python3", "app.py"]
