import json
from security import safe_requests

def check(alive, proxy, apiurl, sema, timeout, testurl):
    try:
        r = safe_requests.get(url=apiurl + '/proxies/' + str(proxy['name']) + '/delay?url='+testurl+'&timeout=' + str(timeout), timeout=10)
        response = json.loads(r.text)
        if 'delay' in response and response['delay'] > 0:
            alive.append(proxy)
    except: pass
    sema.release()
