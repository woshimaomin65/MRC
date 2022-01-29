#coding:utf-8
import json
def js(data):
    print(json.dumps(data, indent=4, default=str, ensure_ascii=False))
