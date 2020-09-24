import yaml

# 解析yaml文件
def getYamlData(yaml_file):
    file = open(yaml_file, 'r', encoding="utf-8")
    file_data = file.read()
    file.close()
    # 将字符串转化为字典或列表
    data = yaml.load(file_data)
    return data