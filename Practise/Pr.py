def main():

    
    
    for case in range(int(input())):
        n, k, m = map(int,input().split())
        s = str(input("Enter power string (S): "))
        ballpower = [int(i) for i in list(s)]
        current_level = 0

        while (current_level < m):
            temp_list = []
            ballpower = [whiteball * k for whiteball in ballpower]
            for whiteball in ballpower:
                if (whiteball > 9):
                    digit = [int(i) for i in str(whiteball)]
                    temp_list.extend(digit)
                else:
                    temp_list.append(whiteball)
            ballpower = temp_list
            current_level+=1
        
        print(len(ballpower))

main()