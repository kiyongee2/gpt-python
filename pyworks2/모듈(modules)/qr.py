
import qrcode

# QR 코드에 담을 데이터
data = "https://kiyongee2.github.io/mysite/"

# QR 코드 생성
img = qrcode.make(data)

# 이미지 저장
img.save("qrcode.png")

print("QR 코드가 생성되었습니다!")