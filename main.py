from flask import Flask,Response,request,json
app = Flask(__name__)

@app.route('/')
def notification_url():
    validationToken = request.args.get('validationToken')
    data = validationToken
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    ) 
    return response   
    # return Response(data=validationToken,content_type="text/plain"),200