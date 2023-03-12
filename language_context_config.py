class LangContextConfig:
    def __init__(self, transcribe_prompt=None, language_from=None, language_to=None, language_keep=None, language_contain=None, other_translate_context=None):
        self.transcribe_prompt = transcribe_prompt
        self.language_from = language_from
        self.language_to = language_to
        self.language_keep = language_keep
        self.language_contain = language_contain
        self.other_translate_context = other_translate_context

def get_lan_config():
    # B站泪腺战士直播间，“lan”是指主播，不是指语言

    # Not a good prompt though
    transcribe_prompt = \
    "不说话显然就是不想聊...能不能告诉我真相啊...这个难道不是校园霸凌吗\n \
    でも、 彼女の悩みの正体を私が勝手に想像して良いのなら でも、彼女の悩みについて、 どう考えても、彼女の悩みについて、私はまだ考えていません。\n \
    嗯？那个...全的那个跟班的女孩子，她的那个跟班女不是失踪了吗？听说是被华子杀了的......你是说...Ribon？\n \
    没错，就是我们的CPTOL预告函的第一封信。上面写的 Ribon，那个蝴蝶结，她正是我们全队的那个跟班女\n \
    从体大弱门到体弱大门我已经不知道该说什么了。就这样吧，能不能专注游戏，受不了。魂小鬼滚出 NG 直播间吧。"

    language_from="Japanese"
    language_keep="English and Mandarin Chinese(Simplified)"
    language_contain="Mandarin Chinese mixed with some Japanese and a little bit English"
    other_translate_context="If there is Traditional Chinese in the input text, only replace Traditional Chinese characters with Simplified Chinese counterparts, and do not make any other modifications to these Chinese characters. The input text is a transcript of a Japanese horror game live stream, the host is a native Chinese speaker who can speak Japanese and English."

    return LangContextConfig(transcribe_prompt=transcribe_prompt, language_from=language_from, language_keep=language_keep, language_contain=language_contain, other_translate_context=other_translate_context)
