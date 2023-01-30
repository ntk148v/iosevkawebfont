#!/bin/bash
###################
# Partial commits #
###################
# Group untracked files by level 2 directory
# For example:
# latest/iosevka
# latest/iosevka-term
# ...
untracked_dirs=$(git ls-files --others --exclude-standard latest | cut -d/ -f-2 | uniq)
while IFS= read -r dir; do
    echo "* Commit directory $dir"
    git add $dir
    git commit -m "Add directory/file $dir"
done < <(printf '%s\n' "$untracked_dirs")

################
# Partial push #
################
# Adjust the following variables as necessary
REMOTE="${1:-origin}"
BRANCH="${2:-$(git rev-parse --abbrev-ref HEAD)}"
BATCH_SIZE="${3:-5}"

echo $REMOTE

# check if the branch exists on the remote
if git show-ref --quiet --verify refs/remotes/$REMOTE/$BRANCH; then
    # if so, only push the commits that are not on the remote already
    range=$REMOTE/$BRANCH..HEAD
else
    # else push all the commits
    range=HEAD
fi
# count the number of commits to push
n=$(git log --first-parent --format=format:x $range | wc -l)

# push each batch
for i in $(seq $n -$BATCH_SIZE 1); do
    # get the hash of the commit to push
    h=$(git log --first-parent --reverse --format=format:%H --skip $i -n1)
    echo "* Push $h..."
    git push $REMOTE ${h}:refs/heads/$BRANCH
done
# push the final partial batch
git push $REMOTE HEAD:refs/heads/$BRANCH
