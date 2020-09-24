import unittest
import HTMLTestRunner


class RunCase:
    allCase = unittest.defaultTestLoader.discover('F:\\study-python\\WangJing_PO\\unitTest', 'test*.py')
    filename = './result.html'  # 定义个报告存放路径，支持相对路径。
    

    def run(self):
        runner = unittest.TextTestRunner()
        runner.run(self.allCase)

    def createReport(self):
        suites = unittest.TestSuite()
        for case in self.allCase:
            suites.addTest(case)
        fp = open(self.filename, 'wb')
        runner = HTMLTestRunner.HTMLTestRunner(
            stream = fp,
            title = 'WaJing项目测试报告',
            description = 'Report_description')
        runner.run(suites)

if __name__ == '__main__':
    p = RunCase()
    p.createReport()