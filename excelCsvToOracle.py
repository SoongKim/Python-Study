#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 01. 필요한 라이브러리와 모듈을 호출

import os
import pandas as pd
from sqlalchemy import create_engine, types
# 경로 파악 기능을 수행하는 os, DataFrame을 읽어들이는 pandas, DB와의 연결 및 쿼리 수행을 위한 sqlalchemy를 호출합니다.


def toOracleDb(id="", pw="", ip="", port="", dbName="", folder_path="dataset"):
    """
    상대경로를 파악하여 "dataset" 이라는 이름을 지닌 폴더에 존재하는 모든 csv 및 excel 파일을 
    파일명으로 Oracle DB에 저장하는 ETL 함수입니다.
    
    id (str): 접속 아이디 데이터를 문자열 타입으로 입력받습니다. ex. "ddd"
    pw (str): 접속 비밀번호 데이터를 문자열 타입으로 입력받습니다. ex. "dddd"
    ip (str): 서버 아이피 주소 데이터를 문자열 타입으로 입력받습니다. ex. "000.000.000.000"
    port (str): 접속 포트 번호 데이터를 문자열 타입으로 입력받습니다. ex. "dddd"
    dbName (str): 접속 DB의 이름 데이터를 문자열 타입으로 입력받습니다. ex. "DD"
    folder_path (str): csv 및 excel 파일이 위치한 폴더 경로로, 상대 경로로 인식합니다.

    Returns:
    None
    """
    
    # 02. 연결 구축 및 파일 불러오기, 전송
    
    # sqlalchemy의 create engine 기능을 사용하여 DataBase와의 링크를 구축합니다.
    # 작동 간 입력 받은 id, pw, ip, port, db이름 데이터를 사용합니다.
    engine = create_engine(f'oracle+cx_oracle://{id}:{pw}@{ip}:{port}/{dbName}')

    # os 모듈을 사용한 경로 탐색 및 파일 선별
    for file in os.listdir(folder_path):
        
        # 대상 파일이 .csv, 혹은 .xlsx로 끝나는 경우만을 대상으로 설정합니다.
        # 해당 작업을 통해 csv, xlsx 확장자를 지닌 파일만을 ETL 대상으로 Fix합니다.
        if file.endswith('.csv') or file.endswith('.xlsx'):
            
            # os 모듈을 통해 dataset 폴더의 경로를 설정해주고
            file_path = os.path.join(folder_path, file)
            
            #df라는 변수명에 xlsx 확장자 파일은 pandas의 read-excel을, csv 파일은 read_csv 기능을 적용합니다.
            df = pd.read_excel(file_path) if file.endswith('.xlsx') else pd.read_csv(file_path)
            
            # DB에 세팅할 테이블 명으로는 파일명을 확장자와 구분짓는 .을 중점으로 나눠 앞에 위치한 파일명을 배치합니다.
            table_name = file.split('.')[0]
            
            # 데이터 타입 변환을 통해 전송 간 효율성을 향상합니다.
            object_columns = list(df.select_dtypes(include='object').columns)
            type_dict = {col: types.VARCHAR(100) for col in object_columns} if object_columns else None
            
            # 설정한 DB Link를 사용하여 df에 저장된 데이터프레임을 오라클DB에 전송합니다.
            # 전송 간 테이블 이름으로는 기설정한 테이블 명을 사용하며,
            # 만약 동일한 이름을 지닌 테이블이 존재하는 경우, 이를 덮어씌웁니다.
            try:
                df.to_sql(name=table_name, if_exists='fail', con=engine, dtype=type_dict, index=False)
            
            # 오류가 발생한 경우에는, 해당 오류를 출력합니다.
            except Exception as e:
                print(e)

