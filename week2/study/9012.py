t = int(input())  # 테스트 케이스 개수 받기

for _ in range(t):
  st = [] # 테스트 케이스마다 스택 초기화
  s = input() # 괄호 입력받기

  for c in s: # 괄호 문자열 루프
    if c == '(':  # 만약 여는 괄호라면 고민 말고 스택에 push
      st.append(c)
    else: # 닫는 괄호인 경우
      if len(st) == 0:  # 스택이 비었다면, 즉 괄호 짝이 안맞는다면 False
        print('NO')
        break
      st.pop()  # 스택이 비지 않았다면 스택의 맨 위 여는 괄호를 뺌
  # 스택이 비는 경우 없이 무사히 for문이 잘 끝나도 끝난 게 아님
  # 만약 스택에 여는 괄호가 남았다면, 닫는 괄호짝이 맞지 않는 것임
  # 즉, 스택이 있다면 False, 스택이 비었다면 True임
  else:
    print('NO') if st else print('YES')

# 제대로 된 괄호가 아닌 경우
# 아래 예시로 생각해보세요
# (1) 닫는 괄호가 더 많음 : (()))() -> if-else에서 걸림
# (2) 여는 괄호가 더 많음 : ((())() -> for-else에서 걸림
# (3) 여닫는 괄호 수가 같지만 순서가 틀림 : )(() -> if-else에서 걸림