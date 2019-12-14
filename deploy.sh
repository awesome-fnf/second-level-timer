#!/bin/bash

display_help() {
    echo "Usage: " >&2
    echo
    echo "Action=            create or update"
    echo "RandomSuffix=      User defined suffix"
    echo "Duration=          Second level duration"
    echo "Input=             Target function event"
    echo "ResourceArn=       Target function resource arn"
    echo "StackId=           If action is 'update' must set this"
    echo "Poject=            sls project"
    echo "Logstore=          sls logstore"
    echo " ./deploy.sh"
    echo 
}

run() {
    StackName=${StackName:-stack-fnf-timer-test}
    Action=${Action:-create}
    RandomSuffix=${RandomSuffix:-test}
    Duration=${Duration:-1}

    params="--TimeoutInMinutes 10 \
            --Parameters.2.ParameterKey RandomSuffix \
            --Parameters.2.ParameterValue $RandomSuffix \
            --Parameters.3.ParameterKey Duration \
            --Parameters.3.ParameterValue $Duration
            --Parameters.4.ParameterKey Project \
            --Parameters.4.ParameterValue $Project \
            --Parameters.5.ParameterKey Logstore \
            --Parameters.5.ParameterValue $Logstore \
            "
    
    if [[ ! $ResourceArn == '' ]]; then
        echo "Target function: ", $ResourceArn
        params+="--Parameters.6.ParameterKey ResourceArn \
                --Parameters.6.ParameterValue $ResourceArn "
    fi

    if [[ $Action == "create" ]]; then
        aliyun ros CreateStack --StackName $StackName $params --TemplateBody "$(cat ./ros.yml)" \
            --Parameters.1.ParameterKey Input \
            --Parameters.1.ParameterValue "$Input"

    elif [[ $Action == "update" ]]; then
        aliyun ros UpdateStack --StackId $StackId $params --TemplateBody "$(cat ./ros.yml)" \
            --Parameters.1.ParameterKey Input \
            --Parameters.1.ParameterValue "$Input"
    fi
}
 
case $1 in
    -h) display_help;;
    help) display_help;;
    *) run $@;;
esac

