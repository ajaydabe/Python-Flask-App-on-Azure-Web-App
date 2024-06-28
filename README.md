# Python-Flask-App-on-Azure-Web-App-Triluxo-Tech

Deploying a basic Flask application on Azure Web App with a CI/CD pipeline using GitHub Actions.

### Web App Service - simplepythonflaskapp

Create a Web App Service using below configurations:

![image](https://github.com/ajaydabe/Python-Flask-App-on-Azure-Web-App-Triluxo-Tech/assets/160045230/1f440dd8-0e4b-47ad-9a63-f1352710200c)

Add the GitHub account and repository details as shown below

![image](https://github.com/ajaydabe/Python-Flask-App-on-Azure-Web-App-Triluxo-Tech/assets/160045230/8b06494e-27a1-4363-968e-247b0d97ca63)


#### Overview

We will get the **Domain** using which we can reach out to our application.

We can use the **Browse** option to see our application.

![image](https://github.com/ajaydabe/Python-Flask-App-on-Azure-Web-App-Triluxo-Tech/assets/160045230/2156909f-fc9a-4430-8bf8-590b62914214)

#### Deployment --> Deployment Center

![image](https://github.com/ajaydabe/Python-Flask-App-on-Azure-Web-App-Triluxo-Tech/assets/160045230/84160899-76ab-4126-aae9-a21daa089851)

#### Deployment --> Deployment Center --> Logs

![image](https://github.com/ajaydabe/Python-Flask-App-on-Azure-Web-App-Triluxo-Tech/assets/160045230/a54f571d-0a6f-46be-aadc-cb56c046177d)

#### GitHub Repository --> Actions

If our configurations are correct in Azure Web App, it will successfully create a workflow as shown below and also save that in repository at /.github/workflow directory.

![image](https://github.com/ajaydabe/Python-Flask-App-on-Azure-Web-App-Triluxo-Tech/assets/160045230/e0796ff2-0768-4db4-a9cc-93f4ec103147)

As you can see below, copy domain and paste on browser to check if app is working or not.

![image](https://github.com/ajaydabe/Python-Flask-App-on-Azure-Web-App-Triluxo-Tech/assets/160045230/08b1c640-aec3-439b-a739-33e448958e86)

When push is made to the GitHub repository, deployment will get started and changes will be deployed on the App.
