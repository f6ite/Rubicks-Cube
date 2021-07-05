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

    Rubicks(f1,f2,f3,f4,f5,f6,f7,f8,f9,l1,l2,l3,l4,l5,l6,l7,l8,l9,r1,r2,r3,r4,r5,r6,r7,r8,r9,u1,u2,u3,u4,u5,u6,u7,u8,u9,t1,t2,t3,t4,t5,t6,t7,t8,t9,b1,b2,b3,b4,b5,b6,b7,b8,b9)

def Complete(f1,f2,f3,f4,f5,f6,f7,f8,f9,l1,l2,l3,l4,l5,l6,l7,l8,l9,r1,r2,r3,r4,r5,r6,r7,r8,r9,u1,u2,u3,u4,u5,u6,u7,u8,u9,t1,t2,t3,t4,t5,t6,t7,t8,t9,b1,b2,b3,b4,b5,b6,b7,b8,b9):
    #There's probably a better way to do this, but this will work for demonstration purposes
    print("The completed Rubicks(f1,f2,f3,f4,f5,f6,f7,f8,f9,l1,l2,l3,l4,l5,l6,l7,l8,l9,r1,r2,r3,r4,r5,r6,r7,r8,r9,u1,u2,u3,u4,u5,u6,u7,u8,u9,t1,t2,t3,t4,t5,t6,t7,t8,t9,b1,b2,b3,b4,b5,b6,b7,b8,b9) cube is as follows:")
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

def Rubicks(f1,f2,f3,f4,f5,f6,f7,f8,f9,l1,l2,l3,l4,l5,l6,l7,l8,l9,r1,r2,r3,r4,r5,r6,r7,r8,r9,u1,u2,u3,u4,u5,u6,u7,u8,u9,t1,t2,t3,t4,t5,t6,t7,t8,t9,b1,b2,b3,b4,b5,b6,b7,b8,b9):
        move = input("Please type first move (F, F', R, R', U, U', B, B', L, L', D, D', where ' denotes an anticlockwise move ")

        ##################
        # Move instances #
        ##################

        if move == "F":
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

            cont = input("Would you like to make another move? ")

            if cont == "yes":
                Rubicks(f1,f2,f3,f4,f5,f6,f7,f8,f9,l1,l2,l3,l4,l5,l6,l7,l8,l9,r1,r2,r3,r4,r5,r6,r7,r8,r9,u1,u2,u3,u4,u5,u6,u7,u8,u9,t1,t2,t3,t4,t5,t6,t7,t8,t9,b1,b2,b3,b4,b5,b6,b7,b8,b9)

            if cont == "no":
                Complete(f1,f2,f3,f4,f5,f6,f7,f8,f9,l1,l2,l3,l4,l5,l6,l7,l8,l9,r1,r2,r3,r4,r5,r6,r7,r8,r9,u1,u2,u3,u4,u5,u6,u7,u8,u9,t1,t2,t3,t4,t5,t6,t7,t8,t9,b1,b2,b3,b4,b5,b6,b7,b8,b9)
        
        if move == "F'":
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

            cont = input("Would you like to make another move? ")

            if cont == "yes":
                Rubicks(f1,f2,f3,f4,f5,f6,f7,f8,f9,l1,l2,l3,l4,l5,l6,l7,l8,l9,r1,r2,r3,r4,r5,r6,r7,r8,r9,u1,u2,u3,u4,u5,u6,u7,u8,u9,t1,t2,t3,t4,t5,t6,t7,t8,t9,b1,b2,b3,b4,b5,b6,b7,b8,b9)

            if cont == "no":
                Complete(f1,f2,f3,f4,f5,f6,f7,f8,f9,l1,l2,l3,l4,l5,l6,l7,l8,l9,r1,r2,r3,r4,r5,r6,r7,r8,r9,u1,u2,u3,u4,u5,u6,u7,u8,u9,t1,t2,t3,t4,t5,t6,t7,t8,t9,b1,b2,b3,b4,b5,b6,b7,b8,b9)

        if move == "R":
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

            cont = input("Would you like to make another move? ")

            if cont == "yes":
                Rubicks(f1,f2,f3,f4,f5,f6,f7,f8,f9,l1,l2,l3,l4,l5,l6,l7,l8,l9,r1,r2,r3,r4,r5,r6,r7,r8,r9,u1,u2,u3,u4,u5,u6,u7,u8,u9,t1,t2,t3,t4,t5,t6,t7,t8,t9,b1,b2,b3,b4,b5,b6,b7,b8,b9)

            if cont == "no":
                Complete(f1,f2,f3,f4,f5,f6,f7,f8,f9,l1,l2,l3,l4,l5,l6,l7,l8,l9,r1,r2,r3,r4,r5,r6,r7,r8,r9,u1,u2,u3,u4,u5,u6,u7,u8,u9,t1,t2,t3,t4,t5,t6,t7,t8,t9,b1,b2,b3,b4,b5,b6,b7,b8,b9)
        
        if move == "R'":
            newt1=b1#
            newt2=b4#
            newt3=b7#
            newb1=u9#
            newb2=u6#
            newb3=u3#
            newu1=f3#
            newu2=f6#
            newu3=f9#
            newf1=t3
            newf2=t6
            newf3=t9

            t9=newt1#
            t6=newt2#
            t3=newt3#
            b1=newb1#
            b4=newb2#
            b7=newb3#
            u3=newu1#
            u6=newu2#
            u9=newu3#
            f3=newf1
            f6=newf2
            f9=newf3

            cont = input("Would you like to make another move? ")

            if cont == "yes":
                Rubicks(f1,f2,f3,f4,f5,f6,f7,f8,f9,l1,l2,l3,l4,l5,l6,l7,l8,l9,r1,r2,r3,r4,r5,r6,r7,r8,r9,u1,u2,u3,u4,u5,u6,u7,u8,u9,t1,t2,t3,t4,t5,t6,t7,t8,t9,b1,b2,b3,b4,b5,b6,b7,b8,b9)

            if cont == "no":
                Complete(f1,f2,f3,f4,f5,f6,f7,f8,f9,l1,l2,l3,l4,l5,l6,l7,l8,l9,r1,r2,r3,r4,r5,r6,r7,r8,r9,u1,u2,u3,u4,u5,u6,u7,u8,u9,t1,t2,t3,t4,t5,t6,t7,t8,t9,b1,b2,b3,b4,b5,b6,b7,b8,b9)

        if move == "U":
            # U move affects Front, Right, Left, Back
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

            cont = input("Would you like to make another move? ")

            if cont == "yes":
                Rubicks(f1,f2,f3,f4,f5,f6,f7,f8,f9,l1,l2,l3,l4,l5,l6,l7,l8,l9,r1,r2,r3,r4,r5,r6,r7,r8,r9,u1,u2,u3,u4,u5,u6,u7,u8,u9,t1,t2,t3,t4,t5,t6,t7,t8,t9,b1,b2,b3,b4,b5,b6,b7,b8,b9)

            if cont == "no":
                Complete(f1,f2,f3,f4,f5,f6,f7,f8,f9,l1,l2,l3,l4,l5,l6,l7,l8,l9,r1,r2,r3,r4,r5,r6,r7,r8,r9,u1,u2,u3,u4,u5,u6,u7,u8,u9,t1,t2,t3,t4,t5,t6,t7,t8,t9,b1,b2,b3,b4,b5,b6,b7,b8,b9)

        if move == "U'":
            # U move affects Front, Right, Left, Back
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

            cont = input("Would you like to make another move? ")

            if cont == "yes":
                Rubicks(f1,f2,f3,f4,f5,f6,f7,f8,f9,l1,l2,l3,l4,l5,l6,l7,l8,l9,r1,r2,r3,r4,r5,r6,r7,r8,r9,u1,u2,u3,u4,u5,u6,u7,u8,u9,t1,t2,t3,t4,t5,t6,t7,t8,t9,b1,b2,b3,b4,b5,b6,b7,b8,b9)
            if cont == "no":
                Complete(f1,f2,f3,f4,f5,f6,f7,f8,f9,l1,l2,l3,l4,l5,l6,l7,l8,l9,r1,r2,r3,r4,r5,r6,r7,r8,r9,u1,u2,u3,u4,u5,u6,u7,u8,u9,t1,t2,t3,t4,t5,t6,t7,t8,t9,b1,b2,b3,b4,b5,b6,b7,b8,b9)

        if move == "B":
            #B Move affects Right, Top, Left, Bottom
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

            cont = input("Would you like to make another move? ")

            if cont == "yes":
                Rubicks(f1,f2,f3,f4,f5,f6,f7,f8,f9,l1,l2,l3,l4,l5,l6,l7,l8,l9,r1,r2,r3,r4,r5,r6,r7,r8,r9,u1,u2,u3,u4,u5,u6,u7,u8,u9,t1,t2,t3,t4,t5,t6,t7,t8,t9,b1,b2,b3,b4,b5,b6,b7,b8,b9)
            if cont == "no":
                Complete(f1,f2,f3,f4,f5,f6,f7,f8,f9,l1,l2,l3,l4,l5,l6,l7,l8,l9,r1,r2,r3,r4,r5,r6,r7,r8,r9,u1,u2,u3,u4,u5,u6,u7,u8,u9,t1,t2,t3,t4,t5,t6,t7,t8,t9,b1,b2,b3,b4,b5,b6,b7,b8,b9)

        if move == "B'":
            #B Move affects Right, Top, Left, Bottom
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

            cont = input("Would you like to make another move? ")

            if cont == "yes":
                Rubicks(f1,f2,f3,f4,f5,f6,f7,f8,f9,l1,l2,l3,l4,l5,l6,l7,l8,l9,r1,r2,r3,r4,r5,r6,r7,r8,r9,u1,u2,u3,u4,u5,u6,u7,u8,u9,t1,t2,t3,t4,t5,t6,t7,t8,t9,b1,b2,b3,b4,b5,b6,b7,b8,b9)
            if cont == "no":
                Complete(f1,f2,f3,f4,f5,f6,f7,f8,f9,l1,l2,l3,l4,l5,l6,l7,l8,l9,r1,r2,r3,r4,r5,r6,r7,r8,r9,u1,u2,u3,u4,u5,u6,u7,u8,u9,t1,t2,t3,t4,t5,t6,t7,t8,t9,b1,b2,b3,b4,b5,b6,b7,b8,b9)

        if move == "L":
            #L move affects Front, Top, Back, Bottom
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

            cont = input("Would you like to make another move? ")

            if cont == "yes":
                Rubicks(f1,f2,f3,f4,f5,f6,f7,f8,f9,l1,l2,l3,l4,l5,l6,l7,l8,l9,r1,r2,r3,r4,r5,r6,r7,r8,r9,u1,u2,u3,u4,u5,u6,u7,u8,u9,t1,t2,t3,t4,t5,t6,t7,t8,t9,b1,b2,b3,b4,b5,b6,b7,b8,b9)

            if cont == "no":
                Complete(f1,f2,f3,f4,f5,f6,f7,f8,f9,l1,l2,l3,l4,l5,l6,l7,l8,l9,r1,r2,r3,r4,r5,r6,r7,r8,r9,u1,u2,u3,u4,u5,u6,u7,u8,u9,t1,t2,t3,t4,t5,t6,t7,t8,t9,b1,b2,b3,b4,b5,b6,b7,b8,b9)
        
        if move == "L'":
            #L move affects Front, Top, Back, Bottom
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

            cont = input("Would you like to make another move? ")

            if cont == "yes":
                Rubicks(f1,f2,f3,f4,f5,f6,f7,f8,f9,l1,l2,l3,l4,l5,l6,l7,l8,l9,r1,r2,r3,r4,r5,r6,r7,r8,r9,u1,u2,u3,u4,u5,u6,u7,u8,u9,t1,t2,t3,t4,t5,t6,t7,t8,t9,b1,b2,b3,b4,b5,b6,b7,b8,b9)
            if cont == "no":
                Complete(f1,f2,f3,f4,f5,f6,f7,f8,f9,l1,l2,l3,l4,l5,l6,l7,l8,l9,r1,r2,r3,r4,r5,r6,r7,r8,r9,u1,u2,u3,u4,u5,u6,u7,u8,u9,t1,t2,t3,t4,t5,t6,t7,t8,t9,b1,b2,b3,b4,b5,b6,b7,b8,b9)

        if move == "D":
            #D move affects Front, Right, Back, Left
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

            cont = input("Would you like to make another move? ")

            if cont == "yes":
                Rubicks(f1,f2,f3,f4,f5,f6,f7,f8,f9,l1,l2,l3,l4,l5,l6,l7,l8,l9,r1,r2,r3,r4,r5,r6,r7,r8,r9,u1,u2,u3,u4,u5,u6,u7,u8,u9,t1,t2,t3,t4,t5,t6,t7,t8,t9,b1,b2,b3,b4,b5,b6,b7,b8,b9)

            if cont == "no":
                Complete(f1,f2,f3,f4,f5,f6,f7,f8,f9,l1,l2,l3,l4,l5,l6,l7,l8,l9,r1,r2,r3,r4,r5,r6,r7,r8,r9,u1,u2,u3,u4,u5,u6,u7,u8,u9,t1,t2,t3,t4,t5,t6,t7,t8,t9,b1,b2,b3,b4,b5,b6,b7,b8,b9)
        
        if move == "D'":
            #D move affects Front, Right, Back, Left
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

            cont = input("Would you like to make another move? ")

            if cont == "yes":
                Rubicks(f1,f2,f3,f4,f5,f6,f7,f8,f9,l1,l2,l3,l4,l5,l6,l7,l8,l9,r1,r2,r3,r4,r5,r6,r7,r8,r9,u1,u2,u3,u4,u5,u6,u7,u8,u9,t1,t2,t3,t4,t5,t6,t7,t8,t9,b1,b2,b3,b4,b5,b6,b7,b8,b9)
            if cont == "no":
                Complete(f1,f2,f3,f4,f5,f6,f7,f8,f9,l1,l2,l3,l4,l5,l6,l7,l8,l9,r1,r2,r3,r4,r5,r6,r7,r8,r9,u1,u2,u3,u4,u5,u6,u7,u8,u9,t1,t2,t3,t4,t5,t6,t7,t8,t9,b1,b2,b3,b4,b5,b6,b7,b8,b9)

Main()
