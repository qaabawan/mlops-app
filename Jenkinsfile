pipeline {
    agent any

    environment {
        DOCKER_USER = 'kaabmalik'
        IMAGE_NAME  = 'mlops-app'
    }

    stages {
        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${IMAGE_NAME} ."
            }
        }

        stage('Tag & Push to Docker Hub') {
            steps {
                sh "docker tag ${IMAGE_NAME} ${DOCKER_USER}/${IMAGE_NAME}:latest"
                sh "docker push ${DOCKER_USER}/${IMAGE_NAME}:latest"
            }
        }

        stage('Automated Deployment') {
            steps {
                sh "docker stop ${IMAGE_NAME} || true"
                sh "docker rm ${IMAGE_NAME} || true"
                sh "docker run -d -p 80:80 --name ${IMAGE_NAME} ${DOCKER_USER}/${IMAGE_NAME}:latest"
            }
        }
    }
}
