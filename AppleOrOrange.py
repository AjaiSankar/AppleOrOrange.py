
from sklearn import tree

redcolor=0
orangecolor=1
smooth=0
rough=1
apple=0
orange=1


features=[[redcolor,smooth],[orangecolor,rough],[redcolor,smooth],
[redcolor,smooth],[orangecolor,rough],[orangecolor,rough],[redcolor,smooth]]
labels=[apple,orange,apple,apple,orange,orange,apple]

classifier=tree.DecisionTreeClassifier()
classifier.fit(features,labels)

inputcolor=input('Enter the color of the fruit: ')
if (inputcolor=='red' or inputcolor=='redcolor' or inputcolor=='Red' or inputcolor=='Redcolor'):
  inputcolornew=0
else:
  inputcolornew=1
inputtexture=input('Enter the texture of the fruit: ')
if (inputtexture=='smooth' or inputtexture=='Smooth'):
  inputtexturenew=0
else:
  inputtexturenew=1

if(classifier.predict([[inputcolornew,inputtexturenew]])==0):
  print('Fruit is an Apple')
else:
  print('Fruit is an Orange')
