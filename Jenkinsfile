pipeline {
    agent any

    stages {
        stage('Voice Authentication') {
            steps {
                script {
                    def result = sh(script: 'python3 voice_auth.py', returnStatus: true)
                    if (result != 0) {
                        error("Voice authentication failed!")
                    }
                }
            }
        }

        stage('Iris Authentication') {
            steps {
                script {
                    def result = sh(script: 'python3 iris_auth.py', returnStatus: true)
                    if (result != 0) {
                        error("Iris authentication failed!")
                    }
                }
            }
        }

        stage('Build') {
            steps {
                echo 'Building...'
                // Your build steps here
            }
        }
    }
}
