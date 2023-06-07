pipeline {
    agent any

    stages {
        stage('Pytest') {
            steps {
                sh("${JENKINS_HOME}/scripts/pytest.sh ${WORKSPACE}")
            }
        }
		
        stage('Email Notification') {
            steps {
                mail(body: "${JOB_NAME}, build ${BUILD_NUMBER} Pytest completed.", subject: 'Pytest completed.', to: 'behai_nguyen@hotmail.com')
            }
        }		
    }
}
