
import logging
from decorators import run_daemon

CHECK_CONNECTORS_JOB_RESTART_DELAY = 10.0


class CheckConnectorJob:

    # __mapper_args__ = {'polymorphic_identity': 'ConnectorCheckJob'}

    @run_daemon
    def execute(self):
        logging.info('Сервис проверки коннекторов был запущен')
        print('Сервис проверки коннекторов был запущен')

        from connector import check_connectors_status
        # timers = EventScheduler()
        check_connectors_status()
        # timers.call_regular_interval(
        #     CHECK_CONNECTORS_JOB_RESTART_DELAY,
        #     check_connectors_status,
        # )
        # for _ in itertools.count(start=1):
        #     self.heartbeat()
        #     timers.run(blocking=False)
