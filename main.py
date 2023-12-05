from flask import Flask,Response,request,json
from urllib.parse import unquote
app = Flask(__name__)

@app.route('/',methods=['GET'])
def notification_url():
    validationToken = request.args.get('validationToken')
    data = validationToken
    #Call yout appian REST API
    #     
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='text/plain'
    ) 
    return response

@app.route('/',methods=['POST'])
def notification_url_post():
    validationToken = request.args.get('validationToken')
    data = unquote(validationToken)
    #Call yout appian REST API    
    response = app.response_class(
        response=data,
        status=200,
        mimetype='text/plain'
    ) 
    return response   
    # return Response(data=validationToken,content_type="text/plain"),200