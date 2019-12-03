### Installation of packages:

#### Creation of Virtual Environment

Python3 has added the feature of adding up a virtual environment, in order to maintain the multiple applications based on python using the same packages with different versions.

```cd CurdWithDjango```

``` python -m venv venv```

Above command will create the **venv**, virtual environment and all packages can be installed with version will remain in the working directory.

#### Installation of Packages:

Python packages are installed using the PiP named as Python Packaging Index using the install command as:

Create a new file **requirements.txt**, containing package name & version(optional) required by application.

**requirements.txt** (Source: filehandling)

`openpyxl`

**Command**

``` pip install -r requirements.txt ```