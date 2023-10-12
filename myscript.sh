scanList = $(gh api \
        -H "Accept: application/vnd.github+json" \
        -H "X-GitHub-Api-Version: 2022-11-28" \
        /repos/anauskadutta/sample1/code-scanning/alerts)

echo "The list of code scan alerts is as follows: $scanList"
