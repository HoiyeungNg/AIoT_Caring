import json

from .models import HeartInfo, BodyStatusInfo, TempInfo


def get_heart_rate():
    heart_rates = HeartInfo.objects.values('heart_rate', 'update_time').order_by('-update_time')[:60]
    print(heart_rates)
    heart_data = []
    for heart_rate in heart_rates:
        heart_data.append(heart_rate)
    return heart_data


def get_body_status_info():
    body_infos = BodyStatusInfo.objects.values('body_status', 'update_time').order_by('-update_time')[:60]
    print(body_infos)
    body_data = []
    for body_info in body_infos:
        body_data.append(body_info)
    return body_data


def get_latest_body_info():
    latest_body_info = BodyStatusInfo.objects.values('body_status').order_by('-update_time')[:1]
    print(latest_body_info)
    body_data = []
    for body_info in latest_body_info:
        body_data.append(body_info)
    return body_data


def get_temp_info():
    environment_infos = TempInfo.objects.values('temperature', 'update_time').order_by('-update_time')[:60]
    print(environment_infos)
    environment_data = []
    for environment_info in environment_infos:
        environment_data.append(environment_info)
    return environment_data


def get_latest_temp():
    latest_environment_info = TempInfo.objects.values('temperature').order_by('-update_time')[:1]
    print(latest_environment_info)
    environment_data = []
    for environment_info in latest_environment_info:
        environment_data.append(environment_info)
    return environment_data
