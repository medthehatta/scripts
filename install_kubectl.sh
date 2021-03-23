#!/bin/bash

version="1.20.5"
while [ "$#" -gt 0 ]; do
    case "$1" in
        -h|--help)
            sed -n '/^while/,/^done/p' "$0" | grep -oP '\S+(?=\)$)'
            exit 0
            ;;
        --link)
            link=1
            shift
            ;;
        --version)
            version="$2"
            shift 2
            ;;
        *)
            break
            ;;
    esac
done


curl -LO "https://storage.googleapis.com/kubernetes-release/release/v$version/bin/linux/amd64/kubectl"
chmod +x ./kubectl
sudo mv ./kubectl "/usr/local/bin/kubectl.$version"
if [ -n "$link" ]; then
    sudo ln -sf "/usr/local/bin/kubectl.$version" "/usr/local/bin/kubectl"
fi
