# HSE Coursework: ML Models

Этот репозиторий содержит модели машинного обучения для предсказания различных диагнозов на основе данных с носимых устройств.

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

## Входные признаки моделей

| Название признака             | Описание                                                                                   | Модель(и)                        |
|-------------------------------|--------------------------------------------------------------------------------------------|----------------------------------|
| Heart_Rate_BPM / Heart Rate   | Пульс (ударов в минуту, int)                                                               | Depression, Hypertension, Sleep  |
| Sleep_Duration_Hours / Sleep Duration | Продолжительность сна (часы, float)                                              | Depression, Hypertension, Sleep  |
| Physical_Activity_Steps / Daily Steps | Количество шагов за день (int)                                                  | Depression, Sleep                |
| Country                       | Страна проживания (строка, например 'Russia')                                              | Hypertension                     |
| Age                           | Возраст (int)                                                                             | Hypertension, Sleep              |
| BMI                           | Индекс массы тела (float)                                                                  | Hypertension                     |
| Physical_Activity_Level       | Уровень физической активности (строка, например 'Low', 'Moderate', ...)                    | Hypertension                     |
| Gender                        | Пол (строка: 'Male' или 'Female')                                                          | Hypertension, Sleep              |
| BMI Category                  | Категория ИМТ (строка, например 'Normal', 'Overweight', ...)                               | Sleep                            |
| Physical Activity Level       | Уровень физической активности (минуты в день, int)                                         | Sleep                            |

## Быстрый старт

1. Запустите соответствующие ноутбуки из папки `ml-models/` для обучения и тестирования моделей.
2. Используйте сохранённые модели (`*.pkl`) для интеграции в приложения или сервисы.

## Требования

- Python 3.10+
- pandas, numpy, scikit-learn, matplotlib, kagglehub и др.
