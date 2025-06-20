# ML

Этот репозиторий содержит модели машинного обучения для предсказания рисков для здоровья на основе данных с носимых устройств.

## Описание моделей

- **Sleep Disorders (Insomnia & Apnea):** Модель для предсказания наличия бессонницы и апноэ сна.
- **Hypertension:** Модель для предсказания риска гипертонии.
- **Depression:** Модель для предсказания риска депрессии.

## Структура репозитория

- `ml-models/` — Jupyter ноутбуки с кодом для обучения и тестирования моделей.
- `models/` — Pydantic-модели и вспомогательные структуры.
- `.env` — переменные окружения (например, параметры подключения к БД).
- `.gitignore` — исключения для git.

## Используемые датасеты

- [Sleep Health and Lifestyle Dataset](https://www.kaggle.com/datasets/uom190346a/sleep-health-and-lifestyle-dataset)
- [Hypertension Risk Prediction Dataset](https://www.kaggle.com/datasets/ankushpanday1/hypertension-risk-prediction-dataset)
- [Mental Health Prediction Using Wearable Dataset](https://www.kaggle.com/datasets/soumitradas1/mental-health-prediction-using-wearable-dataset)

## Быстрый старт

1. Скачайте датасеты с Kaggle по ссылкам выше.
2. Запустите соответствующие ноутбуки из папки `ml-models/` для обучения и тестирования моделей.
3. Используйте сохранённые модели (`*.pkl`) для интеграции в приложения или сервисы.

## Требования

- Python 3.10+
- pandas, numpy, scikit-learn, matplotlib, kagglehub и др.

---
