'''
Date: 2022-02-22 09:48:53
LastEditors: ChocoboQJJ
LastEditTime: 2022-02-23 13:29:29
FilePath: \QPython\ToolKit\ExcelKit.py
'''
import xlrd
import xlwt
import json

def OpenExcel(path):
    """
    :param 函数描述:读取Excel
    :param path:Excel文件的绝对路径(路径带盘符并使用'/'分隔上下级目录)
    :param return:workBook对象
    """
    return xlrd.open_workbook(path)

def ReadSheetByWorkBook(workBook,index=0):
    """
    :param 函数描述:读取工作簿中指定索引的sheet
    :param workBook:需要读取的workBook(workBook对象通过OpenExcel函数来获取)
    :param index:sheet索引,从左至右分别是0,1,2...(默认读取第一个sheet)
    :param return:sheet对象
    """
    return workBook.sheet_by_index(index)

def GetSheetData(sheet):
    """
    :param 函数描述:遍历sheet行列,并存入Json对象
    :param sheet:需要读取的sheet(sheet对象通过ReadSheetByWorkBook函数来获取)
    :param return:Json对象
    """
    sheet_data = list()
    for i in range(sheet.nrows):
        content = list()
        for j in range(sheet.ncols):
            content.append(sheet.cell_value(i,j))
        sheet_data.append(content)
        js = json.dumps(sheet_data)
        print(js)
    return js

# 测试用例(OpenExcel的路径可自行更改)
GetSheetData(ReadSheetByWorkBook(OpenExcel("Resources/Test.xlsx")))