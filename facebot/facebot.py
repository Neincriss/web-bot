#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <https://www.gnu.org/licenses/>.

#the program is developed and maintained by Cristopher Loya <https://github.com/Neincriss>

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

def put(type,attr,info='',offset=20,driver=0):
    web = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//" + type + "[@" + attr + "]")))
    time.sleep(offset)
    if type == "input":
        web.send_keys(info)
    elif type == "button":
        web.click()