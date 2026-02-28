pipeline{
    agent any
    environment{
        U_NAME = "chandansingh95"
        IMAGE_NAME= "python-to-do-app"
        CONTAINER_NAME = "MyToDoApp"

    }
    stages{
        stage("Checkout"){ //This is for checkout.
            steps{
                git branch: 'main', url: 'https://github.com/chandank99/to-do-project.git'
            }
        }
        stage("prepare python"){ // To run the code locally.
            steps{
                sh '''
                pyhton3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }
        stage("Build the docker image"){
            steps{
                sh "docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} ."
        
            }
        }
        stage("Docker Login and Push Image"){
            steps{
                withCredentials([usernamePassword(credentialsId: 'DockerHub', passwordVariable: 'password_docker', usernameVariable: 'username_docker')]) {
                  sh "echo $password_docker | docker login -u $username_docker --password-stdin"
                  sh "docker tag ${IMAGE_NAME}:${BUILD_NUMBER} ${U_NAME}/${IMAGE_NAME}:${BUILD_NUMBER}"
                  sh "docker push ${U_NAME}/${IMAGE_NAME}:${BUILD_NUMBER}"
                }
            }
        }
        stage("Deploy and Run"){
            steps{
                sh "docker stop ${CONTAINER_NAME} || true "
                sh "docker rm ${CONTAINER_NAME} || true "
                sh " docker run -d --name ${CONTAINER_NAME} -p 8000:8000 ${U_NAME}/${IMAGE_NAME}:${BUILD_NUMBER}"
        
            }
        }
    }
}