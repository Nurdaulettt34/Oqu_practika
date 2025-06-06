📚 2025 Кітаптарға Дауыс Беру Веб-қосымшасы
Бұл веб-қосымша кітаптарды қосып, оларды дауыс беру арқылы таңдау және жеңімпазды анықтауға арналған. FastAPI көмегімен серверлік бөлігі жасалған және Tailwind CSS пен Jinja2 арқылы HTML беттері стильдендірілген.

🚀 Қосымшаның негізгі мүмкіндіктері
  ✅ Кітаптарды қосу
  ✅ Барлық кітаптарды қарау және дауыс беру
  ✅ Дауыс беру мерзімін бақылау (7 күн)
  ✅ Жеңімпазды автоматты түрде анықтау

🛠 Қолданылған технологиялар
  Backend: FastAPI (Python)
  Frontend: HTML + Tailwind CSS + Jinja2
  Database: уақытша жады (in-memory database)
  Тестілеу: Дауыс беру мерзімі – 7 күн

📑 Орнату және іске қосу (Pycharm арқылы)
Репозиторийді жүктеу:

bash
git clone https://github.com/Nurdaulettt34/Oqu_practika.git


Немесе ZIP файлын жүктеп, Pycharm-да ашыңыз.

Pycharm-да жаңа виртуалды орта (venv) жасау:
  Pycharm-ды ашыңыз → File → Settings → Project: Oqu_practika → Python Interpreter → Add Interpreter → New environment → Virtualenv таңдаңыз.
  Python нұсқасын көрсетіп, OK батырмасын басыңыз.
Тәуелділіктерді орнату:
  Pycharm-ның төменгі жағындағы Terminal батырмасын ашыңыз.
  Терминалда келесі команданы орындаңыз:

bash
pip install fastapi uvicorn jinja2 pydantic
(қосымша қажет болса: pip install python-multipart)

Қосымшаны іске қосу:

main.py файлын ашып, төменгі жағында тұрған:

python
Copy
Edit
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
бөлігіне курсорды қойып, жасыл «▶» (Run) батырмасын басыңыз.

Немесе терминалда келесі команданы орындаңыз:

bash
uvicorn main:app --reload
Браузерден ашыңыз:

arduino
http://localhost:8000

немесе

cpp
http://127.0.0.1:8000

📌 Дерекқор құрылымы
  books_db — Кітаптардың тізімі (id, атауы, авторы, дауыс саны, жанры)
  votes_db — Кітаптардың дауыс саны
  voting_end — Дауыс берудің аяқталу мерзімі


👥 Авторлар
Сагимбаев Нұрдаулет — nurdauletsagimbaev34@gmail.com

Оралбек Айдос — aidosoralbek57@gmail.com

Құлмаханбет Мұқағали — mukagalikulmahanbet@gmail.com

Мирзалиев Аян — mirzalievayan09@gmail.com


💡 Қосымша ақпарат
Бұл жоба кітапханаларға, мектептерге және оқу клубтарына арналған шағын веб-қосымша ретінде пайдалануға ыңғайлы. Болашақта әлеуметтік желілермен бөлісу, пайдаланушыларды тіркеу және дауыс беру тарихын сақтау сияқты функцияларды қосуды жоспарлап отырмыз.


