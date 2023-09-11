## hostinfo

根据ip查找端口

### 输入

```
--url xxx.com
```

### 输出

```
output = {
        "plugin_result": {
            "exit_code": 0,
            "biz": {
                "output":"输出内容"
            }
        },
        "ver": 1
    }
```

## pocsearch

根据关键字查找poc

### 输入

question 问题
detail 是否展示详情
size 返回个数

```
--question shiro --detail --size 5
```

### 输出

```
output = {
        "plugin_result": {
            "exit_code": 0,
            "biz": {
                "output":"输出内容"
            }
        },
        "ver": 1
    }
```

## cipheranalyse

根据密文分析算法并解密

### 输入

```
--code 密文
```

### 输出

```
output = {
        "plugin_result": {
            "exit_code": 0,
            "biz": {
                "output":"输出内容"
            }
        },
        "ver": 1
    }
```

## headless

根据url获取网页截图

### 输入

```
--url xxx.com
```

### 输出

```
output = {
        "plugin_result": {
            "exit_code": 0,
            "biz": {
                "output":"base64编码图片"
            }
        },
        "ver": 1
    }
```
