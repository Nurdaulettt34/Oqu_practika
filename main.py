from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from typing import Optional
import uuid
from datetime import datetime, timedelta
from pydantic import BaseModel

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Кітаптарды сақтау үшін уақытша "дерекқор"
books_db = [
    {"id": "1", "title": "Абай жолы", "author": "М. Әуезов", "votes": 5, "genres": ["Роман", "Классика"], "added_date": "2023-01-01"},
    {"id": "2", "title": "Махаббат, қызық мол жылдар", "author": "М. Мақатаев", "votes": 8, "genres": ["Роман", "Махаббат"], "added_date": "2023-01-02"},
    {"id": "3", "title": "Бақытсыз Жамал", "author": "М. Дулатов", "votes": 3, "genres": ["Роман", "Әлеуметтік"], "added_date": "2023-01-03"},
]

votes_db = {book["id"]: book["votes"] for book in books_db}
voting_end = datetime.now() + timedelta(days=7)

class Book(BaseModel):
    title: str
    genres: list[str]
    
class Vote(BaseModel):
    book_id: str

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("add_book.html", {
        "request": request,
        "voting_end": voting_end,
        "now": datetime.now()
    })

@app.post("/add-book")
async def add_book(
    request: Request,
    book_name: str = Form(...),
    genre_roman: Optional[str] = Form(None),
    genre_poem: Optional[str] = Form(None),
    genre_story: Optional[str] = Form(None),
    genre_drama: Optional[str] = Form(None)
):
    genres = []
    if genre_roman: genres.append("Роман")
    if genre_poem: genres.append("Поэма")
    if genre_story: genres.append("Әңгіме")
    if genre_drama: genres.append("Драма")
    
    book_id = str(uuid.uuid4())
    new_book = {
        "id": book_id,
        "title": book_name,
        "author": "Авторсыз",
        "genres": genres,
        "votes": 0,
        "added_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    books_db.append(new_book)
    votes_db[book_id] = 0
    
    return RedirectResponse(url="/all-books", status_code=303)

@app.get("/all-books", response_class=HTMLResponse)
async def all_books(request: Request):
    sorted_books = sorted(books_db, key=lambda x: x["votes"], reverse=True)
    all_genres = set(genre for book in books_db for genre in book["genres"])
    
    return templates.TemplateResponse(
        "all_books.html", 
        {
            "request": request,
            "books": sorted_books,
            "all_genres": sorted(all_genres),
            "voting_end": voting_end,
            "total_books": len(books_db),
            "total_votes": sum(votes_db.values()),
            "now": datetime.now()
        }
    )

@app.post("/vote/{book_id}")
async def vote_for_book(book_id: str):
    if book_id in votes_db:
        votes_db[book_id] += 1
        for book in books_db:
            if book["id"] == book_id:
                book["votes"] = votes_db[book_id]
                break
        return {"status": "success", "votes": votes_db[book_id]}
    return {"status": "error", "message": "Book not found"}

@app.get("/winners", response_class=HTMLResponse)
async def show_winners(request: Request):
    if datetime.now() < voting_end:
        return templates.TemplateResponse(
            "winners.html",
            {
                "request": request,
                "voting_over": False,
                "voting_end": voting_end,
                "now": datetime.now()
            }
        )
    
    winner = max(books_db, key=lambda x: x["votes"]) if books_db else None
    
    return templates.TemplateResponse(
        "winners.html",
        {
            "request": request,
            "voting_over": True,
            "winner": winner,
            "voting_end": voting_end,
            "now": datetime.now()
        }
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)