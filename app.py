import math
import streamlit as st

st.set_page_config(
    page_title="내 텀블러, 정말 친환경적일까?",
    layout="centered"
)

# -----------------------------
# 기본 설정
# -----------------------------
MAIN_GREEN = "#00462A"

paper_cup_ef = 0.062782789      # 종이컵
plastic_cup_ef = 0.08644142     # 플라스틱 컵
tumbler_prod_ef = 0.90708507    # 텀블러 생산

# -----------------------------
# 스타일
# -----------------------------
st.markdown(f"""
<style>
.block-container {{
    padding-top: 1.2rem;
    padding-bottom: 2rem;
}}

.green-text {{
    color: {MAIN_GREEN};
    font-weight: 800;
}}

.result-card {{
    background-color: #f7f9fb;
    border: 1px solid #e6ebf1;
    border-radius: 18px;
    padding: 28px 20px;
    text-align: center;
    box-shadow: 0 2px 8px rgba(0,0,0,0.04);
    margin-top: 10px;
    margin-bottom: 10px;
}}

.result-label {{
    font-size: 1.2rem;
    font-weight: 600;
    color: #222;
    margin-bottom: 8px;
}}

.result-number {{
    font-size: 3.2rem;
    font-weight: 800;
    color: {MAIN_GREEN};
    line-height: 1.2;
    margin: 8px 0;
}}

.result-footer {{
    font-size: 1.2rem;
    color: #222;
    margin-top: 6px;
}}

.info-card {{
    background-color: #ffffff;
    border: 1px solid #e6ebf1;
    border-radius: 14px;
    padding: 16px 18px;
    margin-top: 8px;
    margin-bottom: 8px;
    min-height: 118px;
    display: flex;
    flex-direction: column;
    justify-content: center;
}}

.info-title {{
    font-size: 0.95rem;
    color: #666;
    margin-bottom: 6px;
}}

.info-value {{
    font-size: 1.15rem;
    font-weight: 700;
    color: #111;
    line-height: 1.5;
    min-height: 3em;
    display: flex;
    align-items: center;
}}

div.stButton > button {{
    background-color: {MAIN_GREEN};
    color: white;
    border: none;
    border-radius: 10px;
    padding: 0.6em 1.2em;
    font-weight: 700;
}}

div.stButton > button:hover {{
    background-color: {MAIN_GREEN};
    color: white;
    opacity: 0.92;
}}

@media (max-width: 768px) {{
    .block-container {{
        padding-top: 1.6rem !important;
        padding-bottom: 1rem !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
    }}

    h1 {{
        font-size: 1.55rem !important;
        line-height: 1.22 !important;
        margin-top: 0rem !important;
        margin-bottom: 0.45rem !important;
        letter-spacing: -0.02em !important;
        word-break: keep-all !important;
    }}

    h3 {{
        font-size: 1.15rem !important;
        line-height: 1.32 !important;
        margin-top: 0.5rem !important;
        margin-bottom: 0.35rem !important;
        word-break: keep-all !important;
    }}

    p, label, .stMarkdown, .stText {{
        font-size: 0.92rem !important;
        line-height: 1.5 !important;
    }}

    .result-card {{
        padding: 20px 14px !important;
    }}

    .result-label {{
        font-size: 0.95rem !important;
    }}

    .result-number {{
        font-size: 2.1rem !important;
    }}

    .result-footer {{
        font-size: 0.95rem !important;
    }}

    .info-card {{
        min-height: 86px !important;
        padding: 12px 12px !important;
    }}

    .info-title {{
        font-size: 0.8rem !important;
        margin-bottom: 4px !important;
    }}

    .info-value {{
        font-size: 0.95rem !important;
        min-height: 2.2em !important;
        line-height: 1.35 !important;
    }}

    div.stButton > button {{
        width: 100% !important;
        font-size: 0.95rem !important;
        padding: 0.7em 0.9em !important;
    }}
}}
</style>
""", unsafe_allow_html=True)

st.markdown("<div style='margin-top:30px;'></div>", unsafe_allow_html=True)

# -----------------------------
# 상단 로고
# -----------------------------
import base64

def img_to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

ewha_b64 = img_to_base64("ewha_logo.png")
innovation_b64 = img_to_base64("university_innovation.png")

st.markdown(f"""
<style>
.logo-row {{
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    margin-bottom: 1rem;
}}

.logo-left img {{
    width: 160px;
    height: auto;
}}

.logo-right img {{
    width: 155px;
    height: auto;
}}

@media (max-width: 768px) {{
    .logo-left img {{
        width: 105px !important;
    }}

    .logo-right img {{
        width: 100px !important;
    }}

    .logo-row {{
        margin-bottom: 0.6rem !important;
    }}
}}
</style>

<div class="logo-row">
    <div class="logo-left">
        <img src="data:image/png;base64,{ewha_b64}" />
    </div>
    <div class="logo-right">
        <img src="data:image/png;base64,{innovation_b64}" />
    </div>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# 제목
# -----------------------------
st.markdown(
    f"<h1>내 텀블러, 정말 <span class='green-text'>친환경적</span>일까?</h1>",
    unsafe_allow_html=True
)
st.write("사용 습관에 따라, 텀블러를 몇 번 재사용해야 일회용 컵보다 환경에 더 나은지 계산합니다.")

st.markdown("<div style='margin-top:18px;'></div>", unsafe_allow_html=True)

# -----------------------------
# 1. 일회용 컵 선택
# -----------------------------
st.subheader("1. 주로 사용하는 일회용 컵을 선택하세요.")

cup_option = st.selectbox(
    "일회용 컵 종류 선택",
    ["종이컵", "플라스틱 컵"]
)

if cup_option == "종이컵":
    alpha = paper_cup_ef
else:
    alpha = plastic_cup_ef

st.markdown("<div style='margin-top:18px;'></div>", unsafe_allow_html=True)

# -----------------------------
# 2. 세척 방식 선택
# -----------------------------
st.subheader("2. 텀블러를 주로 어떻게 세척하시나요?")

wash_option = st.selectbox(
    "세척 방식 선택",
    [
        "차가운 물로 직접 세척",
        "따뜻한 물로 직접 세척",
        "발포 세정제 사용",
        "식기세척기 사용",
        "텀블러 전용 세척기 사용"
    ]
)

water_option = None
if wash_option in ["차가운 물로 직접 세척", "따뜻한 물로 직접 세척"]:
    water_option = st.selectbox(
        "물 사용 방식 선택",
        [
            "물을 받아서 세척",
            "보통 수준으로 세척",
            "물을 틀어 놓고 세척"
        ]
    )

st.markdown("<div style='margin-top:25px;'></div>", unsafe_allow_html=True)

# -----------------------------
# 결과 버튼
# -----------------------------
show_result = st.button("결과 보기", type="primary")

if show_result:
    wash_ef = None
    display_cup_option = cup_option
    display_wash_option = wash_option

    if wash_option == "차가운 물로 직접 세척":
        if water_option == "물을 받아서 세척":
            wash_ef = 0.0055404350
        elif water_option == "보통 수준으로 세척":
            wash_ef = 0.0068204350
        elif water_option == "물을 틀어 놓고 세척":
            wash_ef = 0.0081004350 
        display_wash_option = f"{wash_option}<br>{water_option}"

    elif wash_option == "따뜻한 물로 직접 세척":
        if water_option == "물을 받아서 세척":
            wash_ef = 0.0137368555 
        elif water_option == "보통 수준으로 세척":
            wash_ef = 0.0314096966 
        elif water_option == "물을 틀어 놓고 세척":
            wash_ef = 0.0490825378 
        display_wash_option = f"{wash_option}<br>{water_option}"

    elif wash_option == "발포 세정제 사용":
        wash_ef = 0.0174121818 

    elif wash_option == "식기세척기 사용":
        wash_ef = 0.0423446175

    elif wash_option == "텀블러 전용 세척기 사용":
        wash_ef = 0.1116584196

    st.divider()
    st.subheader("환경적 손익분기점 산정 결과")

    result_col1, result_col2 = st.columns(2)

    with result_col1:
        st.markdown(f"""
        <div class="info-card">
            <div class="info-title">비교 대상</div>
            <div class="info-value">{display_cup_option}</div>
        </div>
        """, unsafe_allow_html=True)

    with result_col2:
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
  
    
    # -----------------------------
    # 결과 해석 문장
    # -----------------------------
    st.markdown("### 결과 해석")

    if wash_option == "차가운 물로 직접 세척":
        interpretation = "차가운 물로 직접 세척하는 경우, 다른 세척 방식보다 상대적으로 적은 배출량을 보여 손익분기점이 더 빠르게 나타납니다."
    elif wash_option == "따뜻한 물로 직접 세척":
        interpretation = "따뜻한 물을 사용할 경우 물 가열 에너지의 영향으로 배출량이 증가하여, 손익분기점이 더 늦어질 수 있습니다."
    elif wash_option == "발포 세정제 사용":
        interpretation = "발포 세정제 사용은 세정제 자체와 따뜻한 물 사용의 영향이 함께 반영되어 중간 수준의 배출량을 보입니다."
    elif wash_option == "식기세척기 사용":
        interpretation = "식기세척기는 텀블러 1개당 할당량 기준으로 계산되며, 전력 사용의 영향으로 손익분기점이 상대적으로 늦어질 수 있습니다."
    else:
        interpretation = "텀블러 전용 세척기는 전력 사용량의 영향이 커서, 본 연구 조건에서는 손익분기점이 매우 늦거나 발생하지 않을 수 있습니다."

    st.info(interpretation)

    st.markdown("### 계산 기준")
    st.markdown(
        """
        - 본 결과는 **355 mL(톨 사이즈) 일회용 컵과 텀블러** 를 대상으로 계산하였습니다.  
        - 세척 방식에 따라 텀블러가 일회용 컵보다 환경적으로 유리해지는 시점이 달라질 수 있습니다.
        """
    )

    st.markdown("<div style='margin-top:25px;'></div>", unsafe_allow_html=True)

    # -----------------------------
    # 더 자세한 설명
    # -----------------------------
    with st.expander("더 자세한 설명 보기"):
        st.markdown("### 세척 방식별 배출량")

        st.image("wash.png", caption="세척 방식별 1회 배출량", use_container_width=True)

        st.markdown(
            """
            위의 그림은 텀블러 세척 시나리오별 사용 단계 배출량을 비교한 것입니다. 
            수동 냉수 세척은 가장 낮은 배출량을 보였으며, 수동 온수 세척과 발포 세정제 세척은 
            따뜻한 물 사용에 따른 가열 에너지의 영향으로 더 높은 값을 나타냈습니다.
            또한 식기세척기와 텀블러 전용 세척기는 장비 전력 사용이 포함되어 상대적으로 더 큰 배출량을 보였고, 
            특히 텀블러 전용 세척기가 가장 높은 값을 나타냈습니다.
            이를 통해 세척 단계의 환경부하는 단순한 물 사용량보다도 에너지 사용 조건에 크게 좌우됨을 확인할 수 있습니다.
            """
        )

        st.markdown("### 세척 방식별 최소 재사용 횟수")

        st.image("reuse.png", caption="세척 방식별 최소 재사용 횟수", use_container_width=True)

        st.markdown(
            """
            위의 그림은 세척 시나리오별 손익분기점, 즉 텀블러가 일회용 컵보다 환경적으로 유리해지기 위해 필요한 최소 재사용 횟수를 보여줍니다. 
            수동 냉수 세척은 가장 빠른 손익분기점을 보였고, 수동 온수 세척은 물 사용량이 증가할수록 손익분기점이 늦어지는 경향을 나타냈습니다. 
            발포 세정제와 식기세척기 사용은 중간 수준의 재사용 횟수를 보였으며, 
            텀블러 전용 세척기는 세척 1회당 배출량이 커서 본 연구 조건에서는 손익분기점이 발생하지 않았습니다. 
            이를 통해 텀블러의 환경적 이점은 재사용 여부 자체보다도 세척 방식에 크게 좌우됨을 알 수 있습니다.
            """
        )
        st.markdown("### 자세한 결과 보고서")
        try:
            with open("LCA_result_report.pdf", "rb") as file:
                st.download_button(
                    label="결과 보고서 다운로드",
                    data=file,
                    file_name="LCA_result_report.pdf",
                    mime="application/pdf"
                )
        except FileNotFoundError:
            st.caption("결과 보고서 파일을 같은 폴더에 넣으면 다운로드 버튼이 활성화됩니다.")

    st.markdown("### 의견 남기기")
    st.markdown("[의견 조사 참여하기](https://forms.gle/JSXqB2LFNfCukCJj7)")

