import cv2

#Abrindo o arquivo do padrão
padrao = cv2.imread('padrao.bmp')

#Guardando informações a respeito da organização dos dados na matriz
h = padrao.shape[0]
w = padrao.shape[1]
ch = padrao.shape[2]

#print das informações dos pixels da imagem padrão antes do processamento
print(padrao)

#Guardando as faixas de valores dos canais de cores do padrão.
max1=0
min1=255
max2=0
min2=255
max3=0
min3=255


for li in range(0, h): #para cada linha
  for col in range(0, w): #de cada coluna
      if padrao[li,col,0] >= max1:
        max1 = padrao[li,col,0]
      elif padrao[li,col,0] <= min1:
        min1 = padrao[li,col,0] 

for li in range(0, h): #para cada linha
  for col in range(0, w): #de cada coluna
      if padrao[li,col,1] >= max2:
        max2 = padrao[li,col,1]
      elif padrao[li,col,1] <= min2:
        min2 = padrao[li,col,1] 

for li in range(0, h): #para cada linha
  for col in range(0, w): #de cada coluna
      if padrao[li,col,2] >= max3:
        max3 = padrao[li,col,2]
      elif padrao[li,col,2] <= min3:
        min3 = padrao[li,col,2] 

#Leitura da imagem que será trabalhada
imagem = cv2.imread('cafe.bmp')

#Alterando as cores dos pixels que estão dentro da faixa de valores identificados no padrão
l = -1
c = -1
for linhas in imagem:
    l = l + 1
    c = -1
    for coluna in linhas:
        c= c + 1
        #Os canais são separados em BGR (azul, verde e vermelho)
        if (coluna[0] > min1 and coluna[0] < max1) and (coluna[1] > min2 and coluna[1] < max2) and (coluna[2] > min3 and coluna[2] < max3):
            imagem[l,c,2] = 0
            imagem[l,c,1] = 0
            imagem[l,c,0] = 255
#Gravando um novo aqrivo
cv2.imwrite("saida.png", imagem)

#Convertendo para HSV (Segunda parte do exercício)
hsvImage = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)
print(hsvImage)