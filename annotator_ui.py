import streamlit as st
import json
import os
from datetime import datetime

# アノテーション保存ファイル
ANNOTATION_FILE = "annotations.json"

st.title("文学テキスト影響関係アノテーション")

# 入力項目
st.subheader("📘 ターゲットテキスト")
target_text = st.text_area("影響を受けたとされるテキストを入力してください", height=100)

st.subheader("📗 ソーステキスト")
source_text = st.text_area("影響を与えたとされるテキストを入力してください", height=100)

st.subheader("📊 影響度の評価")
influence_score = st.slider("影響の強さ（1: 弱い 〜 5: 強い）", 1, 5, 3)

st.subheader("📝 コメント・メモ")
notes = st.text_area("任意で注釈を入力してください", height=100)

annotator_id = st.text_input("評価者ID", value="user_001")

if st.button("💾 保存"):
    # アノテーションデータの構築
    entry = {
        "target_text": target_text,
        "source_text": source_text,
        "influence_rating": influence_score,
        "notes": notes,
        "annotator_id": annotator_id,
        "timestamp": datetime.now().isoformat()
    }

    # JSONファイルへの保存
    if os.path.exists(ANNOTATION_FILE):
        with open(ANNOTATION_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = []

    data.append(entry)

    with open(ANNOTATION_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    st.success("アノテーションが保存されました！")
