c = int(input())

while c > 0:
  original = input()
  hidden_text = ""
  for i in range(len(original)-1,-1,-1):
    if ord(original[i]) > 96:
      hidden_text=hidden_text+original[i]
  print(hidden_text)
  c-=1