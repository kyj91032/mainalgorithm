# 파이썬 기본 정렬 라이브러리

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

result = sorted(array) # sorted() 함수: 병합 정렬을 기반으로 만들어짐. 퀵 정렬보다 조금 느리지만 최악의 경우에도 O(NlogN) 보장. 집합, 딕셔너리 자료형을 입력해도 리스트로 반환함.
print(result)

array.sort() # sort() 함수: 리스트 객체의 내장 함수. 리스트의 반환 없이 내부 원소가 바로 정렬됨.
print(array)

# key 매개변수 활용: key가 받는 함수를 요소 하나하나에 적용하여 리턴값을 기준으로 정렬함. (map(function, iterable)과 비슷)

array = [('바나나', 2), ('사과', 5), ('당근', 3)]

def setting(data): # key로 사용할 함수 정의
  return data[1]

result = sorted(array, key = setting)
print(result)

result = sorted(array, key = lambda data : data[1]) # key로 사용할 익명 함수(lambda) 정의. key(data)는 data[1]을 리턴.

'''
lambda 함수

람다 함수는 정의와 동시에 사용할 수 있다.
(lambda x : x+1)(3) 는 4 리턴

함수에 이름이 없고, 저장된 변수가 없기 때문에 다시 사용할 수 없지만 람다함수도 객체이기 때문에 정의와 동시에 변수에 담아 계속 사용할 수 있다.
func = lambda x : x + 1
func(4)는 5리턴


'''
