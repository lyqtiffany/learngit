'''
@author: haiwen
@date: 2021/1/15
@file: business.py
'''
from pylib.webapi.common import BaseAPI

class OrganizAPI(BaseAPI):
    #新增init，取parentid
    def __init__(self,cookies):
        super().__init__(cookies)
        #取parentid--列表的第一个元素id
        top_org = self.list_all()[0]
        self.parent_id = top_org['_id']

    #重写add，edit方法，替换parentid
    def add(self,**kwargs):
        #修改一下传染--更新parentid（默认使用总公司id）
        #判断一下是否传递parent，如果传递就什么都不做，如果没有则使用默认的
        if not kwargs.get('parent',None):
            kwargs['parent'] = self.parent_id

        #直接调用父类的add方法，传入修改后的参数
        return super().add(**kwargs)

    def edit(self,_id,**kwargs):
        if not kwargs.get('parent', None):
            kwargs['parent'] = self.parent_id
        # 直接调用父类的add方法，传入修改后的参数
        return super().edit(_id,**kwargs)

#签约对象
class AccountsAPI(BaseAPI):
    pass

#合同
class ContractsAPI(BaseAPI):
    pass


#合同分离
class ContractTypesAPI(BaseAPI):
    pass

if __name__ == '__main__':
    print(OrganizAPI('cookies',).path)
    print(AccountsAPI('cookies',).path)
