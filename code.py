import requests
import time

def downloader(url,file_name):
    print("Start of download {} :- {}".format(file_name,time.ctime(time.time())))
    r = requests.get(url, allow_redirects=True)
    open(file_name, 'wb').write(r.content)
    print("End of download {} :- {}".format(file_name,time.ctime(time.time())))

downloader('https://cdna.artstation.com/p/assets/images/images/001/216/178/large/michael-clarke-ironman-midshot2.jpg?1442363658','ironman.jpg')
downloader('https://static1.comicvine.com/uploads/original/11111/111111959/5169127-3201288658-capta.jpg','captainamerica.jpg')
