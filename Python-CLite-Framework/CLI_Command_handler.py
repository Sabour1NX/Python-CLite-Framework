class Command_handler :
    def __init__ (self):
        self.IsLoop = True

    def help(self):
        print(f"\nCurrent command list:\n{'-'*20}\nexit : Exit the program.\n")
        #print("")请输入help命令提示

    #def helloworld (self,j=int(1)):
    #    j = int(j)
    #    for i in range (j) :
    #        print("Helloworld!")

    #输入你的函数

    def exit(self):
        print("Exiting ...")
        self.IsLoop = False

def main (Script_name = 'I_Script' ):#命名脚本
    try:
        Current_handler = Command_handler()
        print(f"Wellcome to {Script_name}!\nInput 'help' to check commands.")

        while Current_handler.IsLoop:
            print("Please input your command : ")
            usr_Input = input().strip()

            if not usr_Input :
                continue

            cmd_parts = usr_Input.split()
            command = cmd_parts[0]
            args = cmd_parts[1:]
            
            try:
                Target_handler = getattr(Current_handler,command)
                Target_handler(*args)
            except AttributeError:
                print(f"Unknown command : '{command}' !\n")
            except ValueError as e:
                print(f"ValueError : '{e}'")
            except Exception as e:
                print(f"Except : '{e}'")
    except KeyboardInterrupt:
        print("KeyboardInterrupted,exiting...")

if __name__ == "__main__":
    main()