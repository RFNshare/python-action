import requests
import os

api_key = "96f5df77-ba1c-4fc0-91a2-4482f7bd6473"
webhook = "a8d4dCD1C58BadCf8fd383ABAcb526e3ad2c0e3dfAAD2Ff26EeE9bdecCeCcd8441745c86732Db0cb3484cfCc0DeEeA45aeFF"
if not api_key and webhook:
    raise RuntimeError("X-API-KEY or Webhook is Not set")
headers = {'headers': {'X-API-KEY': api_key}}
project = "PROJ-17"
team = 2
host = "https://zeuz.zeuz.ai"


def GetAvailableMachine(machine):
    lst_mech = []
    res = requests.get(f"{host}/api/machines/list?project={project}&team={team}&user_level=Automation", **headers)
    # for i in res.json():
    #     print(i["name"])
    for i in range(len(res.json())):
        if machine in res.json()[i]['name']:
            lst_mech.append(res.json()[i]['name'])
    return lst_mech


def UploadAndReplace():
    res = requests.post(f"{host}/test_case_file_upload/",
                        files={"file": open(".github/bcd.txt", 'rb')},
                        data={"file_upload_tc": "TEST-2148"},
                        verify=False, **headers)
    return res.status_code


def RunBuild(node_id):
    res = requests.post(f"{host}/Home/deploy_presets/webhook/{webhook}/",
                        json={
                            "nodeId": node_id,
                            "objective": "Test Run",
                            "version": "0.0",
                            "runtimeParameters": []
                        }, **headers)
    print(res.text)
    return res.status_code


if __name__ == '__main__':
    machines = GetAvailableMachine("faroque")
    if machines:
        for machine in machines:
            code = RunBuild(machine)
            print(code)
            assert code == 200
    else:
        print("No Machine Available")
