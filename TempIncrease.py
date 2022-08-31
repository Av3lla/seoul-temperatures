import pandas as pd
import matplotlib.pyplot as plt
import time


#기상청자료개방포털 기후통계분석 데이터 파일 읽어오기
data = pd.read_csv('./temperatures.csv', encoding='cp949')

#데이터에서 연도, 연평균기온, 연최저기온, 연최고기온 추출
year_dataframe = data['연도']
year = list(year_dataframe.values)

avg_dataframe = data['평균기온']
avg = list(avg_dataframe.values)

low_dataframe = data['최저기온']
low = list(low_dataframe.values)

high_dataframe = data['최고기온']
high = list(high_dataframe.values)

#연도별 평균, 최저, 최고 기온 분류
dict_avg = {name:value for name, value in zip(year, avg)}
dict_low = {name:value for name, value in zip(year, low)}
dict_high = {name:value for name, value in zip(year, high)}


#변수선언
graph = ''


#명령 입력받기
while True:
    print("\n----------------------------------------------------------------------------------------------------")
    print("현재 사용 가능: \"0000평균기온\", \"0000최저기온\", \"0000최고기온\", \"그래프표시\"\n")
    user = input("하고싶은 것을 입력하세요.: ")
    user_year = user[:4]
    user_want = user[4:]

    time.sleep(1)

    if user_want == '평균기온':
        print(f"\n{user_year}년의 평균기온은 {dict_avg[int(user_year)]}℃ 입니다.")
    elif user_want == '최저기온':
        print(f"\n{user_year}년의 최저기온은 {dict_low[int(user_year)]}℃ 입니다.")
    elif user_want == '최고기온':
        print(f"\n{user_year}년의 최고기온은 {dict_high[int(user_year)]}℃ 입니다.")


    #그래프 그리기
    if user == '그래프표시':
        graph = ''
        
        plt.xlabel('Year')
        plt.ylabel('Temperature')

        plt.xlim([1907, 2021])
        plt.ylim([-30, 50])

        plt.plot(year, avg, label='average')
        plt.plot(year, low, label='lowest')
        plt.plot(year, high, label='highest')

        plt.legend(loc=(0.01, 0.9))

        plt.show()

    time.sleep(1.5)


    isContinue = input("\n계속하시겠습니까?: ")

    if isContinue == 'y':
        isContinue = ''
        time.sleep(1)
        continue
    elif isContinue == 'n':
        print("\n----------------------------------------------------------------------------------------------------")
        print("\n프로그램을 종료합니다.")
        break
    else:
        print("----------------------------------------------------------------------------------------------------")
        print("\n잘못된 입력입니다.")
        break