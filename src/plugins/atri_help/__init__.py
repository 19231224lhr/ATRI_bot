from nonebot import on_command
from nonebot.rule import to_me
from nonebot.matcher import Matcher
from nonebot.adapters import Message
from nonebot.params import Arg, CommandArg, ArgPlainText

weather = on_command("weather", rule=to_me(), aliases={"菜单", "帮助菜单"}, priority=5)


@weather.handle()
async def handle_first_receive(matcher: Matcher, args: Message = CommandArg()):
    plain_text = args.extract_plain_text()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
    if plain_text:
        matcher.set_arg("city", args)  # 如果用户发送了参数则直接赋值
    else:
        city_weather = await get_weather("atri")
        await weather.finish(city_weather)

help_string = "Hello 大家好！我是ATRI，以下是我现在支持的功能：\n\n" \
              "1. 人生重开模拟器：@亚托莉 remake\n" \
              "2. b站单推：@亚托莉 帮助\n" \
              "3. 表情包制作：@亚托莉 头像表情包\n" \
              "4. 原神抽卡记录: 抽卡记录\n" \
              "5. 原神角色评价: 面板+名字+uid\n" \
              "6. 语音模拟: @亚托莉 宁宁说...\n" \
              "7. 词云: (我的)今日词云\n" \
              "8. 占卜: 塔罗牌\n" \
              "9. 小游戏: @亚托莉 五子棋/围棋\n" \
              "10. 疯狂星期四: 疯狂星期...\n" \
              "11. 疫情信息查询: 城市+疫情(政策)\n" \
              "12. logo生成: ph/yt/5000兆/douyin/google 内容\n" \
              "13. 好康的: 涩涩 (x数字)(标签)\n" \
              "14. 点歌: 点歌+关键词\n" \
              "15. 天气预报: 城市+天气\n" \
              "16. 每日一言: 一言\n" \
              "17. 答案之书: 翻看答案+问题\n" \
              "18. 搜图: 搜图+图片\n" \
              "\n" \
              "更多功能，敬请期待，来自你们的智能助理亚托莉。"

@weather.got("city", prompt="你想查询哪个城市的天气呢？")
async def handle_city(city: Message = Arg(), city_name: str = ArgPlainText("city")):
    if city_name not in ["北京", "上海"]:  # 如果参数不符合要求，则提示用户重新输入
        # 可以使用平台的 Message 类直接构造模板消息
        await weather.reject(city.template("你是不是输入有错误，想要查询功能直接输入菜单就可以了，哼。"))

    city_weather = await get_weather(city_name)
    await weather.finish(city_weather)


# 在这里编写获取天气信息的函数
async def get_weather(city: str) -> str:
    return help_string
