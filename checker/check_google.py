import requests as r

hosts = 'https://redirector.googlevideo.com/report_mapping', 'https://redirector.gvt1.com/report_mapping', 'https://redirector-bigcache.googleapis.com/report_mapping'

def main():
    for host in hosts:
        res = r.get(host)
        info = res.text.split('\n')[0]
        print(host, ' : ', info)

if __name__ == '__main__':
      main()
