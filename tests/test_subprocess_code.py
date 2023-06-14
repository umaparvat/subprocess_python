from subprocess_code import check_cmd, sub_popen
import  pytest

class FakeSubProcess:
    def __init__(self, stdout="success", errors=None):
        self.stdout = stdout
        self.errors = errors

    def communicate(self):
        return (self.stdout, self.errors)


class TestSubprocess:


    def test_check_cmd(self, mocker):
        sub_run = mocker.patch("subprocess.run")
        sub_run.return_value = FakeSubProcess()
        assert check_cmd() == "success"

    def test_sub_popen(self, mocker):
        mock_sub_popen = mocker.patch("subprocess.Popen")
        mock_sub_popen.return_value = FakeSubProcess(stdout="Python 3.10.6")
        assert sub_popen() == "Python 3.10.6"