# -*- coding=utf-8 -*-
"""

基于现有网络库的二次封装
    * 代理IP
    * 随机请求头中的用户代理
    * 使用多线程

Author       :   Cucumber
Date         :   10/22/20

"""
import random


def __load_proxies():
    """
    :return:
    """
    proxy_file = "/Users/nashan/Documents/WS/pycharm/python_intern/project/proxies.txt"
    ips = []
    with open(proxy_file, 'r') as proxies:
        for ip in proxies.readlines():
            if ip:
                ips.append(ip.strip())
    # 用于将一个列表中的元素打乱
    random.shuffle(ips)
    return ips


def get_agent():
    """
    :return: 加载本地的用户代理集合
    """
    user_agent_file = "/Users/nashan/Documents/WS/pycharm/python_intern/project/user_agents.txt"
    agents = []
    with open(user_agent_file, 'rb') as agent_file:
        for agent in agent_file.readlines():
            if agent:
                agents.append(agent.strip()[1:-1])
    # 用于将一个列表中的元素打乱
    random.shuffle(agents)
    return agents


def get_proxy():
    return random.randrange(0, len(get_agent()))


def requests_headers():
    """
    :return: 获得随机请求头
    """
    head_connection = ['Keep-Alive', 'close']
    head_accept = ['text/html,application/xhtml+xml,*/*']
    head_accept_language = ['zh-CN,fr-FR;q=0.5', 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3']
    user_agents = get_agent()
    header = {
        'Connection': head_connection[random.randrange(0, len(head_connection))],
        'Accept': head_accept[0],
        'Accept-Language': head_accept_language[random.randrange(0, len(head_accept_language))],
        'User-Agent': user_agents[random.randrange(0, len(user_agents))],
    }
    return header
