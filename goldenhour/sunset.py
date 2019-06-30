import datetime
import logging
import math
import time

from astral import Astral
import pytz


logger = logging.getLogger()


def get_today_sunset_time(location, today):
    return location.sun(today)['sunset']


def get_seconds_until(earlier_time, later_time):
    tdelta = later_time - earlier_time
    return tdelta.total_seconds()


def wait_for_sunset(location, minutes_before=0):
    now = datetime.datetime.now(location.timezone)
    sunset_time = get_today_sunset_time(location, now.date())
    start_time = sunset_time - datetime.timedelta(minutes=minutes_before)
    if start_time < now:
        logger.error('ERROR: too late to start for today\'s sunset')
        exit()

    sleep_seconds = get_seconds_until(now, start_time)
    hours = math.floor(sleep_seconds // (60 * 60))
    minutes = math.floor((sleep_seconds // 60) % 60)
    seconds = math.floor(sleep_seconds % 60)
    logger.info(
        'Waiting {hours} {minutes} {seconds} to start, {minutes_before} minutes before sunset'.format(
            hours='{} hours'.format(hours) if hours > 0 else '',
            minutes='{} minutes'.format(minutes) if minutes > 0 else '',
            seconds='{} seconds'.format(seconds),
            minutes_before=minutes_before,
        )
    )
    time.sleep(sleep_seconds)
