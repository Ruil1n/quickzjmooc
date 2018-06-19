import requests
import json
import threading
url = 'http://student.zjedu.moocollege.com/nodeapi/3.0.1/student/course/uploadLearnRate'
courseId=30004252
startId=30176609
stopId=30176620
headers = {
			'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
			'Content-type': 'application/json',
			'Cookie':'xxxxxx'
		}
def update(id):
	print("当前id:"+str(id))
	for position in range(0,10000,2):
		payload = {'unitId': id,
				'courseId':courseId,
				'playPosition':position
				}
		r = requests.post(url, data=json.dumps(payload), headers=headers)
		if "20004" in r.text:
			print("完成id:"+str(id))
			break
		if "20031" in r.text:
			break
threads = [threading.Thread(target=update, args=(id, )) for id in range(startId,stopId)]
for t in threads:
    t.start()
for t in threads:
    t.join()