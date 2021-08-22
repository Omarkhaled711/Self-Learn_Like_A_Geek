from manimlib.imports import *

SquareArray=[]
arrow=Arrow()

class Learning(Scene):
    def construct(self):
        def Titles(string,shifting,targ,coloring,waiting,fade,scaling=1):
            MainTitle=TextMobject(string,color=coloring)
            MainTitle.scale(scaling)
            self.add(MainTitle)
            MainTitle.shift(shifting)
            self.play(Write(MainTitle))
            MainTitle.generate_target()
            MainTitle.target.shift(targ)
            self.play(MoveToTarget(MainTitle))
            self.wait(waiting)
            if fade==1:
                self.play(FadeOut(MainTitle))
        def squares(number,Xstart,Y,side=1):
            global SquareArray
            for i in range(number):
                vector=np.array([Xstart,Y,0])
                square=Rectangle(height=side,width=side,color=BLUE)
                square.move_to(vector)
                SquareArray.append(square)
                self.add(square)
                self.play(ShowCreation(square))
                Xstart=Xstart+side

        def cross(number,x,y,side=1):
            for i in range(number):
                line1=Line(start=np.array([x,y,0]),end=np.array([x+side,y-1,0]),color=RED)
                line2=Line(start=np.array([x+side,y,0]),end=np.array([x,y-1,0]),color=RED)
                x=x+(side)
                self.add(line1)
                self.play(ShowCreation(line1))
                self.add(line2)
                self.play(ShowCreation(line2))

        def CreateArrow(x,y,x2,y2,Color):
            global arrow
            arrow=Arrow(start=np.array([x,y,0]),end=np.array([x2,y2,0]),color=Color)
            return arrow
        def PlayArrow(x):
            self.add(x)
            self.play(ShowCreation(x))

        def ShiftArrow(x,target):
            x.generate_target()
            x.target.shift(target)
            self.play(MoveToTarget(x))

        def DeleteArray(x):
            for i in range(len(x)):
                self.remove(x[i])
            for i in range(len(x)):
                x.pop()

        self.wait(1)
        self.add_sound("SelfLearning")

        title1=Titles("Self-Learn like a geek",0,3*UP,WHITE,2.5,0)
        SubTitle1=Titles("1)tools",(2*UP+5*LEFT),0,PURPLE,3,0)

        SubTitle2=Titles("2)System",(4.7*LEFT),0,PURPLE,2,1)
        tool1=Titles("a) Version Control System (git)",(UP),0,RED,3,0)
        self.wait(1)
        squares(1,0,-2)
        self.wait(2.5)
        squares(2,1,-2)
        self.wait(5)
        arrow=CreateArrow(2,0,2,-1.7,GREY)
        PlayArrow(arrow)
        self.wait(2)
        for i in range(2):
            ShiftArrow(arrow,LEFT)
            self.wait(1.5)
        DeleteArray(SquareArray)
        self.remove(arrow)
        tool2=Titles("b) Digital notes",1.7*LEFT,0,RED,2,0)
        example1=Titles("Word format",(RIGHT+DOWN),0,GREEN,1,0)
        example2=Titles("Pdf format",(RIGHT+2*DOWN),0,GREEN,1,0)
        example3=Titles("Hand-Written style",(1.8*RIGHT+3*DOWN),0,GREEN,4.5,0)
        img=ImageMobject("xournel")
        img.scale(4)
        self.play(FadeIn(img))
        self.wait(3.5)
        self.clear()
        SubTitle2=Titles("2)System",(2*UP+4.7*LEFT),0,PURPLE,3,0)
        point1=Titles("Archiving system",(UP+3.5*LEFT),0,GREEN,2,0)
        squares(1,0,-1,1.5)
        self.wait(11)
        squares(2,1.5,-1,1.5)
        self.wait(9)
        Explain=Titles("The Versions represent the progress in my understanding",2.5*DOWN,0,RED,10.5,0)
        Explain1=Titles("Our understanding is subjective",(3.5*DOWN+2.7*LEFT),0,RED,46,0)
        self.clear()

        self.wait(1.5)
        Reason1=Titles("Organized",0,(3*UP+5*LEFT),GREEN,15,0)

        squares(2,0,0)
        self.wait(2)
        arrow=CreateArrow(1,2,1,0.5,GREY)
        PlayArrow(arrow)
        self.wait(4)
        label1=Titles("intuitive understanding",(DOWN+0.5*LEFT),0,GREY,1,0,0.32)
        label2=Titles("corrected...",(DOWN+RIGHT),0,GREY,1,0,0.35)

        Reason2=Titles("hidden",(UP+5.3*LEFT),0,GREEN,17,0)
        self.clear()
        self.wait(3)

        Reason3=Titles("Branching",0,(3*UP+5*LEFT),GREEN,3.5,0)
        squares(5,-2,-1)
        self.wait(2)
        cross(1,-0.5,-0.5)
        self.wait(3)
        cross(2,0.5,-0.5)
        self.wait(2)
        arrow=CreateArrow(0,-0.5,1,1,YELLOW)
        PlayArrow(arrow)
        self.wait(2)
        squares(2,1.5,1.5)
        self.wait(8)

        arrow=CreateArrow(-1,-0.5,-1,1,PURPLE)
        PlayArrow(arrow)
        Inputs=Titles("implicit input for another topic",(1.5*LEFT+UP),0,WHITE,0,0,0.5)
        arrow=CreateArrow(-2,-3,-2,-1.5,PURPLE)
        PlayArrow(arrow)

        Outputs=Titles("implicit output of another topic",(3*DOWN+2.2*LEFT),0,WHITE,55,0,0.5)
        self.clear()
        Ending1=Titles("This video was made by:",UP,0,WHITE,0,0)
        Name=Titles("Omar K. ZeinElDin",0,0,BLUE,2,0)
        Ending2=Titles("Bye.. ",2*DOWN,0,WHITE,2,0)


