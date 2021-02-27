
# 为了把a 做为根目录，所以把a目录设置了source root

#
import pytest


if __name__ == '__main__':
    pytest.main(['-s', '--alluredir=tmp/report'])
