import sys

import fabric
import subprocess

import os.path

__tar_file_name = f'/tmp/repository.tar'
__repository_dir = '/tmp'

__external_sources = [{'url': 'https://www.rpmfind.net/linux/epel/9/Everything/x86_64/Packages/g/gprbuild-23.0.0-2.el9.x86_64.rpm', 'user': '', 'password': ''}]

def download_external_sources():
   for external_source in __external_sources:
        subprocess.check_output(['mkdir', '-p', f'{os.path.join(__repository_dir, 'tests/test_input_from_external')}'])
        subprocess.check_output(['curl', external_source])

def execute_container_tests():
    subprocess.check_output(['make', '-C', f'{__repository_dir}/tests'])

def create_repository_tar():
    subprocess.check_output(['tar', '-czvf', f'{os.path.join(__repository_dir, 'tests')}'])

def put_tar_to_target_tester(target_tester_connection : fabric.Connection):
    target_tester_connection.put(__tar_file_name, __tar_file_name)

def extract_tar_file(target_tester_connection : fabric.Connection):
    target_tester_connection.run(f'tar -xzvf {__tar_file_name}')

def execute_make_file_on_target_tester(target_tester_connection : fabric.Connection):
    target_tester_connection.run(f'make -C /tmp/tests')
    target_tester_connection.run(f'tar -czvf /opt/mk1res')

def get_test_output_from_target_tester(target_tester_connection : fabric.Connection):
    target_tester_connection.get('test_output')

if __name__ == sys.main:
    download_external_sources()
    execute_container_tests()
    create_repository_tar()

    c = fabric.Connection(
    host="hostname",
    user="admin",
    connect_kwargs={
        "key_filename": "/home/myuser/.ssh/private.key",
    },
)