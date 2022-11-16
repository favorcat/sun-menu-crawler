# 교직원식당 크롤러
import csv
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("")
firebase_admin.initialize_app(cred)
db = firestore.client()

# 데이터 넣기 전, 기존 데이터 삭제
def delete_collection(coll_ref, batch_size):
    docs = coll_ref.list_documents(page_size=batch_size)
    deleted = 0

    for doc in docs:
        print(f'Deleting doc {doc.id} => {doc.get().to_dict()}')
        doc.delete()
        deleted = deleted + 1

    if deleted >= batch_size:
        return delete_collection(coll_ref, batch_size)
delete_collection(db.collection(u'StaffMenuData'), 5)

# csv 파일 읽어오기
f = open('staff.csv', 'r', encoding='utf-8')
rf = csv.reader(f)

# 데이터 넣기
for line in rf:
  line[1] = line[1].replace("(","")
  line[1] = line[1].replace(")","")
  line[1] = line[1].split(" ")
  
  line[2] = line[2].replace("[","")
  line[2] = line[2].replace("]","")
  line[2] = line[2].replace("'","")
  line[2] = line[2].split(",")
  print(line[2][0])
  
  
  data = {
      u'idx': line[0],
      u'date': line[1][0],
      u'day': line[1][1],
      u'menu': line[2],
  }
  update_time, menu_ref = db.collection(u'StaffMenuData').add(data)
  print(f'Added document with id {menu_ref.id}')