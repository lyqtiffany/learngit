
# 为了把a 做为根目录，所以把a目录设置了source root

# 在a 目录下git init 并且管理Gitee 的仓库 https://gitee.com/lyqtiffany/projectchapter
import pytest


if __name__ == '__main__':
    pytest.main(['-s', '--alluredir=tmp/report'])
