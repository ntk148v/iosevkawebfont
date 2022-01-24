#!/bin/bash
# Get release
repo="be5invis/Iosevka"
latest_release=$(curl --silent "https://api.github.com/repos/$repo/releases/latest" | grep -Po '"tag_name": "\K.*?(?=")')
latest_release_num_only=${latest_release/v/""}
# Check directory exists
current_release=$(cat LATEST_RELEASE)
if [[ "${current_release}" == "${latest_release_num_only}" ]]; then
    echo "Repository is up-to-date"
    exit 0
fi
# Get release
curl -L https://github.com/be5invis/Iosevka/releases/download/${latest_release}/webfont-iosevka-${latest_release_num_only}.zip > ${latest_release_num_only}.zip
rm -rf latest/
unzip ${latest_release_num_only}.zip -d latest
# Clean up
rm ${latest_release_num_only}.zip

echo ${latest_release_num_only} > LATEST_RELEASE
exit 0
