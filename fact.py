from flask import Flask, request, jsonify
import requests

url = 'http://127.0.0.1:5000/im_size'
my_img = {'image': open('/mnt/c/Users/EVELIZGR/OneDrive/Nego/api/factura-autonomo.jpg', 'rb')}
r = requests.post(url, files=my_img)

# convert server response into JSON format.
print(r.json())