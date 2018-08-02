# Installation
## Overview
- Download và cài đặt môi trường Python
- Giới thiệu Sublime Text Editor sử dụng trong khóa học này

## 1. Download và cài đặt môi trường Python in Windows
### Tiến hành download Python 3.6.1
- Bước 1: Truy cập vào trang chủ của Python: [Python org](https://www.python.org/)
- Bước 2: Chọn phiên bản ở mục Downloads và nhập chọn Python 3.6.1 để download
- Bước 3: Sau download hoàn tất. Chúng ta nhấn chọn chạy file **python-3.6.1.exe** để bắt đầu tiến trình cài đặt
- Bước 4: Tick vào ô **Add Python 3.6 to PATH** và chọn **Install Now**
- Bước 5: Khi cửa sổ hiển thị Setup was successful là ta đã cài đặt thành công môi trường Python > Close
- Bước 6: Tiếp đến, ta mở Command Prompt (CMD) để kiểm tra.
	- Để mở Command Prompt bạn dùng tổ hợp phím ***Windows + R*** để mở hộp thoại Run
- Bước 7: Trong cửa sổ Command Prompt, bạn gõ **python > Enter** để kiểm tra
```
C:\Users\PC>python
Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:19:30) [MSC v.1500 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

## 1.1 Python in unix, linux
- hệ điều hành đó đều đã được tích hợp Python 2.x lẫn Python 3.x. Các bạn muốn thao tác với nó chỉ cần mở Terminal và gõ python2 để chọn Python 2.x hoặc python3 để chọn Python 3.x

## 2. Sublime Text Editor
- [Installation](https://www.howkteam.vn/course/huong-dan-cai-dat/huong-dan-cai-dat-sublime-text-3-1534)
- shortkey_sublime.txt

## 3. Install pip(package manager)
- Check that if you have install python and pip:
```
$ python --version

C:\Python27\Scripts>python --version
Python 2.7.14
```
```
$ pip --version
pip 9.0.1 from c:\python27\lib\site-packages (python 2.7)
```
- If there dont have, install separately: [Install pip](https://pip.pypa.io/en/stable/installing/)

## 4. Introduce pipenv: Problems that Pipenv solves
### 4.1 Dependency Management with requirements.txt
- Imagine you work with **flask** So you decide to include the flask dependency in a requirements.txt file:
```
flask
```
> The above requirements.txt file doesn’t specify which version of flask to use\
	In this case, pip install -r requirements.txt will install the latest version by default.\
	This is okay unless there are interface or behavior changes in the newest version that break our application.\
	=> compatible issue headache 

- So, to fix things, you try to be a little more specific in your requirements.txt. You add a version specifier to the flask dependency. This is also called pinning a dependency:
```
flask==0.12.1
```

> Keep in mind that ***flask itself has dependencies as well (which pip installs automatically)***.\
  However, flask itself **doesn’t specify exact versions for its dependencies.**\
  For example, it allows any version of Werkzeug>=0.14.\
  Again, for the sake of this example, let’s say a new version of *Werkzeug=1.12* got released, but it ***introduces a show-stopper bug to your application.***

 > When you do pip install -r requirements.txt in production this time, you will get flask==0.12.1 since you’ve pinned that requirement. However, unfortunately, you’ll get the latest, buggy version of Werkzeug. Again, the product breaks.

 - The real issue here is that ***the build isn’t deterministic***. What I mean by that is that, given the same input (the requirements.txt file), *pip doesn’t always produce the same environment*. At the moment, *you can’t easily replicate the exact environment you have on your development machine in production*.
 	- The typical solution to this problem is to use `pip freeze`. This command allows you to get exact versions for all 3rd party libraries currently installed, including the sub-dependencies pip installed automatically. 
```
Executing pip freeze results in pinned dependencies you can add to a requirements.txt:
click==6.7
Flask==0.12.1
itsdangerous==0.24
Jinja2==2.10
MarkupSafe==1.0
Werkzeug==0.14.1
```

- **Big Fact**
```
The truth is that you really don’t care what version of Werkzeug gets installed as long as it doesn’t break your code. In fact, you probably want the latest version to ensure that you’re getting bug fixes, security patches, new features, more optimization, and so on.
```

## 5. Pipenv Introduction
Now that we’ve addressed the problems, let’s see how Pipenv solves them.

First, let’s install it:
```
$ pip install pipenv
```
Once you’ve done that, you can effectively forget about pip since Pipenv essentially acts as a replacement. 

It also introduces two new files:
> the ***Pipfile*** (which is meant **to replace requirements.txt**) 

> And the ***Pipfile.lock*** (which enables deterministic builds).

Pipenv uses pip and virtualenv under the hood but simplifies their usage with a single command line interface.

### 5.1 Pipfile and pipfile.lock

***Pipfile*** will be superior to ***requirements.txt*** file in a number of ways:

- [TOML](https://github.com/toml-lang/toml) syntax for declaring all types of Python dependencies.
- One Pipfile (as opposed to multiple requirements.txt files).
	- Existing requirements files tend to proliferate into multiple files - e.g. dev-requirements.txt, test-requirements.txt, etc. - but a Pipfile will allow seamlessly ***specifying groups of dependencies in one place.***
	- This will be surfaced as **only two built-in groups *(default & development)***. (see note below)
- Fully specified (and deterministic) environments in the form of **Pipfile.lock**. A deployed application can then be completely redeployed with the same exact versions of all recursive dependencies, by referencing the Pipfile.lock file.

The concrete requirements for a Python Application would come from Pipfile. This would include where the packages should be fetched from and their loose version constraints.

The details of the environment (all installed packages with pinned versions and other details) would be stored in Pipfile.lock, for reproducibility. This file will be automatically generated and should not be modified by the user.

### 5.2. Feature
- Enables truly deterministic builds, while easily specifying only what you want.
- Generates and checks file hashes for locked dependencies.
- Automatically install required Pythons, if pyenv is available.
- Automatically finds your project home, recursively, by looking for a **Pipfile.**
- Automatically generates a Pipfile, if one doesn’t exist.
- Automatically creates a ***virtualenv in a standard location.***
- Automatically adds/removes packages to a Pipfile when they are un/installed.
- Automatically loads .env files, if they exist.

### 5.3. Basic Concept:
- A virtualenv will automatically be created, when one doesn’t exist.
- When no parameters are passed to install, all packages [packages] specified will be installed.
- To initialize a Python 3 virtual environment, run `$ pipenv --three.`
- To initialize a Python 2 virtual environment, run `$ pipenv --two.`
- Otherwise, whatever virtualenv defaults to will be the default.

### 5.4. Pipenv workflow: [Installing pipenv](https://docs.pipenv.org/install/#installing-pipenv)

#### 5.4.1. Check installed at local machine
- Check python and pip installed:
```
$ python --version
$ pip --version
```
- Install pipenv:
```
$ pip install --user pipenv
```
- Upgrade pipenv:
```
$ pip install --user --upgrade pipenv
```
- Clone / create project repository:
```
…
$ cd myproject
```

#### 5.4.2 Install from Pipfile, if there is one:
```
$ pipenv install
```
- Specifying Versions of a Package `$ pipenv install requests==2.13.0`
	- => This will update your Pipfile to reflect this requirement, automatically.

- Specifying Versions of Python
To create a new virtualenv, using a specific version of Python you have installed (and on your PATH), use the --python VERSION flag, like so:

```
Use Python 3:
$ pipenv --python 3

Use Python3.6:
$ pipenv --python 3.6

Use Python 2.7.14:
$ pipenv --python 2.7.14
```
> When given a Python version, like this, **Pipenv will automatically scan your system for a Python that matches that given version**.


#### 5.4.3 Or, add a package to your new project:

- Installing packages for your project
```
$ cd myproject
$ pipenv install <package>
```
- Specifying Versions of a Package `$ pipenv install requests==2.13.0`
	
> This will create new files, **Pipfile**, in your project directory, and a *new virtual environment* for your project if it doesn’t exist already. If you add the **--two or --three flags** to that last command above, *it will initialise your project to use Python 2 or 3*, respectively. *Otherwise the default version of Python will be used*.

```
Creating a Pipfile for this project...
Creating a virtualenv for this project...
Using base prefix '/usr/local/Cellar/python3/3.6.2/Frameworks/Python.framework/Versions/3.6'
New python executable in ~/.local/share/virtualenvs/tmp-agwWamBd/bin/python3.6
Also creating executable in ~/.local/share/virtualenvs/tmp-agwWamBd/bin/python
Installing setuptools, pip, wheel...done.

Virtualenv location: ~/.local/share/virtualenvs/tmp-agwWamBd
Installing requests...
Collecting requests
  Using cached requests-2.18.4-py2.py3-none-any.whl
Collecting idna<2.7,>=2.5 (from requests)
  Using cached idna-2.6-py2.py3-none-any.whl
Collecting urllib3<1.23,>=1.21.1 (from requests)
  Using cached urllib3-1.22-py2.py3-none-any.whl
Collecting chardet<3.1.0,>=3.0.2 (from requests)
  Using cached chardet-3.0.4-py2.py3-none-any.whl
Collecting certifi>=2017.4.17 (from requests)
  Using cached certifi-2017.7.27.1-py2.py3-none-any.whl
Installing collected packages: idna, urllib3, chardet, certifi, requests
Successfully installed certifi-2017.7.27.1 chardet-3.0.4 idna-2.6 requests-2.18.4 urllib3-1.22

Adding requests to Pipfile's [packages]...
P.S. You have excellent taste!
```

#### 5.4.4 Next, activate the Pipenv shell:
- Activate the shell:
```
$ pipenv shell
```

#### 5.4.5 After finish run the code:
- Test to run the code: run a given command from the virtualenv
```
$ pipenv run test.py
```

#### 5.4.6. Environment Management with Pipenv:
The three primary commands you’ll use in managing your pipenv environment are `$ pipenv install, $ pipenv uninstall, and $ pipenv lock.`

##### 5.4.6.1. $ pipenv install
- $ pipenv install is used for *installing packages into the pipenv virtual environment* and *updating your Pipfile*.

Along with the basic install command, which takes the form:
```
$ pipenv install [package names]
```

- The user can provide these additional parameters:
```
--two — Performs the installation in a virtualenv using the system python2 link.
--three — Performs the installation in a virtualenv using the system python3 link.
--python — Performs the installation in a virtualenv using the provided Python interpreter.
```
> Warning\
None of the above commands should be used together. They are also destructive and will delete your current virtualenv before replacing it with an appropriately versioned one.

##### 5.4.6.2. $ pipenv uninstall
-- $ pipenv uninstall supports all of the parameters in pipenv install, as well as two additional options, --all and --all-dev.
```
pipenv uninstall [OPTIONS] [PACKAGE_NAME] [MORE_PACKAGES]...
```
```
--all — This parameter will purge all files from the virtual environment, but leave the Pipfile untouched.
--all-dev — This parameter will remove all of the development packages from the virtual environment, and remove them from the Pipfile.
```

##### 5.4.6.3. $ pipenv lock
- $ pipenv lock is used to ***create a Pipfile.lock***, which declares all dependencies (and sub-dependencies) of your project, their latest available versions, and the current hashes for the downloaded files. This ensures repeatable, and most importantly deterministic, builds.

#### 5.4.7. Show a dependency graph:
- graph will show you a dependency graph of your installed dependencies.
```
$ pipenv graph
requests==2.18.4
  - certifi [required: >=2017.4.17, installed: 2017.7.27.1]
  - chardet [required: >=3.0.2,<3.1.0, installed: 3.0.4]
  - idna [required: >=2.5,<2.7, installed: 2.6]
  - urllib3 [required: <1.23,>=1.21.1, installed: 1.22]
```

## Pipfile Example: [Pipfile](https://github.com/pypa/pipfile/blob/master/examples/Pipfile)
- Check Pipfile

```
$ cat Pipfile
```
```
Pipfile
[[source]]
url = 'https://pypi.python.org/simple'
verify_ssl = true
name = 'pypi'

[requires]
python_version = '2.7'

[packages]
requests = { extras = ['socks'] }
records = '>0.5.0'
django = { git = 'https://github.com/django/django.git', ref = '1.11.4', editable = true }
"e682b37" = {file = "https://github.com/divio/django-cms/archive/release/3.4.x.zip"}
"e1839a8" = {path = ".", editable = true}
pywinusb = { version = "*", os_name = "=='nt'", index="pypi"}

[dev-packages]
nose = '*'
unittest2 = {version = ">=1.0,<3.0", markers="python_version < '2.7.9' or (python_version >= '3.0' and python_version < '3.4
```

## Pipfile.lock Example: [Pipfile.lock](https://github.com/pypa/pipfile/blob/master/examples/Pipfile.lock)

- check Pipfile.lock:
```
$ cat Pipfile.lock
```

```

Pipfile.lock
{
    "_meta": {
        "hash": {
            "sha256": "09da36fcc93fa9b94fbea5282d8206a9d2e13fcec27229ec62c16c134e3e760a"
        },
        "host-environment-markers": {
            "implementation_name": "cpython",
            "implementation_version": "0",
            "os_name": "posix",
            "platform_machine": "x86_64",
            "platform_python_implementation": "CPython",
            "platform_release": "17.0.0",
            "platform_system": "Darwin",
            "platform_version": "Darwin Kernel Version 17.0.0: Thu Aug 24 21:48:19 PDT 2017; root:xnu-4570.1.46~2/RELEASE_X86_64",
            "python_full_version": "2.7.14",
            "python_version": "2.7",
            "sys_platform": "darwin"
        },
        "pipfile-spec": 6,
        "requires": {
            "python_version": "2.7"
        },
        "sources": [
            {
                "name": "pypi",
                "url": "https://pypi.python.org/simple",
                "verify_ssl": true
            }
        ]
    },
    "default": {
        "certifi": {
            "hashes": [
                "sha256:54a07c09c586b0e4c619f02a5e94e36619da8e2b053e20f594348c0611803704",
                "sha256:40523d2efb60523e113b44602298f0960e900388cf3bb6043f645cf57ea9e3f5"
            ],
            ....
     "develop": {
     "argparse": {
         "hashes": [
             "sha256:c31647edb69fd3d465a847ea3157d37bed1f95f19760b11a47aa91c04b666314",
             "sha256:62b089a55be1d8949cd2bc7e0df0bddb9e028faefc8c32038cc84862aefdd6e4"
         ],
         "version": "==1.4.0"
     },

     ...
```

=====================================================================================

[Reference PIPENV](https://docs.pipenv.org/)