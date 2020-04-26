from flask import Flask, request
from werkzeug.utils import secure_filename
import os,json
from db import *

def createfolder(foldername):
    current_directory = os.getcwd()
    final_directory = os.path.join(current_directory, foldername)
    if not os.path.exists(final_directory):
        os.makedirs(final_directory)



def getExpectedAnsKeys(testid):
    response = querDBWithCondition('answer_keys','praTESTS','subject',testid)
    return response

def getSubmissionData():
    actual=""
    finalresponsedict=[]
    allrows = querySubmissionTable("praSubmissions")
    #print(allrows)
    for s in allrows:
        responsedict={}
        responsedict.update({'scantron_id':s[0]})
        responsedict.update({'scantron_url':s[1]})
        responsedict.update({'name':s[2]})
        responsedict.update({'subject':s[3]})
        for values in s[4]: 
            actual=actual+values
        expected=getExpectedAnsKeys(s[3])
        score,newlistval=getSubmissionResponse(actual,expected)
        responsedict.update({'Score':score})
        responsedict.update({'result':newlistval})
        finalresponsedict.append(responsedict)
    #print(finalresponsedict)
    return finalresponsedict

def getSubmissionResponse(actual,expected):
    listactual=list(actual)
    listexpected=list(expected[0][0])
    newlistval={}
    i=0
    score=0
    for a,e in zip(listactual, listexpected):
        i=i+1
        if(str(a)==str(e)):
            score=score+1
        newlistval.update({str(i):{'actual':a,'expected':e}})  
    return score,newlistval

def processTestsAnswerKeys(stringval):
    listval=list(stringval)
    newlistval={}
    i=0
    for s in listval:
        i=i+1
        newlistval.update({str(i):s})
    return newlistval

def getTestsData(dbdata):
    newlistval={}
    for s in dbdata:
        newlistval.update({"test_id":s[0]})
        newlistval.update({"subject":s[1]})
        newlistval.update({"answer_keys":processTestsAnswerKeys(s[2])})
        newlistval.update({"submissions":s[3]})
    return newlistval
