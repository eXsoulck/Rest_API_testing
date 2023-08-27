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
                sh 'python -m venv venv'
                sh 'source venv/bin/activate'
                sh 'venv/bin/python -m pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'venv/bin/python -m pytest'
            }
        }
    }
}