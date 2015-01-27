FROM dockerfile/python
RUN pip install qiniu
ADD  myqiniupload.py /code
COPY  cloudupload /usr/local/bin
