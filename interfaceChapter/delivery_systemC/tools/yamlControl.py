import yaml


def get_yaml_data(fileDir):
    #1 把文件从磁盘加载到内存中，--打开
    fo = open(fileDir, 'r', encoding='utf-8')
    #2- 使用yaml读取
    res = yaml.load(fo, Loader=yaml.FullLoader) #加安全模式
    print(res)
    return res

def get_yamls_data(fileDir):
    resList = []
    #1 把文件从磁盘加载到内存中，--打开
    fo = open(fileDir, 'r', encoding='utf-8')
    #2- 使用yaml读取
    res = yaml.load_all(fo, Loader=yaml.FullLoader) #加安全模式
    #load_all 多个yaml读取
    for one in res:
        resList.append(one)
    return resList

#处理用例数据
def get_yaml_data2(fileDir):
    resList =[]
    #1 把文件从磁盘加载到内存中，--打开
    fo = open(fileDir, 'r', encoding='utf-8')
    #2- 使用yaml读取
    res = yaml.load(fo, Loader=yaml.FullLoader) #加安全模式
    print(res)
    del res[0]
    #返回数据样式--根据项目来
    for one in res:
        resList.append((one['data'], one['resp']))
    return resList



if __name__ == '__main__':
    # get_yaml_data('../configs/conf.yaml')
    # get_yamls_data('../configs/conf.yaml')
    get_yaml_data2('../data/data.yaml')


