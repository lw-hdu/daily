#!/bin/bash

find /data/logs/ -mtime +30 -type f -print -exec rm -rf {} \;

