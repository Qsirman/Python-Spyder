import requests
import os
url = "https://ss0.bdstatic.com/94oJfD_bAAcT8t7mm9GUKT-xh_/timg?image&quality=100&size=b4000_4000&sec=1492751932&di=6a72c422d7b890fa8e58c6c7dc77e3da&src=http://img4.duitang.com/uploads/blog/201406/14/20140614131138_tLA3M.jpeg"
root = "//home//qsirman//Pictures//"
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print("File saved successfully")
    else:
        print("The file has exsisted")
except:
    print("Get failed.")
