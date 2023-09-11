from cipher.main import cipherAnalyse

if __name__ == '__main__':
    import argparse
    import json

    parser = argparse.ArgumentParser()
    parser.add_argument("--code", type=str, default="")
    args = parser.parse_args()
    x = cipherAnalyse(args.code)
    output = {
        "plugin_result": {
            "exit_code": 0,
            "biz": {
            }
        },
        "ver": 1
    }
    output["plugin_result"]["biz"]["output"] = str(x)
    print(json.dumps(output))
