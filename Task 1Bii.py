def flame(a,b):
    flames={"F":"Friendship",
            "L":"Love",
            "A":"Affection",
            "M":"Marriage",
            "E":"Enemy",
            "S":"Siblings"}
    for i in a:
        if i in b:
            a=a.replace(i,'')
            b=b.replace(i,'')
    flamed_name=a+b
    length=len(flamed_name)
    c="FLAMES"
    while len(c) > 1:
        if len(c)>=length:
            c=c.replace(c[length-1],'')

        else:
            newl=length % len(c)
            c=c.replace(c[newl-1],'')
    if c in flames:
        print("The Flame Result= ",flames[c])
name1=input("Enter the first name:")
name2=input("Enter the second name:")
name1=name1.upper()
name2=name2.upper()
flame(name1,name2)