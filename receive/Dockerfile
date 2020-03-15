FROM python:3
COPY . /receive
WORKDIR /receive
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["main.py"]