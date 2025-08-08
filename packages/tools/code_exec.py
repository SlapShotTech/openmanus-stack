import subprocess
import tempfile
import textwrap


class CodeExecTool:
    """Execute Python or shell code in a sandboxed subprocess."""

    def run_python(self, code: str) -> str:
        with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as f:
            f.write(textwrap.dedent(code))
            file_path = f.name
        result = subprocess.run(["python", file_path], capture_output=True, text=True)
        return result.stdout + result.stderr

    def run_shell(self, command: str) -> str:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout + result.stderr