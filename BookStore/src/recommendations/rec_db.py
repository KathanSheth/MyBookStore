import collections
from recommendations_pb2 import BookCategory, BookRecommendation

books_by_category = collections.defaultdict()
books_by_category[BookCategory.MYSTERY] = [
        BookRecommendation(book_id=1, title="The Maltese Falcon"),
        BookRecommendation(book_id=2, title="Murder on the Orient Express"),
        BookRecommendation(book_id=3, title="The Hound of the Baskervilles"),]
books_by_category[BookCategory.SCIENCE_FICTION] = [
        BookRecommendation(book_id=4, title="The Hitchhiker's Guide to the Galaxy"),
        BookRecommendation(book_id=5, title="Ender's Game"),
        BookRecommendation(book_id=6, title="The Dune Chronicles"),
    ]
books_by_category[BookCategory.SELF_HELP] = [
        BookRecommendation(book_id=7, title="The 7 Habits of Highly Effective People"),
        BookRecommendation(book_id=8, title="How to Win Friends and Influence People"),
        BookRecommendation(book_id=9, title="Man's Search for Meaning"),
    ]
