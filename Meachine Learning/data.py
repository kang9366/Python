import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#데이터 전처리
file_path = './data/chipotle.csv'

#sep = seperate, 탭으로 구분한다.
chipo = pd.read_csv(file_path)

#fild 은 dataframe으로 받는다
print(type(chipo))
print(chipo)

tmp_arr=chipo['item_name'].unique()
len(tmp_arr)
print(tmp_arr)

chipo['item_price']=chipo['item_price'].str.lstrip('$')

#집계를 위해 기존 str타입을 float(실수)로 변환
chipo['item_price'].astype(float)

chipo_cost=chipo.groupby('item_name')['item_price'].mean()
chipo_cost.sort_values(ascending=False)


chipo = pd.read_csv(file_path)
chipo.drop(['order_id', 'item_price'], axis='columns', inplace=True)
chipo['choice_description'].fillna('Origin', inplace = True)
print(chipo)

#판매 순위 알아보기
result_tmp=chipo.groupby(['item_name','saurce'])['ingredient'].value_counts()
result_tmp=result_tmp.to_frame()
result_tmp

file_path='./data/chipotle_result.csv'
result_tmp.to_csv(file_path,sep=',')

###시각화
##가장 잘 팔린 메뉴 10개
#차트의 크기를 조정. (가로, 세로)
plt.rcParams["figure.figsize"] = (20,10)

#차트 눈금선을 표기
plt.rcParams['axes.grid'] = True 

#'item_name'과 'quantity'를 별도로 추출
temp_df=pd.DataFrame({'item_name':temp.index,'quantity':temp.values})
x=temp_df['item_name']
y=temp_df['quantity']

plt.bar(x,y)
plt.xlabel('x=item_name')
plt.ylabel('y=quantity')
plt.title('Best Top10')
plt.show()

##식당 사장이 주문해야 할 재료 수량 파악
#음식마다 들어간 'ingredients' 각각의 총합을 알기 위해, 모든 데이터를 추출하여 배열로 재조합
sum=''
for i in chipo['ingredients'] :
    if i !='Origin' :
        sum+=i.strip()
        
arr=sum.split(',')

#한 줄의 배열로 재조합 한 뒤, 재료별로 합쳐 갯수를 세아리기 위해 DataFrame으로 재변환
df=pd.DataFrame(arr,columns=['ingredients'])
df_Top10=df['ingredients'].value_counts().head(10)

#차트로 나타내기 위한 과정
df_temp=pd.DataFrame({'ingredients':df_Top10.index, 'amounts':df_Top10.values})
x=df_temp['ingredients']
y=df_temp['amounts']

plt.bar(x,y)
plt.xlabel('x=ingredients')
plt.ylabel('y=amounts')
plt.show()