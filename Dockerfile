FROM python:3.8
USER root
RUN mkdir /sensor
COPY . /sensor
WORKDIR /sensor
RUN python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt
ENTRYPOINT [ "python" ]
CMD [" /sensor/main.py "]