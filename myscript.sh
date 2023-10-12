scanList=$(gh api \
        -H "Accept: application/vnd.github+json" \
        -H "X-GitHub-Api-Version: 2022-11-28" \
        /repos/anauskadutta/sample1/code-scanning/alerts)

echo "The list of code scan alerts is as follows: $scanList"

for alert in $scanList; do
        # state=${alert.state}
        state=$($alert | jq '.state' --raw-output)
        echo "State: $state"
        # if [ $state=="open" ]; then
        #         issueTitle=${alert.most_recent_instance.message.text}
        #         echo "Title: $issueTitle"
        #         # gh issue create --title $issueTitle
        #         # echo "GitHub issue created"
        # fi
done
