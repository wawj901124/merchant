import xlrd

class ReadExcel(object):
    def __init__(self,filename,sheetname):
        self.filename = filename
        self.sheetname = sheetname
        self.sheet_data = self.get_sheet_data_bysheetname()


    #获取excel中sheet表的内容
    def get_sheet_data_bysheetname(self):
        excel_data = xlrd.open_workbook(self.filename)   #打开excel文件
        sheet_data = excel_data.sheet_by_name(self.sheetname)  #获取sheet表内容
        return sheet_data

    #获取sheet表的行数
    def get_sheet_nrows(self):
        sheet_nrows = self.sheet_data.nrows
        return sheet_nrows

    #获取sheet表的列数
    def get_sheet_ncols(self):
        sheet_ncols = self.sheet_data.ncols
        return sheet_ncols

    #获取sheet表单元格的内容
    def get_sheet_cell_value(self,row,col):
        sheet_cell_value = self.sheet_data.cell_value(row,col)   #获取单元格的内容
        return sheet_cell_value

    #返回sheetdatalist
    def get_test_data_list(self):
        sheet_nrows = self.get_sheet_nrows()
        sheet_ncols = self.get_sheet_ncols()
        testdata = []
        testdata_medium = []
        for i in range(1, sheet_nrows):  # 遍历行数
            for j in range(1, sheet_ncols):  # 遍历列数
                get_cell_value = self.get_sheet_cell_value(i, j)
                testdata_medium.append(get_cell_value)
            testdata.append(testdata_medium)
            testdata_medium = []

        return testdata



if __name__=="__main__":
    readexcel =ReadExcel(filename=r"D:\Users\Administrator\PycharmProjects\merchant\SecondChapt\datas.xls",sheetname=u"登录测试用例")
    testdatalist = readexcel.get_test_data_list()
    print("testdatalist:%s" % testdatalist)
    # readexcel =ReadExcel(filename=r"D:\Users\Administrator\PycharmProjects\merchant\SecondChapt\datas.xls",sheetname=u"登录测试用例")
    # sheet_nrows = readexcel.get_sheet_nrows()
    # print("表格行数：%s" % sheet_nrows)
    # sheet_ncols = readexcel.get_sheet_ncols()
    # print("表格列表数：%s" % sheet_ncols)
    #
    # testdata = []
    # testdata_medium = []
    # for i in range(1,sheet_nrows): #遍历行数
    #     for j in range(1,sheet_ncols):  #遍历列数
    #         get_cell_value = readexcel.get_sheet_cell_value(i,j)
    #         testdata_medium.append(get_cell_value)
    #         print("获取到的数据为：%s" % get_cell_value)
    #     testdata.append(testdata_medium)
    #     testdata_medium = []
    #
    # print("testdata:%s" % testdata)


