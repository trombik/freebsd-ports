#!/bin/sh
git fetch upstream
git checkout master && git reset --hard upstream/master
