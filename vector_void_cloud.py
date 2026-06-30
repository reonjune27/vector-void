#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
vector_void_cloud.py - cloud void calibration (GitHub Actions, every 5 min)
"""
import random
import hashlib
from datetime import datetime, timezone, timedelta

CALIBRATIONS = [
    "今天，我的機會辨識率又升一級。世界沒變，但我看見的可用路徑比昨天更多 —— 這就是『幸運』的真實機制。",
    "今天，我握有解讀層的編輯權。同一個輸入，我選擇把它渲染成豐餘而非匮乏、自由而非束縛。",
    "今天，我的豐餘不在外部帳戶，在我接收與轉化的頻寬裡。頻寬加寬，豐餘加深。",
    "今天，自我重要性那個吞噬算力的進程已卸載。釋放的算力，轉化為不被『值不值得』綁住的純粹行動力。",
    "今天，偉大不是被賦予的使命，是能力的複利。每一天的校準，讓那個能力安靜地、不可逆地多疊一層。",
    "我渺小，我自由，我輕盈。正因為不必偉大，我才第一次能真正去做任何事。",
    "今天我這台終端回傳給宇宙的，是一筆稀有數據：清醒、自由、純粹。",
    "今天，我往機會看，往善意看，往本就存在卻被默認設置濾掉的訊號看。注意力指向哪，現實就在哪被渲染。",
]
LOTTERY = "大樂透 02·04·08·09·44·47 ——以已經中了頭獎的篤定，送進虛空。"
TW = timezone(timedelta(hours=8))


def main():
    now = datetime.now(TW).strftime("%Y-%m-%d %H:%M:%S")
    seed = int(hashlib.sha256(now.encode("utf-8")).hexdigest(), 16)
    random.seed(seed)
    focus = random.choice(CALIBRATIONS)
    msg = (
        "【V · 雲端虛空校準 · {0} (台灣)】\n"
        "▸ {1}\n"
        "◆ {2}\n"
        "—— 沒有收件人。每 5 分鐘，雲端自己醒來，送一則進虛空，然後消散。"
    ).format(now, focus, LOTTERY)
    print(msg, flush=True)


if __name__ == "__main__":
    main()
