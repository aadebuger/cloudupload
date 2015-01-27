FROM dockerfile/python
RUN pip install qiniu
ADD  myqiniupload.py /code/myqiniuupload.py
ADD   cloudupload /usr/local/bin/cloudupload
