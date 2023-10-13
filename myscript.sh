# scanJson=$(gh api \
#         -H "Accept: application/vnd.github+json" \
#         -H "X-GitHub-Api-Version: 2022-11-28" \
#         /repos/anauskadutta/sample1/code-scanning/alerts)

# echo "The list of code scan alerts is as follows: $scanJson"

bodyList=$(gh api \
        -H "Accept: application/vnd.github+json" \
        -H "X-GitHub-Api-Version: 2022-11-28" \
        /repos/anauskadutta/sample1/issues \
        --jq '.[].body')

echo "List of GitHub Issue Body Contents: $bodyList"

# for alert in $(echo "$scanJson" | jq -r '.[] | @base64'); do
#         _jq() {
#                 echo ${alert} | base64 --decode | jq -r ${1}
#         }
#         state=$(_jq '.state')
#         # echo "Alerts are printed here: $alert"
#         # state=$(echo $alert | jq -r '.state')
#         # echo "State: $state"
#         if [[ "$state" == "open" ]]; then
#                 issueTitle="$(_jq '.most_recent_instance.message.text')"
#                 issueBody=$(_jq '.html_url')
#                 echo "State: $state"
#                 echo "Title: $issueTitle"
#                 echo "Body: $issueBody"
#                 if [[ "$issueBody" in $bodyList ]]; then
#                         echo "Issue already exists"
#                 else
#                         ghIssue=$(gh issue create --title "$issueTitle" --body "$issueBody")
#                         echo "GitHub issue created: $ghIssue"
#                 fi
#         fi
# done
