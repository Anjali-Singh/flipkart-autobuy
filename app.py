#Tulsipada Das
#Dr. android Guruji
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from configparser import RawConfigParser
from colorama import Fore, init, deinit
from python3_anticaptcha import ImageToTextTask

opts = Options()





init()
CONFIG = RawConfigParser()
CONFIG.read('config.ini')
driver_path = CONFIG.get('MAIN', 'DRIVER_LOCATION')
email_inp = CONFIG.get('CREDENTIALS', 'USERNAME')
pass_inp = CONFIG.get('CREDENTIALS', 'PASSWORD')
order_link = CONFIG.get('ORDER', 'URL')
cvv_inp = CONFIG.get('ORDER', 'CVV')
addr_input = CONFIG.get('ORDER', 'ADDRESS')
pay_opt_input = CONFIG.get('ORDER', 'PAYMENT')
bankname_input = CONFIG.get('EMIOPTIONS', 'BANK')
tenure_input = CONFIG.get('EMIOPTIONS', 'TENURE')
default_sound = CONFIG.get('SOUND', 'DEFAULT')
frequency = 2500
duration = 2000


def prCyan(skk):
    print(Fore.CYAN + skk)


def prRed(skk):
    print(Fore.RED + skk)


def prGreen(skk):
    print(Fore.GREEN + skk)


def prYellow(skk):
    print(Fore.YELLOW + skk)


url = order_link
prRed('Opening Link in chrome..........')
prCyan('\n')
print('\nLogging in with username:', email_inp)
prYellow('\n')
if pay_opt_input == 'EMI_OPTIONS':
    print('\nEMI Option Selected. \nBANK:', bankname_input, '\nTENURE:', tenure_input, '\n')
else:
    if pay_opt_input == 'PHONEPE':
        print('\nPayment with Phonepe\n')
    else:
        if pay_opt_input == 'NET_OPTIONS':
            print('\nNet Banking Payment Selected\n')
        else:
            if pay_opt_input == 'COD':
                prGreen('COD selected\n')
            else:
                print('\nFull Payment Selected\n')

driver = webdriver.Chrome(options=opts , executable_path=driver_path)

driver.maximize_window()
driver.get("http://www.flipkart.com")
prCyan('\n')


def login_submit():
    print("login your account ")

    driver.find_element_by_xpath("//input[@class='_2zrpKA _1dBPDZ']").send_keys(email_inp);
    driver.find_element_by_xpath("//input[@class='_2zrpKA _3v41xv _1dBPDZ']").send_keys(pass_inp);
    driver.find_element_by_xpath("//button[@class='_2AkmmA _1LctnI _7UHT_c']").click();
    time.sleep(5)

def buy_check():
    driver.get(url)
    try:
        nobuyoption = False
        while nobuyoption == False:
            try:
                driver.refresh()
                time.sleep(1)
                buyprod = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div[1]/div[1]/div[2]/div/ul/li[2]/form/button') 
                print(buyprod.is_enabled())
                nobuyoption = buyprod.is_enabled()

            except Exception as e :
                print(e)
                nobuyoption = False
                prRed('Buy Button Not Clickable')

        buyprod.click()
        prYellow('Buy Button Clicked Successfully')
        buy_recheck()
    except:
        prRed('buy_check Failed. Retrying.')
        time.sleep(2)
        buy_check()


def buy_recheck():
    print("reached here")
    try:
        WebDriverWait(driver, 4).until(EC.title_contains('Flipkart'))
        prYellow('Redirected to Payment')
        skip()
    except:
        prRed('Error in Redirecting to Payment')
        time.sleep(0.5)
        buy_recheck()


def deliver_option():
    try:
        addr_input_final = "//label[@for='" + addr_input + "']"
        try:
            sel_addr = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, addr_input_final)))
            prYellow('Address Selection Button Clickable')
        except:
            prRed('Address Selection Button Not Clickable')
        else:
            sel_addr.click()
            prYellow('Address Selection Button Clicked Successfully')
    except:
        prRed('deliver_option Failed. Retrying.')


def deliver_continue():
    try:
        addr_sal_avl = True
        while addr_sal_avl:
            try:
                address_sel = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '._3K1hJZ ._7UHT_c')))
                address_sel.click()
                addr_sal_avl = False
                print('Address Delivery Button Clickable')
            except:
                addr_sal_avl = True
                print('Address Delivery Button Not Clickable')

        print('Address Delivery Button Clicked Successfully')
    except:
        print('deliver_continue Failed. Retrying.')



def skip():
    time.sleep(4)
    driver.find_element_by_xpath("//*[@class='_2AkmmA _I6-pD _7UHT_c']").click()
    try:
        x = driver.find_element_by_xpath("//*[@src='data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTMiIGhlaWdodD0iMTMiIHZpZXdCb3g9IjAgMCAxMyAxMyIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cGF0aCBkPSJNMS4wNTQgMWwxMC41NDMgMTAuNjVtLjA1NC0xMC41OTZMMSAxMS41OTciIHN0cm9rZT0iIzQxNDE0MSIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgZmlsbD0ibm9uZSIvPjwvc3ZnPgo=']")
        x.click()
        print("skip click")
    except:
        print("skip not click")
    order_summary_continue()


def order_summary_continue(): 
    time.sleep(2)
    driver.find_element_by_xpath("//*[@class='_2AkmmA _2Q4i61 _7UHT_c']").click()
    time.sleep(2)
    if pay_opt_input == 'COD':
        try:
        	# open new tab
            driver.execute_script("window.open('https://www.youtube.com./watch?v=_uUdJalMaF8&ab_channel=T-Series')")
            driver.switch_to.window(driver.window_handles[-1])
            WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Play']"))).click()
            cod_captcha()
        except NoSuchElementException as e:
            print(e)

def cod_captcha():
    try:
        payment_sel = WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="container"]/div/div[2]/div/div[1]/div[4]/div/div/div[1]/div/label[5]/div[2]/div/div'))) 
        payment_sel.click()
        time.sleep(1)
        print("cod button selected")
        prYellow('Type the captcha here:')
        capText = SolveCapcha()
        print(capText)
        payment_sel.send_keys(capText)
        prGreen('\nCaptcha entered successfully.')
        prYellow('\nClicking Confirm Button order:')
        confirm_btn = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '._7UHT_c')))
        confirm_btn.click()
        prGreen('\nOrder confirmed successfully')
    except:
        prRed('\nCaptcha could not be entered. Plese type manually on webpage.')


def SolveCapcha():
    try:
        print("method is called")
        image_link = url + driver.find_element_by_xpath('//*[@id="container"]/div/div[2]/div/div[1]/div[4]/div/div/div[1]/div/label[5]/div[2]/div/div/div[3]/form/div/div[1]/img[1]').get_attribute('src')
        print(image_link)
        ANTICAPTCHA_KEY = "masked"
        user_answer = ImageToTextTask.ImageToTextTask(anticaptcha_key=ANTICAPTCHA_KEY).\
        captcha_handler(captcha_link=image_link)
        print(user_answer['solution']['text'])
        return user_answer['solution']['text']
    except Exception as e:
            print(e)


def payment_continue():
    try:
        pay = None
        try:
            pay = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '._3K1hJZ ._7UHT_c')))
            print('Pay Button Clickable')
        except:
            print('Pay Button Not Clickable')
        else:
            pay.click()
            print('Pay Button Clicked Successfully')
    except:
        print('payment_continue Failed. Retrying.')


def otp_submit():
    try:
        otp = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '._3K1hJZ .l5dwor')))
        otp.clear()
        print('Please enter OTP here:')
        otp_input = input()
        otp.send_keys(otp_input)
        submit_otp = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '._3K1hJZ ._7UHT_c')))
        submit_otp.click()
        print('OTP Submitted Successfully')
    except:
        print('otp_submit Failed. Retrying.')
        time.sleep(0.5)
        otp_submit()


def try_till_otp():
    login_submit()
    buy_check()
    #skip()


if __name__ == '__main__':
    try_till_otp()
