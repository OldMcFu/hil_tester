import pytest

import sys
import os
import fabric
import filecmp
from urllib.parse import urlparse
#Add path to hil testing
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../hil_testing')) 
import bamboo_script

def test_remote_download():
    url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/dc/Grumpy_Cat_%2814556024763%29_%28cropped%29.jpg/800px-Grumpy_Cat_%2814556024763%29_%28cropped%29.jpg'
    repo_dir = os.path.dirname(__file__)
    bamboo_script.download_external_sources([url], repo_dir)

def test_sync_folder_to_tester(): 
    bamboo_script.sync_folder_to_tester('root', '20.0.0.5', '/workspace/hil_testing')

def test_get_folder_from_tester():
    bamboo_script.sync_folder_from_tester('root', '20.0.0.5', '/tmp')

def test_compare_folders():
    compared = filecmp.dircmp('/workspace/hil_testing', '/tmp/tests/test_output/bamboo_sync_folder/hil_testing')
    assert compared.diff_files == [], 'Folder is not equal please check rsync command!'

@pytest.mark.parametrize("cmd,exitcode", [("uname -a", 0), ("this_command_is_invalid", 127)])    
def test_remote_command_exec(cmd, exitcode):
    with fabric.Connection("20.0.0.4", user="root") as remote_system:
        res = bamboo_script.execute_remote_cmd(remote_system, cmd)
        assert res.exited == exitcode, f'stderr is: {res.stderr}'