import requests

host = 'https://redirector.googlevideo.com/report_mapping', 'https://redirector.gvt1.com/report_mapping', 'https://redirector-bigcache.googleapis.com/report_mapping'

def main():
    for hosts in host:
        r = requests.get(hosts)
        info = r.text.split('\n')[0]
        print(hosts, ' : ', info)

if __name__ == '__main__':
      main()
