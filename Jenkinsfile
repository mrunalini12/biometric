pipeline {
    agent any

    stages {
        stage('Prepare Environment') {
            steps {
                script {
                    // Install system dependencies
                    sh 'sudo apt-get update'
                    sh 'sudo apt-get install -y python3-pip portaudio19-dev'

                    // Create a virtual environment
                    sh 'python3 -m venv venv'
                    
                    // Activate the virtual environment and install packages
                    sh '''
                        source venv/bin/activate
                        pip install speechrecognition opencv-python pyaudio
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
