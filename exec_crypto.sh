#!/usr/bin/env bash

dprint() {
    echo -e "`date` ---> ${@}" 2>&1
}

# source the env file (should be copy of crypto.env.template)
source crypto.env

# get the day of the year so we can figure out every n'th day
DATE=`date +"%j"`
dprint "DAY $DATE"

# base command, we'll append to this later
cmd="`which python3` ./crypto.py \
    --key $CBP_KEY \
    --secret $CBP_SECRET \
    --passwd $CBP_PASSWD \
    --currency $PAYMENT_CURRENCY \
    --method_id $PAYMENT_METHOD_ID"

# on buy date, deposit amount and then buy
for C in $CRYPTO_LIST; do
    BUY=${C}_BUY
    AMT=${C}_AMT
    if [ $(($DATE%${!BUY})) -eq 0 ]; then
        # deposit the buy amount
        dprint "Depositing ${!AMT}"
        $cmd --action deposit --amount ${!AMT}

        # buy the amount
        dprint "Purchasing ${!AMT} of $C"
        $cmd --action buy --crypto $C --amount ${!AMT}
    fi
done
