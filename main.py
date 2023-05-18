from http.cookies import SimpleCookie
from urllib.parse import urlparse, parse_qs

def parse_cookie(query: str) -> dict:
    cookie = SimpleCookie()
    cookie.load(query)
    output2 = {k: v.value for k, v in cookie.items()}
    return output2



def parse(URL: str) -> dict:
    parsed_url = urlparse(URL)
    output = parse_qs(parsed_url.query)
    for key, value in output.items():
        output.update({key: str(value[0])})
    return output

if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
    assert parse('/shoes/women-shoes?type=high-heels') == {'type': 'high-heels'}
    assert parse('GET /surfreport/beachId?days=3&units=metric&time=1400') == {'days': '3', 'units': 'metric',
                                                                              'time': '1400'}
    assert parse('GET /surfreport/beachId?days=3&&&units=metric&&&time=1400') == {'days': '3', 'units': 'metric',
                                                                                  'time': '1400'}
    assert parse('https://www.google.com/search?q=abstract+api') == {'q': 'abstract api'}
    assert parse('https://www.google.com/search?q=abstract+api&rlz=1C1CHBF_enUS923US923&oq=abstract+api&aqs=chrome'
                 '..69i57j0i10i433j0j0i10i433j0i10l6.1705j0j7&sourceid=chrome&ie=UTF-8') == {'q': 'abstract api',
                                                                                             'rlz': '1C1CHBF_enUS923US923',
                                                                                             'oq': 'abstract api',
                                                                                             'aqs': 'chrome'
                                                                                                    '..69i57j0i10i433j0j0i10i433j0i10l6.1705j0j7',
                                                                                             'sourceid': 'chrome',
                                                                                             'ie': 'UTF-8'}

    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('any_information') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie('type=high-heels') == {'type': 'high-heels'}
    assert parse_cookie('units=metric;time=1400') == {'units': 'metric', 'time': '1400'}
    assert parse_cookie('keebler=E=mc2') == {'keebler': 'E=mc2'}
    assert parse_cookie('devicePixelRatio=1; ident=exists; __utma=13103r6942.2918;') == {'devicePixelRatio': '1',
                                                                                         'ident': 'exists',
                                                                                         '__utma': '13103r6942.2918'}
    assert parse_cookie(
        'devicePixelRatio=1;ident=exists;'
        '__utma=13103r6942.2918;'
        't_session='
        'BAh7DUkiD3Nlc3NpbWVfZV9uYW1lBjsARkkiH1BhY2lmaWMgVGltZSAoVVMgJiBDYW5hZgitGEpBjsAVEkiFXNpZ25pbl9wZXJzb25faWQGOwBGaQ'
        'MSvRpJIhRsYXN0X2xvZ2luX2RhdGUGOwBGVTogQWN0aXZlU3VwcG9ydDo6VGltZVdpdGhab25lWwhJdToJVGltZQ2T3RzAAABA7QY6CXpvbmVJI'
        'ghVVEMGOwBUSSIfUGFjaWZpZWRfZGFzaGJvYXJkX21lc3NhZ2UGOwBGVA%3D%3D--6ce6ef4bd6bc1a469164b6740e7571c754b31cca') == {
        'devicePixelRatio': '1',
        'ident': 'exists',
        '__utma': '13103r6942.2918',
        't_session': 'BAh7DUkiD3Nlc3NpbWVfZV9uYW1lBjsARkkiH1BhY2lmaWMgVGltZSAoVVMgJiBDYW5hZgitGEpBjsAVEkiFXNpZ25pbl9wZXJzb25faWQGOwBGaQMSvRpJIhRsYXN0X2xvZ2luX2RhdGUGOwBGVTogQWN0aXZlU3VwcG9ydDo6VGltZVdpdGhab25lWwhJdToJVGltZQ2T3RzAAABA7QY6CXpvbmVJIghVVEMGOwBUSSIfUGFjaWZpZWRfZGFzaGJvYXJkX21lc3NhZ2UGOwBGVA%3D%3D--6ce6ef4bd6bc1a469164b6740e7571c754b31cca'}




























 



