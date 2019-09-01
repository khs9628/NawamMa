from django.shortcuts import render, redirect
import serial
import json
from pprint import pprint
from board.models import Board
import board.views

## 지하철 API
# import urllib
# import json
# from pprint import pprint

def mypage(request):
        boards = Board.objects
        return render(request, 'NawamMa/mypage.html', {'boards':boards})

# 단순 소개페이지
def layout(request):
        return render(request, 'NawamMa/index.html')
def maker(request):
        return render(request, 'NawamMa/maker.html')
def extend(request):
        return render(request, 'NawamMa/extend.html')

## 일반자리 관련
def start(request):
        return render(request, 'NawamMa/start.html')

def subway(request):
        departure = request.GET['departure']
        destination = request.GET['destination']
        return render(request, 'NawamMa/subway.html', {'departure':departure, 'destination':destination})

def seat(request, number):
        ser = serial.Serial(
                port='COM4',
                baudrate=9600,
        )

        print('아두이노와 통신 시작')
        print('아두이노의 접속 포트는 COM4 입니다.\n')

        number = number

        while True:
                if ser.readable():
                        res = ser.readline()
                        json_data = json.loads(res.decode()[:-1])  ##json_data -> json으로 파싱된 데이터를 dict형태로 바뀌서 저장
                        print(json_data)
                        return render(request, 'NawamMa/seat.html', {'json_data': json_data, 'number':number})
        #if(val <= 0 )
                else:
                        print("연결을 실패했습니다.")
                        return render(request, 'NawamMa/seat.html') # front 테스트용 임시 return
        
def Mseat(request):
        ser = serial.Serial(
                port='COM4',
                baudrate=9600,
        )

        print('아두이노와 통신 시작')
        print('아두이노의 접속 포트는 COM4 입니다.\n')

        while True:
                if ser.readable():
                        res = ser.readline()
                        json_data = json.loads(res.decode()[:-1])  ##json_data -> json으로 파싱된 데이터를 dict형태로 바뀌서 저장
                        print(json_data)
                        return render(request, 'NawamMa/Mseat.html', {'json_data': json_data})
        #if(val <= 0 )
                else:
                        print("연결을 실패했습니다.")
                        return render(request, 'NawamMa/Mseat.html') # front 테스트용 임시 return



## 임산부자리 관련
def startP(request):
        return render(request, 'NawamMa/startP.html')

def subwayP(request):
        departure = request.GET['departure']
        destination = request.GET['destination']
        return render(request, 'NawamMa/subwayP.html', {'departure':departure, 'destination':destination})

def MseatP(request):
        ser = serial.Serial(
                port='COM4',
                baudrate=9600,
        )

        print('아두이노와 통신 시작')
        print('아두이노의 접속 포트는 COM4 입니다.\n')


        while True:
                if ser.readable():
                        res = ser.readline()
                        json_data = json.loads(res.decode()[:-1])  ##json_data -> json으로 파싱된 데이터를 dict형태로 바뀌서 저장
                        print(json_data)
                        return render(request, 'NawamMa/MseatP.html', {'json_data': json_data})
        # # if(val <= 0 )
                else:
                        print("연결을 실패했습니다.")
                        return redirect('/')
        


def seatP(request, number):
        ser = serial.Serial(
                        port='COM4',
                        baudrate=9600,
                )
        
        print('아두이노와 통신 시작')
        print('아두이노의 접속 포트는 COM4 입니다.\n')

        number = number
        while True:
                if ser.readable():
                        res = ser.readline()
                        json_data = json.loads(res.decode()[:-1])  ##json_data -> json으로 파싱된 데이터를 dict형태로 바뀌서 저장
                        print(json_data)
                        return render(request, 'NawamMa/seatP.html', {'json_data': json_data, 'number':number})
        # # if(val <= 0 )
                else:
                        print("연결을 실패했습니다.")
                        return redirect('/')

# 임산부가 요청보낼 시 아두이노 불과 소리 나오게하는 url
def preRequset(request):
        ser = serial.Serial(
                port='COM4',
                baudrate=9600,
        )

        print('아두이노와 통신 시작')
        print('아두이노의 접속 포트는 COM6 입니다.\n')

        while True:
                c = 'p'
                c = c.encode()
                ser.write(c)
                print(c)

                if ser.readable():
                        stop = ser.readline()
                        stopA = stop.decode()
                        stopB = stopA.strip()
                        print(stopB)
                        if stopB == 'T':
                                #return render(request, 'NawamMa/seatP.html')
                                return redirect('/')

# ### 지하철 API 사용
# ServiceKey = "6369785570726c613235676b55494f"

# # if 문을 사용해서 요청에 따라 다른 url을 호출하도록한다. (API)
# # + dict을 다른 페이지에 보내도록한다. 각 보여주는 페이지를 따로 만들어야할듯?

# url = "http://swopenapi.seoul.go.kr/api/subway/" + ServiceKey + "/json/firstLastTimetable/0/10/%EC%98%A8%EC%88%98"

# request = urllib.request.Request(url)
# response = urllib.request.urlopen(request)
# rescode = response.getcode()
# if(rescode==200):
#     response_body = response.read()
#     print(response_body.decode('utf-8'))
#     dict = json.loads(response_body.decode('utf-8'))
#     pprint(dict)
# else:
#     print("Error Code:" + rescode)

##원리 -> url호출시 json 방식으로 요청한 정보를 보여줌 -> dict객체에 json의 값들을 저장함 -> dict을 하나하나 나눠서 출력해주면 완벽크