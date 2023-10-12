scanJson=$(gh api \
        -H "Accept: application/vnd.github+json" \
        -H "X-GitHub-Api-Version: 2022-11-28" \
        /repos/anauskadutta/sample1/code-scanning/alerts)

echo "The list of code scan alerts is as follows: $scanJson"

alertList=$(echo "$scanJson" | jq -c -r '.[]')

for alert in ${alertList[@]}; do
        # echo "Alerts are printed here: $alert"
        state=$(echo "$alert" | jq '.state' --raw-output)
        # echo "State: $state"
        # if [ $state=="open" ]; then
        #         issueTitle=${alert.most_recent_instance.message.text}
        #         echo "Title: $issueTitle"
        #         # gh issue create --title $issueTitle
        #         # echo "GitHub issue created"
        # fi
done
