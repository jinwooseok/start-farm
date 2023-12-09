import sqlite3
import csv

# SQLite 데이터베이스 연결
db_connection = sqlite3.connect('backend/db.sqlite3')
cursor = db_connection.cursor()

# # CSV 파일에서 데이터 읽어와서 데이터베이스에 적재
csv_file_path = "backend/jeonbook_state_result.csv"
with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # 첫 번째 행은 헤더이므로 건너뜀
    for row in csv_reader:
        insert_query = f'''
        INSERT INTO Area (province, city, details)
        VALUES (?, ?, ?)
        '''
        cursor.execute(insert_query, row)

csv_file_path = "backend/jeonnam_area_result.csv"
with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # 첫 번째 행은 헤더이므로 건너뜀
    for row in csv_reader:
        insert_query = f'''
        INSERT INTO Area (province, city, details)
        VALUES (?, ?, ?)
        '''
        cursor.execute(insert_query, row)

# CSV 파일에서 데이터 읽어와서 데이터베이스에 적재
csv_file_path = "backend/jeonbook_maul_result.csv"
with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # 첫 번째 행은 헤더이므로 건너뜀
    #권역 나누기
    for row in csv_reader:
        area_row = tuple(row[0].split(' '))
<<<<<<< HEAD
        select_query = f'''SELECT id FROM area WHERE province = ? AND city =  ? AND details = ?\;'''
=======
        select_query = f'''SELECT id FROM area WHERE province = ? AND city =  ? AND details = ?;'''
>>>>>>> bd232ebd1add4f25aa246060ea0ee7a2867652df
        cursor.execute(select_query, area_row)
        result = cursor.fetchone()
        insert_query = f'''
        INSERT INTO town (name, area_id)
        VALUES (?,?);
        '''
        cursor.execute(insert_query, (row[1],result[0]))

<<<<<<< HEAD
<<<<<<< HEAD
=======
csv_file_path = "backend/jeonnam_area_result.csv"
with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # 첫 번째 행은 헤더이므로 건너뜀
    for row in csv_reader:
        insert_query = f'''
        INSERT INTO Area (province, city, details)
        VALUES (?, ?, ?)
        '''
        cursor.execute(insert_query, row)

=======
>>>>>>> 841973f06767f156e011430358c25f77e6b8ba3f
csv_file_path = "backend/jeonnam_result.csv"
with open(csv_file_path, 'r') as csv_file:    
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # 첫 번째 행은 헤더이므로 건너뜀
    for row in csv_reader:
        area_row = (row[1],row[2],row[3])
        select_query = f'''SELECT id FROM area WHERE province = ? AND city =  ? AND details = ?;'''
        cursor.execute(select_query, area_row)
        result = cursor.fetchone()
        insert_query = f'''
        INSERT INTO town (name, area_id)
        VALUES (?,?);
        '''
        cursor.execute(insert_query, (row[0],result[0]))



>>>>>>> bd232ebd1add4f25aa246060ea0ee7a2867652df
# 변경사항 커밋 및 연결 닫기
db_connection.commit()
db_connection.close()