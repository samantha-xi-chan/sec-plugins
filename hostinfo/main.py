import requests
from pyquery import PyQuery as pq


def fofa(host):
    url = "https://fofa.info/hosts/" + host
    text = requests.get(url, timeout=30).text
    doc = pq(text)
    ipbase = list(doc(".section .ip-base .ipDiv").items())
    ip = ipbase[0](".ipDRight").text()
    country = ipbase[1](".ipDRight").text()
    city = ipbase[2](".ipDRight").text()
    org = ipbase[3](".ipDRight").text()
    isp = ipbase[4](".ipDRight").text()
    asn = ipbase[5](".ipDRight").text()

    services = list(doc(".componentInfo .lists").items())
    lists = []
    if len(services) > 1:
        for item in services[1:]:
            divs = list(item("div").items())
            if len(divs) >= 3:
                port = divs[1].text()
                service = divs[2].text()
                lists.append({"port": port, "service": service})
    return {"ip": ip, "country": country, "city": city, "org": org, "isp": isp, "asn": asn, "services": lists}


if __name__ == '__main__':
    import argparse
    import json

    parser = argparse.ArgumentParser()
    parser.add_argument("--url", type=str, default="")
    args = parser.parse_args()

    output = {
        "plugin_result": {
            "exit_code": 0,
            "biz": {
            }
        },
        "ver": 1
    }

    ret = fofa(args.url)
    output["plugin_result"]["biz"]["output"] = ret
    print(json.dumps(output))
