import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

fig, ax = plt.subplots()
ax.set_ylim(-4,4)
ax.set_xlim(-12,12)

x = np.arange(-12, 12, 0.01)


#パラメータインプット
param1_col, param2_col = st.columns(2)
#line1
with param1_col:
    st.subheader('ライン1')
    A1 = st.slider(label='振幅1', min_value=0.05, max_value=2.0, value=1.0, step=0.05)
    lambda1 = st.slider(label='波長1', min_value=0.05, max_value=12.0, value=6.0, step=0.05)
    T1 = st.slider(label="周期1", min_value=0.05, max_value=10.0, value=5.0, step=0.05)
    #進行方向
    isPositiveSense1 = st.selectbox("進行方向1",
                                    ("正","負"))
    sense1 = 1
    if isPositiveSense1 == "負":
        sense1 = -1
    else:
        sense1 = 1
    init1 = st.slider(label="初期位相1(x_1π)",min_value=-1.0,max_value=1.0,value=0.0, step=0.5)

    line1_left, line1_right = st.columns(2)
    with line1_left:
        st.write(f'振幅:{A1}')
        st.write(f'波長:{lambda1}')
        st.write(f"周期:{T1}")
    with line1_right:
        st.write(f'進行方向:{isPositiveSense1}')
        st.write(f'初期位相:{init1}π')

#line2
with param2_col:
    st.subheader('ライン2')
    A2 = st.slider(label='振幅2', min_value=0.05, max_value=2.0, value=1.0, step=0.05)
    lambda2 = st.slider(label='波長2', min_value=0.05, max_value=12.0, value=6.0, step=0.05)
    T2 = st.slider(label="周期2", min_value=0.05, max_value=10.0, value=5.0, step=0.05)
    isPositiveSense2 = st.selectbox("進行方向2",
                                    ("正","負"),
                                    index= 1)
    if isPositiveSense2 == "負":
        sense2 = -1
    else:
        sense2 = 1
    init2 = st.slider(label="初期位相2(x_2π)",min_value=-1.0,max_value=1.0,value=0.0, step=0.5)
    
    line2_left, line2_right = st.columns(2)
    with line2_left:
        st.write(f'振幅:{A2}')
        st.write(f'波長:{lambda2}')
        st.write(f"周期:{T2}")
    with line2_right:
        st.write(f'進行方向:{isPositiveSense2}')
        st.write(f'初期位相:{init2}π')

#A sin{2pi(t/T-x/lambda)+ x_0}

line1_paramater = A1*np.sin(2*np.pi* x - init1*np.pi)
line2_paramater = A2*np.sin(2*np.pi*(x )- init2*np.pi)

line1, = ax.plot(x, line1_paramater)
line2, = ax.plot(x, line2_paramater)
line3, = ax.plot(x, line1_paramater + line2_paramater)

def animate(t):
  animation_time = 3
  time = animation_time * t
  line1_param = A1*np.sin(2*np.pi*(t/(animation_time*T1)-(sense1*x/lambda1))- init1*np.pi)
  line2_param = A2*np.sin(2*np.pi*(t/(animation_time*T2)-(sense2*x/lambda2))- init2*np.pi)

  line1.set_ydata(line1_param)
  line2.set_ydata(line2_param)

  line3.set_ydata(line1_param+line2_param)

  plt.title("Time: {}".format(t))

  return line1, line2, line3

ani = animation.FuncAnimation(fig, animate, frames=100, interval=150, blit =True)



st.subheader("波の重ね合わせのグラフ")
st.warning("アニメーションなので描画に時間がかかります。")
components.html(ani.to_jshtml(),height=700)

is_standing_wave = True

if A1 == A2:
    is_A_same = True
else:
    is_A_same = False


is_same_dict = {"A":is_A_same}
st.markdown("""
## 定常波 とは
### 振幅A,周期T,波長λ,速さvが同じ かつ
### 向きが互いに逆向き の2つの波が作る合成波
逆向きの2つの波は
""")
st.latex(r'''
y_1 = A_1 \sin \left\{2\pi \left(\frac{t}{T_1}-\frac{x}{\lambda_1} \right) (+ \delta_1)\right\}\quad(\delta_1\text{は初期位相})
''')
st.latex(r'''
y_2 = A_2 \sin \left\{2\pi \left(\frac{t}{T_2}+\frac{x}{\lambda_2} \right) (+ \delta_2)\right\}\quad(\delta_2\text{は初期位相})
''')
st.write("と表せる。(sinの中の符号に注意) 定常波が存在するとき")
st.latex(r''' 
A_1 = A_2,T_1 = T_2, \lambda_1 = \lambda_2
''')
st.write("である。\
            このような状況は自然に起こりにくいが壁による反射は振幅などの波のパラメータを変えないので定常波が発生する。\
            自由端反射、固定端反射、気柱はその最たる例である。\
            グラフはx-yグラフ、つまりtを動かしている。")
st.write("定常波が発生するのは上のような状況のみであることをパラメータを変えて見てみることで観察せよ。")

