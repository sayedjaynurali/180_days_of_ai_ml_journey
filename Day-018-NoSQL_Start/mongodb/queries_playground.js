use("Bookbase")

db.book.drop()

db.book.insertMany([
  {
    "title": "The Alchemist",
    "author": "Paulo Coelho",
    "pages": 208,
    "genres": ["fiction", "philosophy"],
    "rating": 8.9,
    "publish_year": 1988,
    "publisher": { "name": "HarperCollins", "country": "Brazil" },
    "reviews": [
      {"reviewer": "Alice", "score": 9, "comment": "Inspiring and soulful." },
      { "reviewer": "Ben", "score": 8, "comment": "Simple yet deep." }
    ]
  },
  {
    "title": "To Kill a Mockingbird",
    "author": "Harper Lee",
    "pages": 324,
    "genres": ["fiction", "drama"],
    "rating": 9.5,
    "publish_year": 1960,
    "publisher": { "name": "J.B. Lippincott & Co.", "country": "USA" },
    "reviews": [
      { "reviewer": "Clara", "score": 10, "comment": "A timeless masterpiece." },
      {"reviewer": "David", "score": 9, "comment": "Profound and emotional." }
    ]
  },
  {
    "title": "1984",
    "author": "George Orwell",
    "pages": 328,
    "genres": ["dystopian", "political fiction"],
    "rating": 9.0,
    "publish_year": 1949,
    "publisher": { "name": "Secker & Warburg", "country": "UK" },
    "reviews": [
      { "reviewer": "Emma", "score": 9, "comment": "Chilling and thought-provoking." },
      { "reviewer": "Frank", "score": 8, "comment": "A must-read classic." }
    ]
  },
  {
    "title": "The Hobbit",
    "author": "J.R.R. Tolkien",
    "pages": 310,
    "genres": ["fantasy", "adventure"],
    "rating": 9.2,
    "publish_year": 1937,
    "publisher": { "name": "Allen & Unwin", "country": "UK" },
    "reviews": [
      { "reviewer": "Grace", "score": 10, "comment": "Enchanting and timeless." },
      { "reviewer": "Henry", "score": 9, "comment": "A beautiful journey."}
    ]
  },
  {
    "title": "The Da Vinci Code",
    "author": "Dan Brown",
    "pages": 454,
    "genres": ["thriller", "mystery"],
    "rating": 8.1,
    "publish_year": 2003,
    "publisher": { "name": "Doubleday", "country": "USA" },
    "reviews": [
      { "reviewer": "Irene", "score": 8, "comment": "Fast-paced and clever." },
      { "reviewer": "Jack", "score": 7, "comment": "Interesting plot twists." }
    ]
  },
  {
    "title": "Pride and Prejudice",
    "author": "Jane Austen",
    "pages": 279,
    "genres": ["romance", "classic"],
    "rating": 9.3,
    "publish_year": 1813,
    "publisher": { "name": "T. Egerton", "country": "UK" },
    "reviews": [
      { "reviewer": "Kate", "score": 10, "comment": "Elegant and witty."},
      { "reviewer": "Leo", "score": 9, "comment": "Beautifully written." }
    ]
  }
])

db.book.find({ "author": "George Orwell" })

db.book.find({ "rating": { $gt: 9 } })

db.book.find({ "genres": "fantasy" })

db.book.find({ "publish_year": { $lt: 1950 } })

db.book.find({ "pages": { $gt: 300 } })

db.book.find({ "reviews.score": { $gt: 9 } })

db.book.find({ "reviews.reviewer": "Alice" })

db.book.find({ "rating": { $gte: 8, $lte: 9 } })

db.book.find({ "genres": { $all: ["fiction", "drama"] } })

db.book.find({ "reviews.score": { $lt: 8 } })

db.book.find({}, { "title": 1, "author": 1 })

db.book.find({}, { "title": 1, "rating": 1, "_id": 0 })

db.book.find({}, { "publisher.name": 1, "publisher.country": 1, "_id": 0 })

db.book.find({ "author": "Jane Austen" }, { "title": 1, "publish_year": 1, "_id": 0 })

db.book.find().sort({ "rating": -1 }).limit(3)

db.book.find().sort({ "publish_year": -1 })

db.book.find().sort({ "pages": 1 }).limit(5)

db.book.find({ "genres": "thriller" }).sort({ "rating": -1 })

db.book.find({ "reviews.reviewer": "Ben" })

db.book.find({ "reviews.score": 10 })