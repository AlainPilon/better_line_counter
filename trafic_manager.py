class TraficManager:
  def __init__(self):
    self.counter = 0

  def incoming(self, tracker_id):
    self.counter += 1
    print(f"place incoming callback here for tracker {tracker_id}")


  def outgoing(self, tracker_id):
    self.counter -= 1
    print(f"place outgoing callback here for tracker {tracker_id}")

