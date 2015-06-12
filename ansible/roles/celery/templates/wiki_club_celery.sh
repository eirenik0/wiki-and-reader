#!/bin/bash
### BEGIN INIT INFO
# Provides:          wiki_club_celery
# Required-Start:
# Required-Stop:     wiki_club_celery

# Default-Start:
# Default-Stop:      0 6
# Short-Description: Unmount all network filesystems except the root fs.
# Description:       Also unmounts all virtual filesystems (proc,
#                    devpts, usbfs, sysfs) that are not mounted at the
#                    top level.
### END INIT INFO
. /etc/init.d/functions

start() {
        initlog -c "echo -n Starting celery worker: "
        {{ virtualenv_path }}/bin/python {{ project_path }}/manage.py celery worker --loglevel=info &
        ### Create the lock file ###
        touch /var/lock/subsys/wiki_club_celery
        success $"wiki club Celery worker startup"
        echo
}
# Restart the service FOO
stop() {
        initlog -c "echo -n Stopping FOO server: "
        killproc wiki_club_celery
        ### Now, delete the lock file ###
        rm -f /var/lock/subsys/wiki_club_celery
        echo
}
### main logic ###
case "$1" in
  start)
        start
        ;;
  stop)
        stop
        ;;
  status)
        status FOO
        ;;
  restart|reload|condrestart)
        stop
        start
        ;;
  *)
        echo $"Usage: $0 {start|stop|restart|reload|status}"
        exit 1
esac
exit 0