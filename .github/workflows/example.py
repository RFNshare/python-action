import requests

headers = {'headers': {'X-API-KEY': '91e11016-b53f-4fc0-b715-c5c97b63377f'}}
project = "PROJ-17"
team = 2
host = "https://qa.isara.com"
webhook = "5CEc1C32a03E6cF6Eba64Af2ce18734Ccfa3C0EE9ba83DBebCa1DDDF15DCb7382032575a3cB06fca419bCe4D6EB4D3a74BEc"


def GetAvailableMachine():
    res = requests.get(f"{host}/api/machines/list?project={project}&team={team}&user_level=Automation", **headers)
    for i in range(len(res.json())):
        if "faroque" in res.json()[i]['name']:
            return 1
    return 0


def UploadAndReplace():
    res = requests.post(f"{host}/test_case_file_upload/",
                        files={"file": open("../bcd.txt", 'rb')},
                        data={"file_upload_tc": "TEST-2148"},
                        verify=False, **headers)
    return res.status_code


def RunBuild():
    res = requests.post(f"{host}/Home/deploy_presets/webhook/{webhook}/",
                        json={
                            "nodeId": "faroque_backup",
                            "objective": "CI/CD Test Run",
                            "version": "92.0",
                            "runtimeParameters": []
                        }, **headers)
    return res.status_code


if __name__ == '__main__':
    check = GetAvailableMachine()
    if check == 1:
        code = UploadAndReplace()
    else:
        print("Machine Not Available")

    if code == 200:
        assert RunBuild() == 200
