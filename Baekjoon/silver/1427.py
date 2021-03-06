# 백준 1427번
# 소트인사이드

'''
<문제>
배열을 정렬하는 것은 쉽다. 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.

<입력>
첫째 줄에 정렬하고자하는 수 N이 주어진다. N은 1,000,000,000보다 작거나 같은 자연수이다.

<출력>
첫째 줄에 자리수를 내림차순으로 정렬한 수를 출력한다.
'''

# reverse() / reversed() >> sort() / sorted()의 차이와 같음
# 정렬된 새로운 객체를 반환하거나, 기존의 배열 순서를 뒤집기만하는 차이
N = input()

print(''.join(reversed(sorted(N))))

