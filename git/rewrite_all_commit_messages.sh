new_msg_example=xh -b http://www.programmerexcuses.com | xq -x //center/a
FILTER_BRANCH_SQUELCH_WARNING=1 git filter-branch --force --msg-filter 'echo $(new_msg_example)' --tag-name-filter cat -- HEAD
