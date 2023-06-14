import subprocess


def check_cmd():
    result = subprocess.run(["dir"], shell=True, capture_output=True, text=True)
    return result.stdout

def sub_popen():
    p = subprocess.Popen(["python", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    output, errors = p.communicate()
    return output

if __name__ == "__main__":
    print(check_cmd())
    print(sub_popen())