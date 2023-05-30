FROM python:3.8
USER root
RUN mkdir /sensor
COPY . /sensor
WORKDIR /sensor
RUN python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt
#apache airflow setup
ENV AIRFLOW_HOME=/sensor/airlflow/
ENV AIRFLOW__CORE__DAGBAG_IMPORT_TIMEOUT=1000
ENV AIRFLOW__CORE__ENABLE_XCOM_PICKLING=True
RUN airflow db init
RUN airflow users create -e rohanpatankar926@gmail.com -f rohan -l patankar -p admin -r Admin -u admin
RUN chmod 777 start.sh
RUN apt update -y && apt install awscli -y
ENTRYPOINT [ "/bin/sh" ]
CMD ["start.sh"]