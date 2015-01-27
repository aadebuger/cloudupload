FROM dockerfile/python
RUN pip install qiniu
ADD  myqiniupload.py /code
ADD  cloudupload /usr/local/bin
