import os
# 專案路徑
project_dir  = os.getcwd()
source = os.walk(project_dir)
sd=os.listdir(os.curdir)
print(sd[0])
