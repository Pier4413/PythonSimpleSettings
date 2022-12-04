class SettingsError(Exception):
  """
    Exception handler for settings related problem
  """
  def __init__(self, message : str = "Settings general error") -> None:
    self.message = message
    super.__init__(self.message)