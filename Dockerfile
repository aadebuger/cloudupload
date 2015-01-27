FROM dockerfile/python
RUN pip install qiniu
ADD  myqiniupload.py /code
ADD  clouduplad /usr/local/bin
