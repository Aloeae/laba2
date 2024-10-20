def outer(out_param):
  def inner(in_param):
    return f'Outer def have value: {in_param}'
  return inner(out_param)
  
print(outer('TEST'))



==================== RESTART: C:/Users/tvoym/Downloads/ex.py ===================
Outer def have value: TEST
