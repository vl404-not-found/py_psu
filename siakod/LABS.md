# Лабораторная работа №2
Алгоритмы поиска  строк в массиве и подстроки в строке

Цель работы: изучение алгоритмов поиска, используемых при обработке текстовой информации.

>### Задание на лабораторную работу
1.	Написать программу поиска заданной строки в одномерном массиве строк. Если поиск удачен, то вывести номер найденной строки, в противном случае вывести сообщение, что поиск неудачен.
2.	Написать программу, содержащую функцию прямого поиска  первого вхождение искомой подстроки в массиве строк, вывести номер строки и адрес начала найденной подстроки в строке.
3.	Используя данную функцию, написать программу, выводящую на экран все строки заданного массива строк, содержащие искомую подстроку.
4.	Реализовать функцию искомой подстроки  в строке используя более совершенный алгоритм (дополнительное задание)
5.	Провести экспериментальные исследования времени выполнения алгоритмов и трудоемкости.
6.	Дополнительное задание Реализовать дополнительный алгоритм поиска  (по выбору) и исследовать его.
>### Контрольные вопросы
1.	Как обратиться к любому символу строки?
2.	Определить отношение порядка на множестве строк.
3.	Определить сложность алгоритма сравнения строк.
4.	Определить сложность алгоритма поиска строки в массиве строк.
5.	Определить сложность алгоритма прямого поиска подстроки в строке.
>### Содержание отчета
1.	Название и цель работы.
2.	Схемы алгоритмов.
3.	Теоретические оценки алгоритмов.
4.	Экспериментальные исследования.
5.	Выводы по работе.


# Лабораторная работа №3

Исследование алгоритмов поиска на основе хеширования

Цель работы – изучение различных функций хеширования и методов хранения и поиска информации на основе хеширования.

>### Задание на лабораторную работу.
1.	Написать функции получения хеш – адреса для методов деления, середины квадратов, метод преобразования систем счисления и свертывания.
2.	Используя метод цепочек, определить наиболее эффективную функцию хеширования. Для этого, используя каждую из указанных в п. 1 хеш-функций, заполнять структуру хранения случайной последовательностью из n ключей и подсчитывать количество коллизий.
На вход каждой из хеш-функций должна подаваться одна и та же последовательность ключей в диапазоне от 0 3200.
3.	Написать программу оценки временных характеристик поиска ключей для метода открытой адресации и метода цепочек. Для этого: 
а) используя наилучшую по эффективности функцию хеширования, заполнить n случайными ключами соответствующие структуры хранения согласно методу открытой адресации и методу цепочек;
б) для n случайных ключей определить время их поиска методом открытой адресации и методом цепочек.
4. Дополнительное задание. Реализовать дополнительный алгоритм хеширования(по выбору) и исследовать его.

>### Контрольные вопросы

1.	Когда возникает коллизия при хешировании?
2.	Какие хеш-функции используются для формирования хеш - адресов?
3.	В чем отличие метода открытой адресации от метода цепочек? Преимущества и недостатки каждого метода.

>### Содержание отчета
1.	Название и цель работы.
2.	Схемы алгоритмов вычисления хеш – адреса, расстановки и поиска ключей методами цепочек и открытой адресации.
3.	Теоретические оценки алгоритмов.
4.	Сравнительные временные характеристики исследуемых алгоритмов поиска ключей для метода открытой адресации и метода цепочек. 
5.	Выводы по работе.


# Лабораторная работа №4

Исследование алгоритмов внутренней сортировки

Цель работы – изучение и исследование основных алгоритмов сортировки  данных,  размещенных в оперативной памяти

>### Задание на лабораторную работу

1.	Написать программу, включающую следующие функции:
1)	сортировка 1;
2)	сортировка 2;
3)	проверка массива на упорядоченность;
2.	В основной программе выполнить в зависимости от выбранного в диалоге способ заполнения массива
1)	заполнение массива случайными числами;
2)	 ввод массива с клавиатуры для небольших массивов.
3.	Подсчитать характеристики сортировок (время, число сравнений, число обменов или сдвигов) для каждого из алгоритмов и время для стандартной сортировки и оформить полученные данные в виде таблиц.
4.	Построить графики для  характеристик (время) и сравнить время выполнения.

В пп.1.1-2 продемонстрировать соответствующую сортировку для массива из 10-15 элементов. Вывести на экран исходный массив и промежуточные результаты каждого прохода.
Программа должна решать указанную задачу, динамически создавая в функции main массив для хранения данных на требуемое количество элементов и заполняя его числами. При реализации алгоритма нельзя создавать ни в функции main, ни в других функциях дополнительные рабочие массивы, длина которых явно или неявно зависела бы от длины исходных данных.
Программа должна содержать функции, получающие в качестве параметров указатель на начальный элемент массива и длину массива, а также, возможно, другие параметры, необходимые для решения конкретной задачи.

>### Контрольные вопросы

1.	Какова сложность каждого из рассмотренных выше алгоритмов сортировки?
2.	Определить среднее число обрабатываемых элементов для каждого из алгоритмов сортировки. Эту оценку можно получить из произведения среднего числа проходов и среднего количества элементов, обрабатываемых на каждом проходе.

>### Содержание отчета

1.	Название и цель работы.
8.	Схемы всех исследуемых алгоритмов в соответствии с ГОСТ 19.701-90 (ИСО 5807-85).
2.	Листинг программы
3.	Результаты сортировки для небольших примеров с промежуточными результатами каждого прохода.
4.	Теоретические оценки исследуемых алгоритмов.
5.	Таблица сравнительных характеристик работы алгоритмов для  различных  по размеру массивов данных (не менее 10 различных размеров от 10 до 100000).
6.	Графики функций
7.	Выводы по работе.

>#### Варианты.

1.	Сортировка с переменным шагом (Шелла) и сортировка вставками.
2.	Сортировка с переменным шагом (Шелла) и сортировка бинарными вставками 
3.	Сортировка Хоара (быстрая) с рекурсией  и сортировка простым обменом (пузырьковая)
4.	Сортировка Хоара (быстрая) с рекурсией и  шейкерная сортировка.
5.	Сортировка Хоара (быстрая) с рекурсией  и  выбором опорного элемента ( средний, медиана из 3 элементов: первый, средний и последний).
6.	Сортировки с переменным шагом (Шелла) с различным шагом.
7.	Пирамидальная сортировка и сортировка простым выбором .
8.	Пирамидальная сортировка и пузырьковая сортировка .
9.	 Сортировка Хоара (быстрая) с рекурсией и модификация алгоритма, устраняющая одну ветвь рекурсии: вместо того, чтобы после разделения массива вызывать рекурсивно процедуру разделения для обоих найденных подмассивов, рекурсивный вызов делается только для меньшего подмассива, а больший обрабатывается в цикле в пределах этого же вызова процедуры.
10.	Сортировка слиянием и сортировка подсчетом.
11.	Сортировка слиянием рекурсивная и итерационная(восходящая).
12.	Сортировка слиянием и  сортировка выбором.
13.	Сортировка слиянием  и шейкерная сортировка
14.	Пирамидальная сортировка и сортировка подсчетом
15.	Сортировка Хоара (быстрая) с рекурсией  и подсчетом



# Лабораторная работа №5

Исследование алгоритмов внешней сортировки

Цель работы – изучение и исследование основных алгоритмов сортировки  данных,  размещенных во внешней памяти

Задание на лабораторную работу

>### Написать программу, состоящую из следующих процедур:
1.	Процедура сортировки простым слиянием (двухфазная или однофазная).
2.	Процедура сортировки естественным слиянием (двухфазная или однофазная).
3.	Процедура внутренней сортировки с внешним слиянием с использованием n  файлов.
4.	Характеристики сортировок (время, число сравнений, число обменов).
5.	Процедура заполнения файла случайными числами.
6. Процедура ввода данных с клавиатуры для небольших массивов.
В пп. 1-3 продемонстрировать соответствующую сортировку для файлов из 15-20 элементов. Вывести на экран исходный файл и промежуточные результаты каждой фазы сортировки.
В п. 4 для заданного в диалоге количества элементов файла подсчитать время сортировки.

>### Контрольные вопросы
1.	Чем отличаются алгоритмы внутренней сортировки от алгоритмов внешней сортировки?
2.	Что такое слияние последовательностей?
3.	Чем отличается однофазное слияние от двухфазного?
4.	Что такое серия?
5.	Сколько проходов нужно выполнить для упорядочения с помощью алгоритма простого слияния?

>### Содержание отчета
1.	Название и цель работы.
2.	Схемы всех исследуемых алгоритмов.
3.	Теоретические оценки исследуемых алгоритмов.
4.	Таблица сравнительных характеристик работы алгоритмов для  различных  по размеру файлов данных и графики.
5.	Листинг программы
6.	Результаты работы программы с показом работы алгоритмов
7.	Выводы по работе.
>#### Варианты:
1.	Процедура сортировки простым слиянием двухфазная.
2.	Процедура сортировки естественным слиянием двухфазная.
3.	Процедура сортировки простым слиянием однофазная.
4.	Процедура сортировки естественным слиянием однофазная.
5.	Процедура внутренней сортировки с внешним слиянием с использованием n  файлов.
6.	Процедура внутренней сортировки с внешним слиянием с использованием файлов размерности n

№ варианта | | | |
--- | --- | --- | ---
1 | 1 | 4 | 6
2 | 2 | 3 | 6
3 | 1 | 4 | 6 
4 | 2 | 3 | 6 
5 | 1 | 4 | 5 
6 | 2 | 3 | 5 
7 | 1 | 4 | 5 
8 | 2 | 3 | 5 



 
# Лабораторная работа № 6

Структуры данных
Цель лабораторной работы:- изучение методов организации хранения и обработки  данных на примере списочных структур данных.

Задание на лабораторную работу

Разработать АТД( абстрактный тип данных)  и его реализацию в виде  параметризованного  класса.
В классе должны быть реализованы конструктор без параметров, конструктор копирования, оператор присваивания и переопределены 1-2 оператора (например, сложение как объединение множеств, отношение порядка меньше и/или больше). В классе должна быть реализована операция сортировки, вывод данных в файл и на экран.
Реализовать тот же самый АТД с использованием классов стандартной библиотеки классов
Разработать основную программу тестирования реализаций АТД на 3 различных типах хранимых объектов:
	Базовые типы (int, double)
	Простейшие структурные типы (точка, запись данных о студенте)
	Сложные классы, разработанные вами в курсе программирования 3 семестра
Информацию о стандартной библиотеке можно посмотреть здесь:
•	Технопарк Mail.ru Group: Программирование на С/С++ Лекция 6: Практическое введение в STL. Функциональное программирование в С++ URL:http://www.intuit.ru/studies/courses/3492/734/lecture/26038
•	Библиотека STL http://tenisheff.ru/hgs/po/STL.htm
•	Справочник по библиотеке STL/CLR https://msdn.microsoft.com/ru-ru/library/bb385855.aspx
•	Библиотека STL (Standart Template Library) URL:http://www.itshop.ru/Biblioteka-STL-Standart-Template-Library/l9i22387

>### Контрольные вопросы.
1.	Что такое АТД?
2.	Пример АТД Стэк
3.	В чем отличие логической и физической структур данных
4.	Что такое параметризованный класс?
5.	Какие бывают конструкторы класса?
6.	Как переопределить операторы в классе?

>### Содержание отчета

1.	Название и цель работы.
2.	Описание АТД (операции и их свойства)
3.	Схемы алгоритмов наиболее сложных операций
4.	Листинг программы
5.	Результаты работы программы
6.	Таблица сравнительных характеристик работы программы с различной реализацией АТД.
7.	Выводы по работе

>### Варианты:
1.	Однонаправленный список
2.	Двунаправленный список
3.	Кольцевой однонаправленный список
4.	Кольцевой двунаправленный список
5.	Одномерный динамический массив как список блоков
6.	Двумерный динамический массив как список блоков с одним указателем
7.	Двумерный динамический массив как список блоков с двумя указателями
8.	Стэк на базе списка
9.	Очередь на базе списка
10.	 Дэк на базе списка
11.	 Бинарное сбалансированное дерево
12.	 В-дерево
13.	 Граф
14.	Ориентированный граф
15.	В дерево
16.	 В+ дерево
17.	 Красно-черное дерево
18.	Хэш-таблица



 
# Лабораторная работа № 7

Исследование алгоритмов поиска гамильтоновых циклов в ориентированном графе и задачи коммивояжера для неориентированного графа

Цель лабораторной работы:- изучение и исследование алгоритмов поиска гамильтоновых циклов в ориентированном графе и задачи коммивояжера для неориентированного графа.

Задание на лабораторную работу

>### Написать программу, состоящую из следующих процедур:
1.	Процедура поиска  гамильтоновых  циклов алгоритмом Робертса –Флореса.
2.	Процедура решения задачи коммивояжера методом ветвей и границ.
3.	Процедура решения задачи коммивояжера методом ближайшего города или соседа.
4.	Процедура решения задачи коммивояжера итерационным методом.


>### Контрольные вопросы.

1.	Дайте определение понятию гамильтонов цикл (контур) в графе.
2.	К какому типу задач по временной сложности относится задачи определения гамильтоновых циклов в графе.
3.	Дайте постановку задачи коммивояжера.
4.	Чем отличаются симметричная и несимметричная задачи коммивояжера?
5.	Где на практике используются рассматриваемые задачи?
6.	В чем заключается механизм приведения, используемый в методе ветвей и границ?
7.	Как определяется оптимистическая оценка длины пути?

>### Содержание отчета

1.	Название и цель работы.
2.	Схемы  изучаемых алгоритмов.
3.	Теоретические оценки  алгоритмов.
4.	Выводы по работе.
5.	Листинг программы
6.	Результаты работы программы с исследованием характеристик алгоритмов.


# Лабораторная работа № 8

Цифровой поиск

Цель лабораторной работы:- изучение методов организации хранения и поиска данных с помощью дерева цифрового поиска.

>### Задание на лабораторную работу

1.	Разработать схемы алгоритма.
2.	Разработать дерево  для  заданного примера
3.	Написать программу, состоящую из следующих процедур:
	Процедура формирования дерева цифрового поиска.
	Процедура поиска по дереву.

>### Контрольные вопросы.

1.	Какова структура узла дерева цифрового поиска?
2.	Какова структура дерева  цифрового поиска?
3.	Привести пример формирования дерева цифрового поиска.
4.	Привести пример поиска в  дереве цифрового поиска.

>### Содержание отчета

1.	Название и цель работы.
2.	Схемы алгоритмов формирования дерева цифрового поиска и организации поиска в нем.
3.	Теоретические оценки исследуемых алгоритмов.
4.	Пример работы алгоритма
5.	Листинг программы и результаты работы программы(дополнительное задание)
6.	Выводы по работе.
