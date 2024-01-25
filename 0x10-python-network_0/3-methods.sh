#!/bin/bash

if [[ $# -ne 1 ]]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

url="$1"

allowed_methods=$(curl -sSL -D - "$url" | grep Allow | cut -d ' ' -f2-)

if [[ -n "$allowed_methods" ]]; then
  echo "Allowed methods:"
  echo "$allowed_methods"
else
  echo "Failed to retrieve allowed methods from server."
fi
