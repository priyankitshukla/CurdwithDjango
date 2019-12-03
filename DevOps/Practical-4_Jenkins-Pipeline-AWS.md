## Deployment on EC2 instance:

Access the web interface of Jenkins CI server by going to the following web address using Google Chrome.

```
http://13.12.23.23:8080
```

Enter the username and password for the user created after installing Jenkins **admin/admin@hcl**

On left side, click on **New Item**, and Enter the name as **DeployPython** by selecting as **Pipeline**.

Click on **Configure** to start writing the pipeline.

In the **General section**, check the **GitHub project** and enter the URL as https://github.com/priyankitshukla/CurdwithDjango/.

In **Build Triggers section**, check the **Build periodically** and enter as 

```H * * * *  ```

It will cause the pipeline to trigger every hour.

In the **Pipeline section**, select the **Pipeline script** from the dropdown option.

Copy and paste the pipeline script:

```
node {
 node('slave01') {

  stage('Checkout code') {
   echo 'Checkout code from GitHub'
   git 'https://github.com/priyankitshukla/CurdwithDjango.git'
  }

  stage('Installing the required plugins') {
   dir(workspace) {
    echo 'Setting up the virtual environment and installing plugins'
    sh ''#!/bin/bash
    python3 - m venv venv
    chmod + x. / venv / bin / activate
    source. / venv / bin / activate
    pip3 install - r requirements.txt 
    '''
   }

  }

  stage('Running the test cases of application') {
   dir(workspace) {
    echo 'Executing the test cases'
    sh 'python3 -m unittest'
   }
  }

  stage('Running the application') {
   dir(workspace) {
    echo 'Running the application'
    sh '''
    python3 manage.py makemigrations
    python3 manage.py migrate
    python3 manage.py runserver ''
    '''
   }
  }

 }
}
```



