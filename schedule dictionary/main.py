import time
from plyer import notification

words = ["Allow", "Acheive", "Active"]
meanings = ["let (someone) have or do something",
            "successfully bring about or reach (a desired objective or result) by effort, skill, or courage",
            "the fact or process of doing something, typically to achieve an aim"]


for i in range(len(words)):
    notification.notify(
        title=words[i],
        message=meanings[i],
        app_icon="C:\\Users\\ADmin\\Desktop\\Dice Simulator\\schedule dictionary\\Iconsmind-Outline-Book.ico",
        timeout=4)
    time.sleep(8)
