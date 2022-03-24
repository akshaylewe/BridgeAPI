from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


import psycopg2
import json
import time

connection = psycopg2.connect(user="dbmasteruser",
                password=''')kaueEd2{O}o:;-IqDzn?ZZg<?kKlSML''',
                host="ls-07c37000ca75aa803ceb6218472a0e9c5e315860.czevrhebjaz1.ap-south-1.rds.amazonaws.com",
                port="5432",
                database="postgres")

def fetch(id):
    cursor = connection.cursor()
    cursor.execute('''select * from submissions where "txHash"='{}' '''.format(str(id)))
    print("Selecting rows from submissions table using cursor.fetchall")
    fetched = cursor.fetchall()
    cursor.close()
    return fetched
    
def fetch1(id):
    cursor = connection.cursor()
    cursor.execute('''select "txHash" from submissions ''')
    print("Selecting rows from submissions table using cursor.fetchall")
    fetched = cursor.fetchall()
    print('''select * from submissions where "receiverAddr"='{}' '''.format(str(id)))
    cursor.close()
    return fetched
    

class Submission(APIView):
    
    def post(self, request, format=None):
        time.sleep(20)
        try:
            headers = {
            'Cache-control': 'no-store, max-age=0',
            'X-Frame-Options': 'DENY'
            }
            id = self.request.data ["id"]
            print(id)
            data = fetch(id)
            print(data[0][8])
        except Exception as e:
            print(e)
            return Response({"status": 0, "data": str(e)})
        return Response({"status": 1, "signature": data[0][8], "submissionId": data[0][0], "debridgeId": data[0][4], "data": data})



class Transaction(APIView):
    
    def post(self, request, format=None):
        time.sleep(20)
        try:
            headers = {
            'Cache-control': 'no-store, max-age=0',
            'X-Frame-Options': 'DENY'
            }
            data = fetch1(id)
            print(data)
        except Exception as e:
            raise e
            return Response({"status": 0, "data": str(e)})
        return Response({"status": 1, "data": data})