import requests
import os
api_key = os.environ.get("X_API_KEY")
webhook = os.environ.get("WEBHOOK")
if not api_key and webhook:
    raise RuntimeError("X-API-KEY or Webhook is Not set")
headers = {'headers': {'X-API-KEY': api_key}}
project = "PROJ-17"
team = 2
host = "https://qa.isara.com"


def GetAvailableMachine():
    res = requests.get(f"{host}/api/machines/list?project={project}&team={team}&user_level=Automation", **headers)
    for i in range(len(res.json())):
        if "faroque" in res.json()[i]['name']:
            return 1
    return 0


def UploadAndReplace():
    res = requests.post(f"{host}/test_case_file_upload/",
                        files={"file": open(".github/bcd.txt", 'rb')},
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
    code = RunBuild()
    assert code == 200

