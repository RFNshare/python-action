# import subprocess
#
# serial = ''
# apk_path = "D:\\ZeuZ_Node\\ZeuZ Main\\AutomationLog\\attachments\\TEST-0155\\app-release.apk"
# output = subprocess.check_output(
#     "adb %s install -r \"%s\"" % (serial, apk_path), shell=True, encoding="utf-8"
# )
# print(output)

import requests
import os

# url = f"{host}/Home/ManageTestCases/Edit/{tc}/testcase_update_labels"
# res = requests.get(url, headers=headers, params=params)
# print(res.status_code)
# print(res.text)

api_key = "36b5c8c3-2f84-40f4-999c-38c286592c53"
host = 'https://ts.automationsolutionz.com'
headers = {'X-API-KEY': api_key, 'x-requested-with': 'XMLHttpRequest'}

url = f"{host}/Home/BundleReport/*Folder%3DTexada@&*Folder%3DWeb@&*Automatability%3DAutomated@&*Status%3DReady$%5E$" \
      f"%5E$Milestone%3D2023.01/execution_report_testcases_redone/?project_id=PROJ-17&team_id=2&itemPerPage=100" \
      f"&currentPage=1&status=Failed&UserText=Milestone+-+2023.01%3A+&tcfilters=%5B%22Texada%22%2C%22Web%22%2C" \
      f"%22Automated%22%2C%22Ready%22%5D&tcAttributes=%5B%22Folder%22%2C%22Folder%22%2C%22Automatability%22%2C" \
      f"%22Status%22%5D&tcintersects=%5B%22AND%22%2C%22AND%22%2C%22AND%22%5D"


res = requests.get(url, headers=headers)
print(res.text)
# def add_tag(tc):
#     payload = {}
#     params = {
#         'TC_Id': {tc},
#         'label_id': 'LABEL-42',
#         'label_name': 'Smoke',
#         'user_id': '291'
#     }
#     url = f"{host}/Home/ManageTestCases/Edit/{tc}/testcase_update_labels"
#
#     res = requests.get(url, headers=headers, params=params)
#
#     if res.status_code == 200 and res.text == 'true':
#         print(f'added - {tc}')
#     else:
#         print(f'unable to add - {tc}')
#
#
# res = requests.get(url, headers=headers)
# print(res.status_code)
# count = 0
# for i in res.json()['TableData']:
#     add_tag(i[0])


