import json
import requests
import pandas as pd
from states import states

def NCMEC_parser(state):
    session = requests.Session()
    df = pd.DataFrame(columns = ['name','age','gender','ethnicity','NCMEC_case#','case_type','birth_year','missing_year','missing_city','missing_county','missing_state'])
    query_url_temp = "http://www.missingkids.com/missingkids/servlet/JSONDataServlet?action=publicSearch&searchLang=en_US&search=new&subjToSearch=child&missState=" + state + "&missCountry=US"
    try:
        response_temp = session.get(query_url_temp)
        response_temp_json = json.loads(response_temp.text)
    except:
        print("api timeout T.T")
        quit()

    for i in range(int(response_temp_json['totalPages'])):
        query_url_loop = "http://www.missingkids.com/missingkids/servlet/JSONDataServlet?action=publicSearch&searchLang=en_US&goToPage={}".format(i+1)
        response_loop = session.get(query_url_loop)
        response_loop_json = json.loads(response_loop.text)
        
        for ii in range(len(response_loop_json['persons'])):
            # detailed response
            try:
                detailed_response = session.get("http://www.missingkids.com/missingkids/servlet/JSONDataServlet?action=childDetail&caseNum={}&orgPrefix={}".format(response_loop_json['persons'][ii]["caseNumber"], response_loop_json['persons'][ii]["orgPrefix"]))
                detailed_response_json = json.loads(detailed_response.text)
                person_info = detailed_response_json['childBean']
            except:
                print("api timeout T.T")
                quit()
            
            # first + middle + last name
            person_name = person_info['firstName'] + " " + person_info['lastName']
            if person_info['middleName'] != "":
                person_name.replace("", " {} ".format(person_info['middleName']))
            
            # index number of df
            index_num = (len(response_temp_json['persons']) * i) + ii
            try:
                df.set_value(index_num,'name',person_name)
                df.set_value(index_num,'age',person_info['age'])
                df.set_value(index_num,'gender',person_info['sex'])
                df.set_value(index_num,'ethnicity',person_info['race'])
                df.set_value(index_num,'NCMEC_case#',person_info['caseNumber'])
                df.set_value(index_num,'case_type',person_info['caseType'])
                df.set_value(index_num,'birth_year',person_info['birthDate'].split(' ')[2])
                df.set_value(index_num,'missing_year',person_info['missingDate'].split(' ')[2])
                df.set_value(index_num,'missing_city',person_info['missingCity'])
                df.set_value(index_num,'missing_county',person_info['missingCounty'])
                df.set_value(index_num,'missing_state',person_info['missingState'])
            except:
                print('error T.T - state {} page {} person {}'.format(person_info['missingState'],i+1,ii+1))
                continue
            print("state {} page {} person {} complete".format(person_info['missingState'],i+1,ii+1))
                
    df.to_csv("Resources/NCMEC_{}.csv".format(state), encoding="utf-8", index=False)