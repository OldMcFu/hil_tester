import os
import sys
import fabric
import subprocess


def download_external_sources(external_sources:list, repository_dir:str):
    out_dir = os.path.join(repository_dir, "tests/test_input_from_external")
    subprocess.check_output(['mkdir', '-p', out_dir])
    os.chdir(out_dir)
    for external_source in external_sources:
        subprocess.check_output(['curl', '-O', external_source])
    os.chdir(repository_dir)
        
def sync_folder_to_tester(remote_user:str, remote_host_or_ip:str, repository_dir:str):
    subprocess.check_output(['rsync', '-a', f'{repository_dir}', f'{remote_user}@{remote_host_or_ip}:/tmp/bamboo_sync_folder'])

def sync_folder_from_tester(remote_user:str, remote_host_or_ip:str, repository_dir:str):
    subprocess.check_output(['mkdir', '-p', f'{repository_dir}/tests/test_output'])
    subprocess.check_output(['rsync', '-a', f'{remote_user}@{remote_host_or_ip}:/tmp/bamboo_sync_folder', f'{repository_dir}/tests/test_output'])

def execute_remote_cmd(target_to_tester_connection : fabric.Connection, cmd:str) -> fabric.Result:
    res = target_to_tester_connection.run(cmd, encoding='utf-8', warn=True)
    return res
