#!/usr/bin/env bash

dprint() {
    echo -e "`date` ---> ${@}" 2>&1 |tee -a /var/log/crypto.log
}

dprint "Setup environment for Crypto Tools"
cat /etc/crontabs/root

dprint "Running cron in the foreground ..."
/usr/sbin/crond -f
