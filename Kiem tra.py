import pyodbc
server = 'LAPTOP-VGVERF7M'
database = 'QUAN_LY_HV'
username = 'tuannv'
password = '12345678'
cnxn = pyodbc.connect('DRIVER={SQL server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

try:
    f= open("hoc_vien1.txt",'r',)
    listHV = f.readlines()
    print(listHV)
    #Header
    a=listHV[0].split(":")
    header = (a[1]).replace("\n","")
    print(type(header))
    # DATE:
    b=listHV[1].split(":")
    date = (b[1]).replace("\n","")
    print(b[1])

    # MA_HOC_VIEN
    c=listHV[2].split(":")
    maHV = (c[1]).replace("\n","")
    print(c[1])
    #TEN_HOC_VIEN:
    d=listHV[3].split(":")
    tenHV = (d[1]).replace("\n","")
    print(d[1])
    #Lop HV:
    e=listHV[4].split(":")
    lopHV = (e[1]).replace("\n","")
    print(e[1])
    # Email:
    f=listHV[5].split(":")
    email = (f[1]).replace("\n","")
    print(f[1])
    # sdt
    g=listHV[6].split(":")
    sdt = (g[1]).replace("\n","")
    print(g[1])
except FileNotFoundError:
    print("Loi duong dan")

cursor.execute("INSERT INTO HOC_VIEN VALUES (?,?,?,?,?,?,?)",
            (str(header),str(date),str(maHV),str(tenHV),str(lopHV),str(email),str(sdt)))
cursor.commit()




import smtplib

TO = "tbtoanit@gmail.com"
SUBJECT = "[Tuan] Kiem tra "
TEXT = header+"\n"+date+"\n"+maHV+"\n"+tenHV+"\n"+lopHV+"\n"+email+"\n"+sdt

# Gmail Sign In
gmail_sender = 'tuannguyen.ueh36@gmail.com'
gmail_passwd = '12345678'

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(gmail_sender, gmail_passwd)

BODY = '\r\n'.join(['To: %s' % TO,
                    'From: %s' % gmail_sender,
                    'Subject: %s' % SUBJECT,
                    '', str(TEXT)])
#try:
server.sendmail(gmail_sender, [TO], BODY)
print ('email sent')
#except:


server.quit()
