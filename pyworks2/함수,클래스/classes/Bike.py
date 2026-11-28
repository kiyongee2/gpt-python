
class Bike:
  def __init__(self, color, gears):
    self.color = color
    self.gears = gears

  def get_info(self):
    print(f"색상: {self.color}, 기어 수: {self.gears}")