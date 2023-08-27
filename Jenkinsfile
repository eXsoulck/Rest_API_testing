pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url:'https://github.com/eXsoulck/JSON_API_with_allure'
            }
        }
        stage('Setup environment') {
            steps {
                sh 'python -m pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'python -m pytest'
            }
        }
    }
}