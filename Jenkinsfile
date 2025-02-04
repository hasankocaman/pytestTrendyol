pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Setup Python Environment') {
            steps {
                bat '''
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }
        
        stage('Run Tests') {
            steps {
                bat '''
                    set PYTHONPATH=%WORKSPACE%
                    pytest tests/test_trendyol.py -v --junitxml=test-results.xml --html=test-report.html --self-contained-html
                '''
            }
        }
    }
    
    post {
        always {
            junit '**/test-results.xml'
            publishHTML([
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: '.',
                reportFiles: 'test-report.html',
                reportName: 'HTML Test Report'
            ])
        }
    }
}
