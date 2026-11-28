"""서울 중형택시의 주간 거리 기준 예상 요금 계산."""

BASE_FARE = 4800
BASE_DISTANCE_METERS = 1600
ADDITIONAL_DISTANCE_METERS = 131
ADDITIONAL_FARE = 100


def taxi_fare(distance_meters):
    """이동 거리(미터)에 따른 예상 요금을 원 단위로 반환한다."""
    if distance_meters < 0:
        raise ValueError("이동 거리는 0 이상이어야 합니다.")

    extra_distance = max(0, distance_meters - BASE_DISTANCE_METERS)
    return BASE_FARE + (extra_distance // ADDITIONAL_DISTANCE_METERS) * ADDITIONAL_FARE


def main():
    print("서울 중형택시 주간 거리 기준 예상 요금")
    print("기본 1.6km 4,800원, 이후 131m마다 100원 (2023년 2월 기준)")
    print("시간 요금, 심야·시계외 할증, 통행료 등은 제외합니다.")

    try:
        distance = int(input("이동 거리(미터, 정수): "))
        fare = taxi_fare(distance)
    except ValueError as error:
        print(f"입력 오류: {error}")
        return

    print(f"예상 요금: {fare:,}원")
    print("실제 요금은 운행 상황과 요금 변경에 따라 다를 수 있습니다.")


if __name__ == "__main__":
    main()
