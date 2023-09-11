import json
import os.path
from pathlib import Path

from cipher.Crypto_func import *
from cipher.Plug.decode.htmlunescape import htmlunescape
from cipher.Plug.decode.slashASCII import slashASCII

# 导入自定义解密插件
filename = os.path.join(Path(__file__).resolve().parent, 'Plug', 'config.json')

with open(filename, 'r+', encoding='utf-8') as f:
    Crypto_json = json.load(f)

funcitonary = {
    'de_base16': de_base16,
    'de_base32': de_base32,
    'de_base36': de_base36,
    'de_base58': de_base58,
    'de_base62': de_base62,
    'de_base64': de_base64,
    'de_base85': de_base85,
    'de_base91': de_base91,
    'de_base92': de_base92,
    'rot5': rot5,
    'rot13': rot13,
    'rot18': rot18,
    'rot47': rot47,
    'de_Shellcode': de_Shellcode,
    'de_XXencode': de_XXencode,
    'de_UUencode': de_UUencode,
    'de_Handycode': de_Handycode,
    'de_Tapcode': de_Tapcode,
    'de_Morse': de_Morse,
    'de_Baconian': de_Baconian,
    'de_yunyin': de_yunyin,
    'de_Atbash': de_Atbash,
    'de_Polybius': de_Polybius,
    'de_Quoted': de_Quoted,
    'de_AAencode': de_AAencode,
    'de_Brainfuck': de_Brainfuck,
    'de_Emoji': de_Emoji,
    'de_JJencode': de_JJencode,
    'de_JSfuck': de_JSfuck,
    'de_Jother': de_Jother,
    'de_Socialism': de_Socialism,
    'de_Buddha': de_Buddha,
    'de_Buddha_FoYue': de_Buddha_FoYue,
    'de_Buddha_RuShiWoWen': de_Buddha_RuShiWoWen,
    'de_Caesar': de_Caesar,
    'de_Fence': de_Fence,
    'de_a1z26code': de_a1z26code,
    'de_Url': de_Url,
    'de_010': de_010,
    'htmlunescape': htmlunescape,
    'slashASCII': slashASCII

}


# 识别密文


def Cipherase(cryptostr, keyValue):
    redo_crypto = set(cryptostr.replace('\n', '').replace('\r', ''))  # 密文字符去重
    maybe_list = []  # 密文可能在的列表
    maybe_list_name = []  # 密文可能在的列表-名字
    maby_list_name = []  # 密文大概率在的列表，长度与密文表相等-名字
    back_list_name = []  # 不可能的加密方式-名字

    with open(filename, 'r', encoding='utf-8') as f:
        Crypto_json = json.load(f)

    for i in Crypto_json["Base_crypto"]:
        if len(redo_crypto) <= int(i["alphabet_num"]):
            maybe_list.append(i)
            maybe_list_name.append(i["crypto_name"])
        if len(redo_crypto) == int(i["alphabet_num"]):
            maby_list_name.append(i["crypto_name"])

    # 正则匹配密文的每个字符，不在范围内将该加密类型加入黑名单
    for i in maybe_list:
        a = str(i["range"])
        pattern = compile(r'' + a + '')
        for j in redo_crypto:
            if pattern.match(j) is None:
                back_list_name.append(i["crypto_name"])
                break

    # 移除黑名单中的加密类型
    for i in back_list_name:
        maybe_list_name.remove(i)
        try:
            maby_list_name.remove(i)
        except:
            pass

    # 重选
    if len(maby_list_name) != 0:
        # 取 maybe_list_name 与 maby_list_name 的交集
        result_list = list(
            set(maybe_list_name).intersection(set(maby_list_name)))
    else:
        result_list = maybe_list_name

    result = single_decry(result_list, cryptostr, keyValue, Crypto_json)

    if len(result) == 0:
        return False
    return result

def getCiperName(cryptostr):

    redo_crypto = set(cryptostr.replace('\n', '').replace('\r', ''))  # 密文字符去重
    maybe_list = []  # 密文可能在的列表
    maybe_list_name = []  # 密文可能在的列表-名字
    maby_list_name = []  # 密文大概率在的列表，长度与密文表相等-名字
    back_list_name = []  # 不可能的加密方式-名字

    with open(filename, 'r', encoding='utf-8') as f:
        Crypto_json = json.load(f)

    for i in Crypto_json["Base_crypto"]:

        if len(redo_crypto) <= int(i["alphabet_num"]):
            maybe_list.append(i)
            maybe_list_name.append(i["crypto_name"])
        if len(cryptostr) == int(i["alphabet_num"]):
            maby_list_name.append(i["crypto_name"])

    # 正则匹配密文的每个字符，不在范围内将该加密类型加入黑名单
    for i in maybe_list:
        a = str(i["range"])
        pattern = compile(r'' + a + '')
        for j in redo_crypto:
            if pattern.match(j) is None:
                back_list_name.append(i["crypto_name"])
                break

    # 移除黑名单中的加密类型
    for i in back_list_name:
        maybe_list_name.remove(i)
        try:
            maby_list_name.remove(i)
        except:
            pass

    # 重选
    if len(maby_list_name) != 0:
        # 取 maybe_list_name 与 maby_list_name 的交集
        result_list = list(
            set(maybe_list_name).intersection(set(maby_list_name)))
    else:
        result_list = maybe_list_name
    with open(filename, 'r', encoding='utf-8') as f:
        cryptoJson = json.load(f)
    name_result = []
    for i in result_list:
        for j in cryptoJson["Base_crypto"]:
            if i == j["crypto_name"]:
                name_result.append(j["name"])

    if len(name_result) == 0:
        return False
    else:
        return name_result


def single_decry(result_list, cryptostr, keyValue, cryptoJson):
    # 获取由 result_list 与相应的key 组成的字典
    result_dict = {}
    for i in result_list:
        for j in cryptoJson["Base_crypto"]:

            if i == j["crypto_name"]:
                try:
                    result_dict[i] = j["key"]
                    break
                except:
                    result_dict[i] = 'False'  # key不存在的时候，默认为 False
                    break

    # 看能否正常解密
    for i in result_list:

        try:
            if funcitonary.get(i):
                if result_dict[i] == 'True' and keyValue != '':

                    res = (funcitonary.get(i)(cryptostr, keyValue)).decode()  # 调用函数解密

                else:
                    res = (funcitonary.get(i)(cryptostr)).decode()  # 调用函数解密

            if len(res) != 0 and res[:3] != "[-]" and res != cryptostr:  # 成功返回解密结果
                pass
            else:
                result_list[result_list.index(i)] = ''

        except Exception as e:
            result_list[result_list.index(i)] = ''
    result = [i for i in result_list if i != '']

    return result


def getType(result):

    # 由result中的crypto_name获取name
    with open(filename, 'r', encoding='utf-8') as f:
        cryptoJson = json.load(f)
    name_result = []
    for i in result:
        for j in cryptoJson["Base_crypto"]:
            if i == j["crypto_name"]:
                name_result.append(j["name"])

    if len(name_result) == 0:
        return False
    else:
        return name_result


def trig_func(cryp, cryptostr):
    if cryptostr == '':
        return False

    result = (funcitonary.get("{}".format(cryp))(cryptostr)).decode()
    if len(result) != 0 and result[:3] != "[-]":
        return result
    return False


def cipherDecode(cipherStr, ketValue, deep, text=''):
    typeList = Cipherase(cipherStr, ketValue)


    if not typeList:
        # print("解密失败")
        return False
    else:
        typeNameList = getType(typeList)

        if not typeNameList:
            # print("解密失败")
            return False
        else:
            for (index, ketValue) in enumerate(typeList):
                typeName = getType([ketValue])[0]

                if deep == 0:
                    result = trig_func(ketValue, cipherStr)
                    text += typeName + ',decode:' + result + '\n'

                    return {"data": result, "text": text}
                else:
                    result = trig_func(ketValue, cipherStr)
                    text += typeName + ',decode:' + result + '\n'
                    # print(deep, "decode:", result)
                    deep -= 1
                    return {"data": cipherDecode(result, ketValue, deep, text), "text": text}


def cipherAnalyse(cipher, value="", deepLength=100):
    result = cipherDecode(cipher, value, deepLength)
    if result:
        typeList = Cipherase(cipher, value)
        typeName = getType(typeList)
        while True:

            if isinstance(result, dict) and result['data']:
                result = result['data']
            else:
                result = result['text']
                break
        finalResult = result.split('\n')[len(result.split('\n')) - 2]
        ret = {
            "originEncodeType": typeName,
            "type": finalResult.split(',')[0],
            "result": finalResult.split(',')[1].split(':')[1],
            "log": result
        }
    else:
        typeNameResult = getCiperName(cipher)

        ret = {
            "originEncodeType": '',
            "type": typeNameResult,
            "result": "解码失败，您提供的编码格式可能为：" + ','.join(typeNameResult),
            "log": ""
        }
    return json.dumps(ret,ensure_ascii=False)

if __name__ == '__main__':
    cipher = "%E5%8F%A3%E8%AF%80%E6%88%91%E9%99%AA%E4%B8%BE%E6%8A%A5v%E5%93%A6%E5%91%9C"
    x = cipherAnalyse(cipher)
    print(x)

