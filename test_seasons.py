from seasons import check_date

def main():
  test_check_date()

def test_check_date():
  assert check_date('2003,12,13') == ('2003','12','13')
  assert check_date('2003,4,8') == None
  assert check_date('July,11,25') == None

if __name__ == "__main__" :
  main()