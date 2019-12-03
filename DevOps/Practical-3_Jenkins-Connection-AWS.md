## Connecting Jenkins master with Slave Machine (AWS):

### Pre-requisites:

- Virtual machines ( 2 EC2 instance on AWS)  with CentOS installed
- Permission to execute root commands
- Putty Client (optional but preferred)

Install the jenkins on a EC2 instance and we call it *Jenkins_Master* and the other EC2 instance as Agent:

There are multiple ways to connect the jenkins server with slave node like using SSH, Windows admin account & JNLP. We are using the SSH method for the connection.

## Setup Agent

Login to ***Agent*** EC2 instance using the putty terminal and login as root

```
[ec2-user@ip-172-31-21-45 ~]# sudo su
```

Install the java version:

```
[root@ip-172-31-21-45 ~]# yum -y update
[root@ip-172-31-21-45 ~]# yum install -y java-1.8.0-openjdk
[root@ip-172-31-21-45 ~]# java -version
```

Add the jenkins user:

```
[root@ip-172-31-21-45 ~]# useradd -m -s /bin/bash jenkinspasswd Jenkins
[root@ip-172-31-21-45 ~]# passwd Jenkins
```

Enter the password for jenkins user as prompted as ***jenki_hcl***

Enable the password authentication method in the sshd_config file:

```
[root@ip-172-31-21-45 ~]# sudo vim /etc/ssh/sshd_config
```

Change the password authentication from 

**PasswordAuthentication no**

to 

**PasswordAuthentication yes**

Restart the sshd service:

```
[root@ip-172-31-21-45 ~]# sudo service sshd restart
```

Reference: https://aws.amazon.com/premiumsupport/knowledge-center/ec2-password-login/

### Setup Jenkins_Master

Login to ***Jenkins_Master*** using the putty terminal and login as root

```
[ec2-user@ip-172-31-11-45 ~]$ sudo su
[root@ip-172-31-11-45 ec2-user]# sudo vim /etc/passwd
```

Change the last line of file from **/bin/false** to **/bin/bash**

```jenkins:x:996:994:Jenkins Automation Server:/var/lib/jenkins:/bin/bash```

Save the changes and exit the editor:

```
[root@ip-172-31-11-45 ec2-user]# su - jenkins
```

Generate the ssh public/private key pair to communicate:

```
-bash-4.2$ mkdir ~/.ssh && cd ~/.ssh
-bash-4.2$ ssh-keygen
```

It will generate the keys in the directory /var/lib/jenkins/.ssh/id_rsa (Private Key) & /var/lib/jenkins/.ssh/id_rsa.pub as public key.

### Copy the SSH Key from Master to Agent

Upload the key **id_rsa.pub** from the master to agent nodes assuming *172.31.21.45* is IP of Agent instance.

```
-bash-4.2$ ssh-copy-id jenkins@172.31.21.45
```

Type the Jenkins user password as  ***jenki_hcl***

View the private key generated **id_rsa** and paste in notepad.

```
-bash-4.2$ less ~/.ssh/id_rsa
```

Starts with ----- BEGIN RSA PRIVATE KEY------- and ends with ---- ENDS RSA PRIVATE KEY -----------. Copy the content including the commenting lines.

### Setup Credentials on Jenkins

Open your Jenkins dashboard and click on the '**Credentials**' menu on the left and click the '**global**' domain link. Click on '**Add Credentials**'.

In the authentication method choose:

- Kind: SSH Username with private key
- Scope: Global
- Username: jenkins
- Private key: Paste the **id_rsa** private key of Jenkins user from the master server which we copied in last step.

Click 'OK'.



## Add New Slave Nodes

On the Jenkins dashboard, click the **Manage Jenkins** menu, and click **Manage Nodes**

Click the 'New Node'.

Type the node name ***slave01***, choose the **permanent agent**, and click 'OK'.

Some information details.

- Description: slave01 node agent server
- Remote root directory: /home/jenkins
- Labels: slave01
- Launch method: Launch slave agent via SSH, type the host ip address of Agent *172.31.21.45*, choose the authentication using 'Jenkins' credential.

Now click 'Save' button and wait for the master server to connect to all agent nodes and launch the agent services.

Jenkins slave nodes has been added to the master server.