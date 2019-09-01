# 나왐마
지하철 자리 배치 서비스

### 라이브러리
    pip install django-allauth : 소셜로그인 구현
    pip install pySerial : 아두이노 시리얼 통신 구현
    pip install Pillow : 게시판 사진 업로드 구현


### Project 구조
    프로젝트 이름 : project
    
    * app
    board : 게시판 관련 APP
    member : 계정 관련 APP
    accounts : 소셜 계정 관련 APP
    NawamMa : 전체적인 기능 관련 APP

### Project 소개
    지하철 자리를 효율적으로 관리하고 사용자들이 쉽게 자리를 찾을 수 있도록 도와주는 
    임산부들이 자리를 양보받을 수 있게 환경을 만들어주는
    서비스가 되는 것이 목표입니다.

    주요 기능 2가지
    1. 지하철 자리 현황
    
    2. 임산부 자리 요청

    WEB 과 APP Arduino 3가지를 활용하여 구성
    WEB : 지하철 전광판 등에 표시 가능
    APP : 주 사용자들이 사용
    Arduino : 서버와 통신을 통해 신호를 보내고 값을 가져옴
    



#### url 주소
[![현수쓰](/static/assets/img/logo_50.png)](https://khs9628board.herokuapp.com)

### 하루를 기록하다 :feet:
