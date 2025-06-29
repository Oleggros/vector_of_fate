
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Вектор Судьбы", layout="centered")
st.title("Вектор Судьбы")
st.write("Пройди тест и узнай свою поведенческую карту!")

# Сбор имени и почты
name = st.text_input("Ваше имя")
email = st.text_input("Ваш email")

if name and email:
    st.write("Отлично, давайте начнем тест!")

    # Вопросы по категориям
    categories = {
        "Делатель": [
            "Когда я получаю задачу, мне важно сразу приступить к её выполнению.",
            "Я предпочитаю делать, а не обсуждать.",
            "Я расстраиваюсь, если обсуждение затягивается и не переходит в действие.",
            "Мне легче разбираться в процессе, чем долго планировать заранее."
        ],
        "Говоритель": [
            "Мне легко даётся вдохновлять других и доносить идеи.",
            "Я часто беру слово в обсуждениях и люблю делиться мыслями.",
            "Коммуникация — ключевой инструмент в моей работе.",
            "Иногда я могу говорить больше, чем делать."
        ],
        "Решатель": [
            "Прежде чем что-то делать, я анализирую возможные последствия.",
            "Мне важно понимать стратегию и общую картину.",
            "Я часто беру на себя ответственность за выбор направления.",
            "Мне трудно принимать поспешные решения без анализа."
        ],
        "Исполнитель": [
            "Я хорошо выполняю задачи по чёткому плану.",
            "Я чувствую удовлетворение, когда завершаю начатое.",
            "Мне легче работать по инструкции, чем изобретать с нуля.",
            "Я предпочитаю ясные цели и конкретные ожидания."
        ]
    }

    scores = {}
    submitted = True

    with st.form("behavior_form"):
        for cat, questions in categories.items():
            st.write(f"### {cat}")
            total = 0
            for q in questions:
                total += st.slider(q, 1, 5, 3, key=q)
            scores[cat] = total
        submitted = st.form_submit_button("Показать результат")

    if submitted:
        st.write(f"Спасибо, {name}! Вот ваша поведенческая карта:")

        # Визуализация кругов
        behavior_types = list(scores.keys())
        raw_scores = list(scores.values())
        radii = [s / 20 for s in raw_scores]
        positions = {
            'Делатель': (-1, 0),
            'Говоритель': (0, 1),
            'Решатель': (1, 0),
            'Исполнитель': (0, -1)
        }

        fig, ax = plt.subplots(figsize=(6, 6))
        for i, btype in enumerate(behavior_types):
            x, y = positions[btype]
            circle = plt.Circle((x, y), radii[i], alpha=0.4, label=f"{btype}: {raw_scores[i]}/20")
            ax.add_patch(circle)
            ax.text(x, y, btype, ha='center', va='center', fontsize=10, weight='bold')

        ax.set_xlim(-2, 2)
        ax.set_ylim(-2, 2)
        ax.set_aspect('equal')
        ax.axis('off')
        plt.legend(loc='upper right')
        plt.title("Карта Поведенческих Типов", fontsize=14)
        st.pyplot(fig)

else:
    st.info("Пожалуйста, введите имя и email для начала теста.")
