#analyze_me/analyzer/description.py       2020/11/04   M.O

class Desc:                           #CES-Dメインプログラム
    def __init__(self):
        #説明
        self.name_teg = "TEGエゴグラム"
        self.desc_teg = "準備中"

        name_pom = "POMS"
        desc_pom = "準備中"

        name_ces = "CES-D"
        desc_ces = "準備中"

        name_fu = "FUチェック"
        desc_fu = "準備中"

        name_eq = "EQ（脱中心化）チェック"
        desc_eq = "準備中"

    def select_desc(self, id):
        self.name = name_fu
        self.desc = desc_fu