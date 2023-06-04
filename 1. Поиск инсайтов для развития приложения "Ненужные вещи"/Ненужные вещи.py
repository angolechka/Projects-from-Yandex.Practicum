#!/usr/bin/env python
# coding: utf-8

# # Выпускной проект

# # Материалы

# * [Презентация](https://disk.yandex.ru/i/gh2XDBDr8l-kMg)
# * [Дашборд](https://public.tableau.com/app/profile/anna4635/viz/Final_project_app/Dashboard1?publish=yes)

# # Оглавление

# 1. [Цель исследования](#goal)
# 2. [Описание данных](#description)
# 3. [Декомпозиция аналитической задачи](#decomposition)
# 4. [Ход исследования](#project)
#     * [Загрузка данных](#start) 
#     * [Изучение общей информации и предобработка данных](#preprocessing)
#     * [Анализ данных](#analysis)
#     * [Изучение воронки событий](#funnel)
#     * [Проверка гипотез](#hypothesis)
#     * [Выводы](#conclusion)

# # <a id='goal'> Цель исследования </a>  

# Приложение "Ненужные вещи" уже достаточно популярное. Мы любим опираться на числа и проводим исследования регулярно. В текущем исследовании мы хотим найти интересные инсайты, которые помогут нам стать еще лучше.
# 
# Результаты анализа и рекомендации по улучшению продукта мы представим продакт-менеджеру.

# # <a id='description'> Описание данных </a>  

# Датасет содержит данные о событиях, совершенных в мобильном приложении "Ненужные вещи". В нем пользователи продают свои ненужные вещи, размещая их на доске объявлений.
# 
# В датасете содержатся данные пользователей, впервые совершивших действия в приложении после 7 октября 2019 года.
# 
# Колонки в *mobile_sources.csv*: 
# 
# - `userId` — идентификатор пользователя,
# - `source` — источник, с которого пользователь установил приложение.
# 
# Колонки в *mobile_dataset.csv*: 
# 
# - `event.time` — время совершения,
# - `user.id` — идентификатор пользователя,
# - `event.name` — действие пользователя.
# 
# Виды действий:
# 
# - `advert_open` — открыл карточки объявления,
# - `photos_show` — просмотрел фотографий в объявлении,
# - `tips_show` — увидел рекомендованные объявления,
# - `tips_click` — кликнул по рекомендованному объявлению,
# - `contacts_show` и `show_contacts` — посмотрел номер телефона,
# - `contacts_call` — позвонил по номеру из объявления,
# - `map` — открыл карту объявлений,
# - `search_1`—`search_7` — разные действия, связанные с поиском по сайту,
# - `favorites_add` — добавил объявление в избранное.

# # <a id='decomposition'> Декомпозиция аналитической задачи </a>  

# ## Шаг 1. Открыть файл с данными и изучить общую информацию 

# * Открыть файлы `mobile_dataset.csv` и `mobile_sources.csv`

# ## Шаг 2. Подготовить данные

# * Рассмотреть типы данных в каждом столбце. Откорректировать, если это необходимо
# * Проверить наличие пропусков в данных
# * Проверить наличие дубликатов
# * Объединить два датасета в один
# * Для событий `contacts_show` и `show_contacts` (посмотрел номер телефона) сделать единое обозначение, напр. `contacts_show`

# ## Шаг 3. Исследовательский анализ данных

# * Сколько всего пользователей в логе?
# * Сколько в среднем событий приходится на одного пользователя?
# * Данными за какой период мы располагаем? Найти максимальную и минимальную даты. Построить гистрограмму по дате и времени
# * Построить гистограмму, отображающую количество пользователей, пришедших из разных источников
# * Посмотреть, как меняется количество событий по дням. Построить диаграмму распределения

# ## Шаг 4. Изучить воронку событий

# * Посмотреть, как часто разные события встречаются в логах. Отсортировать события по частоте
# * Посчитать, сколько пользователей совершали каждое из этих событий. Отсортировать события по числу пользователей 
# * Предположить, в каком порядке происходят события до просмотра контактов
# * Разбить события на сессии (~ 30 мин)
# * Изучить, от каких событий зависит реализация целевого действия, т.е. просмотра контактов
# * Оценить, какие действия чаще совершают те пользователи, которые просматривают контакты
# * По воронкам событий посчитать, какая доля пользователей проходит на следующий шаг воронки (от числа пользователей на предыдущем)
# * Сравнить воронки по конверсии и времени до целевого действия

# ## Шаг 5. Проверить статистические гипотезы

# Гипотезы:
# * Одни пользователи совершают действия `tips_show` и `tips_click`, другие — только `tips_show`. Проверить гипотезу: **конверсия в просмотры контактов различается у этих двух групп**.
# * Одни пользователи ищут объявления самостоятельно и совершают действия `search_1`—`search_7`, другие пользуются рекомендациями, т.е. совершают действия `tips_click`или `tips_show`. Проверить гипотезу: **конверсия в просмотры контактов различается у этих двух групп**.
# * Одни пользователи скачали приложение, прийдя с источника Yandex, а другие - из Google. Проверить гипотезу: **конверсия в просмотры контактов между теми пользователями, которые совершили установку приложения, прийдя с источника yandex и пользователями, совершившими установку из источника google, различаются.**

# ## Шаг 6. Сделать выводы

# * Дать рекомендации продакт-менеджеру по улучшению приложения, основываясь на проведенном исследовании

# ## Шаг 7. Подготовить презентацию

# * Для создания презентации использовать любой удобный инструмент, но отправить презентацию нужно обязательно в формате pdf, прикрепив ссылку на файл в основном проекте

# ## Шаг 8. Построить дашборд

# * Создать дашборд из любого полного набора
# * Чтобы отправить дашборд, приложить к проекту ссылку на файл

# # <a id='project'> Ход исследования </a>  

# ## <a id='start'> Загрузка данных </a>  

# In[1]:


# импортируем все библиотеки, которые будут нужны для выполнения исследования

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import math as mth
from scipy import stats as st
from datetime import datetime as dt
from datetime import timedelta
import plotly.express as px
from plotly import graph_objects as go
from statsmodels.stats.proportion import proportions_ztest


# In[2]:


# откроем рабочие файлы

try:
    dataset_raw = pd.read_csv('/datasets/mobile_dataset.csv')
except:
    dataset_raw = pd.read_csv('https://code.s3.yandex.net/datasets/mobile_dataset.csv')
    
try:
    sources_raw = pd.read_csv('/datasets/mobile_sources.csv')
except:
    sources_raw = pd.read_csv('https://code.s3.yandex.net/datasets/mobile_sources.csv')


# In[3]:


# создадим копии датафреймов

dataset = dataset_raw.copy(deep=True)
sources = sources_raw.copy(deep=True)


# ## <a id='preprocessing'> Изучение общей информации и предобработка данных </a>

# In[4]:


# создадим функцию для вывода предобработки данных

def info(data):
    # посмотрим общую информацию о файле 
    print('Общая информация о датафрейме:')
    data.info()
    
    # выведем на экран 5 строчек таблицы
    
    pd.options.display.max_colwidth = 100
    pd.set_option('display.max_columns', 20)
    display(data.head(5))
    
    # посчитаем количество пропущенных значений

    print('Количество пропущенных значений:')
    print(data.isna().sum().sort_values(ascending=False))
    
    # посчитаем количество полных дубликатов

    print()
    print('Количество полных дубликатов: ', data.duplicated().sum())


# In[5]:


# рассмотрим датафрейм dataset

info(dataset)


# In[6]:


# рассмотрим датафрейм sources

info(sources)


# In[7]:


# переименуем столбцы в датафреймах

dataset = dataset.rename(columns = {'event.time':'event_time', 'event.name':'event_name', 'user.id':'user_id'})
sources = sources.rename(columns = {'userId':'user_id'})


# In[8]:


# приведем дату в колонке event_time к нужному типу

dataset['event_time'] = pd.to_datetime(dataset['event_time']).round('1s')


# In[9]:


# объединим два датасета в один

data = dataset.merge(sources, on='user_id')
data.head()


# In[10]:


# добавим колонку с датой

data['date'] = data['event_time'].dt.date


# In[11]:


# укажем единое обозначение для события "посмотрел номер телефона"

data['event_name'] = data['event_name'].replace('show_contacts', 'contacts_show')


# In[12]:


# объединим информацию по событию "поиск по сайту"

search_replace = ['search_1', 'search_2', 'search_3', 'search_4', 'search_5', 'search_6', 'search_7']
name = 'search'
data['event_name'] = data['event_name'].replace(search_replace, name)


# In[13]:


# сохраняем файл на локальный компьютер

# data.to_csv('data.csv', sep='\t', encoding='utf-8')
# data.to_csv(r'C:\Users\Анна\Desktop\Яндекс.Практикум\Аналитик данных\Выпускной проект\data.csv')


# **Вывод:**
# 1. Датасеты были изучены, проведена их предобработка.
# 2. Пропусков в данных и полных дубликатов обнаружено не было
# 3. Столбец *event_time* в датасете *dataset* был переведен в формат *datetime*
# 4. Названия столбцов всех датасетов были приведены к удобному формату
# 5. Два датасета были объединены в один, содержащий 74197 записи
# 6. Указано единое обозначение для события "посмотрел номер телефона" и "поиск"

# ## <a id='analysis'> Анализ данных </a>

# ### Посмотрим, какое количество пользователей записано в логе

# In[14]:


user_number = data['user_id'].nunique()
print(f'Количество уникальных пользователей в логе: {user_number}')


# ### Изучим, сколько в среднем событий приходится на одного пользователя

# In[15]:


# сделаем сводную таблицу по количеству событий для каждого пользователя

events_per_user = (
    data.pivot_table(
    index = 'user_id',
    values = 'event_name',
    aggfunc = 'count'
    ).rename(columns={'event_name':'count'})
    .sort_values(by='count', ascending=False)
    .reset_index()
)


# In[16]:


# посмотрим, как распределено количество событий среди пользователей

fig = plt.figure(figsize=(15,5))
ax_1 = fig.add_subplot(1, 2, 1)
ax_2 = fig.add_subplot(1, 2, 2)

y = events_per_user['count']
ax_1.boxplot(y)
ax_1.set_xlabel('Количество событий')
ax_2.boxplot(y)
ax_2.set_xlabel('Количество событий')
ax_2.set_ylim([0,20])

fig.show()


# In[17]:


data_out_share = events_per_user.query('count > 17.5')['user_id'].count() / events_per_user['user_id'].count()
print(f'Процент выбросов в данных по количеству событий на пользователя {data_out_share:.2%}')


# > Выбросов получилось большое количество (за выброс считаем количество событий на пользователя больше 17.5). Поэтому в данном случае необходимо использовать медиану для определения среднего числа событий на пользователя.

# In[18]:


# посчитаем, сколько в среднем событий приходится на пользователя

events_avg = events_per_user['count'].median()
print('Среднее количество событий на пользователя: ', events_avg.round(0))


# > **На пользователя в среднем приходится 9 событий**

# ### Рассмотрим, данными за какой период мы располагаем. Найдем максимальную и минимальную даты.

# In[19]:


# найдем максимальную и минимальную даты в датасете

min_date = data['event_time'].min().date()
print('Минимальная дата: ', min_date)
max_date = data['event_time'].max().date()
print('Максимальная дата: ', max_date)


# In[20]:


distribution_event = data.groupby(['date','event_name']).agg({'event_time':'count'}).reset_index()
distribution_event.columns = ['date', 'event_name', 'event_count']
count_sum = distribution_event.groupby('date').agg({'event_count':'sum'})['event_count'].reset_index()
count_sum.columns = ['date', 'event_sum']
distribution_event = distribution_event.merge(count_sum, on='date', how='left')


# In[21]:


distribution_event.head()


# In[22]:


# посмотрим на распределение событий по дням

plt.figure


# In[23]:


fig_distribution_event_2 = px.bar(distribution_event.query('event_name !="tips_show"'), x='date', y='event_count', color='event_name')
fig_distribution_event_2.update_layout(title_text='Распределение событий по дням без учета tips_show')
fig_distribution_event_2.for_each_trace(lambda t: t.update(name=t.name.split("=")[0]))
fig_distribution_event_2.show()


# * **Очень большое количество событий `tips_show` и очень мало `tips_click`, конверсия низкая**
# * **Пользователи чаще пользуются самостоятельным поиском объявлений на сайте**
# * **Пользователи редко добавляют объявления в избранное**

# ### Построим диаграмму, отображающую количество пользователей, пришедших из разных источников

# In[24]:


users_per_source = (
    data.pivot_table(
        index = 'source',
        values = 'user_id',
        aggfunc = 'nunique'
    ).rename(columns={'user_id':'total_number'})
    .sort_values(by='total_number', ascending=False)
    .reset_index()
)


# In[25]:


# функции для построения графиков
# круговая диаграмма

def pie(labels, values, colors, text, title):
    colors = colors
    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    fig.update_traces(marker=dict(colors=colors), textinfo='percent+value')
    fig.update_layout(title=title, # указываем заголовок графика
                      width=600, # указываем размеры графика
                      height=500,
                      annotations=[dict(x=1.12, # вручную настраиваем аннотацию легенды
                                        y=1.05,
                                        text=text,
                                        showarrow=False)])
    fig.show()
    
# столбчатая диаграмма

def bar(data, x, y, text, title, xaxis_title, yaxis_title):
    fig = px.bar(data, 
                 x=x, # указываем столбец с данными для оси X
                 y=y, # указываем столбец с данными для оси Y
                 text=text, # добавляем аргумент, который отобразит текст с информацией
                 color_discrete_sequence=px.colors.qualitative.Pastel1
                )
    # оформляем график

    fig.update_layout(title=title,
                       xaxis_title=xaxis_title,
                       yaxis_title=yaxis_title)

    fig.show() # выводим график


# In[26]:


# построим круговую диаграмму, отображающую количество посетителей, пришедших из разных источников

colors = ['F7A4A4', 'FCDDB0', '863A6F']
title = 'Количество посетителей, пришедших из разных источников'
text = 'Источник'
labels = users_per_source['source']
values = users_per_source['total_number']

pie(labels, values, colors, text, title)


# > **Почти половина пользователей (45.1%) установили приложение из Яндекса, 26.3% - из Google, а остальные пользователи установили приложение из других источников**

# ### Посмотрим, как меняется количество событий по дням

# In[27]:


events_per_date = (
    data.pivot_table(
        index = 'date',
        values = 'event_name',
        aggfunc = 'count'
    ).rename(columns={'event_name':'total_number'})
    .sort_values(by='total_number', ascending=False)
    .reset_index()
)


# In[28]:


# строим столбчатую диаграмму 

x = 'date'
y = 'total_number'
color_continuous_scale = 'sunset'
title = 'Количество событий в зависимости от дня'
xaxis_title = 'Дата'
yaxis_title = 'Количество событий'

bar(events_per_date, x, y, y, title, xaxis_title, yaxis_title)


# > **Самое большое количество событий (3360) было зафиксировано 23 октября 2019, а самое минимальное (1843) - 12 октября 2019. В период с 21 по 31 октября наблюдается больше всего событий.**

# ### Вывод

# 1. **Данные охватывают временной промежуток с 7 октября по 3 ноября 2019 года.**
# 2. **В логе зафиксировано 4293 уникальных пользователей.**
# 3. **В среднем на пользователя приходится по 9 событий.**
# 4. **Почти половина пользователей (45.1%) установили приложение из Яндекса, 26.3% - из Google, а остальные пользователи установили приложение из других источников.**
# 5. **Самое большое количество событий (3360) было зафиксировано 23 октября 2019, а самое минимальное (1843) - 12 октября 2019. В период с 21 по 31 октября наблюдается больше всего событий.**
# 6. **Очень большое количество событий `tips_show` и очень мало `tips_click`, конверсия низкая**
# 7. **Пользователи чаще пользуются самостоятельным поиском объявлений на сайте**

# ## <a id='funnel'> Изучение воронки событий </a>

# ### Посмотрим, как часто разные события встречаются в логе. Отсортируем события по частоте

# In[29]:


# создадим сводную таблицу, показывающую, сколько раз встречается то или иное событие в логе

events = (
    data.pivot_table(
        index='event_name',
        values='user_id',
        aggfunc='count'
    ).rename(columns={'user_id':'total_count'})
    .sort_values(by='total_count', ascending=False)
    .reset_index()
)


# In[30]:


# строим столбчатую диаграмму

x_1 = 'event_name'
y_1 = 'total_count'
title_1 = 'Количество разных событий в логе'
xaxis_title_1 = 'Тип события'
yaxis_title_1 = 'Количество событий'

bar(events, x_1, y_1, y_1, title_1, xaxis_title_1, yaxis_title_1)


# >**В логе чаще всего встречается событие *увидел рекомендованные объявления*. Это автоматическое событие, и оно никак не отражает взаимодействие пользователя с приложением. Просмотр фотографий в объявлении занимает второе место в рейтинге событий по частоте, затем идет самостоятельный поиск.**

# ### Посчитаем, сколько пользователей совершали каждое из этих событий. Отсортируем события по числу пользователей

# In[31]:


users_per_events = (
    data.pivot_table(
        index='event_name',
        values='user_id',
        aggfunc='nunique'
    ).rename(columns={'user_id':'total_count'})
    .sort_values(by='total_count', ascending=False)
    .reset_index()
)


# In[32]:


# строим столбчатую диаграмму

x_2 = 'event_name'
y_2 = 'total_count'
title_2 = 'Количество пользователей, совершивших событие'
xaxis_title_2 = 'Тип события'
yaxis_title_2 = 'Количество пользователей'

bar(users_per_events, x_2, y_2, y_2, title_2, xaxis_title_2, yaxis_title_2)


# >**Больше всего пользователей совершают событие *увидел рекомендованные объявления*. Это автоматическое событие, и оно никак не отражает взаимодействие пользователя с приложением. Далее идет событие *поиск*, и это логично, а затем *открыл карту объявлений***

# ### Предположим, в каком порядке происходят события в приложении

# Виды действий:
# 
# - `advert_open` — открыл карточки объявления,
# - `photos_show` — просмотрел фотографий в объявлении,
# - `tips_show` — увидел рекомендованные объявления,
# - `tips_click` — кликнул по рекомендованному объявлению,
# - `contacts_show` и `show_contacts` — посмотрел номер телефона,
# - `contacts_call` — позвонил по номеру из объявления,
# - `map` — открыл карту объявлений,
# - `search_1`—`search_7` — разные действия, связанные с поиском по сайту,
# - `favorites_add` — добавил объявление в избранное.

# **Составим несколько воронок:**
# 
# 1. `search` --> `advert_open` --> `contacts_show` --> `favorites_add` --> `contacts_call`
# 2. `tips_show` --> `tips_click` -->  `contacts_show` --> `favorites_add` --> `contacts_call`
# 3. `tips_show`--> `search` --> `advert_open` --> `contacts_show`  --> `contacts_call`

# ### Разобьем события на сессии

# In[33]:


# создадим копию датафрейма и добавим столбец с id события

data_session = data.copy(deep=True)


# In[34]:


# отсортируем данные по user_id и event_time, чтобы события каждого пользователя шли последовательно

data_session = data_session.sort_values(['user_id', 'event_time']).reset_index()


# In[35]:


data_session = data_session.rename(columns={'index':'id'}) 


# In[36]:


data_session


# In[37]:


# в колонке ’diff’ для каждого события отдельного пользователя посчитаем разницу между последовательными событиями

data_session['diff'] = data_session.groupby('user_id')['event_time'].diff()


# In[38]:


data_session.head()


# In[39]:


# создадим вспомогательный датафрейм ’session_start_df’
# этот датафрейм будет содержать события, которые произошли спустя более,
# чем 30 минут (1800 сек) после предыдущего, либо события, которые были первыми для пользователя (NaT в колонке ’diff’).

session_start_df = data_session[(data_session['diff'].isnull()) | (data_session['diff'] > '1800 seconds')]


# In[40]:


session_start_df_copy = session_start_df.copy(deep=True)
session_start_df_copy['session_id'] = session_start_df_copy['id'] 


# In[41]:


data_session = data_session.sort_values('id')
session_start_df_copy = session_start_df_copy.sort_values('id')


# In[42]:


# объединим между собой данные основного и вспомогательного датафреймов

data_session_total = pd.merge_asof(data_session, session_start_df_copy[['id','user_id','session_id']],on='id',by='user_id')


# In[43]:


# найдем события, которые были первыми в сессиях

data_session_total['is_first_event_in_session'] = data_session_total['id'] == data_session_total['session_id']


# In[44]:


# вычислим время, проведенное на странице

data_session_total['time_on_page'] = (
    data_session_total.groupby(['session_id'])['event_time'].diff(periods=1).shift(-1)/ np.timedelta64(1, 's')
)


# In[45]:


data_session_total.head()


# In[46]:


# составим таблицу, где для каждой сессии будут указаны время начала, окончания и ее длительность

session_duration = (
    data_session_total.pivot_table(
        index=['session_id', 'user_id', 'source'],
        values='time_on_page',
        aggfunc='sum'
    ).rename(columns={'time_on_page':'session_duration'})
    .sort_values(by='session_id')
    .reset_index()
)

session_start = (
    data_session_total.pivot_table(
        index=['session_id'],
        values='event_time',
        aggfunc='min'
    ).rename(columns={'event_time':'session_start'})
    .sort_values(by='session_id')
    .reset_index()
)

session_end = (
    data_session_total.pivot_table(
        index=['session_id'],
        values='event_time',
        aggfunc='max'
    ).rename(columns={'event_time':'session_end'})
    .sort_values(by='session_id')
    .reset_index()
)

user_by_session = session_duration.merge(session_start, on='session_id', how='left')
user_by_session = user_by_session.merge(session_end, on='session_id', how='left')


# In[47]:


user_by_session.head()


# In[48]:


# объединим таблицы *data_session_total* и *user_by_session*

total = data_session_total.merge(user_by_session, on=['session_id', 'user_id', 'source'], how='left')
total.head()


# In[49]:


# отбросим те сессии, чья длительность составляет больше 30 мин (1800 секунд)

good_sessions = total.query('session_duration <= 1800')
good_sessions.boxplot('session_duration')
plt.show()


# ### По воронкам событий посчитаем, какая доля пользователей проходит на следующий шаг воронки (от числа пользователей на предыдущем)

# **Рассмотрим воронку 1:**
# 
# `search` --> `advert_open` --> `contacts_show` --> `favorites_add` --> `contacts_call`
# 
# Т.е. пользователи самостоятельно искали объявления в приложении без использования рекомендаций

# In[50]:


data_tips_click = good_sessions.query('event_name == "tips_click"')
tips_click_users_list = data_tips_click['user_id'].unique().tolist() # пользователи, кликнувшие по рекомендации
data_search = good_sessions.query('event_name == "search"')
search_users_list = data_search['user_id'].unique().tolist() # пользователи, совершившие поисковые действия

search_funnel = good_sessions.query('user_id not in @tips_click_users_list')
search_funnel = search_funnel.query('user_id in @search_users_list')
search_funnel =  search_funnel.query(
    'event_name != "tips_show" and event_name != "tips_click" and event_name != "map" and event_name != "photos_show"'
)

search_funnel_count = search_funnel['event_name'].value_counts().to_frame().reset_index()['event_name'].to_list()
search_funnel_name = search_funnel['event_name'].value_counts().to_frame().reset_index()['index'].to_list()


fig = go.Figure()
fig.add_trace(go.Funnel(
    y = search_funnel_name,
    x = search_funnel_count,
    textposition = "auto",
    textinfo = "value+percent initial+percent previous"
))
fig.update_layout(title='Воронка взаимодействий пользователей, кто воспользовался только поисковой системой')
fig.show()


# **Вывод по анализу воронки 1:**
# * После поиска по сайту 30% пользователей открыли карточку объявления
# * Из них 53% пользователей просмотрели контакты (16% от общего числа пользователей, совершавших поисковые действия)
# * После просмотра контактов 53% пользователей добавили объявление в избранное
# * 41% пользователей, добавивших объявление в избранное, позвонили продавцам. Они составляют всего 4% от общего числа пользователей, совершавших поисковые действия в приложении

# **Рассмотрим воронку 2:**
# 
# `tips_show` --> `tips_click` --> `contacts_show` --> `favorites_add` --> `contacts_call`
# 
# Т.е. пользователи используют рекомендации

# In[51]:


tips_click_funnel = good_sessions.query('user_id not in @search_users_list')
tips_click_funnel = tips_click_funnel.query('user_id in @tips_click_users_list')
tips_click_funnel = tips_click_funnel.query(
    'event_name !="search" and event_name != "map" and event_name !="advert_open"'
)
tips_click_funnel_count = tips_click_funnel['event_name'].value_counts().to_frame().reset_index()['event_name'].to_list()
tips_click_funnel_name = tips_click_funnel['event_name'].value_counts().to_frame().reset_index()['index'].to_list()

fig = go.Figure()
fig.add_trace(go.Funnel(
    y = tips_click_funnel_name,
    x = tips_click_funnel_count,
    textposition = "auto",
    textinfo = "value+percent initial+percent previous"
))
fig.update_layout(title='Воронка взаимодействий пользователей, кто воспользовался только рекомендательной системой')
fig.show()


# **Вывод по анализу воронки 2:**
# * Лишь 17% пользователей, увидевших рекомендацию, перешли на это объявление
# * Из 380 пользователей, перешедших на рекомендованное объявление, 44% посмотрели контакты продавца
# * 3% от начального количества пользователей добавили объявление в избранное
# * Звонков продавцу в этой воронке нет

# ### Сравним воронки по конверсии и времени до целевого действия

# In[52]:


# рассмотрим время до целевого действия для пользователей, кто пользовался самостоятельным поиском

search_users = good_sessions.query('user_id not in @tips_click_users_list')
search_users = search_users.query('user_id in @search_users_list')
contacts_show_min_time = (
    search_users.query('event_name =="contacts_show"')
                .groupby(['session_id'])
                .agg({'event_time':'min'})
                .sort_values(by='event_time')
)
min_time = search_users.groupby(['session_id']).agg({'event_time':'min'}).sort_values(by='event_time')
contacts_show_time = min_time.merge(contacts_show_min_time, on ='session_id', how='right').reset_index()
contacts_show_time = contacts_show_time.rename(columns={'event_time_x':'session_start', 'event_time_y':'contacts_show'})
contacts_show_time['td'] = contacts_show_time['contacts_show'] - contacts_show_time['session_start']
contacts_show_time['td'] = contacts_show_time['td'] / np.timedelta64(1,'m')
contacts_show_time.head()


# In[53]:


# посмотрим, как распределяется время до целевого события для воронки 1

fig = plt.figure(figsize=(15,5))
ax_1 = fig.add_subplot(1, 2, 1)
ax_2 = fig.add_subplot(1, 2, 2)

y = contacts_show_time['td']
ax_1.boxplot(y)
ax_1.set_xlabel('Время до целевого события')
ax_2.boxplot(y)
ax_2.set_xlabel('Время до целевого события')
ax_2.set_ylim([0,20])

fig.show()


# In[54]:


search_time_median = contacts_show_time['td'].median()
print(f'Средняя продолжительность поиска до целевого события: {search_time_median:.0f} минут(ы)')


# > **Для воронки 1 средняя продолжительность поиска до целевого события составила 2 минуты.**

# In[55]:


# рассмотрим время до целевого действия для пользователей, кто пользовался рекомендациями

tips_click_users = good_sessions.query('user_id not in @search_users_list')
tips_click_users = tips_click_users.query('user_id in @tips_click_users_list')
tips_contacts_show_min_time = (
    tips_click_users.query('event_name =="contacts_show"')
                .groupby(['session_id'])
                .agg({'event_time':'min'})
                .sort_values(by='event_time')
)
tips_min_time = tips_click_users.groupby(['session_id']).agg({'event_time':'min'}).sort_values(by='event_time')
tips_contacts_show_time = tips_min_time.merge(tips_contacts_show_min_time, on ='session_id', how='right').reset_index()
tips_contacts_show_time = tips_contacts_show_time.rename(columns={'event_time_x':'session_start', 'event_time_y':'contacts_show'})
tips_contacts_show_time['td'] = tips_contacts_show_time['contacts_show'] - tips_contacts_show_time['session_start']
tips_contacts_show_time['td'] = tips_contacts_show_time['td'] / np.timedelta64(1,'m')
tips_contacts_show_time.head()


# In[56]:


# посмотрим, как распределяется время до целевого события для воронки 2

fig = plt.figure(figsize=(15,5))
ax_1 = fig.add_subplot(1, 2, 1)
ax_2 = fig.add_subplot(1, 2, 2)

y = tips_contacts_show_time['td']
ax_1.boxplot(y)
ax_1.set_xlabel('Время до целевого события')
ax_2.boxplot(y)
ax_2.set_xlabel('Время до целевого события')
ax_2.set_ylim([0,20])

fig.show()


# In[57]:


tips_time_median = tips_contacts_show_time['td'].median()
print(f'Средняя продолжительность действий до целевого события при использовании рекомендаций: {tips_time_median:.0f} минут (ы)')


# > **Для воронки 2 средняя продолжительность действий до целевого события при использовании рекомендаций также составила 2 минуты**

# ### Общий вывод по анализу воронок

# 1. **При самостоятельном поиске объявлений пользователи в 30% случаев открывают карточку объявления. Из них 53% смотрят контакты, что составляет 16% от общего числа пользователей, совершавших поисковые действия. Среднее время поиска до совершения целевого события - просмотра контактов - составляет 2 минуты.**
# 2. **При использовании рекомендаций только 17% пользователей переходят на эти объявления. Конверсия при переходе из события "кликнул на рекомендованное объявление" в "просмотрел контакты" составляет 44%, что ниже, чем для самостоятельного поиска. Можно сделать вывод, что система рекомендаций работает недостаточно хорошо, поскольку низкий как процент просмотра рекомендаций, так и конверсия в просмотр контактов продавца. Средняя продолжительность действий до целевого события при использовании рекомендаций составляет 2 минуты, так же, как в случае самостоятельного поиска. Это говорит нам о том, что воронки отличаются только в конверсии в целевое действие - просмотр контактов.**

# ## <a id='hypothesis'> Проверка гипотез </a>

# Гипотезы:
# * Одни пользователи совершают действия `tips_show` и `tips_click`, другие — только `tips_show`. Проверить гипотезу: **конверсия в просмотры контактов различается у этих двух групп**.
# * Одни пользователи ищут объявления самостоятельно и совершают действия `search_1`—`search_7`, другие пользуются рекомендациями, т.е. совершают действия `tips_click`или `tips_show`. Проверить гипотезу: **конверсия в просмотры контактов различается у этих двух групп**.
# * Одни пользователи скачали приложение, прийдя с источника Yandex, а другие - из Google. Проверить гипотезу: **конверсия в просмотры контактов между теми пользователями, которые совершили установку приложения, прийдя с источника yandex и пользователями, совершившими установку из источника google, различается.**

# ### Гипотеза 1: конверсия в просмотры контактов различается у групп пользователей, совершивших *tips_show* и *tips_click* и только *tips_show*

# **Нулевая гипотеза: различий в конверсии между группами нет.** 
#     
# **Альтернативная: различия в конверсии между группами есть.**

# Сформируем датафрейм и проверим гипотезу о наличии статистически значимой разницы с помощью z-критерия:

# Пусть группа пользователей, которые совершали только *tips_show* - группа А; а пользователи, которые использовали *tips_click* - группа В

# In[58]:


data_tips_show = good_sessions.query('event_name == "tips_show"')
tips_show_users_list = data_tips_show['user_id'].unique().tolist() # пользователи, увидевшие рекомендации

only_tips_show = good_sessions.query('user_id not in @tips_click_users_list')
only_tips_show = only_tips_show.query('user_id in @tips_show_users_list')
only_tips_show = only_tips_show.query(
    'event_name == "tips_show" or event_name == "contacts_show"'
)

tips_show_and_tips_click = good_sessions.query('user_id in @tips_click_users_list and user_id in @tips_show_users_list')
tips_show_and_tips_click = tips_show_and_tips_click.query(
    'event_name == "tips_show" or event_name == "contacts_show"'
)


# In[59]:


# количество событий "tips_show" и "contacts_show" в 1ой группе

tips_show_and_tips_click_funnel_count = (
    tips_show_and_tips_click['event_name'].value_counts().to_frame().reset_index()['event_name'].to_list()
)
tips_show_and_tips_click_funnel_count


# In[60]:


# количество событий "tips_show" и "contacts_show" во 2ой группе

only_tips_show_funnel_count = only_tips_show['event_name'].value_counts().to_frame().reset_index()['event_name'].to_list()
only_tips_show_funnel_count


# In[61]:


columns = ['group', 'contacts_show', 'user_count']
data_groups_hyp1 = [
    ['A', only_tips_show_funnel_count[1], only_tips_show_funnel_count[0]],
    ['B', tips_show_and_tips_click_funnel_count[1], tips_show_and_tips_click_funnel_count[0]]
]

pd.set_option('display.precision', 2)
test_hyp1 = pd. DataFrame(data=data_groups_hyp1, columns=columns)
test_hyp1 = test_hyp1.set_index('group')
test_hyp1['CR, %'] = test_hyp1['contacts_show']/test_hyp1['user_count']*100
test_hyp1


# In[62]:


alpha = .05 # критический уровень статистической значимости

# за успех считаем событие, когда пользователь просмотрел контакты
successes = np.array([test_hyp1['contacts_show'][0], test_hyp1['contacts_show'][1]])
    
# количество попыток - общее число пользователей в группе
trials = np.array([test_hyp1['user_count'][0], test_hyp1['user_count'][1]])

stat, pval = proportions_ztest(successes, trials)
print('P-value равно','{0:0.3f}'.format(pval))
if pval < alpha:
    print('Отвергаем нулевую гипотезу: между долями есть значимая разница')
else:
    print('Не получилось отвергнуть нулевую гипотезу, нет оснований считать доли разными'
    ) 


# > **Конверсия в просмотры контактов для групп пользователей, совершивших *tips_show* и *tips_click* и только *tips_show* равны соответственно 5.79% и 6.44%. Т.е. конверсия для группы, что не кликает по рекомендованным объявлениям, чуть выше**

# ### Гипотеза 2: конверсия в *contacs_show* между теми пользователями, которые совершили действия *tips_click* и пользователями, которые использовали *search*, различается

# Нулевая гипотеза: различий в конверсии между группами нет. 
#     
# Альтернативная: различия в конверсии между группами есть.

# In[63]:


click = tips_click_funnel.query('event_name == "tips_show" or event_name == "contacts_show"')
search = search_funnel.query('event_name == "search" or event_name == "contacts_show"')


# Пусть группа пользователей, которые совершали поиск в приложении - группа А; а пользователи, которые использовали tips_click - группа В

# In[64]:


# количество событий "search" и "contacts_show" в 1ой группе

search_funnel_count = (
    search['event_name'].value_counts().to_frame().reset_index()['event_name'].to_list()
)
search_funnel_count


# In[65]:


# количество событий "tips_show" и "contacts_show" во 2ой группе

click_count = (
    click['event_name'].value_counts().to_frame().reset_index()['event_name'].to_list()
)
click_count


# In[66]:


columns = ['group', 'contacts_show', 'user_count']
data_groups_hyp2 = [
    ['A', search_funnel_count[1], search_funnel_count[0]],
    ['B', click_count[1], click_count[0]]
]

test_hyp2 = pd. DataFrame(data=data_groups_hyp2, columns=columns)
test_hyp2 = test_hyp2.set_index('group')
test_hyp2['CR, %'] = test_hyp2['contacts_show']/test_hyp2['user_count']*100
test_hyp2


# In[67]:


alpha = .05 # критический уровень статистической значимости

# за успех считаем событие, когда пользователь просмотрел контакты
successes_hyp2 = np.array([test_hyp2['contacts_show'][0], test_hyp2['contacts_show'][1]])
    
# количество попыток - общее число пользователей в группе
trials_hyp2 = np.array([test_hyp2['user_count'][0], test_hyp2['user_count'][1]])

stat, pval = proportions_ztest(successes_hyp2, trials_hyp2)
print('P-value равно','{0:0.3f}'.format(pval))
if pval < alpha:
    print('Отвергаем нулевую гипотезу: между долями есть значимая разница')
else:
    print('Не получилось отвергнуть нулевую гипотезу, нет оснований считать доли разными'
    ) 


# > **Конверсия в *contacs_show* для группы, где пользователи совершили действия *tips_click* равна 7.46% и 15.58% для группы, где пользователи использовали поиск. Это различие значимо.**

# ### Гипотеза 2: конверсия в просмотры контактов между теми пользователями, которые совершили установку приложения, прийдя с источника yandex и пользователями, совершившими установку из источника google, различается.

# Нулевая гипотеза: различий в конверсии между группами нет. 
#     
# Альтернативная: различия в конверсии между группами есть.

# In[68]:


yandex = total.query('source =="yandex" and event_name == "contacts_show"')
google = total.query('source =="google" and event_name == "contacts_show"')


# In[69]:


users_count_by_source = total.query('source !="other"').groupby('source')['user_id'].nunique()


# In[70]:


users_by_events = (
    total.query('event_name == "contacts_show" and source !="other"')
    .pivot_table(index='source',columns='event_name', values='user_id', aggfunc='nunique')
    .reset_index()
)

users_by_events['user_count'] = users_by_events['source'].apply(lambda x: users_count_by_source.loc[x])
users_by_events = users_by_events.set_index('source')
users_by_events.columns = ['contacts_show', 'user_count']
users_by_events


# In[71]:


alpha = .05 # критический уровень статистической значимости

# за успех считаем событие, когда пользователь просмотрел контакты
successes = np.array([users_by_events['contacts_show'][0], users_by_events['contacts_show'][1]])
    
# количество попыток - общее число пользователей в группе
trials = np.array([users_by_events['user_count'][0], users_by_events['user_count'][1]])

stat, pval = proportions_ztest(successes, trials)
print('P-value равно','{0:0.3f}'.format(pval))
if pval < alpha:
    print('Отвергаем нулевую гипотезу: между долями есть значимая разница')
else:
    print('Не получилось отвергнуть нулевую гипотезу, нет оснований считать доли разными'
    ) 


# > **Различий в конверсии в просмотры контактов между теми пользователями, которые совершили установку приложения, прийдя с источника yandex и пользователями, совершившими установку из источника google, нет.**

# ### Общий вывод по этапу проверки гипотез
# 1. Конверсия в просмотры контактов для групп пользователей, совершивших tips_show и tips_click и только tips_show равны соответственно 5.79% и 6.44%. Т.е. конверсия для группы, что не кликает по рекомендованным объявлениям, чуть выше.
# 2. Конверсия в contacs_show для группы, где пользователи совершили действия tips_click равна 7.46% и 15.58% для группы, где пользователи использовали поиск. Это различие значимо.
# 3. Различий в конверсии в просмотры контактов между теми пользователями, которые совершили установку приложения, прийдя с источника yandex и пользователями, совершившими установку из источника google, нет.

# ## <a id='conclusion'> Выводы </a>

# **В ходе исследования были выявлены следующие инсайты:**
# 1. При самостоятельном поиске объявлений пользователи в 30% случаев открывают карточку объявления. Из них 53% смотрят контакты, что составляет 16% от общего числа пользователей, совершавших поисковые действия. Среднее время поиска до совершения целевого события - просмотра контактов - составляет 2 минуты.
# 2. При использовании рекомендаций только 17% пользователей переходят на эти объявления. Конверсия при переходе из события "кликнул на рекомендованное объявление" в "просмотрел контакты" составляет 44%, что ниже, чем для самостоятельного поиска. Можно сделать вывод, что система рекомендаций работает недостаточно хорошо, поскольку низкий как процент просмотра рекомендаций, так и конверсия в просмотр контактов продавца. Средняя продолжительность действий до целевого события при использовании рекомендаций составляет 2 минуты, так же, как в случае самостоятельного поиска. Это говорит нам о том, что воронки отличаются только в конверсии в целевое действие - просмотр контактов.
# 3. Конверсия в просмотры контактов для групп пользователей, совершивших tips_show и tips_click и только tips_show равны соответственно 5.79% и 6.44%. Т.е. конверсия для группы, что не кликает по рекомендованным объявлениям, чуть выше.
# 5. Конверсия в contacs_show для группы, где пользователи совершили действия tips_click равна 7.46% и 15.58% для группы, где пользователи использовали поиск. Это различие значимо.
# 6. Различий в конверсии в просмотры контактов между теми пользователями, которые совершили установку приложения, прийдя с источника yandex и пользователями, совершившими установку из источника google, нет.
# 
# **Рекомендации продакт-менеджеру:**
# * Стоит уделить особое внимание системе рекомендаций в приложении, т.к. ею пользуются очень малое количество пользователей. Конверсия в просмотр контактов для воронки, где пользователь кликает по рекомендованному объявлению также ниже, чем в случае самостоятельного поиска. Хорошая система рекомендаций может сократить время на поиски "того самого" товара и удержать пользователей, а также привлечь новых. 

# In[ ]:




