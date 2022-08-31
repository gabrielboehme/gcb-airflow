from copy import deepcopy
import os

from airflow.configuration import conf
from airflow.config_templates.airflow_local_settings import DEFAULT_LOGGING_CONFIG

S3_LOG_FOLDER = conf.get('logging', 'REMOTE_BASE_LOG_FOLDER')
LOGGING_CONFIG = deepcopy(DEFAULT_LOGGING_CONFIG)
FILENAME_TEMPLATE= conf.get_mandatory_value('logging', 'LOG_FILENAME_TEMPLATE')
BASE_LOG_FOLDER = conf.get_mandatory_value('logging', 'BASE_LOG_FOLDER')

# add an additional handler
LOGGING_CONFIG['handlers']['s3.task'] = {
    'class': 'airflow.providers.amazon.aws.log.s3_task_handler.S3TaskHandler',
    'formatter': 'airflow',
    'base_log_folder': os.path.expanduser(BASE_LOG_FOLDER),
    's3_log_folder': S3_LOG_FOLDER,
    'filename_template': "{{ ti.dag_id }}/{{ ti.task_id }}_{{ ts }}_{{ try_number }}.log",
    'filters': ['mask_secrets'],
}

LOGGING_CONFIG['loggers']['airflow.task']['handlers'] = ["s3.task"]