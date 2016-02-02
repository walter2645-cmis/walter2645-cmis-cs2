myName = "Walter"#defines myName
myAgeinYears = 19.1#defines myAgeinYears
myHeightinMeters = 1.73#defines myHeightinMeters
sideofsquare = 1#defines sideofsquare
lengthofrectangle = 2#defines lengthofrectangle
heightofrectangle = 3#defines heightofrectangle
myAgeinMonths = myAgeinYears*12#calculates myAgeinMonths using myAgeinYears
yearsbeforedeath = 71-myAgeinYears#calculates yearsbeforedeath using myAgeinYears
myHeightinFeet = myHeightinMeters*3.28084#calculates myHeihtinFeet using myHeightinMeters
diffFromAverageHeight = 1.734-myHeightinMeters#calculates diffFromAverageHeight using myHeightinMeters
areaofsquare = sideofsquare*sideofsquare#calculates areaofsquare using sideofsquare
halfvolumeofcube = areaofsquare*sideofsquare/2.0#calculates halfvolumeofcube using sideofsquare
oneNinthofRectangleArea = lengthofrectangle*heightofrectangle/9.0#calculates oneNinthofRectangleArea using lengthofrectangle and heightofrectangle
print "My name is " + myName + ". I am " + str(myAgeinYears) + " years old, which means i have apporximately " + str(yearsbeforedeath) + " years left to live. I am " + str(myHeightinMeters) + " meters tall, equivalent to " + str(myHeightinFeet) + " feet."#prints a brief description of me
print "A side of a square is " , sideofsquare , " unit(s) in length. The area of that square is " , areaofsquare , " unit(s) squared. The length of a rectangle is " , lengthofrectangle , " units, and the height of that rectangle is " , heightofrectangle , " units. One ninth of the rectangle's area is " , oneNinthofRectangleArea , " units squared."#prints some random data about a square and a rectangle
print ";) "*10000#prints 10000 winking smiley faces
