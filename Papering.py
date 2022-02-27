import pyautogui
import pyperclip
import time

a = 0
first = input("도배할 단어나 문장을 입력해주세요\n")
cho = float(input("기다릴 초를 입력해주세요(소수도 됩니다)\n"))
bun = int(input("몇번 반복할까요\n"))
time.sleep(1)
print(3)
time.sleep(1)
print(2)
time.sleep(1)
print(1)
while a < bun:
    a = a + 1
    pyperclip.copy(first)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    time.sleep(cho)
print(f"도배가 끝났습니다. 총 {bun*2}개의 채팅을 쳤어요")
