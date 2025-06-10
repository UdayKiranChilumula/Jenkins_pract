pipeline {
    agent any

    stages {
        stage('Storing sensitive info') {
            steps {
                sh '''
                    echo 'This is a highly sensitive info' > secrets.log
                '''
            }
        }
        
    }
    post{
        always{
            archiveArtifacts artifacts : "*.log"
            sh '''
                rm -rf secret.log
            '''
        }
        failure{
            echo 'this will execute as we caused a failre'
        }
        success{
            echo 'this wont execute as one of the stage is failed'
        }
    }
}