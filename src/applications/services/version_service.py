import pip
import json
import logging
import platform
import subprocess

from .utils.re_util import get_only_version

logger = logging.getLogger(__name__)


class VersionService:

    @staticmethod
    def get_python_version():
        return platform.python_version()

    @staticmethod
    def get_pip_version():
        return pip.__version__

    @staticmethod
    def get_library_version(library_name: str):
        cmd = f'pip3 freeze | grep {library_name}'
        ps = subprocess.Popen(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT)
        output = ps.communicate()[0]
        version = get_only_version(text=output.decode())

        if version is None:
            return '-'
        return version

    @staticmethod
    def get_pip_list(format: str = 'json'):
        """
        ref: https://minus9d.hatenablog.com/entry/2021/06/08/220614
        :return:
        """
        if format not in ('json', 'freeze', 'columns'):
            raise ValueError

        list_files = subprocess.run(
            ['pip3', 'list', '--format', format], capture_output=True)

        match format:
            case 'json':
                return json.loads(list_files.stdout)
            case 'freeze':
                return list_files.stdout
            case _:
                pass
