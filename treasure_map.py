print("""
 /\  /\  /\  /\  /\  /\  /\  /\  /\  /\  /\  /\  /\  /\  /\  /\  /\  /\  /\  /\  /\  /\ 
//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\
\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//
 \/  \/  \/  \/  \/  \/  \/  \/  \/  \/  \/  \/  \/  \/  \/  \/  \/  \/  \/  \/  \/  \/ 
 /\                                                                                  /\ 
//\\  ________  __                  __        ________  __                          //\\
\\// |        \|  \                |  \      |        \|  \                         \\//
 \/  | $$$$$$$$ \$$ _______    ____| $$       \$$$$$$$$| $$____    ______            \/ 
 /\  | $$__    |  \|       \  /      $$         | $$   | $$    \  /      \           /\ 
//\\ | $$  \   | $$| $$$$$$$\|  $$$$$$$         | $$   | $$$$$$$\|  $$$$$$\         //\\
\\// | $$$$$   | $$| $$  | $$| $$  | $$         | $$   | $$  | $$| $$    $$         \\//
 \/  | $$      | $$| $$  | $$| $$__| $$         | $$   | $$  | $$| $$$$$$$$          \/ 
 /\  | $$      | $$| $$  | $$ \$$    $$         | $$   | $$  | $$ \$$     \          /\ 
//\\  \$$       \$$ \$$   \$$  \$$$$$$$          \$$    \$$   \$$  \$$$$$$$         //\\
\\//                                                                                \\//
 \/                                                                                  \/ 
 /\                                                                                  /\ 
//\\  ________                                                                      //\\
\\// |        \                                                                     \\//
 \/   \$$$$$$$$______    ______    ______    _______  __    __   ______    ______    \/ 
 /\     | $$  /      \  /      \  |      \  /       \|  \  |  \ /      \  /      \   /\ 
//\\    | $$ |  $$$$$$\|  $$$$$$\  \$$$$$$\|  $$$$$$$| $$  | $$|  $$$$$$\|  $$$$$$\ //\\
\\//    | $$ | $$   \$$| $$    $$ /      $$ \$$    \ | $$  | $$| $$   \$$| $$    $$ \\//
 \/     | $$ | $$      | $$$$$$$$|  $$$$$$$ _\$$$$$$\| $$__/ $$| $$      | $$$$$$$$  \/ 
 /\     | $$ | $$       \$$     \ \$$    $$|       $$ \$$    $$| $$       \$$     \  /\ 
//\\     \$$  \$$        \$$$$$$$  \$$$$$$$ \$$$$$$$   \$$$$$$  \$$        \$$$$$$$ //\\
\\//                                                                                \\//
 \/                                                                                  \/ 
 /\  /\  /\  /\  /\  /\  /\  /\  /\  /\  /\  /\  /\  /\  /\  /\  /\  /\  /\  /\  /\  /\ 
//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\
\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//
 \/  \/  \/  \/  \/  \/  \/  \/  \/  \/  \/  \/  \/  \/  \/  \/  \/  \/  \/  \/  \/  \/ 
""")

print("Welcome to the Treasure Island.")
print("Your mission is to find the treasure.")
path_1 = input('''You're at a cross road. Where do you want to go?
        left or right?\n''')

if (path_1 == "left"):
    print("Congrats! You survived.")
    path_2 = input('''You have arrived at a wide river. What will you do?
            a. Wait for a boat
            b. Swim across\n''')

    if (path_2 == "a"):
        print("Congrats! You survived.")
        path_3 = input('''You have reached an island with two caves. Which one do you enter?
                       a. Cave with torches
                       b. Dark Cave\n''')
        if (path_3 == "a"):
            print("Congrats! You survived.")
            path_4 = input('''You have reached an ancient temple, there are two levers. Which one will you pull?
                           a. Golden Lever
                           b. Rusty Lever\n''')
            if (path_4 == "a"):
                print("Congrats! You survived.")
                path_5 = input('''Hell yeah, You have two chests sit in front of you. Which one will you open?
                               a. Emerald Chest
                               b. Ruby Chest\n''')
                if (path_5 == "b"):
                    print("Congrats! You found the treasure.")
                    print("🥳🥳🥳")
                else:
                    print("BOOM! You just bursted yourself. Game Over!")
            else:
                print("Oh No! You activated a booby trap. Game Over!")
        else:
            print("Oh No! You fell into a trap. Game Over!")
    else:
        print("Oh No! You got eaten by the crocodiles. Game Over!")
else:
    print("Oh No! You entered a Snake Pit. Game Over!")
