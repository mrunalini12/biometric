pipeline {
    agent any

    stages {
        stage('Prepare Environment') {
            steps {
                script {
                    // Create a virtual environment
                    sh 'python3 -m venv venv'
                    
                    // Activate the virtual environment and install packages
                    sh '''
                        source venv/bin/activate
                        pip install speechrecognition opencv-python
                    '''
                }
            }
        }
        stage('Run Voice Authentication') {
            steps {
                script {
                    // Activate the virtual environment and run the script
                    sh '''
                        source venv/bin/activate
                        python3 voice_auth.py
                    '''
                }
            }
        }
        stage('Run Iris Authentication') {
            steps {
                script {
                    // Activate the virtual environment and run the script
                    sh '''
                        source venv/bin/activate
                        python3 iris_auth.py
                    '''
                }
            }
        }
    }
}
