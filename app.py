import math
import streamlit as st

st.set_page_config(
    page_title="내 텀블러, 정말 친환경적일까?",
    layout="centered"
)

st.title("내 텀블러, 정말 친환경적일까?")
st.write("사용 습관에 따라 텀블러의 환경적 손익분기점을 계산합니다.")

# 기본 배출계수
paper_cup_ef = 0.062782789   # 종이컵
plastic_cup_ef = 0.086441    # 플라스틱 컵
tumbler_prod_ef = 0.9071     # 텀블러 생산

# 카드 스타일
st.markdown("""
<style>
.result-card {
    background-color: #f7f9fb;
    border: 1px solid #e6ebf1;
    border-radius: 18px;
    padding: 28px 20px;
    text-align: center;
    box-shadow: 0 2px 8px rgba(0,0,0,0.04);
    margin-top: 10px;
    margin-bottom: 10px;
}
.result-label {
    font-size: 1.2rem;
    font-weight: 600;
    color: #222;
    margin-bottom: 8px;
}
.result-number {
    font-size: 3.2rem;
    font-weight: 800;
    color: #0f6cbd;
    line-height: 1.2;
    margin: 8px 0;
}
.result-footer {
    font-size: 1.2rem;
    color: #222;
    margin-top: 6px;
}
.info-card {
    background-color: #ffffff;
    border: 1px solid #e6ebf1;
    border-radius: 14px;
    padding: 16px 18px;
    margin-top: 8px;
    margin-bottom: 8px;
}
.info-title {
    font-size: 0.95rem;
    color: #666;
    margin-bottom: 4px;
}
.info-value {
    font-size: 1.15rem;
    font-weight: 700;
    color: #111;
}
</style>
""", unsafe_allow_html=True)

st.subheader("1. 주로 사용하는 일회용 컵")
cup_option = st.selectbox(
    "일회용 컵 종류 선택",
    ["종이컵", "플라스틱 컵"]
)

if cup_option == "종이컵":
    alpha = paper_cup_ef
else:
    alpha = plastic_cup_ef

st.subheader("2. 세척 방식 선택")
wash_option = st.selectbox(
    "세척 방식",
    ["수동 냉수", "수동 온수", "발포 세정제", "식기세척기", "텀블러 전용 세척기"]
)

# 수동 세척일 때만 물 사용 습관 선택
water_option = None
if wash_option in ["수동 냉수", "수동 온수"]:
    water_option = st.selectbox(
        "물 사용 습관",
        ["물 적게 (1L)", "물 보통 (2L)", "물 많이 (3L)"]
    )

# 결과 버튼
show_result = st.button("결과 보기", type="primary")

if show_result:
    wash_ef = None
    display_wash_option = wash_option

    if wash_option == "수동 냉수":
        if water_option == "물 적게 (1L)":
            wash_ef = 0.0055404350
        elif water_option == "물 보통 (2L)":
            wash_ef = 0.0061804350
        elif water_option == "물 많이 (3L)":
            wash_ef = 0.0068204350
        display_wash_option = f"{wash_option} / {water_option}"

    elif wash_option == "수동 온수":
        if water_option == "물 적게 (1L)":
            wash_ef = 0.0214640307
        elif water_option == "물 보통 (2L)":
            wash_ef = 0.0380276263
        elif water_option == "물 많이 (3L)":
            wash_ef = 0.0545912220
        display_wash_option = f"{wash_option} / {water_option}"

    elif wash_option == "발포 세정제":
        wash_ef = 0.0251393569

    elif wash_option == "식기세척기":
        wash_ef = 0.0423446175

    elif wash_option == "텀블러 전용 세척기":
        wash_ef = 0.1116584196

    st.divider()
    st.subheader("결과")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"""
        <div class="info-card">
            <div class="info-title">비교 대상</div>
            <div class="info-value">{cup_option}</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="info-card">
            <div class="info-title">선택한 세척 방식</div>
            <div class="info-value">{display_wash_option}</div>
        </div>
        """, unsafe_allow_html=True)

    if alpha <= wash_ef:
        st.error("현재 조건에서는 세척 1회 배출량이 일회용 컵 배출량보다 크거나 같아 손익분기점이 발생하지 않습니다.")
    else:
        a_threshold = tumbler_prod_ef / (alpha - wash_ef)
        a_min = math.floor(a_threshold) + 1

        st.markdown(f"""
        <div class="result-card">
            <div class="result-label">최소 재사용 횟수는</div>
            <div class="result-number">{a_min}회</div>
            <div class="result-footer">입니다.</div>
        </div>
        """, unsafe_allow_html=True)