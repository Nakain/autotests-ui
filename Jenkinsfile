pipeline {
        agent any

        environment {
            PYTHON   = 'C:/Users/Personal Computer/jenkins/autotests-venv/Scripts/python.exe'
            UI_COV   = 'C:/Users/Personal Computer/jenkins/autotests-venv/Scripts/ui-coverage-tool.exe'
            PLAYWRIGHT_BROWSERS_PATH = 'C:/Users/Personal Computer/AppData/Local/ms-playwright'
        }

        options {
            timestamps()
            buildDiscarder(logRotator(numToKeepStr: '20'))

        }

        stages {
            stage('Run tests') {
                steps {
                    withEnv(['APP_URL=https://nikita-filonov.github.io/qa-automation-engineer-ui-course',
                             'HEADLESS=true',
                             'BROWSERS=["chromium"]',
                             'TEST_USER.USERNAME=username',
                             'TEST_DATA.IMAGE_PNG_FILE=./testdata/files/image.png',
                             'UI_COVERAGE_APPS=[{"key":"ui-course","url":"https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login","name":"UI Course","tags":["UI","COURSES"],"repository":"https://github.com/Nakain/autotests-ui"}]',
                             'UI_COVERAGE_HTML_REPORT_FILE=./coverage.html']) {
                        withCredentials([usernamePassword(credentialsId: 'autotests-user',
                                                           usernameVariable: 'TEST_USER.EMAIL',
                                                           passwordVariable: 'TEST_USER.PASSWORD')]) {
                            bat '"%PYTHON%" -m pytest -m regression --junitxml=report.xml --alluredir=./allure-results --numprocesses 2'
                        }
                    }
                }
            }

            stage('Coverage report') {
                steps {
                    withEnv(['UI_COVERAGE_APPS=[{"key":"ui-course","url":"https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login","name":"UI Course","tags":["UI","COURSES"],"repository":"https://github.com/Nakain/autotests-ui"}]',
                             'UI_COVERAGE_HTML_REPORT_FILE=./coverage.html']) {
                        bat '"%UI_COV%" save-report'
                    }
                }
            }

            stage('Publish') {
                steps {
                    junit allowEmptyResults: true, testResults: 'report.xml'
                    allure results: [[path: 'allure-results']]
                }
            }
        }

        post {
            always {
                archiveArtifacts artifacts: 'report.xml, allure-results/**, coverage.html, coverage-history.json, coverage-report.json',
                                 allowEmptyArchive: true
            }
        }
    }