scanJson=$(gh api \
        -H "Accept: application/vnd.github+json" \
        -H "X-GitHub-Api-Version: 2022-11-28" \
        /repos/anauskadutta/sample1/code-scanning/alerts)

echo "The list of code scan alerts is as follows: $scanJson"

for alert in $(echo "$scanJson" | jq -r '.[] | @base64'); do
        _jq() {
                echo ${alert} | base64 --decode | jq -r ${1}
        }
        state=$(_jq '.state')
        # echo "Alerts are printed here: $alert"
        # state=$(echo $alert | jq -r '.state')
        echo "State: $state"
        if [[ "$state" == "open" ]]; then
                issueTitle="$(_jq '.most_recent_instance.message.text')"
                issueBody=$(_jq '.instances_url')
                echo "Title: $issueTitle"
                echo "Body: $issueBody"
                # ghIssue=$(gh issue create --title $issueTitle --body $issueBody)
                # echo "GitHub issue created: $ghIssue"
        fi
done
