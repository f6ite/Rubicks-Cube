def Main():
    #######################
    # Variable assignment #
    #######################

    f1=f2=f3=f4=f5=f6=f7=f8=f9="G"      #Front face
    l1=l2=l3=l4=l5=l6=l7=l8=l9="O"      #Left face
    r1=r2=r3=r4=r5=r6=r7=r8=r9="R"      #Right face
    u1=u2=u3=u4=u5=u6=u7=u8=u9="Y"      #Bottom face
    t1=t2=t3=t4=t5=t6=t7=t8=t9="W"      #Top face
    b1=b2=b3=b4=b5=b6=b7=b8=b9="B"      #Back face

    ###############################################################
    # Visualisation of the values #
    #                
                    #______________#
                    # T1 | T2 | T3 #
                    # T4 | T5 | T6 #
                    # T7 | T8 | T9 #
    #_______________#______________#_____________________________#
    # L1 | L2 | L3  # F1 | F2 | F3 # R1 | R2 | R3 # B1 | B2 | B3 #
    # L4 | L5 | L6  # F4 | F5 | F6 # R4 | R5 | R6 # B4 | B5 | B6 #
    # L7 | L8 | L9  # F7 | F8 | F9 # R7 | R8 | R9 # B7 | B8 | B9 #
    #_______________#______________#_____________________________#
                    # U1 | U2 | U3 #
                    # U4 | U5 | U6 #
                    # U7 | U8 | U9 #
                    #______________#

    ################################################################

    Rubiks(f1,f2,f3,f4,f5,f6,f7,f8,f9,l1,l2,l3,l4,l5,l6,l7,l8,l9,r1,r2,r3,r4,r5,r6,r7,r8,r9,u1,u2,u3,u4,u5,u6,u7,u8,u9,t1,t2,t3,t4,t5,t6,t7,t8,t9,b1,b2,b3,b4,b5,b6,b7,b8,b9)

def Complete(f1,f2,f3,f4,f5,f6,f7,f8,f9,l1,l2,l3,l4,l5,l6,l7,l8,l9,r1,r2,r3,r4,r5,r6,r7,r8,r9,u1,u2,u3,u4,u5,u6,u7,u8,u9,t1,t2,t3,t4,t5,t6,t7,t8,t9,b1,b2,b3,b4,b5,b6,b7,b8,b9):
    #There's probably a better way to do this, but this will work for demonstration purposes
    print("The completed Rubiks cube is as follows:")
    print("Front Face:")
    print(f1 + " " + f2 + " " + f3)
    print(f4 + " " + f5 + " " + f6)
    print(f7 + " " + f8 + " " + f9)
    print(" ")
    print("Left Face:")
    print(l1 + " " + l2 + " " + l3)
    print(l4 + " " + l5 + " " + l6)
    print(l7 + " " + l8 + " " + l9)
    print(" ")
    print("Right Face:")
    print(r1 + " " + r2 + " " + r3)
    print(r4 + " " + r5 + " " + r6)
    print(r7 + " " + r8 + " " + r9)
    print(" ")
    print("Back Face:")
    print(b1 + " " + b2 + " " + b3)
    print(b4 + " " + b5 + " " + b6)
    print(b7 + " " + b8 + " " + b9)
    print(" ")
    print("Top Face:")
    print(t1 + " " + t2 + " " + t3)
    print(t4 + " " + t5 + " " + t6)
    print(t7 + " " + t8 + " " + t9)
    print(" ")
    print("Bottom Face:")
    print(u1 + " " + u2 + " " + u3)
    print(u4 + " " + u5 + " " + u6)
    print(u7 + " " + u8 + " " + u9)

def Continuation():
            cont = input("Would you like to make another move? ")

            if cont == "yes" or "Yes":
                Rubiks(f1,f2,f3,f4,f5,f6,f7,f8,f9,l1,l2,l3,l4,l5,l6,l7,l8,l9,r1,r2,r3,r4,r5,r6,r7,r8,r9,u1,u2,u3,u4,u5,u6,u7,u8,u9,t1,t2,t3,t4,t5,t6,t7,t8,t9,b1,b2,b3,b4,b5,b6,b7,b8,b9)

            if cont == "no" or "No":
                Complete(f1,f2,f3,f4,f5,f6,f7,f8,f9,l1,l2,l3,l4,l5,l6,l7,l8,l9,r1,r2,r3,r4,r5,r6,r7,r8,r9,u1,u2,u3,u4,u5,u6,u7,u8,u9,t1,t2,t3,t4,t5,t6,t7,t8,t9,b1,b2,b3,b4,b5,b6,b7,b8,b9)

def Rubiks(f1,f2,f3,f4,f5,f6,f7,f8,f9,l1,l2,l3,l4,l5,l6,l7,l8,l9,r1,r2,r3,r4,r5,r6,r7,r8,r9,u1,u2,u3,u4,u5,u6,u7,u8,u9,t1,t2,t3,t4,t5,t6,t7,t8,t9,b1,b2,b3,b4,b5,b6,b7,b8,b9):
        move = input("Please type a move (F, F', R, R', U, U', B, B', L, L', D, D', where ' denotes an anticlockwise move ")

        ##################
        # Move instances #
        ##################

        if move == "F" or "f":

            # These handle the rotate around the edges of the moved side
            newt1=l3
            newt2=l6
            newt3=l9
            newr1=t7
            newr2=t8
            newr3=t9
            newu1=r7
            newu2=r4
            newu3=r1
            newl1=u1
            newl2=u2
            newl3=u3

            t9=newt1
            t8=newt2
            t7=newt3
            r1=newr1
            r4=newr2
            r7=newr3
            u3=newu1
            u2=newu2
            u1=newu3
            l3=newl1
            l6=newl2
            l9=newl3

            #This handles the rotation of the square that is being moved
            newtop1=f7
            newtop2=f4
            newtop3=f1
            newtop4=f8
            newtop6=f2
            newtop7=f9
            newtop8=f6
            newtop9=f3

            f1=newtop1
            f2=newtop2
            f3=newtop3
            f4=newtop4
            f6=newtop6
            f7=newtop7
            f8=newtop8
            f9=newtop9

            Continuation()(f1,f2,f3,f4,f5,f6,f7,f8,f9,l1,l2,l3,l4,l5,l6,l7,l8,l9,r1,r2,r3,r4,r5,r6,r7,r8,r9,u1,u2,u3,u4,u5,u6,u7,u8,u9,t1,t2,t3,t4,t5,t6,t7,t8,t9,b1,b2,b3,b4,b5,b6,b7,b8,b9)
        
        if move == "F'" or "f'":

            # These handle the rotate around the edges of the moved side
            newt1=r1
            newt2=r4
            newt3=r7
            newr1=u3
            newr2=u2
            newr3=u1
            newu1=l3
            newu2=l6
            newu3=l9
            newl1=t9
            newl2=t8
            newl3=t7

            t7=newt1
            t8=newt2
            t9=newt3
            r1=newr1
            r4=newr2
            r7=newr3
            u1=newu1
            u2=newu2
            u3=newu3
            l3=newl1
            l6=newl2
            l9=newl3

            #This handles the rotation of the square that is being moved
            newtop1=f3
            newtop2=f6
            newtop3=f9
            newtop4=f2
            newtop6=f8
            newtop7=f1
            newtop8=f4
            newtop9=f7

            f1=newtop1
            f2=newtop2
            f3=newtop3
            f4=newtop4
            f6=newtop6
            f7=newtop7
            f8=newtop8
            f9=newtop9


            Continuation()(f1,f2,f3,f4,f5,f6,f7,f8,f9,l1,l2,l3,l4,l5,l6,l7,l8,l9,r1,r2,r3,r4,r5,r6,r7,r8,r9,u1,u2,u3,u4,u5,u6,u7,u8,u9,t1,t2,t3,t4,t5,t6,t7,t8,t9,b1,b2,b3,b4,b5,b6,b7,b8,b9)

        if move == "R" or "r":

            # These handle the rotate around the edges of the moved side
            newt1=f3
            newt2=f6
            newt3=f9
            newb1=t9
            newb2=t6
            newb3=t3
            newu1=b7
            newu2=b4
            newu3=b1
            newf1=u3
            newf2=u6
            newf3=u9

            t3=newt1
            t6=newt2
            t9=newt3
            b1=newb1
            b4=newb2
            b7=newb3
            u3=newu1
            u6=newu2
            u9=newu3
            f3=newf1
            f6=newf2
            f9=newf3

            #This handles the rotation of the square that is being moved
            newtop1=r7
            newtop2=r4
            newtop3=r1
            newtop4=r8
            newtop6=r2
            newtop7=r9
            newtop8=r6
            newtop9=r3

            r1=newtop1
            r2=newtop2
            r3=newtop3
            r4=newtop4
            r6=newtop6
            r7=newtop7
            r8=newtop8
            r9=newtop9

Continuation()
        if move == "R'" or "r'":

            # These handle the rotate around the edges of the moved side
            newt1=b1
            newt2=b4
            newt3=b7
            newb1=u9
            newb2=u6
            newb3=u3
            newu1=f3
            newu2=f6
            newu3=f9
            newf1=t3
            newf2=t6
            newf3=t9

            t9=newt1
            t6=newt2
            t3=newt3
            b1=newb1
            b4=newb2
            b7=newb3
            u3=newu1
            u6=newu2
            u9=newu3
            f3=newf1
            f6=newf2
            f9=newf3

            #This handles the rotation of the square that is being moved
            newtop1=r3
            newtop2=r6
            newtop3=r9
            newtop4=r2
            newtop6=r8
            newtop7=r1
            newtop8=r4
            newtop9=r7

            r1=newtop1
            r2=newtop2
            r3=newtop3
            r4=newtop4
            r6=newtop6
            r7=newtop7
            r8=newtop8
            r9=newtop9

Continuation()
        if move == "U" or "u":

            # These handle the rotate around the edges of the moved side
            newf1=r1
            newf2=r2
            newf3=r3
            newr1=b1
            newr2=b2
            newr3=b3
            newl1=f1
            newl2=f2
            newl3=f3
            newb1=l1
            newb2=l2
            newb3=l3

            f1=newf1
            f2=newf2
            f3=newf3
            r1=newr1
            r2=newr2
            r3=newr3
            l1=newl1
            l2=newl2
            l3=newl3
            b1=newb1
            b2=newb2
            b3=newb3

            #This handles the rotation of the square that is being moved
            newtop1=t7
            newtop2=t4
            newtop3=t1
            newtop4=t8
            newtop6=t2
            newtop7=t9
            newtop8=t6
            newtop9=t3

            t1=newtop1
            t2=newtop2
            t3=newtop3
            t4=newtop4
            t6=newtop6
            t7=newtop7
            t8=newtop8
            t9=newtop9

Continuation()
        if move == "U'" or "u'":

            # These handle the rotate around the edges of the moved side
            newf1=l1
            newf2=l2
            newf3=l3
            newr1=f1
            newr2=f2
            newr3=f3
            newb1=r1
            newb2=r2
            newb3=r3
            newl1=b1
            newl2=b2
            newl3=b3

            f1=newf1
            f2=newf2
            f3=newf3
            r1=newr1
            r2=newr2
            r3=newr3
            b1=newb1
            b2=newb2
            b3=newb3
            l1=newl1
            l2=newl2
            l3=newl3

            #This handles the rotation of the square that is being moved
            newtop1=u3
            newtop2=u6
            newtop3=u9
            newtop4=u2
            newtop6=u8
            newtop7=u1
            newtop8=u4
            newtop9=u7

            u1=newtop1
            u2=newtop2
            u3=newtop3
            u4=newtop4
            u6=newtop6
            u7=newtop7
            u8=newtop8
            u9=newtop9

Continuation()
        if move == "B" or "b":

            # These handle the rotate around the edges of the moved side
            newr1=u9
            newr2=u8
            newr3=u7
            newt1=r3
            newt2=r6
            newt3=r9
            newl1=t3
            newl2=t2
            newl3=t1
            newu1=l1
            newu2=l4
            newu3=l7

            r3=newr1
            r6=newr2
            r9=newr3
            t1=newt1
            t2=newt2
            t3=newt3
            l1=newl1
            l4=newl2
            l7=newl3
            u7=newu1
            u8=newu2
            u9=newu3

            #This handles the rotation of the square that is being moved
            newtop1=b7
            newtop2=b4
            newtop3=b1
            newtop4=b8
            newtop6=b2
            newtop7=b9
            newtop8=b6
            newtop9=b3

            b1=newtop1
            b2=newtop2
            b3=newtop3
            b4=newtop4
            b6=newtop6
            b7=newtop7
            b8=newtop8
            b9=newtop9

Continuation()
        if move == "B'" or "b'":

            # These handle the rotate around the edges of the moved side
            newr1=t1
            newr2=t2
            newr3=t3
            newt1=l7
            newt2=l4
            newt3=l1
            newl1=u7
            newl2=u8
            newl3=u9
            newu1=r9
            newu2=r6
            newu3=r3

            r3=newr1
            r6=newr2
            r9=newr3
            t1=newt1
            t2=newt2
            t3=newt3
            l1=newl1
            l4=newl2
            l7=newl3
            u7=newu1
            u8=newu2
            u9=newu3

            #This handles the rotation of the square that is being moved
            newtop1=b3
            newtop2=b6
            newtop3=b9
            newtop4=b2
            newtop6=b8
            newtop7=b1
            newtop8=b4
            newtop9=b7

            b1=newtop1
            b2=newtop2
            b3=newtop3
            b4=newtop4
            b6=newtop6
            b7=newtop7
            b8=newtop8
            b9=newtop9

Continuation()
        if move == "L" or "l":

            # These handle the rotate around the edges of the moved side
            newt1=b9
            newt2=b6
            newt3=b3
            newb1=u7
            newb2=u4
            newb3=u1
            newu1=f1
            newu2=f4
            newu3=f7
            newf1=t1
            newf2=t4
            newf3=t7

            t1=newt1
            t4=newt2
            t7=newt3
            b3=newb1
            b6=newb2
            b9=newb3
            u1=newu1
            u4=newu2
            u7=newu3
            f1=newf1
            f4=newf2
            f7=newf3

            #This handles the rotation of the square that is being moved
            newtop1=l7
            newtop2=l4
            newtop3=l1
            newtop4=l8
            newtop6=l2
            newtop7=l9
            newtop8=l6
            newtop9=l3

            l1=newtop1
            l2=newtop2
            l3=newtop3
            l4=newtop4
            l6=newtop6
            l7=newtop7
            l8=newtop8
            l9=newtop9
            
Continuation()
        if move == "L'" or "l'":

            # These handle the rotate around the edges of the moved side
            newt1=f1
            newt2=f4
            newt3=f7
            newb1=t7
            newb2=t4
            newb3=t1
            newu1=b9
            newu2=b6
            newu3=b3
            newf1=u1
            newf2=u4
            newf3=u7

            t1=newt1
            t4=newt2
            t7=newt3
            b3=newb1
            b6=newb2
            b9=newb3
            u1=newu1
            u4=newu2
            u7=newu3
            f1=newf1
            f4=newf2
            f7=newf3

            #This handles the rotation of the square that is being moved
            newtop1=b3
            newtop2=b6
            newtop3=b9
            newtop4=b2
            newtop6=b8
            newtop7=b1
            newtop8=b4
            newtop9=b7

            b1=newtop1
            b2=newtop2
            b3=newtop3
            b4=newtop4
            b6=newtop6
            b7=newtop7
            b8=newtop8
            b9=newtop9

Continuation()
        if move == "D" or "d":

            # These handle the rotate around the edges of the moved side
            newf1=l7
            newf2=l8
            newf3=l9
            newr1=f7
            newr2=f8
            newr3=f9
            newb1=r7
            newb2=r8
            newb3=r9
            newl1=b7
            newl2=b8
            newl3=b9


            f7=newf1
            f8=newf2
            f9=newf3
            r7=newr1
            r8=newr2
            r9=newr3
            b7=newb1
            b8=newb2
            b9=newb3
            l7=newl1
            l8=newl2
            l9=newl3

            #This handles the rotation of the square that is being moved
            newtop1=u7
            newtop2=u4
            newtop3=u1
            newtop4=u8
            newtop6=u2
            newtop7=u9
            newtop8=u6
            newtop9=u3

            u1=newtop1
            u2=newtop2
            u3=newtop3
            u4=newtop4
            u6=newtop6
            u7=newtop7
            u8=newtop8
            u9=newtop9

Continuation()
        if move == "D'" or "d'":

            # These handle the rotate around the edges of the moved side
            newf1=r7
            newf2=r8
            newf3=r9
            newr1=b7
            newr2=b8
            newr3=b9
            newb1=l7
            newb2=l8
            newb3=l9
            newl1=f7
            newl2=f8
            newl3=f9
            

            f7=newf1
            f8=newf2
            f9=newf3
            r7=newr1
            r8=newr2
            r9=newr3
            b7=newb1
            b8=newb2
            b9=newb3
            l7=newl1
            l8=newl2
            l9=newl3

            #This handles the rotation of the square that is being moved
            newtop1=u3
            newtop2=u6
            newtop3=u9
            newtop4=u2
            newtop6=u8
            newtop7=u1
            newtop8=u4
            newtop9=u7

            u1=newtop1
            u2=newtop2
            u3=newtop3
            u4=newtop4
            u6=newtop6
            u7=newtop7
            u8=newtop8
            u9=newtop9

Continuation()
Main()
