import urllib2
import time


def getIP():
    ip1 = urllib2.urlopen('http://automation.whatismyip.com/n09230945.asp').read()
    return ip1


def loop():
    while True:
        ip_txt = getIP()

        # This will create a new file or **overwrite an existing file**.
        f = open("C:\Users\Daniel\Dropbox\Public\index.html", "w")
        try:
            f.write('<a href="http://%s">%s</a>' % (ip_txt, ip_txt))
            print("File saved on dropbox")
        except IOError:
            pass
        finally:
            f.close()

        # Send get request to server
        #print(urllib2.urlopen("http://localhost:8000/app/addip/?ip=%s" % ip_txt).read())
        print(urllib2.urlopen("http://daniel-pc.aws.af.cm/addip/?ip=%s" % ip_txt).read())

        time.sleep(60 * 10)

if __name__ == "__main__":
    loop()
