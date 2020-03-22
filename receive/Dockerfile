FROM ubuntu
COPY . /receive
WORKDIR /receive
RUN \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y python python-pip python-dev
RUN pip install -r requirements.txt
#ENTRYPOINT ["python"]
CMD ["nameko", "run", "--config" ,"foobar.yaml", "main"]
