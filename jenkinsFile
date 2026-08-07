pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code from Git'
                checkout scm
            }
        }
        stage('Build') {
            steps {
                echo 'Building the application'
                sh 'echo Build step running...'
                // Replace with: sh 'mvn -B clean package'
            }
        }
        stage('Test') {
            steps {
                echo 'Running automated tests'
                sh 'echo Test step running...'
                // Replace with: sh 'mvn test'
            }
        }
        stage('Package') {
            steps {
                echo 'Packaging build artifact'
                sh 'echo Packaging complete'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully.'
        }
        failure {
            echo 'Pipeline failed. Check console output.'
        }
    }
}
