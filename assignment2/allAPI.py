from flask import Flask, request
from werkzeug.utils import secure_filename
import os,json
from db import *
from uploadFileController import *
from flask import send_file

ALLOWED_EXTENSIONS = ['pdf', 'txt', 'json']
UPLOAD_FOLDER = 'files'


app = Flask(__name__)
  
@app.route('/api/tests',methods=['POST'])          
def store_actual_tests_answers():    
    req = request.json 
    subject=req["subject"]
    answer_keys=req["answer_keys"]
    colval=""
    for values in answer_keys.values(): 
        colval=colval+values
    processTestsAnswerKeys(colval)
    insertInDB(subject,colval,"")
    dbdata = queryTestsTable("praTESTS")
    response=getTestsData(dbdata)
    response=json.dumps(response)
    return response 

@app.route("/api/tests/<id>/scantrons", methods=['POST','PUT'])
def upload_file(id):
    file = request.files['data']
    filename=secure_filename(file.filename)
    createfolder(UPLOAD_FOLDER)
    file.save(os.path.join(UPLOAD_FOLDER, filename))  
    f = open(os.path.join(UPLOAD_FOLDER, filename),"r")
    data=json.load(f) 
    anscolval=""
    for values in data['answers'].values(): 
        anscolval=anscolval+values
    subject= data['subject']
    name=data['name']
    scantron_url= "http://127.0.0.1:5000/files/"+filename
    scantron_id=id
    insertInSubmissionDB(scantron_id,scantron_url,name,subject,anscolval,-1)
    response=getSubmissionData()
    response=json.dumps(response)
    return response

@app.route("/api/tests/<id>", methods=['GET'])
def getAllScantron(id):
    submissionres=getSubmissionData()
    #print(submissionres)
    dbdata = querDBWithConditionTESTS('praTESTS','rowid',id)
    testres=getTestsData(dbdata)
    testres['submissions']=submissionres
    response=json.dumps(testres)
    return response

@app.route('/files/<filename>',methods=['GET'])
def downloadFile(filename):
    path = os.path.join(UPLOAD_FOLDER, filename)
    return send_file(path, as_attachment=True)


if __name__=="__main__":
    app.run(port=5000, debug=True)