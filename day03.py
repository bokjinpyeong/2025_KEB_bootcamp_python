import random
drinks = ["위스키", "와인", "소주", "고량주" ]
foods = ["초콜릿", "치즈", "삼겹살", "양꼬치"]

drinks.insert(4,"사케")
foods.insert(4,"광어회")
a="ㅇ칸녕"

print(len(a))

while True:
    ramdom_number = random.randint(0, len(drinks)-1)
    random_drinks = drinks[ramdom_number]
    ramdom_foods = foods[ramdom_number]
    menu = input(f'다음 술중에 고르세요.\n1) {drinks[0]}   2) {drinks[1]}   3) {drinks[2]}   4) {drinks[3]}   5) {drinks[4]} 6) random 7) 종료 : ')
    if menu == '1':
        print(f'{drinks[0]}에 어울리는 안주는 {foods[0]} 입니다')
    elif menu == '2':
        print(f'{drinks[1]}에 어울리는 안주는 {foods[1]} 입니다')
    elif menu == '3':
        print(f'{drinks[2]}에 어울리는 안주는 {foods[2]} 입니다')
    elif menu == '4':
        print(f'{drinks[3]}에 어울리는 안주는 {foods[3]} 입니다')
    elif menu == '5':
        print(f'{drinks[4]}에 어울리는 안주는 {foods[4]} 입니다')
    elif menu == '6':
        print(f'{random_drinks}에 어울리는 안주는 {ramdom_foods} 입니다')
    elif menu == '7':
        print(f'다음에 또 오세요')
        break