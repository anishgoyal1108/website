#!/usr/bin/env sh
# Build the site and run the post-build gates.
set -e
cd "$(dirname "$0")/.."
hugo --gc --cleanDestinationDir "$@"
python3 scripts/check_public.py
