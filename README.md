# Catcher#
---
security tool like Regshot tool over windows platform allows you to quickly take a snapshot
of your registry and then compare it with a second one - done after doing system changes or
installing a new software product or run a malware.

# help #
---

Usage: ./catcher.py [options]

Options:
    -h, --help              show this help
    -f, --first-shot        take your first shot
    -s, --second-shot       take your second shot
    -p, --compare           compare first and second shots
    -c, --clear             clear the previous shots
    -t, --target            set target path

Required:
    if your target is file system, you must run program as root.

Example:
    ./catcher.py -f -t /User/lnxg33k
    ./catcher.py -s -t /User/lnxg33k
    ./catcher.py -p
    ./catcher.py -c
