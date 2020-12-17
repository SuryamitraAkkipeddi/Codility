import sys

def solution(A):
  result = 0
  length = len(A)
  valueList = [0]
  for i in range(length):
    valueList.append(valueList[i] + A[i])

  minAvg = sys.float_info.max
  for i in range(length - 1):
    index1 = i + 1
    index2 = i + 2
    avg = (valueList[index1 + 1] - valueList[i]) / 2.0
    if(avg < minAvg):
      minAvg = avg
      result = i

    if(i < length - 2):
      avg = (valueList[index2 + 1] - valueList[i]) / 3.0
      if(avg < minAvg):
        minAvg = avg
        result = i

  return result