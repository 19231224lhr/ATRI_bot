#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import nonebot
from nonebot.adapters.onebot.v11 import Adapter as ONEBOT_V11Adapter

# Custom your logger
# 
# from nonebot.log import logger, default_format
# logger.add("error.log",
#            rotation="00:00",
#            diagnose=False,
#            level="ERROR",
#            format=default_format)

# You can pass some keyword args config to init function
nonebot.init()
app = nonebot.get_asgi()

driver = nonebot.get_driver()
driver.register_adapter(ONEBOT_V11Adapter)

nonebot.load_builtin_plugins("echo")
nonebot.load_plugin("nonebot_plugin_remake")    # 人生重开模拟器插件
nonebot.load_plugin("haruka_bot")   # bilibili单推插件
nonebot.load_plugin("nonebot_plugin_petpet")   # 头像插件
nonebot.load_plugin("nonebot_plugin_gachalogs")   # 原神抽卡记录分析
nonebot.load_plugin("nonebot_plugin_gspanel")   # 原神角色评价
nonebot.load_plugin("nonebot_plugin_tts_gal")   # gal语音
nonebot.load_plugin("nonebot_plugin_wordcloud")   # 词云
nonebot.load_plugin("nonebot_plugin_tarot")   # 塔罗牌
nonebot.load_plugin("nonebot_plugin_boardgame")   # 棋类游戏
nonebot.load_plugin("nonebot_plugin_repeater")   # 复读机
nonebot.load_plugin("nonebot_plugin_crazy_thursday")   # 疯狂星期四
nonebot.load_plugin("nonebot_plugin_covid19_news")   # 疫情信息查询
# nonebot.load_plugin("nonebot_plugin_fortune")   # 今日运势，有bug，暂不使用
# nonebot.load_plugin("nonebot_plugin_weather_lite")   # 天气查询
nonebot.load_plugin("nonebot_plugin_logo")   # logo生成
nonebot.load_plugin("nonebot_plugin_setu_now")   # 涩图插件1
nonebot.load_plugin("nonebot_plugin_simplemusic")   # 点歌插件
nonebot.load_plugin("nonebot_plugin_heweather")   # 天气预报
nonebot.load_plugin("nonebot_plugin_hitokoto")   # 一言
nonebot.load_plugin("nonebot_plugin_answersbook")   # 答案之书
nonebot.load_plugin("nonebot_plugin_hikarisearch")   # 搜图

nonebot.load_plugins("src/plugins")

# Please DO NOT modify this file unless you know what you are doing!
# As an alternative, you should use command `nb` or modify `pyproject.toml` to load plugins
# nonebot.load_from_toml("pyproject.toml")

# Modify some config / config depends on loaded configs
# 
# config = driver.config
# do something...


if __name__ == "__main__":
    nonebot.logger.warning("Always use `nb run` to start the bot instead of manually running!")
    nonebot.run(app="__mp_main__:app")
