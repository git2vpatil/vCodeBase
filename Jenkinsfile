pipeline {
    agent any
    stages {
        stage('Pylint/PEP8 Analysis') {
            steps {
                bat 'pylint --output-format=parseable --msg-template="{path}:{line}: [{msg_id}({symbol}), {obj}] {msg}" --rcfile src/conf/config.pylintrc %WORKSPACE% >lint1.log | exit 0'
                bat 'pep8 --config src/conf/config.pep8  . >peplint1.log | exit 0'
                step([
                        $class: 'WarningsPublisher',
                        parserConfigurations: [[
                            parserName: 'Pylint',
                            pattern: 'lint1.log']],
                        unstableTotalAll           : '0',
                        usePreviousBuildAsReference: true
                    ])
                step([
                        $class: 'WarningsPublisher',
                        parserConfigurations: [[
                            parserName: 'Pep8',
                            pattern: 'peplint1.log']],
                        unstableTotalAll           : '0',
                        usePreviousBuildAsReference: true
                    ])
                bat 'echo "BUILD END"'
            }
        }
    }
}