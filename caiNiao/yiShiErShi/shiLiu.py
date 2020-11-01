import datetime

if __name__ == '__main__':
    #输出今日日期，格式是ddmmyyyy
    print(datetime.date.today().strftime('%d%m%Y'))

    #输出指定日期，格式是dd/mm/yyyy
    testDate = datetime.date(1941, 4, 5)
    print(testDate.strftime('%d/%m/%Y'))

    #日期算数运算
    testDate= testDate + datetime.timedelta(days=1)
    print(testDate.strftime('%d/%m/%Y'))

    #日期替换
    testDate = testDate.replace(year=testDate.year +1)
    print(testDate.strftime('%d/%m/%Y'))

