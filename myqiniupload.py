# -*- coding: utf-8 -*-
'''
Created on 2014年3月5日

@author: aadebuger
'''

#import qiniu.io
#import qiniu.rs
#import qiniu.conf 
import qiniu
from qiniu import Auth, set_default, etag, PersistentFop, build_op, op_save

import sys

import os
def token(bucket_name):
    print os.getenv("accesskey")
    print os.getenv("secretkey")
 #   qiniu.conf.ACCESS_KEY = os.getenv("accesskey")
 #   qiniu.conf.SECRET_KEY = os.getenv("secretkey")
 #   policy = qiniu.rs.PutPolicy(bucket_name)
 #   uptoken = policy.token()
    newauth = Auth(os.getenv("accesskey"), os.getenv("secretkey"))

    return newauth.upload_token(bucket_name);

def tokenext(bucket_name,accesskey,secretkey):
    qiniu.conf.ACCESS_KEY = accesskey
    qiniu.conf.SECRET_KEY = secretkey
    policy = qiniu.rs.PutPolicy(bucket_name)
    uptoken = policy.upload_token()
    return uptoken

def cloudupload(uptoken,key,localfile):


#    localfile = "%s" % __file__

    ret, err = qiniu.put_file(uptoken, key, localfile)
    if err is not None:
        sys.stderr.write('error: %s ' % err)
    print 'ret=',ret
    return


if __name__ == '__main__':
        v =token(sys.argv[1])
        print 'v=',v
#        cloudupload(v,"zhangxuanlingyin.apk","/Users/aadebuger/Downloads/zhangxuanlingyin.apk");
        cloudupload(v,sys.argv[2],sys.argv[3]);
