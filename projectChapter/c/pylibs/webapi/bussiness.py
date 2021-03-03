'''
@author: haiwen
@date: 2021/3/1
@file: bussiness.py
'''
from pylibs.webapi.common import BaseAPI
# from .common import BaseAPI

#部门API
class OrganizAPI(BaseAPI):
    def __init__(self,cookies):
        super().__init__(cookies)
        # 总公司id = 部门列表的第一个元素的id
        self.top_parent = self.list_all()[0]['_id']

    def add(self,**kwargs): # parent=xxxxxxxxx
        # 如果传参中带prarent，就用参数指定的parent
        # 如果没有传parent 就用默认的总公司
        if 'parent' not in kwargs:
            kwargs['parent']=self.top_parent

        return super().add(**kwargs)  #不要忘记return

    def update(self, _id , **kwargs):  # parent=xxxxxxxxx
        # 如果传参中带prarent，就用参数指定的parent
        # 如果没有传parent 就用默认的总公司
        if 'parent' not in kwargs:
            kwargs['parent'] = self.top_parent

        return super().update( _id ,**kwargs)  # 不要忘记return

    def delete_all(self):
        orgs = self.list_all()[1:]  #第一个是总部 不用删除
        for org in orgs:
            self.delete(org['_id'])


#合同API
class ContractsAPI(BaseAPI):
    pass

