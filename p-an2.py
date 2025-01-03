import streamlit as st

#로딩 풍선
# import time 

# # 방법 1 progress bar 
# latest_iteration = st.empty()
# bar = st.progress(0)

# for i in range(100):
#   # Update the progress bar with each iteration.
#   latest_iteration.text(f'Iteration {i+1}')
#   bar.progress(i + 1)
#   time.sleep(0.05)
#   # 0.05 초 마다 1씩증가

# st.balloons()
# # 시간 다 되면 풍선 이펙트 보여주기 

# 빈칸
# st.header('')


#과과연 프로젝트
#sidebar 추가
st.sidebar.title('피겨스케이트 분석가 :ice_skate:')

#sidebar 선택 박스
whattodo = st.sidebar.selectbox(
    '무엇을 알아보시겠습니까?',
    ('선택지 없음','이론적 원리 탐구', '자세 교정 프로그램'), 
    index=0
)

if whattodo == '선택지 없음':
    # 타이틀 적용 예시
    st.title('과학과제연구 프로젝트')

    # 캡션 적용
    st.caption('20905 김세은')


    # divider 삽입
    st.divider()

    # Subheader 적용
    st.subheader('안녕하세요! :sparkles:')
    st.markdown("피겨의 채점기준에는 기술점, 구성점 등이 있습니다.")
    st.markdown("그 중 **기술점**은 점프, 스핀, 스텝을 요소로 하여 채점하며, 이 중에서 점프의 감점 요인으로 :violet[회전수 부족]과 :violet[엣지 오류] 등이 있습니다.")
    st.markdown("**:blue[회전수 부족이 되는 이유와 회전수를 채우기 위한 방법을 탐구]** 하고, 이중에서 감점 요인에 부합하지 않기 위해 **:blue[팔의 자세를 교정하는 프로그램]** 을 제작하였습니다.")
elif whattodo == '이론적 원리 탐구':
    # Header 적용
    st.header('1. 이론적 원리 탐구')
    

     # 탭 생성 : 첫번째 탭의 이름은 Tab A 로, Tab B로 표시합니다. 
    tab1, tab2, tab3, tab4= st.tabs(['⠀⠀⠀','무게중심' , '회전력','알쓸신잡'])

    with tab1:
         st.write("과학적 원리를 하나 :red[선택해 주세요]:grey_exclamation:")

    with tab2:
    # 무게중심을 누르면 표시될 내용
          st.subheader('무게중심')
          st.write('먼저, **뛰기 직전에는 무릎을 많이 굽히고 상체를 앞으로 기울여서** 무게중심을 앞으로 합니다. 무게 중심을 앞으로 하면 가속도가 붙어 점프를 뛰기 전의 속도가 높아집니다. 도약할 때 많은 운동량을 가지고 뛰어올라야 더 **높이 뛰어 회전할 충분할 시간을 확보**할 수 있기 때문입니다.')
          st.image("1.png")
          st.latex(r'P = mv')
          st.write("운동량은 속도*질량이므로 속도가 클수록 운동량은 커지게 되므로 무게 중심을 앞으로 해서 속도를 높여야 합니다.")
          st.write("회전수를 다 채워도 안정적인 착지를 하지 못하면 감점 요인이 됩니다. 착지를 할 때에는 **무릎을 많이 굽혀 무게 중심을 낮춰야** 합니다. 무게 중심을 낮추면 안정적인 자세가 되어 넘어질 확률을 줄일 수 있습니다. 이를 잘 보여주는 예시로 우리나라의 김진서 선수가 있습니다.")
          col1,col2 = st.columns([1,1])
          # 공간을 1:1 으로 분할하여 col1과 col2라는 이름을 가진 컬럼을 생성합니다.  

          with col1 :
          # column 1 에 담을 내용
             st.image("6.png", width=300)
          with col2 :
          # column 2 에 담을 내용
             st.image("67.png", width = 300 ,  caption = "무릎을 굽혀 무게 중심을 낮추는 김진서 선수")
          st.write("**→ 무게중심의 측면에서 보면, 뛰기 직전에는 무게 중심을 앞으로 하고 착지할 때는 무게중심을 낮추는 것이 감점 요인을 제거할 수 있습니다.**")
        
    with tab3:
    # 회전력을 누르면 표시될 내용 
          st.subheader('회전력')
          st.write('뛰기 전에는 무게중심으로부터의 거리를 최대한 멀리해야 뛰기 위한 힘을 축적할 수 있습니다. 뛰고 난 후 공중에서는 뛰기 전과는 다르게 팔과 다리를 최대한 모아야 합니다.')
          st.video('677.mp4')
          st.write('이는 **각운동량 보존 법칙**으로 설명할 수 있습니다.')
          st.latex(r'L  = r × mv')
          st.write('각운동량은 물체로부터의 거리 * 질량속도로 구할 수 있는데, 이 각운동량이 보존되는 것이 각운동량 보존 법칙입니다. 선수의 질량이 일정하기 때문에 **선수로부터의 거리와 속도는 반비례**한다고 할 수 있습니다. 선수가 처음에는 팔을 벌려 거리를 멀게했다가(r증가) 돌면서 팔을 모으면 r이 감소하므로 도는 속도는 증가하게 됩니다.')
          st.write('즉, 팔과 다리를 편 상태로 회전을 시작하면 **각운동량이 커지게** 되고 **뛰어오른 후에 팔과 다리를 모으면** 각운동량을 보존해야 하기 때문에 **회전의 속도가 빨라지게** 됩니다. 회전이 빠를수록 공중에서 회전수를 안정적으로 채울 수 있게 되므로 최대한 팔을 모아야 합니다.')
          st.write('**→ 뛰기 전에는 팔과 다리를 최대한 벌리고, 뛰어오른 후의 공중에서는 팔과 다리를 모아야 회전력을 높여 감점 확률을 제거할 수 있습니다.**')

    with tab4:
    # 알쓸신잡을 누르면 표시될 내용 
          st.subheader('알아두면 쓸데"있"는 신비한 잡학사전')
          st.write('**1. 피겨 경기장의 빙판 속 음펨바 효과**')
          col1,col2 = st.columns([1,1])
          # 공간을 1:1 으로 분할하여 col1과 col2라는 이름을 가진 컬럼을 생성합니다.  

          with col1 :
          # column 1 에 담을 내용
             st.image("111.jpeg")
          with col2 :
          # column 2 에 담을 내용
             st.image("112.jpeg")
          st.write('**음펨바 효과** : 뜨거운 물이 차가운 물보다 빨리 어는 효과')
          st.write('2018 평창 올림픽 때, 경기장에서는 물에서 최대한 공기를 빼낸 뒤 섭씨 50도로 따뜻하게 맞추었다.')
          st.write('그 이유는, 많은 에너지를 축적한 따듯한 물이 찬물보다 **에너지를 더 빨리 방출**하기 때문이다. 아직 음펨바 효과의 원인은 완전히 밝혀지지 않았다.')
          st.header('')
          st.write("**2. '쿼트러플 점프'가 가능한 과학적 이유**")
          st.write('미국 뉴욕타임즈는 피겨스케이팅과 뇌의 과학적인 관계에 대해 소개했다.')
          st.image("3.jpg")
          st.write('일반인은 아이스링크에 발을 디딜 때 미끄러지는 느낌을 받는다. 이때 넘어지지 않도록 신체를 앞으로 기울이라는 일련의 뇌 신호를 내보낸다. 한 마디로 반사 작용이 일어나는 것이다.')
          st.write('피겨스케이팅을 반복적으로 연습하다 보면 이 **반사 작용**이 약해진다는 사실이 밝혀졌다. 선수들은 미끄러지는 느낌을 자연스럽게 받아들이고 균형을 담당하는 소뇌의 연결 부위를 강화하는 것으로 분석됐다. ')
          st.write('기존 연구에 따르면 스피드 스케이팅 선수는 일반인에 비해 **소뇌**의 오른쪽이 더 크다. 스피드스케이팅 선수가 트랙의 커브를 따라 왼쪽으로 회전하기 위해 오른발로 균형을 잡을 때 오른쪽이 활성화되기 때문이다.')
          st.header('')
          st.write("**3. 스케이트 날에도 과학적 원리가 숨겨져 있다!**")
          col3,col4 = st.columns([1,1])

          
          with col3 :
          # column 3 에 담을 내용
             st.image("1234.jpg")
             st.write('얼음과 스케이트 날이 만나는 부분의 **마찰력**이 작아 자연스럽게 미끄러져 속력을 낼 수 있도록 도와준다.')
             st.write('또한, 대부분의 사람들은 물보다 얼음이 더 미끄럽다고 생각하지만, 얼음 위에 있는 **물로 이루어진 얇은 층**이 쉽게 미끄러지도록 도와준다.')
             st.write('결국 스케이트 날의 **마찰과 압력으로 인한 열**이 얼음을 녹여 자연스럽게 미끄러져 속력을 낼 수 있도록 도와준다.')
          with col4 :
          # column 4 에 담을 내용
             st.image("12345.jpg")
             st.write('피겨스케이팅의 빠른 속도와 회전은 스케이트 날의 모양과도 관련이 있다.')
             st.write('스케이트의 날 앞쪽에 있는 **토(toe)는** 미끄러운 얼음 위에서 땅을 찍으며 점프할 수 있도록 설계되어 있으며,')
             st.write('날 중앙에 파여있는 홈인 **엣지(edge)는** 다양한 연기를 해야하는 피겨스케이팅에서 쉽게 방향을 바꿀 수 있다.')
             


else:
    # Header 적용
    st.header('2. 과학적 원리가 적용된 자세 교정 프로그램')
    col5,col6 = st.columns([1,1])

    with col5 :
          # column 5 에 담을 내용
             st.link_button("자세 교정 프로그램 (상체 위주)", "https://url.kr/8bkdnj")
             st.image('12323.png', width = 200 , caption = "자세 교정 프로그램 QR 코드")
    with col6 :
          # column 6 에 담을 내용
             st.link_button("자세 교정 프로그램 (하체 위주)", "https://teachablemachine.withgoogle.com/models/ewAeG-p7X/")
             st.image('2323.png', width = 200 , caption = "자세 교정 프로그램 QR 코드")
   
    st.header('')      
    st.caption('아이폰 사용자일 경우 사용이 제한될 수 있습니다.')
