from flask import Flask,jsonify,request
import json 

response=''
app = Flask(__name__)

@app.route('/name',methods=['GET','POST'])
def nameRoute():
    global response
    if request.method=='POST':
        request_data=request.data
        request_data=json.loads(request_data.decode('utf-8'))
        url = request_data['url']
        response = f'{url} ochesindhi royyy'
        return response
    else:
        return jsonify({url:request_data['url']})


if __name__=="__main__":
    app.run(debug=True,host='192.168.0.104')