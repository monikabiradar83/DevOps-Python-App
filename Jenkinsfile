pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t flask-app .'
            }
        }

        stage('Run Container') {
            steps {
                bat 'docker rm -f flask-container || exit 0'
                bat 'docker run -d -p 5000:5000 --name flask-container flask-app'
            }
        }
    }
}