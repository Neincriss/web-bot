from selenium import webdriver
from time import sleep
import requests, json
from facebot import facebot
import os
from datetime import date
from datetime import datetime

n = 0
p = 0
file_path = os.path.realpath(__file__)
file_path = file_path.replace('main.py','')

fecha = str(date.today())
now = datetime.now()

id = str(now.year)+str(now.month)+str(now.day)+str(now.hour)+str(now.minute)+str(now.second)

pub_file = "pubs/pub"+id+".csv"
pub_log = open(pub_file, "w")


print("usuario api wordpress:")
wp_username = "user"#str(input())
print("contraseña api wordpress:")
wp_password = "pass"#input('')
print("usuario facebook:")
user = "yourfacebook@mail.com"#str(input())
print("contraseña facebook:")
password = "pass"#input()
print("offset action")
ofst = 20#float(input())

# you need to put de path of the driver you are using, gecko driver is firefox driver
driver = webdriver.Firefox(executable_path=r"C:\\geckodriver\geckodriver.exe")
driver.get("https://mobile.facebook.com")

facebot.put(type='input', attr="name='email'",info=user, offset=0, driver=driver)
facebot.put(type='input', attr="name='pass'",info=password, offset=0, driver=driver)
facebot.put(type='button', attr="name='login'", offset=ofst, driver=driver)
facebot.put(type='button', attr="class='_54k8 _56bs _26vk _56b_ _56bw _56bu'", offset=20, driver=driver)

pub_log.write('"indice","titulo","identificador","status","fecha","hora"\n')
pub_log.close()



with open('groups.txt') as g:
    groups = g.readlines()
    for x in groups:
        with open('sku.txt') as l:
            pubs = l.readlines()
            for y in pubs:
                sleep(20)
                driver.get("https://mobile.facebook.com/groups/" + str(x))

                request = requests.get('https://www.yourwordpresspage.com/wp-json/wc/v3/products?sku='+str(y.replace('\n','')),auth=(wp_username, wp_password))
                json_pb = json.loads(request.text)
                try:
                    now = datetime.now()
                    hora = str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
                    pub = open(pub_file,'a')
                    facebot.put(type='button', attr="value='Vender'", offset=20, driver=driver)
                    facebot.put("input", "placeholder='¿Qué vendes?'", json_pb[0]['name'],0, driver)
                    facebot.put("input", "placeholder='Precio'", json_pb[0]['price'],0, driver)
                    response = requests.get("https://yourwordpresspage.com/wp-content/uploads/banners/" + str(json_pb[0]['sku'])+".png")
                    pic = open("sample_image.png", "wb")
                    pic.write(response.content)
                    pic.close()
                    facebot.put("input", "name='file1'", file_path+"sample_image.png", 20, driver)
                    facebot.put(type="button", attr="value='Publicar'", offset=20, driver=driver)

                    pub.write('"'+str(p)+'","'+driver.title+'","'+str(x).replace('\n','')+'","publicado","'+fecha+'","'+hora+'"\n')
                    print(driver.title+":"+str(x).replace('\n','')+": publicado: "+fecha+"->"+hora)
                    p = p + 1
                except:
                    pub.write('"'+str(p)+'","'+driver.title+'","'+str(x).replace('\n','')+'","fallido","'+fecha+'","'+hora+'"\n')
                    print(str(x).replace('\n','')+":  fallido"+": "+fecha+"->"+hora)
                    n = n + 1



txt = open("pubs/finish"+id+".txt", "w")
txt.write("publicaciones fallidas:"+str(n)+": "+fecha+"\n")
print("publicaciones fallidas:"+str(n)+": "+fecha+"\n")
txt.write("publicaciones concretadas:"+str(p)+": "+fecha+"\n")
print("publicaciones concretadas:"+str(p)+": "+fecha+"\n")
txt.close()
pub_log.close()