# 기본 매개 변수
# 거듭제곱 함수 예제
def power(base, exponent=2):
  return base ** exponent

# 함수 호출 예제
print(power(3))       # 기본 지수 2 사용, 3^2 = 9
print(power(2, 3))    # 지수 3 사용, 2^3 = 8

# 서울 중형택시 요금 계산기 (거리 요금 기준)
# 기본요금: 1.6km까지 4,800원 / 이후 131m마다 100원 (주간)
def taxi_fare(distance, base_fare=4800, unit_fare=100):
    base_km = 1.6                      # 기본 거리(km)
    unit_m = 131                       # 거리 요금이 붙는 단위(m)

    if distance <= base_km:            # 기본 거리 이내면 기본요금만
        return base_fare

    extra_m = round((distance - base_km) * 1000)   # 기본 거리를 넘은 거리(m)
    count = extra_m // unit_m                      # 131m를 몇 번 달렸나
    return base_fare + count * unit_fare

# 함수 호출 예제
print(taxi_fare(1))              # 주간 1km: 기본 거리 이내 → 4800
print(taxi_fare(5))              # 주간 5km: 기본요금 4800 + 거리 요금
print(taxi_fare(5, 5800, 120))   # 심야(22~23시, 02~04시) 5km
print(taxi_fare(5, 6700, 140))   # 심야(23~02시) 5km