
import yaml
def read_yml(path):
    res = yaml.safe_load(open(path,encoding='utf-8'))
    return res

if __name__ == '__main__':
    res = read_yml('../../conf/api_config.yml')
    print(res)
