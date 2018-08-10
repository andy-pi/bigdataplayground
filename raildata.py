'''
Uk Rail Historical Service Performance
wiki.openraildata.com/index.php/TOC_Code
http://wiki.openraildata.com/index.php/HSP
'''

import requests, json
import pandas as pd
import config

class UKRailHSP(object):
    '''
    A client for the rail hsp api
    '''

    def __init__(self, USERNAME, PASSWORD):
        self.USERNAME = USERNAME
        self.PASSWORD = PASSWORD
        self.headers = {'content-type': 'application/json'}
        self.auth=requests.auth.HTTPBasicAuth(USERNAME, PASSWORD)
    
    def get_servicemetrics(self,data):
        r = requests.post('https://hsp-prod.rockshore.net/api/v1/serviceMetrics', auth=self.auth,data=json.dumps(data),headers=self.headers)
        return json.loads(r.text)
        
    def get_servicedetails(self,rid):
        data = { "rid" : rid }
        r = requests.post('https://hsp-prod.rockshore.net/api/v1/serviceDetails', auth=self.auth,data=json.dumps(data),headers=self.headers)
        return json.loads(r.text)
        
    def get_toc_codes(self):
        page = pd.read_html('http://wiki.openraildata.com/index.php/TOC_Codes')
        toc_codes = page[0]
        toc_codes.drop([1,2],axis=1, inplace=True)
        toc_codes.columns=[toc_codes.get_value(0,0),toc_codes.get_value(0,3)]
        toc_codes.drop([0], axis=0, inplace=True)
        return toc_codes
        
    def get_crs_codes(self):
        crs_codes = pd.read_csv('RailReferences.csv', header=None)
        crs_codes.drop([4,5,6,7,8,9,10,11],axis=1, inplace=True)
        crs_codes.columns=[crs_codes.get_value(0,0), crs_codes.get_value(0,1),crs_codes.get_value(0,2),crs_codes.get_value(0,3)]
        crs_codes.drop([0], axis=0, inplace=True)
        return crs_codes
        
    def search_station(self,searchstring):
        allstations=self.get_crs_codes()
        return allstations.loc[allstations['StationName'].str.contains(searchstring, case=False)]
        
    def search_toc_code(self,searchstring):
        allcodes=self.get_toc_codes()
        return allcodes.loc[allcodes['Company Name'].str.contains(searchstring, case=False)]
        

if __name__ == "__main__":

    rail = UKRailHSP(USERNAME, PASSWORD)
    #print rail.get_toc_codes().head()#.get_value(37,"ATOC Code")
    print rail.search_station("shef")
    #print rail.search_toc_code("south")
    
    data={
    "from_loc":"SHF",
    "to_loc":"STP",
    "from_time":"0800",
    "to_time":"0900",
    "from_date":"2016-02-01",
    "to_date":"2016-12-01",
    "days":"SUNDAY",

    }

    #print rail.get_servicemetrics(data)
    print rail.get_servicedetails(201606052544657)