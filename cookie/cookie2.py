from urllib import request
from http.cookiejar import CookieJar
cookiejar = CookieJar
handler = request.HTTPCookieProcessor(cookiejar)
