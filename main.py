import platform
import socket
import subprocess
import json
import psutil
from pip._vendor import requests


# Get processor information
def get_processor_info():
    return subprocess.check_output("lscpu", shell=True).strip().decode().split('\n')[13].split(':')[1].lstrip()

# Get operative system name
def get_os_name():
    return subprocess.check_output("uname -s -n", shell=True).lstrip().rstrip().decode()

# Get operative system version
def get_os_version():
    return subprocess.check_output("uname -v", shell=True).lstrip().rstrip().decode()

# Get server ip in which is excecuted the agent
def get_server_ip():
    return subprocess.check_output("hostname -I", shell=True).lstrip().rstrip().decode()

# Get the list of running processes
def get_running_processes():
    listOfProcessNames = list()
    for proc in psutil.process_iter():
        pInfoDict = proc.as_dict(attrs=['pid', 'name', 'cpu_percent'])
        listOfProcessNames.append(pInfoDict)
    return listOfProcessNames

# Get the list of active users
def get_active_users():
    formated_users = []
    users_array = subprocess.check_output("users", shell=True).lstrip().rstrip().decode().split(' ')
    for user in users_array:
        formated_users.append({'name': user})
    return formated_users

# Assembly the json payload to send
def build_json_data(processor_info, os_name, os_version, server_ip, running_processes, active_users):
    data = {'processor': processor_info,
            'operative_system':
                {'name': os_name,
                 'version': os_version
                 },
            'server_ip': server_ip,
            'active_processes': running_processes,
            'active_users': active_users
            }

    return data

# Send the json payload to the compliance-api
def send_json_data(url, data):
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    try:
        response = requests.post(url, data=json.dumps(data), headers=headers)
    except Exception as e:
        print('Fail to sent info to server api')
        response = e
    return response

def main():
    processor_info = get_processor_info()
    os_name = get_os_name()
    os_version = get_os_version()
    server_ip = get_server_ip()
    running_processes = get_running_processes()
    active_users = get_active_users()
    data = build_json_data(processor_info, os_name, os_version, server_ip, running_processes, active_users)

    # url to replace if use docker to run container application agent to container api
    # url = "http://api:5000/api/v1/compliance/system_info"
    # url to replace if you run application agent locally to container api
    # url = "http://0.0.0.0:5000/api/v1/compliance/system_info"
    # url to replace if you run both apps locally without docker
    url = "http://127.0.0.1:5000/api/v1/compliance/system_info"

    response = send_json_data(url, data)
    if response is not None:
        print('Status info ' + str(response))


if __name__ == "__main__":
    main()
