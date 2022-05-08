import os
# os.path.dirname 去掉文件名，返回目录
# __file__ 当前文件的path
current_dir = os.path.dirname(os.path.dirname(__file__))
# 配置文件路径
config_dir = os.path.join(current_dir, "config")
testCase_dir = os.path.join(current_dir, "test_Case")
testData_dir = os.path.join(current_dir, "test_data")
testReport_dir = os.path.join(current_dir, "test_report")

