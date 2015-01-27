FROM dockerfile/python
RUN pip install qiniu
ADD  myqiniupload.py /code/myqiniupload.py
ADD   cloudupload /usr/local/bin/cloudupload
RUN chmod a+x   /usr/local/bin/cloudupload
