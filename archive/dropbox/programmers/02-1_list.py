# 02-1_list.py
def solution(L, x):
    i = 0
    for e in L:
        if ( e < x ):
            i += 1
        else:
            break
    L.insert(i, x)  
    answer = L
    return answer
    
#if __name__ == "main":
if __name__ == "__main__":
  list_1 = [20,37,58,72,91]
  print(list_1)
  print("")
  a = solution( list_1, 65)
  print(a)
  
  list_2 = [20,37,58,72,91]
  a = solution( list_2, 15)
  print(a)

  list_3 = [20,37,58,72,91]
  a = solution( list_3, 100)
  print(a)
  