# Assignment
# v2.4) 메뉴 삭제 추가에 대응되는 코드를 추가하시오.
import random


#
# d_s_p={"위스키" : ['초콜릿', 50_000]}
# print(d_s_p["위스키"])
# print(d_s_p["위스키"][1])



drinks = ["위스키", "와인", "소주", "고량주"]
snacks = ["초콜릿", "치즈", "삽겹살", "양꼬치"]
prices=[50000, 30000, 5000, 7500]
def print_menu(n):
    print(f'{drinks[n]}에 어울리는 안주는 {snacks[n]} 입니다')




drinks.append("사케")
snacks.append("광어회")
prices.append(40000)
snacks[0] = "낙곱새"

drinks.append("데킬라")
snacks.append("소금")
prices.append(50000)

menu_list = '다음 술중에 고르세요.\n'
for i in range(len(drinks)):
    menu_list = menu_list + f'{i+1}) {drinks[i]}  '
menu_list = menu_list + f'{len(drinks)+1}) 아무거나  {len(drinks)+2}) 종료 : '
#print(menu_list)

# f'다음 술중에 고르세요.\n1) {drinks[0]}   2) {drinks[1]}   3) {drinks[2]}   4) {drinks[3]}   5) {drinks[4]}   6) 아무거나   7) 종료 : '
while True:
    menu = int(input(menu_list))
    if 1 <= menu<=len(drinks):
        print_menu(int(menu) - 1)
    # if menu == '1':
    #     print_menu(int(menu)-1)
    # elif menu == '2':
    #     print_menu(int(menu)-1)
    # elif menu == '3':
    #     print_menu(int(menu)-1)
    # elif menu == '4':
    #     print_menu(int(menu) - 1)
    # elif menu == '5':
    #     print_menu(int(menu)-1)
    elif menu == len(drinks)+1:
        random_index = random.randint(0, len(drinks)-1)
        print(f'{drinks[random_index]}에 어울리는 안주는 {snacks[random_index]} 입니다')
    elif menu == len(drinks)+2:
        print(f'다음에 또 오세요')
        break