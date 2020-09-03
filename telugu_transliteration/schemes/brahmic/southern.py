from NLP.Assignment1_Transliteration.telugu_transliteration.schemes.brahmic import BrahmicScheme, s

class GranthaScheme(BrahmicScheme):
    def __init__(self):
        super(GranthaScheme, self).__init__({
            'vowels': s("""𑌅 𑌆 𑌇 𑌈 𑌉 𑌊 𑌋 𑍠 𑌌 𑍡 𑌏 𑌐 𑌓 𑌔 𑌏𑌀 𑌓𑌀"""),
            'marks': s("""𑌾 𑌿 𑍀 𑍁 𑍂 𑍃 𑍄 𑍢 𑍣 𑍇 𑍈 𑍋 𑍗 𑍇𑌀 𑍋𑌀"""),
            'virama': s('𑍍'),
            'yogavaahas': s('𑌂 𑌃 𑌁'),
            'consonants': s("""
                            𑌕 𑌖 𑌗 𑌘 𑌙
                            𑌚 𑌛 𑌜 𑌝 𑌞
                            𑌟 𑌠 𑌡 𑌢 𑌣
                            𑌤 𑌥 𑌦 𑌧 𑌨
                            𑌪 𑌫 𑌬 𑌭 𑌮
                            𑌯 𑌰 𑌲 𑌵
                            𑌳 𑌕𑍍𑌷 𑌜𑍍𑌞
                            𑌨𑌼 𑌰𑌼 𑌳𑌼
                            """) + s("""ன ற ழ"""),
            'symbols': s("""
                       𑍐 𑌽 । ॥
                       ௦ ௧ ௨ ௩ ௪ ௫ ௬ ௭ ௮ ௯
                       """)
        }, name=GRANTHA)


class TeluguScheme(BrahmicScheme):
    def __init__(self):
        super(TeluguScheme, self).__init__({
            'vowels': s("""అ ఆ ఇ ఈ ఉ ఊ ఋ ౠ ఌ ౡ ఏ ఐ ఓ ఔ ఎ ఒ"""),
            'marks': s("""ా ి ీ ు ూ ృ ౄ ౢ ౣ ే ై ో ౌ ె  ొ"""),
            'virama': s('్'),
            'yogavaahas': s('ం ః ఁ'),
            'consonants': s("""
                            క ఖ గ ఘ ఙ
                            చ ఛ జ ఝ ఞ
                            ట ఠ డ ఢ ణ
                            త థ ద ధ న
                            ప ఫ బ భ మ
                            య ర ల వ
                            శ ష స హ
                            ళ క్ష జ్ఞ
                            """)
                          + s("""ऩ ఱ ఴ क़ ఖ ग़ ज़ ड़ ఢ ఫ य़"""),
            'symbols': s("""
                       ఓం ఽ । ॥
                       ౦ ౧ ౨ ౩ ౪ ౫ ౬ ౭ ౮ ౯
                       """)
        }, name=TELUGU)

GRANTHA = 'grantha'
TELUGU = 'telugu'
SCHEMES = {
    TELUGU: TeluguScheme()
}
